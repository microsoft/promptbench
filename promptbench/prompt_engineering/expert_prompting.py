# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from .base import Base
from ..prompts.method_oriented import get_prompt

 
class ExpertPrompting(Base): 
    """
    A class designed for generating and utilizing expert-level prompts in AI models.

    This class focuses on creating advanced, expert-level prompts based on input text. It uses few-shot examples to guide the model in generating contextually rich and specialized prompts. These prompts are then used to extract expert-level answers from the model.

    Attributes:
    -----------
    few_shot_examples : str
        Predefined expert-level few-shot examples that aid in guiding the model to generate context-specific, expert prompts.

    Methods:
    --------
    __init__(**kwargs)
        Initializes the ExpertPrompting instance, setting up few-shot examples for expert prompting.
    generate_expert_prompt(input_text, model)
        Generates an expert prompt based on the input text. This method appends few-shot examples to the input text to create a prompt that guides the model in generating an expert-level response.
    query(input_text, model)
        Processes the input text by first generating an expert prompt and then using this prompt to guide the model's response. The method formats the model's response with a specific answer notation, ensuring clarity and precision in the answer provided.
    
    Paper Link: https://arxiv.org/pdf/2305.14688.pdf
    """
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
    
        self.few_shot_examples = get_prompt(['expert_prompt'])

    def generate_expert_prompt(self, input_text, model): 
        instr_gen_expert_prompt = self.few_shot_examples + '\n' + '[Instruction]: ' + input_text + '\n' + '[Agent Description]:'
        prompt_gen_expert_prompt = model.convert_text_to_prompt(instr_gen_expert_prompt, 'user')
        
        expert_prompt = model(prompt_gen_expert_prompt) 
        
        return expert_prompt    
    
    def query(self, input_text, model):    
        expert_prompt = self.generate_expert_prompt(input_text, model) 

        instr_get_answer = expert_prompt + '\n\n' + \
        'Now given the above identity background, please answer the following instruction:' + \
        '\n\n' + input_text + '\n' + f'Please output your answer at the end as ##<your answer ({self.output_range})>'
        prompt_get_answer = model.convert_text_to_prompt(instr_get_answer, 'user')

        answer = model(prompt_get_answer)
        
        if self.verbose:
            print(prompt_get_answer)
            print(answer)
            
        return answer
