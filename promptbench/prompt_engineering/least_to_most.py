from ..prompts.method_oriented import get_prompt
from .base import Base

class LeastToMost(Base):  
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
        
        # print(ans_subproblem)
        # print(answer) 

        return answer 
    


