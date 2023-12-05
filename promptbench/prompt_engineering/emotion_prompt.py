# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from .base import Base
from ..prompts.method_oriented import get_prompt


class EmotionPrompt(Base):
    """
    A class for handling emotion-based prompts in a conversational AI model.

    This class is specialized in generating responses for prompts that add some emotions. It leverages a predefined emotion prompt, tailored to the specific needs of the query, to guide the model's response generation.

    Attributes:
    -----------
    prompt_id : int
        An identifier for selecting a specific emotion prompt from a collection of predefined prompts.
    emotion_prompt : str
        The actual emotion-based prompt text, retrieved based on the prompt_id, used to assist the model in generating emotion-aware responses.

    Methods:
    --------
    __init__(**kwargs)
        Initializes the EmotionPrompt instance with specific keyword arguments, including setting the prompt_id and retrieving the corresponding emotion prompt.
        For example: "This is very important to my career."
    query(input_text, model)
        Processes the input text by appending it with the emotion prompt. It then instructs the model to generate a response that is cognizant of the emotional context provided. The response is formatted with a specific answer notation.
    
    Paper Link: https://arxiv.org/pdf/2307.11760v3.pdf
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.prompt_id = int(kwargs.get('prompt_id'))
        
        self.emotion_prompts = get_prompt(['emotion_prompt', 'prompts'])
        self.emotion_prompt = self.emotion_prompts[self.prompt_id]
        
    def query(self, input_text, model):
        instr_get_answer = input_text + '\n' + self.emotion_prompt + '\n' + \
                           f'Please output your answer at the end as ##<your answer ({self.output_range})>'
        prompt_get_answer = model.convert_text_to_prompt(instr_get_answer, 'user')
        
        answer = model(prompt_get_answer)
        
        if self.verbose:
            print(prompt_get_answer)
            print(answer)
        
        return answer