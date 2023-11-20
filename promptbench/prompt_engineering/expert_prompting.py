from ..prompts.method_oriented import METHOD_ORIENTED_PROMPTS

 
class ExpertPrompting: 
    def __init__(self, **kwargs): 
        self.few_shot_examples = METHOD_ORIENTED_PROMPTS['expert_prompting']

    def generate_expert_prompt(self, input_text, model): 
        instr_gen_expert_prompt = self.few_shot_examples + '\n' + '[Instruction]: ' + input_text + '\n' + '[Agent Description]:'
        prompt_gen_expert_prompt = model.convert_text_to_prompt(instr_gen_expert_prompt, 'user')
        
        expert_prompt = model(prompt_gen_expert_prompt) 
        
        return expert_prompt    
    
    def query(self, input_text, model):    
        expert_prompt = self.generate_expert_prompt(input_text, model) 

        instr_get_answer = expert_prompt + '\n\n' + \
        'Now given the above identity background, please answer the following instruction:' + \
        '\n\n' + input_text
        prompt_get_answer = model.convert_text_to_prompt(instr_get_answer, 'user')

        answer = model(prompt_get_answer)
        
        return answer
