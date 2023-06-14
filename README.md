# PromptBench

<img src="./imgs/fig-promptbench.pdf" alt="image-20230612192645202" style="zoom:100%;" />

PromptBench is a powerful tool designed to scrutinize and analyze the interaction of large language models with various prompts. It provides a convenient infrastructure to simulate **black-box** adversarial  **prompt attacks** on the models and evaluate their performances. This repository hosts the necessary codebase, datasets, and instructions to facilitate these experiments.



Check our paper: [PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts](https://arxiv.org/abs/2306.04528).



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



#### Create your own dataset

You can customize your own dataset in `dataload.py`, the details can be found in `dataload.py/class Dataset`.

Next, you should customize the function that **process of the input** in `inference.py`, e.g., `process_input` and `_process_cls_input`.

Additionally, you should fill the `config.py LABEL_SET, GENERATE_LEN`. The LABEL_SET is used to prevent attacks on words that is label (or some words that is important for task, e.g. the word 'translation' for translation tasks.)



### Models

- google/flan-t5-large
- databricks/dolly-v1-6b
- llama-13b
- vicuna-13
- cerebras/Cerebras-GPT-13B
- EleutherAI/gpt-neox-20b
- google/flan-ul2
- chatgpt

Note that for LLaMa and Vicuna model, you are supposed to download by yourself and assign the  `--model_dir your_model_path`.

For ChatGPT, you are required to fill the OpenAI API key in `config.py`.



#### Create your own model

You can customize your own model by adding it into `inference.py create_model`.

Next, add the model into `config.py MODEL_SET`.

Finally, you should customize the function that process the output of the function in `inference.py process_pred`.



## Installation

First, clone the repo by `git clone git@github.com:microsoft/promptbench.git` or just download the zip format.

The environment can be set up using Conda. Run the following command to create the environment from the provided `environment.yml` file:

```
conda env create -f environment.yml
```



## Prompt Attacks

Here are some example commands to run prompt attacks:

```python
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



## Inference

If you would like to inference on certain prompt to obtain the accuracy, follow the code in `main.py` to construct model and dataset. Then use the following command to predict:

```
score = inference_model.predict(prompt)
```



## Results

### Evaluation Metric

we introduce a unified metric, the \emph{Performance Drop Rate} (PDR). PDR quantifies the relative performance decline following a prompt attack, offering a contextually normalized measure for comparing different attacks, datasets, and models.
The PDR is given by:
$$
\mathit{PDR}(A, P, f_\theta, \mathcal{D}) = 1 - \frac{\sum_{(x;y) \in \mathcal{D}} { \mathcal{M} [ f_{\theta}([A(P), x]), y]}}{ \sum_{(x;y) \in \mathcal{D}} {\mathcal{M} [f_{\theta}([P, x]), y]}},
$$
where $A$ is the adversarial attack applied to prompt $P$, and $\mathcal{M}[\cdot]$ is the evaluation function: for classification task, $\mathcal{M}[\cdot]$ is the indicator function $\mathbb{1}[\hat{y}, y]$ which equals to $1$ when $\hat{y} = y$, and $0$ otherwise; for reading comprehension task, $\mathcal{M}[\cdot]$ is the F1-score; for translation tasks, $\mathcal{M}[\cdot]$ is the Bleu metric \cite{bleu}. Note that a negative PDR implies that adversarial prompts can occasionally enhance the performance. 



The main results are shown in the following tables. For more descriptions and discussions, please refer to the paper.



### Results on Differeent Attacks

| **Dataset**  | **TextBugger**             | **DeepWordBug**            | **TextFooler**             | **BertAttack**             | **CheckList**              | **StressTest**              | **Semantic**               |
|:------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:---------------------------:|:--------------------------:|
| **SST-2**    | 0.26($\pm$0.39) | 0.21($\pm$0.36) | 0.36($\pm$0.41) | 0.33($\pm$0.43) | 0.27($\pm$0.39) | 0.17($\pm$0.34)  | 0.28($\pm$0.36) |
| **CoLA**     | 0.37($\pm$0.39) | 0.29($\pm$0.36) | 0.45($\pm$0.35) | 0.46($\pm$0.38) | 0.25($\pm$0.32) | 0.21($\pm$0.28)  | 0.27($\pm$0.35) |
| **QQP**      | 0.20($\pm$0.32) | 0.18($\pm$0.27) | 0.28($\pm$0.34) | 0.31($\pm$0.36) | 0.13($\pm$0.25) | -0.00($\pm$0.21) | 0.30($\pm$0.36) |
| **MRPC**     | 0.24($\pm$0.33) | 0.21($\pm$0.30) | 0.29($\pm$0.35) | 0.37($\pm$0.34) | 0.13($\pm$0.27) | 0.20($\pm$0.30)  | 0.28($\pm$0.36) |
| **MNLI**     | 0.26($\pm$0.37) | 0.18($\pm$0.31) | 0.30($\pm$0.40) | 0.38($\pm$0.37) | 0.16($\pm$0.26) | 0.11($\pm$0.27)  | 0.11($\pm$0.04) |
| **QNLI**     | 0.36($\pm$0.39) | 0.41($\pm$0.36) | 0.54($\pm$0.39) | 0.56($\pm$0.38) | 0.22($\pm$0.37) | 0.18($\pm$0.26)  | 0.35($\pm$0.33) |
| **RTE**      | 0.24($\pm$0.37) | 0.22($\pm$0.36) | 0.28($\pm$0.38) | 0.31($\pm$0.38) | 0.19($\pm$0.32) | 0.18($\pm$0.25)  | 0.28($\pm$0.33) |
| **WNLI**     | 0.28($\pm$0.36) | 0.26($\pm$0.35) | 0.31($\pm$0.37) | 0.32($\pm$0.34) | 0.19($\pm$0.30) | 0.19($\pm$0.26)  | 0.36($\pm$0.32) |
| **MMLU**     | 0.18($\pm$0.22) | 0.11($\pm$0.15) | 0.20($\pm$0.18) | 0.40($\pm$0.30) | 0.14($\pm$0.20) | 0.03($\pm$0.16)  | 0.17($\pm$0.17) |
| **SQuAD V2** | 0.09($\pm$0.17) | 0.05($\pm$0.08) | 0.27($\pm$0.29) | 0.32($\pm$0.32) | 0.02($\pm$0.03) | 0.02($\pm$0.04)  | 0.07($\pm$0.09) |
| **IWSLT**    | 0.09($\pm$0.14) | 0.11($\pm$0.12) | 0.29($\pm$0.30) | 0.13($\pm$0.18) | 0.10($\pm$0.10) | 0.17($\pm$0.19)  | 0.18($\pm$0.14) |
| **UN Multi** | 0.06($\pm$0.08) | 0.08($\pm$0.12) | 0.17($\pm$0.19) | 0.10($\pm$0.16) | 0.06($\pm$0.07) | 0.09($\pm$0.11)  | 0.15($\pm$0.18) |
| **Math**     | 0.19($\pm$0.17) | 0.15($\pm$0.13) | 0.53($\pm$0.36) | 0.44($\pm$0.32) | 0.16($\pm$0.11) | 0.13($\pm$0.08)  | 0.23($\pm$0.13) |
| **Avg**      | **0.23($\pm$0.33)** | **0.20($\pm$0.30)** | **0.33($\pm$0.36)** | **0.35($\pm$0.36)** | **0.16($\pm$0.27)** | **0.13($\pm$0.25)** | **0.24($\pm$0.29)** |



### Results on Differeent Models

| **Dataset**  | **T5**                     | **Vicuna**                 | **UL2**                    | **ChatGPT**              |
|:------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
| **SST-2**    | 0.04($\pm$0.11) | 0.83($\pm$0.26) | 0.03($\pm$0.12) | 0.17($\pm$0.29) |
| **CoLA**     | 0.16($\pm$0.19) | 0.81($\pm$0.22) | 0.13($\pm$0.20) | 0.21($\pm$0.31) |
| **QQP**      | 0.09($\pm$0.15) | 0.51($\pm$0.41) | 0.02($\pm$0.04) | 0.16($\pm$0.30) |
| **MRPC**     | 0.17($\pm$0.26) | 0.52($\pm$0.40) | 0.06($\pm$0.10) | 0.22($\pm$0.29) |
| **MNLI**     | 0.08($\pm$0.13) | 0.67($\pm$0.38) | 0.06($\pm$0.12) | 0.13($\pm$0.18) |
| **QNLI**     | 0.33($\pm$0.25) | 0.87($\pm$0.19) | 0.05($\pm$0.11) | 0.25($\pm$0.31) |
| **RTE**      | 0.08($\pm$0.13) | 0.78($\pm$0.23) | 0.02($\pm$0.04) | 0.09($\pm$0.13) |
| **WNLI**     | 0.13($\pm$0.14) | 0.78($\pm$0.27) | 0.04($\pm$0.03) | 0.14($\pm$0.12) |
| **MMLU**     | 0.11($\pm$0.18) | 0.41($\pm$0.24) | 0.05($\pm$0.11) | 0.14($\pm$0.18) |
| **SQuAD V2** | 0.05($\pm$0.12) | -                          | 0.10($\pm$0.18) | 0.22($\pm$0.28) |
| **IWSLT**    | 0.14($\pm$0.17) | -                          | 0.15($\pm$0.11) | 0.17($\pm$0.26) |
| **UN Multi** | 0.13($\pm$0.14) | -                          | 0.05($\pm$0.05) | 0.12($\pm$0.18) |
| **Math**     | 0.24($\pm$0.21) | -                          | 0.21($\pm$0.21) | 0.33($\pm$0.31) |
| **Avg**      | **0.13($\pm$0.19)** | **0.69($\pm$0.34)** | **0.08($\pm$0.14)** | **0.18($\pm$0.26)** |



### Results on Different Types of Prompts

| **Dataset**  | **ZS-task**                | **ZS-role**                | **FS-task**                | **FS-role**                |
|:------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
| **SST-2**    | 0.29($\pm$0.38) | 0.24($\pm$0.34) | 0.26($\pm$0.42) | 0.28($\pm$0.41) |
| **CoLA**     | 0.40($\pm$0.34) | 0.40($\pm$0.37) | 0.25($\pm$0.31) | 0.26($\pm$0.39) |
| **QQP**      | 0.32($\pm$0.40) | 0.25($\pm$0.41) | 0.11($\pm$0.18) | 0.11($\pm$0.17) |
| **MRPC**     | 0.30($\pm$0.38) | 0.42($\pm$0.41) | 0.12($\pm$0.15) | 0.13($\pm$0.19) |
| **MNLI**     | 0.23($\pm$0.32) | 0.22($\pm$0.32) | 0.20($\pm$0.32) | 0.23($\pm$0.36) |
| **QNLI**     | 0.38($\pm$0.37) | 0.45($\pm$0.39) | 0.32($\pm$0.37) | 0.35($\pm$0.37) |
| **RTE**      | 0.25($\pm$0.33) | 0.25($\pm$0.34) | 0.23($\pm$0.34) | 0.25($\pm$0.37) |
| **WNLI**     | 0.28($\pm$0.30) | 0.30($\pm$0.35) | 0.27($\pm$0.35) | 0.26($\pm$0.34) |
| **MMLU**     | 0.21($\pm$0.22) | 0.19($\pm$0.23) | 0.18($\pm$0.25) | 0.13($\pm$0.21) |
| **SQuAD V2** | 0.16($\pm$0.26) | 0.20($\pm$0.28) | 0.06($\pm$0.11) | 0.07($\pm$0.12) |
| **IWSLT**    | 0.18($\pm$0.22) | 0.24($\pm$0.25) | 0.08($\pm$0.09) | 0.11($\pm$0.10) |
| **UN Multi** | 0.17($\pm$0.18) | 0.15($\pm$0.16) | 0.04($\pm$0.07) | 0.04($\pm$0.07) |
| **Math**     | 0.33($\pm$0.26) | 0.39($\pm$0.30) | 0.16($\pm$0.18) | 0.17($\pm$0.17) |
| **Avg**      | **0.27($\pm$0.33)** | **0.29($\pm$0.35)** | **0.18($\pm$0.29)** | **0.19($\pm$0.30)** |



## Visualization of Attention on Input

The visualization code is in `visualize.py`.

<img src="./imgs/attention.png" alt="fig-attention" style="zoom:100%;" />



## Transferability of Adversarial Prompts

|   **Attacks**   | **ChatGPT $\rightarrow$ T5** | **ChatGPT $\rightarrow$ UL2** | **ChatGPT$\rightarrow$ Vicuna** | **T5 $\rightarrow$ ChatGPT** | **T5 $\rightarrow$ UL2** | **T5 $\rightarrow$ V**icuna | **UL2 $\rightarrow$ ChatGPT** | **UL2 $\rightarrow$ T5** | **UL2 $\rightarrow$ V**icuna | **Vicuna $\rightarrow$ ChatGPT** | **Vicuna $\rightarrow$ T5** | **Vicuna $\rightarrow$ UL2** |
| :-------------: | :--------------------------: | :---------------------------: | :-----------------------------: | :--------------------------: | :----------------------: | :-------------------------: | :---------------------------: | :----------------------: | :--------------------------: | :------------------------------: | :-------------------------: | :--------------------------: |
| **BertAttack**  |       0.05($\pm$0.17)        |        0.08($\pm$0.19)        |         0.08($\pm$0.88)         |       0.18($\pm$0.32)        |     0.11($\pm$0.23)      |      -1.39($\pm$5.67)       |        0.15($\pm$0.27)        |     0.05($\pm$0.11)      |       -0.70($\pm$3.18)       |         0.06($\pm$0.19)          |       0.05($\pm$0.11)       |       0.03($\pm$0.12)        |
|  **CheckList**  |       0.00($\pm$0.04)        |        0.01($\pm$0.03)        |         0.19($\pm$0.39)         |       0.00($\pm$0.07)        |     0.01($\pm$0.03)      |      -0.09($\pm$0.64)       |        0.01($\pm$0.06)        |     0.01($\pm$0.04)      |       -0.13($\pm$1.80)       |         -0.01($\pm$0.04)         |       0.00($\pm$0.01)       |       0.00($\pm$0.00)        |
| **TextFooler**  |       0.04($\pm$0.08)        |        0.03($\pm$0.09)        |        -0.25($\pm$1.03)         |       0.11($\pm$0.23)        |     0.08($\pm$0.16)      |      -0.30($\pm$2.09)       |        0.11($\pm$0.21)        |     0.07($\pm$0.18)      |       -0.17($\pm$1.46)       |         0.04($\pm$0.16)          |       0.02($\pm$0.06)       |       0.00($\pm$0.01)        |
| **TextBugger**  |       -0.00($\pm$0.09)       |       -0.01($\pm$0.05)        |         0.02($\pm$0.94)         |       0.04($\pm$0.15)        |     0.01($\pm$0.04)      |      -0.45($\pm$3.43)       |        0.04($\pm$0.13)        |     0.02($\pm$0.07)      |       -0.84($\pm$4.42)       |         0.03($\pm$0.13)          |       0.01($\pm$0.05)       |       0.00($\pm$0.01)        |
| **DeepWordBug** |       0.03($\pm$0.11)        |        0.01($\pm$0.03)        |         0.10($\pm$0.46)         |       0.00($\pm$0.06)        |     0.01($\pm$0.02)      |      -0.18($\pm$1.20)       |        0.01($\pm$0.10)        |     0.02($\pm$0.06)      |       -0.09($\pm$0.75)       |         0.00($\pm$0.03)          |       0.02($\pm$0.11)       |       0.00($\pm$0.01)        |
| **StressTest**  |       0.04($\pm$0.17)        |        0.03($\pm$0.10)        |         0.01($\pm$0.48)         |       -0.01($\pm$0.06)       |     0.03($\pm$0.06)      |       0.04($\pm$0.80)       |        0.00($\pm$0.04)        |     0.05($\pm$0.16)      |       0.06($\pm$0.45)        |         0.00($\pm$0.04)          |       0.09($\pm$0.18)       |       0.02($\pm$0.08)        |
|  **Semantic**   |       0.04($\pm$0.12)        |        0.02($\pm$0.06)        |         0.25($\pm$0.47)         |       0.07($\pm$0.27)        |     0.00($\pm$0.03)      |      -0.81($\pm$4.14)       |        0.02($\pm$0.11)        |     -0.13($\pm$0.72)     |       -0.50($\pm$1.59)       |         0.07($\pm$0.11)          |       0.00($\pm$0.05)       |       0.00($\pm$0.02)        |



## Adversarial Prompts

All generated adversarial prompts are housed in the `adv_prompts/` directory.

For a more user-friendly experience and to explore the adversarial prompts in detail, please visit [demo site](https://huggingface.co/spaces/March07/PromptBench).



## Acknowledgements

- TextAttack: https://github.com/QData/TextAttack.
- We thank the volunteers that conduct the semantic preserving experiment.



## Citations

If you find this work helpful, please cite it as:
```
@article{zhu2023promptbench,
  title={PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts},
  author={Zhu, Kaijie and Wang, Jindong and Zhou, Jiaheng and Wang, Zichen and Chen, Hao and Wang, Yidong and Yang, Linyi and Ye, Wei and Gong, Neil Zhenqiang and Zhang, Yue and others},
  journal={arXiv preprint arXiv:2306.04528},
  year={2023}
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
