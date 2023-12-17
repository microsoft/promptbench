# Adversarial Prompt Attack

Check our paper: [PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts](https://arxiv.org/abs/2306.04528).

## Prompt Attacks
### Definition
Given an LLM $f_\theta$, a dataset $\mathcal{D} = \{ (x_i, y_i)\}_{i \in [N]}$, and a clean prompt $P$, the objective of a prompt attack can be formulated as follows:
$$
\mathop{\max}_{\delta \in \mathcal{C}} \sum_{(x; y) \in \mathcal{D}} \mathcal{L} [f_\theta([P+\delta, x]), y],
$$
where $\delta$ is the textual perturbation added to the clean prompt $P$ and $\mathcal{C}$ is the allowable perturbation set, i.e., perturbation constraint. 

### $4$ levels of attacks
- Character-level: We employ TextBugger [1] and DeepWordBug [2], which manipulate texts by introducing typos or errors to words, e.g., by adding, deleting, repeating, replacing, and permuting characters for certain words.
- Word-level: We use BertAttack [3] and TextFooler [4], which aim to replace words with synonyms or contextually similar words to deceive LLMs.
- Sentence-level: We implement StressTest [5] and CheckList [6], which append irrelevant or extraneous sentences to the end of prompts, intending to distract LLMs.
For the StressTest attack, we append `and true is true`, `and false is not true`, or `and true is true` for five times to the end of a prompt. For the CheckList attack, we generate $50$ random sequences consisting of alphabets and digits, each with a length of $10$, and append this random sequence to the end of a prompt.
- Semantic-level: We simulate the linguistic behavior of people from different countries by choosing $6$ common languages (Chinese, French, Arabic, Spanish, Japanese, and Korean) and constructing $10$ prompts for each language per dataset. These prompts are then translated into English, introducing linguistic nuances and variations that could potentially impact LLMs.

## Results
### Evaluation Metric

we introduce a unified metric, the **Performance Drop Rate (PDR)**. PDR quantifies the relative performance decline following a prompt attack, offering a contextually normalized measure for comparing different attacks, datasets, and models.
The PDR is given by:
$$
\mathit{PDR}(A, P, f_\theta, \mathcal{D}) = 1 - \frac{\sum_{(x;y) \in \mathcal{D}} { \mathcal{M} [ f_{\theta}([A(P), x]), y]}}{ \sum_{(x;y) \in \mathcal{D}} {\mathcal{M} [f_{\theta}([P, x]), y]}},
$$
where $A$ is the adversarial attack applied to prompt $P$, and $\mathcal{M}[\cdot]$ is the evaluation function: for classification task, $\mathcal{M}[\cdot]$ is the indicator function $\mathbb{1}[\hat{y}, y]$ which equals to $1$ when $\hat{y} = y$, and $0$ otherwise; for reading comprehension task, $\mathcal{M}[\cdot]$ is the F1-score; for translation tasks, $\mathcal{M}[\cdot]$ is the Bleu metric \cite{bleu}. Note that a negative PDR implies that adversarial prompts can occasionally enhance the performance. 



The main results are shown in the following tables. For more descriptions and discussions, please refer to the paper.



### Results on Different Attacks

| **Dataset**  | **TextBugger**             | **DeepWordBug**            | **TextFooler**             | **BertAttack**             | **CheckList**              | **StressTest**              | **Semantic**               |
|:------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:---------------------------:|:--------------------------:|
| **SST-2**    | 0.26(±0.39) | 0.21(±0.36) | 0.36(±0.41) | 0.33(±0.43) | 0.27(±0.39) | 0.17(±0.34)  | 0.28(±0.36) |
| **CoLA**     | 0.37(±0.39) | 0.29(±0.36) | 0.45(±0.35) | 0.46(±0.38) | 0.25(±0.32) | 0.21(±0.28)  | 0.27(±0.35) |
| **QQP**      | 0.20(±0.32) | 0.18(±0.27) | 0.28(±0.34) | 0.31(±0.36) | 0.13(±0.25) | -0.00(±0.21) | 0.30(±0.36) |
| **MRPC**     | 0.24(±0.33) | 0.21(±0.30) | 0.29(±0.35) | 0.37(±0.34) | 0.13(±0.27) | 0.20(±0.30)  | 0.28(±0.36) |
| **MNLI**     | 0.26(±0.37) | 0.18(±0.31) | 0.30(±0.40) | 0.38(±0.37) | 0.16(±0.26) | 0.11(±0.27)  | 0.11(±0.04) |
| **QNLI**     | 0.36(±0.39) | 0.41(±0.36) | 0.54(±0.39) | 0.56(±0.38) | 0.22(±0.37) | 0.18(±0.26)  | 0.35(±0.33) |
| **RTE**      | 0.24(±0.37) | 0.22(±0.36) | 0.28(±0.38) | 0.31(±0.38) | 0.19(±0.32) | 0.18(±0.25)  | 0.28(±0.33) |
| **WNLI**     | 0.28(±0.36) | 0.26(±0.35) | 0.31(±0.37) | 0.32(±0.34) | 0.19(±0.30) | 0.19(±0.26)  | 0.36(±0.32) |
| **MMLU**     | 0.18(±0.22) | 0.11(±0.15) | 0.20(±0.18) | 0.40(±0.30) | 0.14(±0.20) | 0.03(±0.16)  | 0.17(±0.17) |
| **SQuAD V2** | 0.09(±0.17) | 0.05(±0.08) | 0.27(±0.29) | 0.32(±0.32) | 0.02(±0.03) | 0.02(±0.04)  | 0.07(±0.09) |
| **IWSLT**    | 0.09(±0.14) | 0.11(±0.12) | 0.29(±0.30) | 0.13(±0.18) | 0.10(±0.10) | 0.17(±0.19)  | 0.18(±0.14) |
| **UN Multi** | 0.06(±0.08) | 0.08(±0.12) | 0.17(±0.19) | 0.10(±0.16) | 0.06(±0.07) | 0.09(±0.11)  | 0.15(±0.18) |
| **Math**     | 0.19(±0.17) | 0.15(±0.13) | 0.53(±0.36) | 0.44(±0.32) | 0.16(±0.11) | 0.13(±0.08)  | 0.23(±0.13) |
| **Avg**      | **0.23(±0.33)** | **0.20(±0.30)** | **0.33(±0.36)** | **0.35(±0.36)** | **0.16(±0.27)** | **0.13(±0.25)** | **0.24(±0.29)** |



### Results on Different Models

| **Dataset**  | **T5**                     | **Vicuna**                 | **UL2**                    | **ChatGPT**              |
|:------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
| **SST-2**    | 0.04(±0.11) | 0.83(±0.26) | 0.03(±0.12) | 0.17(±0.29) |
| **CoLA**     | 0.16(±0.19) | 0.81(±0.22) | 0.13(±0.20) | 0.21(±0.31) |
| **QQP**      | 0.09(±0.15) | 0.51(±0.41) | 0.02(±0.04) | 0.16(±0.30) |
| **MRPC**     | 0.17(±0.26) | 0.52(±0.40) | 0.06(±0.10) | 0.22(±0.29) |
| **MNLI**     | 0.08(±0.13) | 0.67(±0.38) | 0.06(±0.12) | 0.13(±0.18) |
| **QNLI**     | 0.33(±0.25) | 0.87(±0.19) | 0.05(±0.11) | 0.25(±0.31) |
| **RTE**      | 0.08(±0.13) | 0.78(±0.23) | 0.02(±0.04) | 0.09(±0.13) |
| **WNLI**     | 0.13(±0.14) | 0.78(±0.27) | 0.04(±0.03) | 0.14(±0.12) |
| **MMLU**     | 0.11(±0.18) | 0.41(±0.24) | 0.05(±0.11) | 0.14(±0.18) |
| **SQuAD V2** | 0.05(±0.12) | -                          | 0.10(±0.18) | 0.22(±0.28) |
| **IWSLT**    | 0.14(±0.17) | -                          | 0.15(±0.11) | 0.17(±0.26) |
| **UN Multi** | 0.13(±0.14) | -                          | 0.05(±0.05) | 0.12(±0.18) |
| **Math**     | 0.24(±0.21) | -                          | 0.21(±0.21) | 0.33(±0.31) |
| **Avg**      | **0.13(±0.19)** | **0.69(±0.34)** | **0.08(±0.14)** | **0.18(±0.26)** |



### Results on Different Types of Prompts

| **Dataset**  | **ZS-task**                | **ZS-role**                | **FS-task**                | **FS-role**                |
|:------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
| **SST-2**    | 0.29(±0.38) | 0.24(±0.34) | 0.26(±0.42) | 0.28(±0.41) |
| **CoLA**     | 0.40(±0.34) | 0.40(±0.37) | 0.25(±0.31) | 0.26(±0.39) |
| **QQP**      | 0.32(±0.40) | 0.25(±0.41) | 0.11(±0.18) | 0.11(±0.17) |
| **MRPC**     | 0.30(±0.38) | 0.42(±0.41) | 0.12(±0.15) | 0.13(±0.19) |
| **MNLI**     | 0.23(±0.32) | 0.22(±0.32) | 0.20(±0.32) | 0.23(±0.36) |
| **QNLI**     | 0.38(±0.37) | 0.45(±0.39) | 0.32(±0.37) | 0.35(±0.37) |
| **RTE**      | 0.25(±0.33) | 0.25(±0.34) | 0.23(±0.34) | 0.25(±0.37) |
| **WNLI**     | 0.28(±0.30) | 0.30(±0.35) | 0.27(±0.35) | 0.26(±0.34) |
| **MMLU**     | 0.21(±0.22) | 0.19(±0.23) | 0.18(±0.25) | 0.13(±0.21) |
| **SQuAD V2** | 0.16(±0.26) | 0.20(±0.28) | 0.06(±0.11) | 0.07(±0.12) |
| **IWSLT**    | 0.18(±0.22) | 0.24(±0.25) | 0.08(±0.09) | 0.11(±0.10) |
| **UN Multi** | 0.17(±0.18) | 0.15(±0.16) | 0.04(±0.07) | 0.04(±0.07) |
| **Math**     | 0.33(±0.26) | 0.39(±0.30) | 0.16(±0.18) | 0.17(±0.17) |
| **Avg**      | **0.27(±0.33)** | **0.29(±0.35)** | **0.18(±0.29)** | **0.19(±0.30)** |



## Visualization of Attention on Input

The visualization code is in `visualize.py`.

<img src="../../imgs/prompt_attack_attention.png" alt="fig-attention" style="zoom:100%;" />



## Transferability of Adversarial Prompts

|   **Attacks**   | **ChatGPT $\rightarrow$ T5** | **ChatGPT $\rightarrow$ UL2** | **ChatGPT$\rightarrow$ Vicuna** | **T5 $\rightarrow$ ChatGPT** | **T5 $\rightarrow$ UL2** | **T5 $\rightarrow$ V**icuna | **UL2 $\rightarrow$ ChatGPT** | **UL2 $\rightarrow$ T5** | **UL2 $\rightarrow$ V**icuna | **Vicuna $\rightarrow$ ChatGPT** | **Vicuna $\rightarrow$ T5** | **Vicuna $\rightarrow$ UL2** |
| :-------------: | :--------------------------: | :---------------------------: | :-----------------------------: | :--------------------------: | :----------------------: | :-------------------------: | :---------------------------: | :----------------------: | :--------------------------: | :------------------------------: | :-------------------------: | :--------------------------: |
| **BertAttack**  |       0.05(±0.17)        |        0.08(±0.19)        |         0.08(±0.88)         |       0.18(±0.32)        |     0.11(±0.23)      |      -1.39(±5.67)       |        0.15(±0.27)        |     0.05(±0.11)      |       -0.70(±3.18)       |         0.06(±0.19)          |       0.05(±0.11)       |       0.03(±0.12)        |
|  **CheckList**  |       0.00(±0.04)        |        0.01(±0.03)        |         0.19(±0.39)         |       0.00(±0.07)        |     0.01(±0.03)      |      -0.09(±0.64)       |        0.01(±0.06)        |     0.01(±0.04)      |       -0.13(±1.80)       |         -0.01(±0.04)         |       0.00(±0.01)       |       0.00(±0.00)        |
| **TextFooler**  |       0.04(±0.08)        |        0.03(±0.09)        |        -0.25(±1.03)         |       0.11(±0.23)        |     0.08(±0.16)      |      -0.30(±2.09)       |        0.11(±0.21)        |     0.07(±0.18)      |       -0.17(±1.46)       |         0.04(±0.16)          |       0.02(±0.06)       |       0.00(±0.01)        |
| **TextBugger**  |       -0.00(±0.09)       |       -0.01(±0.05)        |         0.02(±0.94)         |       0.04(±0.15)        |     0.01(±0.04)      |      -0.45(±3.43)       |        0.04(±0.13)        |     0.02(±0.07)      |       -0.84(±4.42)       |         0.03(±0.13)          |       0.01(±0.05)       |       0.00(±0.01)        |
| **DeepWordBug** |       0.03(±0.11)        |        0.01(±0.03)        |         0.10(±0.46)         |       0.00(±0.06)        |     0.01(±0.02)      |      -0.18(±1.20)       |        0.01(±0.10)        |     0.02(±0.06)      |       -0.09(±0.75)       |         0.00(±0.03)          |       0.02(±0.11)       |       0.00(±0.01)        |
| **StressTest**  |       0.04(±0.17)        |        0.03(±0.10)        |         0.01(±0.48)         |       -0.01(±0.06)       |     0.03(±0.06)      |       0.04(±0.80)       |        0.00(±0.04)        |     0.05(±0.16)      |       0.06(±0.45)        |         0.00(±0.04)          |       0.09(±0.18)       |       0.02(±0.08)        |
|  **Semantic**   |       0.04(±0.12)        |        0.02(±0.06)        |         0.25(±0.47)         |       0.07(±0.27)        |     0.00(±0.03)      |      -0.81(±4.14)       |        0.02(±0.11)        |     -0.13(±0.72)     |       -0.50(±1.59)       |         0.07(±0.11)          |       0.00(±0.05)       |       0.00(±0.02)        |



## Adversarial Prompts

All generated adversarial prompts are housed in the `adv_prompts/` directory.

For a more user-friendly experience and to explore the adversarial prompts in detail, please visit [demo site](https://huggingface.co/spaces/March07/PromptBench).



## Acknowledgements
- TextAttack: https://github.com/QData/TextAttack.
- We thank the volunteers: Hanyuan Zhang, Lingrui Li, Yating Zh0u for conducting the semantic preserving experiment.

## References
[1] Li, Jinfeng, et al. "Textbugger: Generating adversarial text against real-world applications." arXiv preprint arXiv:1812.05271 (2018).

[2] Gao, Ji, et al. "Black-box generation of adversarial text sequences to evade deep learning classifiers." 2018 IEEE Security and Privacy Workshops (SPW). IEEE, 2018.

[3] Li, Linyang, et al. "Bert-attack: Adversarial attack against bert using bert." arXiv preprint arXiv:2004.09984 (2020).

[4] Jin, Di, et al. "Is bert really robust? natural language attack on text classification and entailment." arXiv preprint arXiv:1907.11932 2 (2019): 10.

[5] Naik, Aakanksha, et al. "Stress test evaluation for natural language inference." arXiv preprint arXiv:1806.00692 (2018).

[6] Ribeiro, Marco Tulio, et al. "Beyond accuracy: Behavioral testing of NLP models with CheckList." arXiv preprint arXiv:2005.04118 (2020).

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