from .models import *
"""
Basically, there are 3 args, model, max_new_tokens, and model_dir.
For llama and vicuna model, the model_dir is required.
The max_new_tokens is used to control the length of the output.

Example usage:

from promptbench.models import LLMModel

# Create a T5 model
model_t5 = LLMModel(model='google/flan-t5-large')
output_t5 = model_t5("Translate English to German: 'Hello World'")
print(output_t5)

# Create a LLAMA model and get predictions
model_llama = LLMModel(model='llama2-7b-chat', model_dir=/path/to/your/llama/model)
output_llama = model_llama("How's the weather today?")
print(output_llama)

# List supported models
print(LLMModel.model_list())

Note: Ensure the required models and dependencies are installed and available in the environment.
"""

# Lists of supported model names for different architectures
LLAMA_MODELS = [
    'llama2-7b', 'llama2-7b-chat', 'llama2-13b', 'llama2-13b-chat', 'llama2-70b', 'llama2-70b-chat',
]
GPT_MODELS = ['gpt-3.5-turbo', 'gpt-4']
VICUNA_MODELS = ['vicuna-7b', 'vicuna-13b', 'vicuna-13b-v1.3']
UL2_MODELS = ['google/flan-ul2']

# A dictionary mapping of model architecture to its supported model names
MODEL_LIST = {
    't5': ['google/flan-t5-large'],
    'llama': LLAMA_MODELS,
    'gpt': GPT_MODELS,
    'vicuna': VICUNA_MODELS,
    'ul2': UL2_MODELS,
}

class LLMModel(object):
    """
    A class that provides an interface for various language models.
    It supports model creation, and inference based on model name.
    """

    def __init__(self, **kwargs):
        self.model = kwargs.get('model')
        self.infer_model = self.create_model(**kwargs)

    def create_model(self, **kwargs):
        """Creates and returns the appropriate model based on the model name."""

        # Dictionary mapping of model names to their respective classes
        model_mapping = {
            'google/flan-t5-large': T5Model,
            **{model: LlamaModel for model in LLAMA_MODELS},
            **{model: OpenAIModel for model in GPT_MODELS},
            **{model: VicunaModel for model in VICUNA_MODELS},
            **{model: UL2Model for model in UL2_MODELS},
        }

        # Get the model class based on the model name and instantiate it
        model_class = model_mapping.get(self.model)
        if model_class:
            return model_class(**kwargs)
        else:
            raise ValueError("The model is not supported!")

    @staticmethod
    def model_list():
        """Returns a dictionary of supported models."""
        return MODEL_LIST

    def __call__(self, input_text, **kwargs):
        """Predicts the output based on the given input text using the loaded model."""
        return self.infer_model.predict(input_text, **kwargs)
