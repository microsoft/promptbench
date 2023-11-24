from abc import ABC, abstractmethod

from .base import Base
from ..prompts.method_oriented import get_prompt

class BaseCoT(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cot_trigger= get_prompt(['chain_of_thought', 'cot_trigger'])
        
        if self.dataset_name == "aqua":
            self.direct_answer_trigger = "Therefore, among A through E, the answer is"
        elif self.dataset_name == "gsm8k":
            self.direct_answer_trigger = "Therefore, the answer (arabic numerals) is"
        elif self.dataset_name == "addsub":
            self.direct_answer_trigger = "Therefore, the answer (arabic numerals) is"
        elif self.dataset_name == "multiarith":
            self.direct_answer_trigger = "Therefore, the answer (arabic numerals) is"
        elif self.dataset_name == "strategyqa":
            self.direct_answer_trigger = "Therefore, the answer (Yes or No) is"
        elif self.dataset_name == "svamp":
            self.direct_answer_trigger = "Therefore, the answer (arabic numerals) is"
        elif self.dataset_name == "singleeq":
            self.direct_answer_trigger = "Therefore, the answer (arabic numerals) is"
        elif self.dataset_name == "bigbench_date":
            self.direct_answer_trigger = "Therefore, among A through F, the answer is"
        elif self.dataset_name == "bigbench_object_tracking":
            self.direct_answer_trigger = "Therefore, among A through C, the answer is"
        elif self.dataset_name == "coin_flip":
            self.direct_answer_trigger = "Therefore, the answer (Yes or No) is"
        elif self.dataset_name == "last_letters":
            self.direct_answer_trigger = "Therefore, the answer is"
        elif self.dataset_name == "csqa":
            self.direct_answer_trigger = "Therefore, among A through E, the answer is"
    
    @abstractmethod
    def query(self, input_text, model):
        pass
    

class ZSCoT(BaseCoT):  
    def __init__(self, **kwargs):      
        super().__init__(**kwargs)
    
    def query(self, input_text, model):   
        prompt_question = model.convert_text_to_prompt(input_text, 'user')
        
        instr_get_answer = self.cot_trigger + '\n' + \
                           f'Please output your answer at the end as ##<your answer ({self.output_range})>'
        prompt_get_answer = model.convert_text_to_prompt(instr_get_answer, 'assistant')
        
        prompt_get_answer = model.concat_prompts([prompt_question, prompt_get_answer])
        
        answer = model(prompt_get_answer)

        # print(answer)
        return answer
    
        # if self.show_process == True: 
        #     self.llm.visualize_prompt(
        #         prompt + [{'role': 'assistant', 'content': answer}] 
        #     ) 

class CoT(BaseCoT):
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
        
        # print(instr_question)
        # print(instr_get_answer)
        # print(answer)
        return answer
          
        
         
     