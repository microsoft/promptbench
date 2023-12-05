# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from abc import ABC, abstractmethod

from .base import Base
from ..prompts.method_oriented import get_prompt

class BaseCoT(Base):
    """
    A base class for implementing Chain of Thought (CoT) reasoning in models.

    This class serves as a foundational component for models that employ the CoT approach to process and answer queries. It sets up the basic structure and methods that are common across different CoT implementations.

    Attributes:
    -----------
    cot_trigger : str
        A string prompt that activates the Chain of Thought reasoning process in the model.

    Methods:
    --------
    __init__(**kwargs)
        Initializes the BaseCoT instance with specified keyword arguments.
    query(input_text, model)
        An abstract method to be implemented by subclasses, defining how a query is processed and answered by the model.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cot_trigger= get_prompt(['chain_of_thought', 'cot_trigger'])
    
    @abstractmethod
    def query(self, input_text, model):
        pass
    

class ZSCoT(BaseCoT):  
    """
    A class for implementing Zero-Shot Chain of Thought (ZSCoT) reasoning.

    This class is designed for situations where no prior examples (zero-shot) are provided to the model. It utilizes the base CoT approach and extends it to work in a zero-shot learning environment.

    Methods:
    --------
    __init__(**kwargs)
        Initializes the ZSCoT instance with specified keyword arguments.
    query(input_text, model)
        Processes the input text and uses the model to generate a response using zero-shot CoT reasoning. The method constructs a prompt sequence, queries the model, and returns the model's answer.
    
    Paper Link: https://arxiv.org/pdf/2205.11916.pdf
    """
    def __init__(self, **kwargs):      
        super().__init__(**kwargs)
    
    def query(self, input_text, model):   
        prompt_question = model.convert_text_to_prompt(input_text, 'user')
        
        instr_get_answer = self.cot_trigger + '\n' + \
                           f'Please output your answer at the end as ##<your answer ({self.output_range})>'
        prompt_get_answer = model.convert_text_to_prompt(instr_get_answer, 'assistant')
        
        prompt_get_answer = model.concat_prompts([prompt_question, prompt_get_answer])
        
        answer = model(prompt_get_answer)
        
        if self.verbose:
            print(prompt_get_answer)
            print(answer)
        
        return answer


class CoT(BaseCoT):
    """
    Paper
    A class for implementing Chain of Thought (CoT) reasoning with few-shot examples.

    This class enhances the base CoT approach by incorporating few-shot learning, where a small number of example cases are used to guide the model's reasoning process.

    Attributes:
    -----------
    few_shot_examples : str
        A string containing few-shot examples relevant to the dataset_name, aiding the model in understanding and responding to queries.

    Methods:
    --------
    __init__(**kwargs)
        Initializes the CoT instance with specified keyword arguments and loads few-shot examples.
    query(input_text, model)
        Processes the input text and uses the model to generate a response. The method constructs a sequence of prompts, including few-shot examples, to guide the model's reasoning before querying it for an answer.
        
    Paper Link: https://arxiv.org/pdf/2201.11903.pdf
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.few_shot_examples = get_prompt(['chain_of_thought', self.dataset_name])
    
    def query(self, input_text, model):
        instr_question = self.few_shot_examples + '\n'+ 'Q: ' + input_text + '\n' + 'A:'
        prompt_question = model.convert_text_to_prompt(instr_question, 'user')
        instr_get_answer = self.cot_trigger + '\n' + \
                           f'Please output your answer at the end as ##<your answer ({self.output_range})>'
        prompt_get_answer = model.convert_text_to_prompt(instr_get_answer, 'assistant')
        prompt_get_answer = model.concat_prompts([prompt_question, prompt_get_answer])
        
        answer = model(prompt_get_answer)
        
        if self.verbose:
            print(prompt_get_answer)
            print(answer)
        
        return answer
          
        
         
     