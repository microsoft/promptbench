# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from ..prompts.method_oriented import get_prompt
from .base import Base

class LeastToMost(Base):  
    """
    A class designed to implement the 'least-to-most' prompting strategy in AI models.

    This class utilizes a step-by-step approach, breaking down complex problems into simpler sub-problems. It leverages few-shot examples tailored to specific datasets to guide the model in sequentially addressing each part of a problem, ultimately leading to a comprehensive solution.

    Attributes:
    -----------
    few_shot : str
        Custom few-shot examples specific to the dataset name provided in the keyword arguments. These examples serve as templates to guide the model in breaking down and solving problems step-by-step.

    Methods:
    --------
    __init__(**kwargs)
        Initializes the LeastToMost instance, setting up few-shot examples based on the provided dataset name.
    query(input_text, model)
        Processes the input text using the 'least-to-most' approach. It first breaks down the problem into sub-problems using the few-shot examples and then sequentially solves each sub-problem. The method combines these steps to construct a comprehensive answer to the original problem. The final answer is formatted with a specific notation for clarity and consistency.
        
    Paper Link: https://arxiv.org/pdf/2205.10625.pdf
    """
    def __init__(self, **kwargs):      
        super().__init__(**kwargs)
        
        self.few_shot = get_prompt(['least_to_most', self.dataset_name])

    def query(self, input_text, model):    
        instr_breakdown = self.few_shot + '\n\n' + 'Q: ' + input_text + '\n' + 'A: Let’s break down this problem, then solve it one by one.'
        prompt_breakdown = model.convert_text_to_prompt(instr_breakdown, 'user')
        
        # break down problem to sub-problems and solve them one by one
        ans_subproblem = model(prompt_breakdown)    
        answer_trigger = f'Please output your answer at the end as ##<your answer ({self.output_range})>'
        
        prompt_get_answer = model.concat_prompts([prompt_breakdown, 
                                           model.convert_text_to_prompt(ans_subproblem, 'assistant'),
                                           model.convert_text_to_prompt(answer_trigger, 'user')
                                        ])
        answer = model(prompt_get_answer)       

        if self.verbose:
            print(prompt_get_answer)
            print(answer)
        
        return answer 
    


