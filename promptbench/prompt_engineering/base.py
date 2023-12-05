# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

class Base:
    def __init__(self, **kwargs): 
        self.dataset_name  = kwargs.get('dataset')
        self.verbose = kwargs.get('verbose', False)
        
        if self.dataset_name == "gsm8k":
            self.output_range = "arabic numerals"
        elif self.dataset_name == "csqa":
            self.output_range = "among A through E"
        elif self.dataset_name == "bigbench_date":
            self.output_range = "among A through F"
        elif self.dataset_name == "bigbench_object_tracking":
            self.output_range = "among A through C"
        elif self.dataset_name == "qasc":
            self.output_range = "among A through H"
        elif self.dataset_name == "numersense":
            self.output_range = "numbers expressed in English words, e.g. 'one', 'two', 'three', ..." 
        elif self.dataset_name == "last_letter_concat":
            self.output_range = "English letter combinations, e.g. 'afsa', 'abgsa', ..."
        else:
            self.output_range = "No format restrictions"
            
    
    def query(self, input_text, model):
        instr_get_answer = input_text  + '\n' + \
                           f'Please output your answer at the end as ##<your answer ({self.output_range})>'
        prompt_get_answer = model.convert_text_to_prompt(instr_get_answer, 'user')
        
        answer = model(prompt_get_answer)
        
        # print(instr_get_answer)
        # print(answer)
        return answer
        