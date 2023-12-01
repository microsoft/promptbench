# PromptBench

<img src="./imgs/promptbench.png" alt="promptbench" style="zoom:100%;" />

**PromptBench** is a unified library for evaluating and understanding large language models.


## What does promptbench currently contain?
1. **Quick access your model performance:** We provide a user-friendly interface for quick build models, load dataset, and evaluate model performance.
2. **Prompt Engineering:**
3. **Evaluating adversarial prompts:** promptbench integrated [prompt attacks](https://arxiv.org/abs/2306.04528) [1] for researchers simulate black-box adversarial prompt attacks on the models and evaluate their performances.
4. **Dynamic evaluation to mitigate potential test data contamination:** we integrated the dynamic evaluation framework [DyVal](https://arxiv.org/pdf/2309.17167) [2], which generates evaluation samples on-the-fly with controlled complexity.


## Where should I get started?
If you want to
1. **evaluate my model on existing benchmarks:** please refer to the `examples/basic.ipynb` for constructing your evaluation pipeline.
2. **test the effects of different prompting techniques:** 
3. **examine the robustness for prompt attacks**, please refer to `examples/prompt_attack.ipynb` to construct the attacks.
4. **use DyVal for evaluation:** please refer to `examples/dyval.ipynb` to construct DyVal datasets.

## Installation
### Install via `pip`

Simply run `pip install promptbench`.

### Install via github

First, clone the repo `git clone git@github.com:microsoft/promptbench.git`.

Then, 

```cmd
cd promptbench
pip install -r requirements.txt
```

## Supported Datasets and Models

### Datasets

We support a range of datasets to facilitate comprehensive analysis, including:

- GLUE: SST-2, CoLA, QQP, MRPC, MNLI, QNLI, RTE, WNLI
- MMLU
- SQuAD V2
- IWSLT 2017
- UN Multi
- Math
- Bool Logic (BigBench)
- Valid Parentheses (BigBench)
- 

### Models

- google/flan-t5-large
- databricks/dolly-v1-6b
- llama2-13b
- llama2-13b-chat
- llama2-7b
- llama2-7b-chat
- vicuna-13b
- vicuna-13b-v1.3
- cerebras/Cerebras-GPT-13B
- EleutherAI/gpt-neox-20b
- google/flan-ul2
- chatgpt
- gpt4


## Acknowledgements

- TextAttack: https://github.com/QData/TextAttack.
- We thank the volunteers: Hanyuan Zhang, Lingrui Li, Yating Zhou for conducting the semantic preserving experiment.
- [1] Zhu, Kaijie, et al. "PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts." arXiv preprint arXiv:2306.04528 (2023).
- [2] Zhu, Kaijie, et al. "DyVal: Graph-informed Dynamic Evaluation of Large Language Models." arXiv preprint arXiv:2309.17167 (2023).



## Citations

If you find this work helpful, please cite it as:
```
@article{zhu2023promptbench,
  title={PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts},
  author={Zhu, Kaijie and Wang, Jindong and Zhou, Jiaheng and Wang, Zichen and Chen, Hao and Wang, Yidong and Yang, Linyi and Ye, Wei and Gong, Neil Zhenqiang and Zhang, Yue and others},
  journal={arXiv preprint arXiv:2306.04528},
  year={2023}
}

@article{zhu2023dyval,
  title={DyVal: Graph-informed Dynamic Evaluation of Large Language Models},
  author={Zhu, Kaijie and Chen, Jiaao and Wang, Jindong and Gong, Neil Zhenqiang and Yang, Diyi and Xie, Xing},
  journal={arXiv preprint arXiv:2309.17167},
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
