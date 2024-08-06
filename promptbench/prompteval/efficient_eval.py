import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA

from ..utils import InputProcess, OutputProcess
from .methods import StratSample, ExtendedRaschModel

def get_prompt_embedding(prompt_list):
    """
    Returns the embedding of a list of prompts using the given model.
    """
    pca_dim = 25
    embedder = SentenceTransformer('sentence-transformers/facebook-dpr-question_encoder-multiset-base')
    pca = PCA(n_components=pca_dim)
    X = pca.fit_transform(embedder.encode(prompt_list))
    
    return X

# 挑选部分数据，然后测试，得到Y
def get_Y_seen(model, prompt_list, example_list, proj_func, budget=1000):
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
    extended_rasch_cov = ExtendedRaschModel()
    extended_rasch_cov.fit(seen_examples, Y_seen, X)
    S_hat_cov = extended_rasch_cov.get_Y_hat().mean(1)
    
    return S_hat_cov

def show_result(S_hat_cov):
    data = [S_hat_cov]
    labels = ['PromptEval (cov)']
    plt.boxplot(data, labels=labels)
    plt.ylabel(f"Performance Distribution")
    plt.savefig('result.png')
    plt.show()  
    
    # 计算data均值并返回
    mean_data = np.mean(S_hat_cov)
    return mean_data
    

def efficient_eval(model, prompt_list, example_list, proj_func, budget=1000):
    # get prompt embedding
    X = get_prompt_embedding(prompt_list)
    # get Y_seen
    seen_examples, Y_seen = get_Y_seen(model, prompt_list, example_list, proj_func, budget)
    # fit Y
    S_hat_cov = fit_Y(X, Y_seen, seen_examples)
    # show result
    mean = show_result(S_hat_cov)
    
    return mean