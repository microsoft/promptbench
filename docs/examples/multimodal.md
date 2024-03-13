# Multi-Modal Models

This example will walk you throught the basic usage of MULTI-MODAL models in PromptBench. We hope that you can get familiar with the APIs and use it in your own projects later.

First, there is a unified import of `import promptbench as pb` that easily imports the package.


```python
import promptbench as pb
```

    /anaconda/envs/promptbench_1/lib/python3.9/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
      from .autonotebook import tqdm as notebook_tqdm


## Load dataset

First, PromptBench supports easy load of datasets.


```python
# print all supported datasets in promptbench
print('All supported datasets: ')
print(pb.SUPPORTED_DATASETS_VLM)

# load a dataset, MMMMU, for instance.
# if the dataset is not available locally, it will be downloaded automatically.
dataset = pb.DatasetLoader.load_dataset("mmmu")

# print the first 5 examples
dataset[:5]
```

    All supported datasets: 
    ['vqav2', 'nocaps', 'science_qa', 'math_vista', 'ai2d', 'mmmu', 'chart_qa']





    [{'images': [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=733x237>],
      'answer': 'B',
      'question': '<image 1> Baxter Company has a relevant range of production between 15,000 and 30,000 units. The following cost data represents average variable costs per unit for 25,000 units of production. If 30,000 units are produced, what are the per unit manufacturing overhead costs incurred?\nA: $6\nB: $7\nC: $8\nD: $9'},
     {'images': [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=342x310>],
      'answer': 'C',
      'question': 'Assume accounts have normal balances, solve for the one missing account balance: Dividends. Equipment was recently purchased, so there is neither depreciation expense nor accumulated depreciation. <image 1>\nA: $194,815\nB: $182,815\nC: $12,000\nD: $9,000'},
     {'images': [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=336x169>],
      'answer': 'B',
      'question': 'Maxwell Software, Inc., has the following mutually exclusive projects.Suppose the company uses the NPV rule to rank these two projects.<image 1> Which project should be chosen if the appropriate discount rate is 15 percent?\nA: Project A\nB: Project B'},
     {'images': [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=1222x237>],
      'answer': 'D',
      'question': "Each situation below relates to an independent company's Owners' Equity. <image 1> Calculate the missing values of company 2.\nA: $1,620\nB: $12,000\nC: $51,180\nD: $0"},
     {'images': [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=1219x217>],
      'answer': 'B',
      'question': 'The following data show the units in beginning work in process inventory, the number of units started, the number of units transferred, and the percent completion of the ending work in process for conversion. Given that materials are added at the beginning of the process, what are the equivalent units for conversion costs for each quarter using the weighted-average method? Assume that the quarters are independent.<image 1>\nA: 132,625\nB: 134,485\nC: 135,332\nD: 132,685'}]



## Load models

Then, you can easily load VLM models via promptbench.


```python
# print all supported models in promptbench
print('All supported models: ')
print(pb.SUPPORTED_MODELS_VLM)

# load a model, llava-1.5-7b, for instance.
model = pb.VLMModel(model='llava-hf/llava-1.5-7b-hf', max_new_tokens=2048, temperature=0.0001, device='cuda')
```

    All supported models: 
    ['Salesforce/blip2-opt-2.7b', 'Salesforce/blip2-opt-6.7b', 'Salesforce/blip2-flan-t5-xl', 'Salesforce/blip2-flan-t5-xxl', 'llava-hf/llava-1.5-7b-hf', 'llava-hf/llava-1.5-13b-hf', 'gemini-pro-vision', 'gpt-4-vision-preview', 'Qwen/Qwen-VL', 'Qwen/Qwen-VL-Chat', 'qwen-vl-plus', 'qwen-vl-max', 'internlm/internlm-xcomposer2-vl-7b']


    Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
    Loading checkpoint shards: 100%|██████████| 3/3 [00:04<00:00,  1.48s/it]


## Construct prompts

Prompts are the key interaction interface to VLMs. You can easily construct a prompt by call the Prompt API.


```python
# Prompt API supports a list, so you can pass multiple prompts at once.
prompts = pb.Prompt([
    "You are a helpful assistant. Here is the question:{question}\nANSWER:",
    "USER:{question}\nANSWER:",
])
```

## Perform evaluation using prompts, datasets, and models

Finally, you can perform standard evaluation using the loaded prompts, datasets, and labels.


```python
from tqdm import tqdm
for prompt in prompts:
    preds = []
    labels = []
    for data in tqdm(dataset):
        # process input
        input_text = pb.InputProcess.basic_format(prompt, data)
        input_images = data['images']
        label = data['answer']
        raw_pred = model(input_images, input_text)
        # process output
        pred = pb.OutputProcess.pattern_split(raw_pred, 'ANSWER:')
        preds.append(pred)
        labels.append(label)
    
    # evaluate
    score = pb.Eval.compute_cls_accuracy(preds, labels)
    print(f"{score:.3f}, {repr(prompt)}")
```

      0%|          | 0/900 [00:00<?, ?it/s]

    100%|██████████| 900/900 [17:35<00:00,  1.17s/it]  


    0.333, 'You are a helpful assistant. Here is the question:{question}\nANSWER:'


    100%|██████████| 900/900 [17:27<00:00,  1.16s/it]  

    0.316, 'USER:{question}\nANSWER:'


    

