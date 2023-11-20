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
    
    def convert_text_to_prompt(self, text, role):
        """Constructs multi_turn conversation for complex methods in prompt engineering."""
        if self.model == ['gpt4', 'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0301', 'gpt-3.5-turbo']:
            return {'role': role, 'content': text} 
        else:
            return str(role) + ': ' + str(text) + '\n'

    def concat_prompts(self, prompt_list):
        """Concatenates the prompts into a single prompt."""
        if self.model == ['gpt4', 'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0301', 'gpt-3.5-turbo']:
            return self._gpt_concat_prompts(prompt_list)
        else:
            return self._other_concat_prompts(prompt_list)
        
    def _gpt_concat_prompts(self, prompt_list):
        """
        Concatenate prompts from various inputs into a single list of dictionaries.

        The function accepts any number of keyword arguments, each of which can be either
        a dictionary or a list of dictionaries. It concatenates all inputs into a single list.

        Returns:
            A list of dictionaries containing all the prompts from the input arguments.
        """
        # Initialize an empty list to hold all dictionaries
        all_prompts = []

        # Iterate over each keyword argument
        for arg in prompt_list:
            # Check if the argument is a dictionary, and if so, add it to the list
            if isinstance(arg, dict):
                all_prompts.append(arg)
            # Check if the argument is a list of dictionaries
            elif isinstance(arg, list) and all(isinstance(item, dict) for item in arg):
                # Extend the list with the dictionaries from the current argument
                all_prompts.extend(arg)
            else:
                raise ValueError("All arguments must be dictionaries or lists of dictionaries.")

        return all_prompts

    def _other_concat_prompts(self, prompt_list):
        """
        Concatenate prompts from various inputs into a single strings.

        The function accepts any number of keyword arguments, each of which must be
        a string. It concatenates all inputs into a single string.

        Returns:
            A string containing all the prompts from the input arguments.
        """
        # Initialize an empty string to hold all prompts
        all_prompts = ""

        # Iterate over each keyword argument
        for arg in prompt_list:
            # Check if the argument is a string, and if so, add it to the list
            if isinstance(arg, str):
                all_prompts = all_prompts + '\n' + arg
            else:
                raise ValueError("All arguments must be strings.")

        return all_prompts
    
    def __call__(self, input_text, **kwargs):
        """Predicts the output based on the given input text using the loaded model."""
        return self.infer_model.predict(input_text, **kwargs)
