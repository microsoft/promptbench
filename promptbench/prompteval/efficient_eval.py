# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
#
# Source Attribution:
# The majority of this code is derived from the following sources:
# - PromptEval GitHub Repository: https://github.com/felipemaiapolo/prompteval

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA

from ..utils import InputProcess, OutputProcess
from .methods import StratSample, ExtendedRaschModel

def get_prompt_embedding(prompt_list, pca_dim):
    """
    Generates prompt embeddings using a pre-trained sentence transformer model and reduces 
    their dimensionality using PCA (Principal Component Analysis).

    Parameters:
    prompt_list (list of str): A list of text prompts for which embeddings are to be generated.
    pca_dim (int): The number of principal components to retain during dimensionality reduction.

    Returns:
    np.ndarray: A matrix where each row corresponds to the reduced-dimensionality embedding 
                of a prompt.
    """
    
    embedder = SentenceTransformer('sentence-transformers/facebook-dpr-question_encoder-multiset-base')
    pca = PCA(n_components=pca_dim)
    X = pca.fit_transform(embedder.encode(prompt_list))
    
    return X

def get_Y_seen(model, prompt_list, example_list, proj_func, budget=1000):
    """
    Generates a matrix of observed (seen) examples and their corresponding labels based on 
    model predictions. The function randomly samples examples up to the given budget and 
    evaluates the model's performance on those examples.

    Parameters:
    model (promptbench.LLMModel): The model to evaluate.
    prompt_list (list of str): A list of prompts used to generate input for the model.
    example_list (list): A list of labeled examples used for evaluation.
    proj_func (function): A function used to project model outputs into a classification 
                          space or other relevant space.
    budget (int, optional): The maximum number of examples to be evaluated. Defaults to 1000.

    Returns:
    tuple: 
        seen_examples (np.ndarray): A boolean matrix indicating which examples were observed 
                                    (True) and which were not (False).
        Y_seen (np.ndarray): A matrix where each element is 1 if the model's prediction matches 
                             the true label, 0 otherwise, and -99 for unseen examples.
    """
    
    # create an empty matrix Y, with 'template_num' columns, and 'dataset_size' rows
    example_num = len(example_list)
    prompt_num = len(prompt_list)
    Y_seen = np.zeros((prompt_num, example_num))

    # 随机抽样
    seen_examples = StratSample(np.zeros(Y_seen.shape).astype(bool), budget, random_seed=0)

    # using np.where to find the indices of all True elements
    true_indices = np.where(seen_examples)

    # iterate over all True indices and fill in the corresponding values in Y_seen
    for row, col in tqdm(zip(true_indices[0], true_indices[1]), total=len(true_indices[0])):
        prompt = prompt_list[row]
        data = example_list[col]
        # test it!
        input_text = InputProcess.basic_format(prompt, data)
        label = data['label']
        raw_pred = model(input_text)
        # process output
        pred = OutputProcess.cls(raw_pred, proj_func)
        Y_seen[row, col] = 1 if pred == label else 0

        # mark the unseen examples
        Y_seen[~seen_examples] = -99 #just a placeholder for non-observed
    
    return seen_examples, Y_seen
    
def fit_Y(X, Y_seen, seen_examples):
    """
    Fits a model to the seen examples using the Extended Rasch Model and calculates the 
    predicted scores for each prompt.

    Parameters:
    X (np.ndarray): The matrix of prompt embeddings.
    Y_seen (np.ndarray): The matrix of observed example results (1 for correct, 0 for incorrect, 
                         -99 for unseen).
    seen_examples (np.ndarray): A boolean matrix indicating which examples were observed.

    Returns:
    np.ndarray: A vector of predicted scores for each prompt, calculated as the mean score 
                across all seen examples.
    """
    
    extended_rasch_cov = ExtendedRaschModel()
    extended_rasch_cov.fit(seen_examples, Y_seen, X)
    S_hat_cov = extended_rasch_cov.get_Y_hat().mean(1)
    
    return S_hat_cov

def visualize_result(data):
    """
    Visualizes the distribution of model performance using a histogram, boxplot, and 
    cumulative distribution function (CDF).

    Parameters:
    data (np.ndarray): A vector of performance scores to be visualized.

    Returns:
    None: The function displays and saves the plots as 'combined_result.png'.
    """
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # first subplot - Histogram
    axes[0].hist(data, alpha=0.75, density=True, label='PromptEval')
    # axes[0].hist(groundtruth, alpha=0.75, density=True, label='Ground Truth')
    axes[0].set_xlabel("Performance")
    axes[0].set_ylabel("Density")

    # second subplot- Boxplot
    axes[1].boxplot([data], labels=['PromptEval (cov)'])
    axes[1].set_ylabel("Performance Distribution")

    # third subplot - CDF
    bins = np.linspace(0, 1.1, 100)
    axes[2].hist(data, density=True, cumulative=True, bins=bins, histtype='step', linewidth=1.5, label='PromptEval')
    # axes[2].hist(groundtruth, density=True, cumulative=True, bins=bins, histtype='step', linewidth=1.5, label='Ground Truth')
    axes[2].set_xlim(0.0, 1.0)
    axes[2].legend(fontsize=10)
    axes[2].set_xlabel(f"Performance")
    axes[2].set_ylabel("CDF")

    plt.tight_layout()

    plt.savefig('combined_result.png')
    plt.show() 


def efficient_eval(model, prompt_list, example_list, proj_func, budget=1000, visualize=True, pca_dim=25, method='EmbPT'):
    """
    Efficient evaluation of a model on a list of prompts and examples.
    
    Parameters:
    model (promptbench.LLMModel): The model to evaluate. This is typically a large language model that 
                                  will generate responses based on the provided prompts.
    prompt_list (list of str): A list of prompts for which the model's performance will be evaluated.
    example_list (list): A list of examples used for evaluation purposes. These examples are used 
                         in conjunction with the prompts to generate model responses.
    proj_func (function): A projection function used to map the model's output to a desired space 
                          (e.g., embedding space or scoring space).
    budget (int, optional): The maximum number of examples to be used for evaluation. 
                            Defaults to 1000.
    visualize (bool, optional): Whether to visualize the results. If True, a visualization of 
                                the model's performance will be generated. Defaults to True.
    pca_dim (int, optional): The number of principal components to retain when using PCA 
                             for dimensionality reduction in the EmbPT method. Defaults to 25.
    method (str, optional): The evaluation method to be used. Can be 'EmbPT' for embedding-based 
                            prompt tuning or 'Rasch' for Rasch model evaluation. Defaults to 'EmbPT'.
    
    Returns:
    dict: A dictionary containing the following keys:
        'full_performances' (np.ndarray): The complete list of model performance scores 
                                          for each prompt after fitting the examples.
        'quantiles' (dict): A dictionary containing the 5th, 25th, 50th, 75th, and 95th 
                            percentiles of the performance scores.
        'average' (float): The average performance score across all prompts.
        'std_dev' (float): The standard deviation of the performance scores.
    visual_result: if you set visualize=True, the function will generate combined_result.png for you to see the result.
    """
    
    # get prompt embedding
    if method == 'EmbPT':
        X = get_prompt_embedding(prompt_list, pca_dim)
    elif method == 'Rasch':
        X = None
    else:
        raise ValueError("Invalid method specified")
    
    # get Y_seen
    seen_examples, Y_seen = get_Y_seen(model, prompt_list, example_list, proj_func, budget)
    # fit Y
    S_hat_cov = fit_Y(X, Y_seen, seen_examples)  # n个prompt最终的scores
    
    # Calculate quantiles (5th, 25th, 50th, 75th, 95th)
    percentile_list = [5, 25, 50, 75, 95]
    quantiles = np.percentile(S_hat_cov, percentile_list)
    quantiles_dict = {str(k): v for k, v in zip(percentile_list, quantiles)}

    # Calculate the average
    average = np.mean(S_hat_cov)
    # Calculate the standard deviation
    std_dev = np.std(S_hat_cov)
    
    if visualize:
        visualize_result(S_hat_cov)
    
    # Return the calculated statistics
    return {
        'full_performances': S_hat_cov,
        'quantiles': quantiles_dict,
        'average': average,
        'std_dev': std_dev
    }