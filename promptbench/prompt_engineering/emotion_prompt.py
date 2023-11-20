from ..prompts.method_oriented import METHOD_ORIENTED_PROMPTS


class EmotionPrompt:
    def __init__(self, **kwargs):
        self.prompt_id = kwargs.get('prompt_id')
        self.dataset_name = kwargs.get('dataset')
        
        self.emotion_prompt = METHOD_ORIENTED_PROMPTS['emotion_prompts']['prompts'][self.prompt_id]
        
    def query(self, input_text, model):
        instr_get_answer = input_text + ', ' + self.emotion_prompt
        prompt_get_answer = model.convert_text_to_prompt(instr_get_answer, 'user')
        
        answer = model(prompt_get_answer)
        
        return answer