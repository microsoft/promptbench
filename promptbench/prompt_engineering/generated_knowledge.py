from ..prompts.method_oriented import METHOD_ORIENTED_PROMPTS


class GeneratedKnowledge:  
    def __init__(self, **kwargs):      
        self.dataset_name = kwargs.get('dataset')
        self.few_shot_examples = METHOD_ORIENTED_PROMPTS['generated_knowledge'][self.dataset_name]
        
        if self.dataset_name == 'numersense':
            self.direct_answer_trigger = "What is <mask> ?"
        else:  # 自己设计的 designed by myself
            pass
    
    def generate_knowledge(self, input_text, model):  
        instr_gen_knowledge = self.few_shot_examples.replace('{question}', input_text)   
            
        prompt_gen_knowledge = model.convert_text_to_prompt(
            instr_gen_knowledge, 'user' 
        )
        
        # TODO: receive more settings for query
        knowledges = model(prompt_gen_knowledge)
        
        knowledges = list(set([_ for _ in knowledges if _ != '']))
        knowledge  = ' '.join(knowledges) 
        
        return knowledge

    def query(self, input_text, model):  
        knowledge = self.generate_knowledge(input_text, model) 
          
        prompt_get_answer = model.convert_text_to_prompt(
            input_text + '\n' + knowledge + '\n' + self.direct_answer_trigger, 'user'
        )
        res = model(prompt_get_answer)  
        
        # if self.show_process == True: 
        #     self.llm.visualize_prompt(
        #         prompt_converted + [self.llm.convert_message_to_prompt(answer, 'assistant')]
        #     )
        
        return res