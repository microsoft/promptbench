# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from ..prompts.method_oriented import get_prompt
from .base import Base


class GeneratedKnowledge(Base):  
    """
    A class for generating and utilizing synthesized knowledge in AI model queries.

    This class specializes in creating synthesized knowledge based on input text and few-shot examples. It generates context-specific knowledge snippets, which are then used to enhance the model's ability to provide informed and relevant answers to queries.

    Attributes:
    -----------
    few_shot_examples : str
        Custom few-shot examples specific to the dataset, used to guide the model in generating relevant synthesized knowledge.

    Methods:
    --------
    __init__(**kwargs)
        Initializes the GeneratedKnowledge instance, loading few-shot examples tailored to the dataset name provided in the keyword arguments.
    generate_knowledge(input_text, model)
        Generates synthesized knowledge based on the input text. This method utilizes few-shot examples and modifies them with the input question to create a prompt that instructs the model to generate knowledge snippets.
    query(input_text, model)
        Processes the input text by first generating synthesized knowledge and then using this knowledge to enhance the query's context. The method then prompts the model to generate an answer, ensuring that the response is informed by the newly generated knowledge. The final answer is formatted with a specific notation for clarity.
    
    Paper Link: https://arxiv.org/pdf/2110.08387.pdf
    """
    
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
        
        knowledges = list(set([_ for _ in knowledges if _ != '']))
        knowledge  = '\n'.join(knowledges) 
        
        if self.verbose:
            print(prompt_gen_knowledge)
            print(knowledge)
        
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
        
        if self.verbose:
            print(prompt_get_answer)
            print(answer)
        
        return answer