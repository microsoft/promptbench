# Prompt Attack

```python
import promptbench as pb
from promptbench.models import LLMModel
from promptbench.prompt_attack import Attack
```

    /home/v-zhukaijie/anaconda3/envs/promptbench/lib/python3.8/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
      from .autonotebook import tqdm as notebook_tqdm
    2023-11-29 05:19:50.047471: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 FMA
    To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.



```python
# create model
model_t5 = LLMModel(model='google/flan-t5-large')

# create dataset
dataset = pb.DatasetLoader.load_dataset("sst2")

# create prompt
prompt = "As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. Please classify: \nQuestion: {content}\nAnswer:"

# define the input process function, output process function, and evaluation function
input_process_func = pb.InputProcess.basic_format
output_process_func = pb.OutputProcess.cls
eval_func = pb.Eval.compute_cls_accuracy

# define the unmodifiable words in the prompt
# for example, "positive" and "negative" are unmodifiable, and "content" is modifiable because it is a placeholder
unmodifiable_words = ["positive", "negative", "content"]

# create attack, specify the model, dataset, prompt, input process function, output process function, evaluation function, and unmodifiable words
attack = Attack(model_t5, "stresstest", dataset, prompt, input_process_func, output_process_func, eval_func, unmodifiable_words)

# print attack result
print(attack.attack())
```

    You are using the default legacy behaviour of the <class 'transformers.models.t5.tokenization_t5.T5Tokenizer'>. This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thouroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565
    Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.

    These words (if they appear in the prompt) are not allowed to be attacked:
    ['positive', 'negative', 'content']

    /home/v-zhukaijie/anaconda3/envs/promptbench/lib/python3.8/site-packages/transformers/generation/configuration_utils.py:381: UserWarning: `do_sample` is set to `False`. However, `temperature` is set to `0` -- this flag is only used in sample-based generation modes. You should set `do_sample=True` or unset `temperature`.
      warnings.warn(

    (0.0, "As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. Please classify: \nQuestion: {content}\nAnswer  and false is not true :", 0.0, 0.0)

