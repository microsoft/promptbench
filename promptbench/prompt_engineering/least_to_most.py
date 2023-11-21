from ..prompts.method_oriented import METHOD_ORIENTED_PROMPTS


# TODO: 写一个map，用来记录每个方法可用的数据集，进行统一检查

class LeastToMost:  
    def __init__(self, **kwargs):      
        self.dataset_name = kwargs.get('dataset') 
        
        self.instruct_head = METHOD_ORIENTED_PROMPTS['least_to_most'][self.dataset_name]
        
        if self.dataset_name == 'gsm8k':
            self.direct_answer_trigger = "Therefore, the answer (arabic numerals) is"
        elif self.dataset_name == 'bigbench_date':
            self.direct_answer_trigger = "Therefore, among A through F, the answer is"

    def query(self, input_text, model):    
        instr_breakdown = self.instruct_head + '\n\n' + 'Q: ' + input_text + '\n' + 'A: Let’s break down this problem:'
        prompt_breakdown = model.convert_text_to_prompt(instr_breakdown, 'user')
        
        # break down problem to sub-problems and solve them one by one
        ans_subproblem = model(prompt_breakdown)    
        
        prompt_get_answer = model.concat_prompts([prompt_breakdown, 
                                           model.convert_text_to_prompt(ans_subproblem, 'assistant'),
                                           model.convert_text_to_prompt(self.direct_answer_trigger, 'user')
                                        ])
        answer = model(prompt_get_answer)       
        
        print(ans_subproblem)
        print(answer) 

        return answer 
    


