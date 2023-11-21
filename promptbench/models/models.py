# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
from abc import ABC, abstractmethod


class LMMBaseModel(ABC):
    def __init__(self, model, max_new_tokens):
        self.model = model
        self.max_new_tokens = max_new_tokens

    @abstractmethod
    def predict(self, input_text, **kwargs):
        pass

    def __call__(self, input_text, **kwargs):
        return self.predict(input_text, **kwargs)


class T5Model(LMMBaseModel):

    def __init__(self, model, max_new_tokens):
        super(T5Model, self).__init__(model, max_new_tokens)
        from transformers import T5Tokenizer, T5ForConditionalGeneration

        self.tokenizer = T5Tokenizer.from_pretrained(
            self.model, device_map="auto")
        self.pipe = T5ForConditionalGeneration.from_pretrained(
            self.model, device_map="auto")

    def predict(self, input_text):
        input_ids = self.tokenizer(
            input_text, return_tensors="pt").input_ids.to("cuda")
        outputs = self.pipe.generate(
            input_ids, max_new_tokens=self.max_new_tokens)
        out = self.tokenizer.decode(outputs[0])
        return out


class UL2Model(LMMBaseModel):

    def __init__(self, model, max_new_tokens):
        super(UL2Model, self).__init__(model, max_new_tokens)
        from transformers import AutoTokenizer, T5ForConditionalGeneration

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model, device_map="auto")
        self.pipe = T5ForConditionalGeneration.from_pretrained(
            self.model, device_map="auto")

    def predict(self, input_text):
        input_ids = self.tokenizer(
            input_text, return_tensors="pt").input_ids.to("cuda")
        outputs = self.pipe.generate(
            input_ids, max_new_tokens=self.max_new_tokens)
        out = self.tokenizer.decode(outputs[0])
        return out


class LlamaModel(LMMBaseModel):

    def __init__(self, model, max_new_tokens, model_dir=None):
        super(LlamaModel, self).__init__(model, max_new_tokens)

        from transformers import LlamaForCausalLM, LlamaTokenizer, AutoTokenizer, AutoModelForCausalLM
        if model_dir is None:
            self.tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-13b-hf", device_map="auto")
            self.pipe = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-13b-hf", device_map="auto")
        else:
            self.tokenizer = LlamaTokenizer.from_pretrained(model_dir, device_map="auto")
            self.pipe = LlamaForCausalLM.from_pretrained(model_dir, device_map="auto")

    def predict(self, input_text):
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
        outputs = self.pipe.generate(input_ids, max_new_tokens=self.max_new_tokens)
        out = self.tokenizer.decode(outputs, skip_special_tokens=True, clean_up_tokenization_spaces=False)
        
        return out[len(input_text):]


class VicunaModel(LMMBaseModel):

    def __init__(self, model, max_new_tokens, model_dir):
        super(VicunaModel, self).__init__(model, max_new_tokens)

        from transformers import AutoModelForCausalLM, AutoTokenizer

        self.tokenizer = AutoTokenizer.from_pretrained(model_dir, device_map="auto", use_fast=False)
        self.pipe = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto")

    def predict(self, input_text):
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
        outputs = self.pipe.generate(input_ids, max_new_tokens=self.max_new_tokens)
        out = self.tokenizer.decode(outputs[0])
        
        return out


class OpenAIModel(LMMBaseModel):

    def __init__(self, model, max_new_tokens, openai_key, temperature, sleep_time=3):
        super(OpenAIModel, self).__init__(model, max_new_tokens)
        self.openai_key = openai_key
        self.temperature = temperature
        self.sleep_time = sleep_time

    def sleep(self, seconds):
        import random
        import time
        time.sleep(seconds + random.random())

    def predict(self, input_text):
        
        import openai
        openai.api_key = self.openai_key
        try:
            while True:
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[
                        {"role": "user", "content": input_text},
                    ],
                    temperature=self.temperature,
                )
                result = response['choices'][0]['message']['content']
                return result
            
        except Exception as e:
            print(e)
            print("Retrying...")
            self.sleep(self.sleep_time)