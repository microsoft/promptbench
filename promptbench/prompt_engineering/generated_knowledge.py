from ..prompts.method_oriented import get_prompt
from .base import Base


class GeneratedKnowledge(Base):  
    def __init__(self, **kwargs):      
        super().__init__(**kwargs)
        
        self.few_shot_examples = get_prompt(['generated_knowledge', self.dataset_name])
    
    def generate_knowledge(self, input_text, model):  
        instr_gen_knowledge = self.few_shot_examples.replace('{question}', input_text)   
            
        prompt_gen_knowledge = model.convert_text_to_prompt(
            instr_gen_knowledge, 'user' 
        )
        
        # TODO: receive more settings for query
        knowledges = model(prompt_gen_knowledge, temperature=1.0, n=1, max_tokens=60)
        # print(knowledges)
        
        knowledges = list(set([_ for _ in knowledges if _ != '']))
        knowledge  = '\n'.join(knowledges) 
        
        # print(knowledge)
        return knowledge

    def query(self, input_text, model):  
        if "Answer Choices" in input_text:
            raw_question = input_text.split("Answer Choices", 1)[0]
        else:
            raw_question = input_text
        
        knowledge = self.generate_knowledge(raw_question, model) 
          
        instr_get_answer = knowledge + '\n\n' + input_text + '\n' + \
                           f'Please output your answer at the end as ##<your answer({self.output_range})>'
        prompt_get_answer = model.convert_text_to_prompt(
            instr_get_answer, 'user'
        )
        answer = model(prompt_get_answer)  
        
        # if self.show_process == True: 
        #     self.llm.visualize_prompt(
        #         prompt_converted + [self.llm.convert_message_to_prompt(answer, 'assistant')]
        #     )
        # print(instr_get_answer)
        # print(answer)
        
        return answer