from abc import ABC, abstractmethod

from ..prompts.method_oriented import METHOD_ORIENTED_PROMPTS

class Base:
    def __init__(self, **kwargs):
        self.cot_trigger = METHOD_ORIENTED_PROMPTS['chain_of_thought']['cot_trigger']      
        self.dataset_name = kwargs.get('dataset')
        
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
        elif self.dataset_name == "object_tracking":
            self.direct_answer_trigger = "Therefore, among A through C, the answer is"
        elif self.dataset_name == "coin_flip":
            self.direct_answer_trigger = "Therefore, the answer (Yes or No) is"
        elif self.dataset_name == "last_letters":
            self.direct_answer_trigger = "Therefore, the answer is"
    
    @abstractmethod
    def query(self, input_text, model):
        pass
    

class ZSCoT(Base):  
    def __init__(self, **kwargs):      
        super().__init__(**kwargs)
    
    def query(self, input_text, model):   
        prompt_question = model.convert_text_to_prompt(input_text, 'user')
        prompt_zscot = model.convert_text_to_prompt(self.cot_trigger, 'assistant')
        
        prompt_get_chain_path = model.concat_prompts([prompt_question, prompt_zscot])
        
        chain_path = model(prompt_get_chain_path)
        
        instr_cot = self.cot_trigger + '\n' + chain_path + '\n' + self.direct_answer_trigger
        prompt_cot = model.convert_text_to_prompt(instr_cot, 'assistant')
        
        prompt_get_answer = model.concat_prompts([prompt_question, prompt_cot])
        answer = model(prompt_get_answer)  
        
        # print(chain_path)
        # print(answer)
        return answer
    
        # if self.show_process == True: 
        #     self.llm.visualize_prompt(
        #         prompt + [{'role': 'assistant', 'content': answer}] 
        #     ) 

class CoT(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.few_shot_examples = METHOD_ORIENTED_PROMPTS['chain_of_thought'][self.dataset_name]['few_shot']
    
    def query(self, input_text, model):
        instr_question = self.few_shot_examples + '\n'+ 'Q: ' + input_text + '\n' + 'A:'
        prompt_question = model.convert_text_to_prompt(instr_question, 'user')
        prompt_cot = model.convert_text_to_prompt(self.cot_trigger, 'assistant')
        prompt_get_answer = model.concat_prompts([prompt_question, prompt_cot])
        answer = model(prompt_get_answer)
        return answer
          
        
         
     