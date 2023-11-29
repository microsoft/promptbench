from .base import Base
from ..prompts.method_oriented import get_prompt


class EmotionPrompt(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.prompt_id = int(kwargs.get('prompt_id'))
        
        self.emotion_prompt = get_prompt(['emotion_prompt', 'prompts', self.prompt_id])
        
    def query(self, input_text, model):
        instr_get_answer = input_text + ' ' + self.emotion_prompt + '\n' + \
                           f'Please output your answer at the end as ##<your answer ({self.output_range})>'
        prompt_get_answer = model.convert_text_to_prompt(instr_get_answer, 'user')
        
        answer = model(prompt_get_answer)
        
        # print(instr_get_answer)
        # print(answer)
        return answer