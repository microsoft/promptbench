Each module in promptbench can be easily extended. In the following, we provide basic guidelines for customizing your own datasets, models, prompt engineering methods, and evaluation metrics.

## Add new datasets
Adding new datasets involves two steps:

- Implementing a New Dataset Class: Datasets are supposed to be implemented in `dataload/dataset.py` and inherit from the `Dataset` class. For your custom dataset, implement the `__init__` method to load your dataset. We recommend organizing your data samples as dictionaries to facilitate the input process.
- Adding an Interface: After customizing the dataset class, register it in the `DataLoader` class within `dataload.py`.



## Add new models
Similar to adding new datasets, the addition of new models also consists of two steps.
- Implementing a New Model Class: Models should be implemented in `dataload/model.py`, inheriting from the `LLMModel` class. In your customized model, you should implement `self.tokenizer` and `self.model`. You may also customize your own `predict` function for inference. If the `predict` function is not customized, the default `predict` function inherited from `LLMModel` will be used.
- Adding an Interface: After customizing the model class, register it in the `_create_model` function within the `class LLMModel` in `__init__.py`.



## Add new prompt engineering methods
Adding new methods in prompt engineering is similar to steps of C.1 and C.2.

- Implementing a New Methods Class: Methods should be implemented in \\ `prompt\_engineering` Module. Firstly, create a new `.py` file for your methods.
    Then implement two functions: `\_\_init\_\_` and `query`. For unified management, two points need be noticed: 1. all methods should inherits from `Base` class that has common code for prompt engineering methods. 2. prompts used in methods should be stored in `prompts/method\_oriented.py`.
- Adding an Interface: After implementing a new methods, register it in the `METHOD\_MAP` that is used to map method names to their corresponding class.


## Add new metrics and input/output process functions
New evaluation metrics should be implemented as static functions in `class Eval` within the `metrics` module. Similarly, new input/output process functions should be implemented as static functions in `class InputProcess` and `class OutputProcess` in the `utils` module.