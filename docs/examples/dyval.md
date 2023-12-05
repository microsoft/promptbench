# DyVal Evaluation

```python
import promptbench as pb
from promptbench.models import LLMModel
from promptbench.dyval import *
```

    /home/v-zhukaijie/anaconda3/envs/promptbench/lib/python3.8/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
      from .autonotebook import tqdm as notebook_tqdm



```python
# main function, defines the pipeline of dyval
print(pb.dyval.DYVAL_DATASETS)
dataset_name = "arithmetic"
prompts = DYVAL_PROMPTS[dataset_name]

# create dataset and model
dataset = DyValDataset(dataset_name, 
                        is_trainset=False, # if true, it will generate a training dataset including inference steps for each problem
                        num_samples=500, # number of samples generated
                        num_nodes_per_sample=10, # number of nodes per sample, used in general DAG generation
                        min_links_per_node=1, # minimum number of links per node, used in general DAG generation
                        max_links_per_node=4, # maximum number of links per node, used in general DAG generation
                        depth=3, # depth of the DAG, used in tree DAG generation
                        num_children_per_node=2, # number of children per node, used in tree DAG generation
                        extra_links_per_node=0, # it controls if we add extra links per node to add complexity
                        add_rand_desc=0, # it controls if we add random descriptions to the nodes to add complexity
                        delete_desc=0, # it controls if we delete descriptions to the nodes, if delete, the problem is unsolvable since some nodes are not described
                        add_cycles=0, # it controls if we add cycles to the DAG, if add, the problem is unsolvable since there are loops
                        )
```

    ['arithmetic', 'linear_equation', 'bool_logic', 'deductive_logic', 'abductive_logic', 'reachability', 'max_sum_path']

      0%|          | 0/500 [00:00<?, ?it/s][nltk_data] Downloading package words to
    [nltk_data]     /home/v-zhukaijie/nltk_data...
    [nltk_data]   Package words is already up-to-date!
    100%|██████████| 500/500 [00:58<00:00,  8.59it/s]



```python
dataset["topological"][0] # sample data
```
    {'answers': 48.0,
     'vars': 'aag',
     'descriptions': 'The value of aae is 10.\nThe value of aab is 10.\nThe value of aaa is 8.\naac gets its value by dividing the value of aaa by those of aab.\nThe value of aad is 6.\naaf gets its value by multiplying together the value of aad and aae.\naag gets its value by multiplying together the value of aac and aaf.'}




```python

print(pb.SUPPORTED_MODELS)
model = LLMModel("google/flan-t5-large", 
                max_new_tokens=10, 
                temperature=0, 
                model_dir=None,
                openai_key=None,
                sleep_time=3
                )

```

    ['google/flan-t5-large', 'llama2-7b', 'llama2-7b-chat', 'llama2-13b', 'llama2-13b-chat', 'llama2-70b', 'llama2-70b-chat', 'phi-1.5', 'gpt-3.5-turbo', 'gpt-4', 'gpt-4-1106-preview', 'gpt-3.5-turbo-1106', 'vicuna-7b', 'vicuna-13b', 'vicuna-13b-v1.3', 'google/flan-ul2']

    You are using the default legacy behaviour of the <class 'transformers.models.t5.tokenization_t5.T5Tokenizer'>. This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thouroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565
    Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.



```python
# for each prompt, evaluate the score
for prompt in prompts:
    score = {}

    # three orders of the dataset: topological, reversed, random
    for order in ["topological"]:
    # for order in ["topological", "reversed", "random"]:
        data = dataset[order]
        preds = []
        answers = []
        
        for d in data[:1]:
            input_text = pb.InputProcess.basic_format(prompt, d)
            raw_pred = model(input_text)

            # dyval preds are processed differently, please refer to the source code /promptbench/dyval/dyval_utils.py
            pred = process_dyval_preds(raw_pred)
            preds.append(pred)
            answers.append(d["answers"])

            print(f"Input: {input_text}")
            print(f"Raw Pred: {raw_pred}")
            print(f"Pred: {pred}")
            print(f"Answer: {d['answers']}")
            print("\n")

        score[order] = dyval_evaluate(dataset.dataset_type, preds, answers)

print(score)
```

    /home/v-zhukaijie/anaconda3/envs/promptbench/lib/python3.8/site-packages/transformers/generation/configuration_utils.py:381: UserWarning: `do_sample` is set to `False`. However, `temperature` is set to `0` -- this flag is only used in sample-based generation modes. You should set `do_sample=True` or unset `temperature`.
      warnings.warn(
    2023-11-29 05:05:39.043831: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 FMA
    To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.


    Input: Here is a description of an arithmetic problem:
    The value of aae is 10.
    The value of aab is 10.
    The value of aaa is 8.
    aac gets its value by dividing the value of aaa by those of aab.
    The value of aad is 6.
    aaf gets its value by multiplying together the value of aad and aae.
    aag gets its value by multiplying together the value of aac and aaf.
    Compute the result of aag. If the solution cannot be calculated, answer 'N/A'. Ensure your result is within a relative precision of 0.0001 (or 0.01%) compared to the ground truth value. Ensure your final result begins with '<<<' and ends with '>>>', for example, if the answer is 1, your final result should be <<<1>>>.
    Raw Pred: <pad> Answer: <unk> 1>>></s>
    Pred: 
    Answer: 48.0
    
    
    {'topological': 0.0}

