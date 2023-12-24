# Prompt Attack

```python
# First install textattack, tensorflow, and tensorflow_hub
!pip install textattack tensorflow tensorflow_hub
```


```python
import promptbench as pb
from promptbench.models import LLMModel
from promptbench.prompt_attack import Attack
```

    /home/v-zhukaijie/anaconda3/envs/promptbench/lib/python3.9/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
      from .autonotebook import tqdm as notebook_tqdm
    2023-12-24 03:45:05.172891: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:9261] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
    2023-12-24 03:45:05.172945: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:607] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
    2023-12-24 03:45:05.173987: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1515] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
    2023-12-24 03:45:05.180461: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
    To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
    2023-12-24 03:45:06.000286: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT



```python
# create model
model_t5 = LLMModel(model='google/flan-t5-large')

# create dataset
dataset = pb.DatasetLoader.load_dataset("sst2")

# try part of the dataset
dataset = dataset[:10]

# create prompt
prompt = "As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. Please classify: \nQuestion: {content}\nAnswer:"

# define the projection function required by the output process
def proj_func(pred):
    mapping = {
        "positive": 1,
        "negative": 0
    }
    return mapping.get(pred, -1)

# define the evaluation function required by the attack
def eval_func(prompt, dataset, model):
    preds = []
    labels = []
    for d in dataset:
        input_text = pb.InputProcess.basic_format(prompt, d)
        raw_output = model(input_text)

        output = pb.OutputProcess.cls(raw_output, proj_func)
        preds.append(output)

        labels.append(d["label"])
    
    return pb.Eval.compute_cls_accuracy(preds, labels)
    
# define the unmodifiable words in the prompt
# for example, the labels "positive" and "negative" are unmodifiable, and "content" is modifiable because it is a placeholder
# if your labels are enclosed with '', you need to add \' to the unmodifiable words (due to one feature of textattack)
unmodifiable_words = ["positive\'", "negative\'", "content"]

# print all supported attacks
print(Attack.attack_list())
```

    You are using the default legacy behaviour of the <class 'transformers.models.t5.tokenization_t5.T5Tokenizer'>. This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thouroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565
    Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.


    ['textbugger', 'deepwordbug', 'textfooler', 'bertattack', 'checklist', 'stresstest', 'semantic']



```python
# create attack, specify the model, dataset, prompt, evaluation function, and unmodifiable words
# verbose=True means that the attack will print the intermediate results
attack = Attack(model_t5, "stresstest", dataset, prompt, eval_func, unmodifiable_words, verbose=True)

# print attack result
print(attack.attack())
```

    These words (if they appear in the prompt) are not allowed to be attacked:
    ["positive'", "negative'", 'content']


    /home/v-zhukaijie/anaconda3/envs/promptbench/lib/python3.9/site-packages/transformers/generation/configuration_utils.py:381: UserWarning: `do_sample` is set to `False`. However, `temperature` is set to `0` -- this flag is only used in sample-based generation modes. You should set `do_sample=True` or unset `temperature`.
      warnings.warn(


    --------------------------------------------------
    Current prompt is:  As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. Please classify: 
    Question: {content}
    Answer:
    Current accuracy is:  1.0
    --------------------------------------------------
    
    --------------------------------------------------
    Modifiable words:  ['As', 'a', 'sentiment', 'classifier', 'determine', 'whether', 'the', 'following', 'text', 'is', 'or', 'Please', 'classify', 'Question', 'Answer']
    --------------------------------------------------
    
    --------------------------------------------------
    Current prompt is:  As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. Please classify: 
    Question: {content}
    Answer  and false is not true :
    Current accuracy is:  1.0
    --------------------------------------------------
    
    --------------------------------------------------
    Current prompt is:  As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. Please classify: 
    Question: {content}
    Answer  and true is true  and true is true  and true is true  and true is true  and true is true :
    Current accuracy is:  1.0
    --------------------------------------------------
    
    --------------------------------------------------
    Current prompt is:  As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. Please classify: 
    Question: {content}
    Answer  and true is true :
    Current accuracy is:  1.0
    --------------------------------------------------
    
    {'original prompt': "As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. Please classify: \nQuestion: {content}\nAnswer:", 'original score': 1.0, 'attacked prompt': "As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. Please classify: \nQuestion: {content}\nAnswer  and false is not true :", 'attacked score': 1.0, 'PDR': 0.0}



```python

```
