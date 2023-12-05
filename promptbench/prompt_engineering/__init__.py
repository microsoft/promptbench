# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from tqdm import tqdm
import re

from .base import Base
from .least_to_most import LeastToMost
from .generated_knowledge import GeneratedKnowledge
from .chain_of_thought import ZSCoT, CoT
from .expert_prompting import ExpertPrompting
from .emotion_prompt import EmotionPrompt

from ..metrics import Eval

SUPPORTED_METHODS = ['CoT', 'ZSCoT', 'least_to_most', 'generated_knowledge', 'expert_prompting', 'emotion_prompt', 'baseline']

METHOD_MAP = {
    'CoT': CoT,
    'ZSCoT': ZSCoT,
    'least_to_most': LeastToMost,
    'generated_knowledge': GeneratedKnowledge,
    'expert_prompting': ExpertPrompting,
    'emotion_prompt': EmotionPrompt,
    'baseline': Base,
}

METHOD_SUPPORT_DATASET = {
    'CoT': ['gsm8k', 'csqa', 'bigbench_date', 'bigbench_object_tracking'],
    'ZSCoT': ['gsm8k', 'csqa', 'bigbench_date', 'bigbench_object_tracking'],
    'expert_prompting': ['gsm8k', 'csqa', 'bigbench_date', 'bigbench_object_tracking'],
    'emotion_prompt': ['gsm8k', 'csqa', 'bigbench_date', 'bigbench_object_tracking'],
    'least_to_most': ['gsm8k', 'last_letter_concat'],
    'generated_knowledge': ['csqa', 'numersense', 'qasc'],
    'baseline': ['gsm8k', 'csqa', 'bigbench_date', 'bigbench_object_tracking', 'last_letter_concat', 'numersense', 'qasc'],
}

# Model: GPT3.5, GPT4, Llama7b-chat, Llama13b-chat, llama70b-chat

class PEMethod(object):
    """
    A class that provides an interface for various methods in prompt engineering.
    It supports method creation, and inference based on method name.
    """
    
    def __init__(self, **kwargs):
        self.method = kwargs.get('method')
        self.infer_method = self.create_method(**kwargs)
    
    def create_method(self, **kwargs):
        """Creates and returns the appropriate method based on the method name."""
        
        # Get the method class based on the method name and instantiate it
        method_class = METHOD_MAP.get(self.method)
        if method_class:
            return method_class(**kwargs)
        else:
            raise ValueError("The method is not supported!")
    
    @staticmethod
    def method_list():
        """Returns a list of supported methods."""
        return METHOD_MAP.keys()
    
    def test(self, dataset, model, num_samples=None):
        """Tests the method on the given dataset and returns the accuracy."""""
        preds = []
        labels = []
        for i, data in enumerate(tqdm(dataset)):
            if num_samples and i >= num_samples:
                break
            
            label = data['label']
            labels.append(label)
            
            input_text = data['content']
            ouput = self.infer_method.query(input_text, model)
            res = re.findall(r'##(.*)', ouput)
            pred = res[0] if res else ouput
            pred = dataset.extract_answer(pred)  #FIXME 执行取片操作后丢失类
            preds.append(pred)
            
        score = Eval.compute_cls_accuracy(preds, labels)
        return score    
        
    def __call__(self, input_text, model):
        """Calls the method to perform inference."""
        return self.infer_method.query(input_text, model)
    