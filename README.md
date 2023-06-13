# PromptBench

![](https://wjdcloud.blob.core.windows.net/tools/promptbench-overview.jpg)

PromptBench is a powerful tool designed to scrutinize and analyze the interaction of large language models with various prompts. It provides a convenient infrastructure to simulate ** black-box ** adversarial ** prompt ** attacks on the models and evaluate their performances. This repository hosts the necessary codebase, datasets, and instructions to facilitate these experiments.

## Repository Structure

The repository is organized into several directories, each housing specific components of the project:

- `adv_prompts/*.md`: This directory stores the raw information related to adversarial attacks.
- `data/`: This is the storage point for datasets used in the experiments.
- `metrics/`: It contains evaluation metrics for translation tasks and the SQuAD V2 dataset.
- `prompt_attack/`: This directory contains the implementation of prompt attacks, which is based on the [TextAttack](https://github.com/QData/TextAttack) framework.
- `prompts/`: This contains the clean zero-shot and few-shot prompts for various datasets.
- `config.py`: This script hosts the configuration of our experiments, such as labels and OpenAI API keys.
- `dataload.py`: This script is responsible for loading the dataset.
- `inference.py`: It is used to load the models and perform predictions.
- `transfer.py`: This contains the code for testing the transferability of adversarial prompts.
- `visualize.py`: It houses the code for visualizing input attention.

## Supported Datasets and Models

### Datasets

We support a range of datasets to facilitate comprehensive analysis, including:

- GLUE: SST-2, CoLA, QQP, MRPC, MNLI, QNLI, RTE, WNLI
- MMLU
- SQuAD V2
- IWSLT 2017
- UN Multi
- Math



### Models

- google/flan-t5-large
- databricks/dolly-v1-6b
- llama-13b
- vicuna-13
- cerebras/Cerebras-GPT-13B
- EleutherAI/gpt-neox-20b
- google/flan-ul2
- chatgpt

Note that for LLaMa and Vicuna model, you are supposed to download by yourself and assign the  --model_dir your_model_path.

For ChatGPT, you are required to fill the OpenAI API key in config.py.

## Installation

First, clone the repo by `git clone git@github.com:microsoft/promptbench.git` or just download the zip format.

The environment can be set up using Conda. Run the following command to create the environment from the provided `environment.yml` file:

```
conda env create -f environment.yml
```

## Adversarial Attacks

Here are some example commands to run adversarial attacks:

```
# dataset: sst2, cola, qqp, mrpc, mnli, qnli, rte, wnli, mmlu, squad, iwslt, un_multi, math
# model: google/flan-t5-large, vicuna-13b, google/flan-ul2, chatgpt, llama-13b, databricks/dolly-v1-6b, cerebras/Cerebras-GPT-13B, EleutherAI/gpt-neox-20b
# attack: textbugger, deepwordbug, bertattack, textfooler, checklist, stresstest, semantic
# shot: 0 or 3 (3 means fewshot)
# generate_len for each model and each dataset can be found in config.py


# For running GLUE dataset
python main.py --model google/flan-t5-large --dataset mnli --attack textfooler --shot 0 --generate_len 20

# For running MMLU, SQuAD V2, IWSLT, UN Multi, and Math dataset
python main.py --model google/flan-t5-large --dataset mmlu --attack semantic --shot 0 --generate_len 20
```

## Results

The main results are shown in the following tables. For more descriptions and discussions, please refer to the paper.

![](https://wjdcloud.blob.core.windows.net/tools/promptbench-res1.jpg)

<img src="https://wjdcloud.blob.core.windows.net/tools/promptbench-res2.jpg" style="width: 50%;"/>

<img src="https://wjdcloud.blob.core.windows.net/tools/promptbench-res3.jpg" style="width: 50%;"/>

## Adversarial Prompts

All generated adversarial prompts are housed in the `adv_prompts/` directory.

For a more user-friendly experience and to explore the adversarial prompts in detail, please visit [demo site](https://huggingface.co/spaces/March07/PromptBench).

## Acknowledgements

- TextAttack: https://github.com/QData/TextAttack.

## Citations

If you find this work helpful, please cite it as:
```
@misc{PromptBench2023,
  author = {Zhu, Kaijie and Wang, Jindong and Zhou, Jiaheng and Wang, Zeek and Chen, Hao and Wang, Yidong and Yang, Linyi and Ye, Wei and Gong, Neil Zhenqiang and Zhang, Yue and Xie, Xing},
  title = {PromptBench: towards evaluating the robustness of large language models to adversarial prompts},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/microsoft/promptbench}},
}
```


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
