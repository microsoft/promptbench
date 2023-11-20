# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
from abc import ABC, abstractmethod


class LMMBaseModel(ABC):
    def __init__(self, **kwargs):
        self.raw_dataset = None
        self.model = kwargs.get('model', None)
        self.max_new_tokens = kwargs.get('max_new_tokens', 20)

    @abstractmethod
    def predict(self, input_text, **kwargs):
        pass

    def __call__(self, input_text, **kwargs):
        return self.predict(input_text, **kwargs)


class T5Model(LMMBaseModel):

    def __init__(self, **kwargs):
        super(T5Model, self).__init__(**kwargs)
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

    def __init__(self, **kwargs):
        super(UL2Model, self).__init__(**kwargs)
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

    def __init__(self, **kwargs):
        super(LlamaModel, self).__init__(**kwargs)
        model_dir = kwargs.get('model_dir', None)
        if not model_dir:
            raise ValueError("model_dir is required for llama model!")

        from transformers import LlamaForCausalLM, LlamaTokenizer

        self.tokenizer = LlamaTokenizer.from_pretrained(
            model_dir, device_map="auto")
        self.pipe = LlamaForCausalLM.from_pretrained(
            model_dir, device_map="auto")

    def predict(self, input_text):
        input_ids = self.tokenizer(
            input_text, return_tensors="pt").input_ids.to("cuda")
        generate_ids = self.pipe.generate(
            input_ids, max_new_tokens=self.max_new_tokens)
        out = self.tokenizer.batch_decode(
            generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        return out


class VicunaModel(LMMBaseModel):

    def __init__(self, **kwargs):
        super(VicunaModel, self).__init__(**kwargs)
        model_dir = kwargs.get('model_dir', None)
        if not model_dir:
            raise ValueError("model_dir is required for llama model!")

        from transformers import AutoModelForCausalLM, AutoTokenizer

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_dir, device_map="auto", use_fast=False)
        self.pipe = AutoModelForCausalLM.from_pretrained(
            model_dir, device_map="auto")

    def predict(self, input_text):
        input_ids = self.tokenizer(
            input_text, return_tensors="pt").input_ids.to("cuda")
        outputs = self.pipe.generate(
            input_ids, max_new_tokens=self.max_new_tokens)
        out = self.tokenizer.decode(outputs[0])
        return out


class OpenAIModel(LMMBaseModel):

    def __init__(self, **kwargs):
        super(OpenAIModel, self).__init__(**kwargs)
        self.openai_key = kwargs.get('openai_key', None)
        self.temperature = kwargs.get('temperature', 0.0)
        self.sleep_time = kwargs.get('sleep_time', 0)
        if not self.openai_key:
            raise ValueError("openai_key is required for openai model!")

        if self.temperature > 0:
            raise Warning("Temperature is not 0, so that the results may not be reproducable!")

        if self.sleep_time > 0:
            raise Warning("We suggest to set sleep time > 0 (i.e., 5).")

    def sleep(self, seconds):
        import random
        import time
        time.sleep(seconds + random.random())

    # TODO: openai new version support
    def predict(self, input_text):
        
        import openai
        openai.api_key = self.openai_key
        
        if isinstance(input_text, list):
            messages = input_text
        elif isinstance(input_text, dict):
            messages = [input_text]
        else:
            messages = [{"role": "user", "content": input_text}]
        
        retry_count = 0
        while retry_count < 3:
            try:
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=messages,
                    temperature=self.temperature,
                )
                result = response['choices'][0]['message']['content']
                return result
                
            except Exception as e:
                print(e)
                print("Retrying...")
                self.sleep(self.sleep_time)
                retry_count += 1