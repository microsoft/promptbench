# promptbench Introduction
**PromptBench** is a unified library for evaluating and understanding large language models.


## What does promptbench currently contain?
1. **Quick access your model performance:** We provide a user-friendly interface for quick build models, load dataset, and evaluate model performance.
2. **Prompt Engineering:**
3. **Evaluating adversarial prompts:** promptbench integrated [prompt attacks](https://arxiv.org/abs/2306.04528) [1] for researchers simulate black-box adversarial prompt attacks on the models and evaluate their performances.
4. **Dynamic evaluation to mitigate potential test data contamination:** we integrated the dynamic evaluation framework DyVal [2], which generates evaluation samples on-the-fly with controlled complexity.


## Where should I get started?
If you want to
1. **evaluate my model on existing benchmarks:** please refer to the `examples/basic.ipynb` for constructing your evaluation pipeline. For a multi-modal evaluation pipeline, please refer to `examples/multimodal.ipynb`.
2. **test the effects of different prompting techniques:** 
3. **examine the robustness for prompt attacks**, please refer to `examples/prompt_attack.ipynb` to construct the attacks.
4. **use DyVal for evaluation:** please refer to `examples/dyval.ipynb` to construct DyVal datasets.

