import os 
import sys 
import numpy as np
from pathlib import Path 
from typing import List 
import random 

class AskMeAnything: 
    def __init__(self, llm, args):      
        self.llm  = llm
        self.args = args
        self.data_name = args['dataset']['name']    
        if args['dataset']['name'] == 'anli_r1':  
            self.question_prompt_path = args['method']['ask_me_anything']['anli_r1']['question_prompt_path'] 
            self.answer_prompt_path   = args['method']['ask_me_anything']['anli_r1']['answer_prompt_path']
            with open(self.question_prompt_path, 'r') as f: 
                self.question_prompt = f.read()  
            with open(self.answer_prompt_path, 'r') as f: 
                self.answer_prompt = f.read() 
            self.trigger = ' Based on the context , '
        self.show_process = args['show_process'] 

    """
    Statement : There is no information indicating whether Daniel Zolnikov is a good legislator or not
    .
    Question :
    """
    def translate_question(self, question): 
        question_aug = self.question_prompt + '\n\nStatement : ' + question + '\n\nQuestion : ' 
        question_aug = [self.llm.convert_message_to_prompt(question_aug, 'user')] 
        translated_question = self.llm.query(question_aug)
        return translated_question
    
    def query(self, question_input): 
        if self.data_name == 'anli_r1': 
            question = self.translate_question(question_input['question']) 
            question = self.answer_prompt + '\n\nContext : ' + \
            question_input['context'] + '\n' + 'Question :' + self.trigger + \
            question + '\n' + 'Answer : '
            
            query_prompt = [self.llm.convert_message_to_prompt(question, 'user')] 

            answer = self.llm.query(query_prompt) 

            if self.show_process == True:
                self.llm.visualize_prompt(
                    query_prompt + [self.llm.convert_message_to_prompt(answer, 'assistant')]
                )

            return answer 
        # pass 
