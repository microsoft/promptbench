class Base:
    def __init__(self, **kwargs): 
        self.dataset_name  = kwargs.get('dataset')
        
        if self.dataset_name == "gsm8k":
            self.output_range = "arabic numerals"
        elif self.dataset_name == "csqa":
            self.output_range = "among A through E"
        elif self.dataset_name == "bigbench_date":
            self.output_range = "among A through F"
        elif self.dataset_name == "bigbench_object_tracking":
            self.output_range = "among A through C"
    
    def query(self, input_text, model):
        instr_get_answer = input_text  + '\n' + \
                           f'Please output your answer at the end as ##<your answer ({self.output_range})>'
        prompt_get_answer = model.convert_text_to_prompt(instr_get_answer, 'user')
        
        answer = model(prompt_get_answer)
        
        # print(instr_get_answer)
        # print(answer)
        return answer
        