# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
from abc import ABC, abstractmethod


class LMMBaseModel(ABC):
    def __init__(self, model, max_new_tokens, temperature=0):
        self.model = model
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature

    def predict(self, input_text, **kwargs):
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

        outputs = self.pipe.generate(input_ids, 
                                     max_new_tokens=self.max_new_tokens, 
                                     temperature=self.temperature,
                                     **kwargs)
        
        out = self.tokenizer.decode(outputs[0])
        return out

    def __call__(self, input_text, **kwargs):
        return self.predict(input_text, **kwargs)


class PhiModel(LMMBaseModel):

    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None):
        super(PhiModel, self).__init__(model, max_new_tokens, temperature)
        from transformers import AutoTokenizer, AutoModelForCausalLM
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto", device_map="auto")
        self.pipe = AutoModelForCausalLM.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto", device_map="auto")


class T5Model(LMMBaseModel):

    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None):
        super(T5Model, self).__init__(model, max_new_tokens, temperature)
        from transformers import T5Tokenizer, T5ForConditionalGeneration
        
        # TODO: implement system_prompt
        
        self.tokenizer = T5Tokenizer.from_pretrained(
            self.model, device_map="auto")
        self.pipe = T5ForConditionalGeneration.from_pretrained(
            self.model, device_map="auto")


class UL2Model(LMMBaseModel):

    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None):
        super(UL2Model, self).__init__(model, max_new_tokens, temperature)
        from transformers import AutoTokenizer, T5ForConditionalGeneration

        # TODO: implement system_prompt

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model, device_map="auto")
        self.pipe = T5ForConditionalGeneration.from_pretrained(
            self.model, device_map="auto")


class LlamaModel(LMMBaseModel):

    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None, model_dir=None):
        super(LlamaModel, self).__init__(model, max_new_tokens, temperature)
        if system_prompt is None:
            self.system_prompt = "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."
        else:
            self.system_prompt = system_prompt
        from transformers import LlamaForCausalLM, LlamaTokenizer, AutoTokenizer, AutoModelForCausalLM
        
        # TODO: rename Llama2 model to be consistent with huggingface
        # TODO: add default huggingface loader
        self.tokenizer = LlamaTokenizer.from_pretrained(model_dir, device_map="auto")
        self.pipe = LlamaForCausalLM.from_pretrained(model_dir, device_map="auto")

    def predict(self, input_text, **kwargs):
        # input_text = f"<s>[INST] <<SYS>>{self.system_prompt}<</SYS>>\n{input_text}[/INST]"
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
        outputs = self.pipe.generate(input_ids, 
                                     max_new_tokens=self.max_new_tokens, 
                                     temperature=self.temperature,
                                     **kwargs)
        
        out = self.tokenizer.decode(outputs[0], 
                                    skip_special_tokens=True, 
                                    clean_up_tokenization_spaces=False)
        
        return out[len(input_text):]


class VicunaModel(LMMBaseModel):

    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None, model_dir=None):
        super(VicunaModel, self).__init__(model, max_new_tokens, temperature, system_prompt)

        # TODO: implement system_prompt

        from transformers import AutoModelForCausalLM, AutoTokenizer

        self.tokenizer = AutoTokenizer.from_pretrained(model_dir, device_map="auto", use_fast=False)
        self.pipe = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto")

    def predict(self, input_text, **kwargs):
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
        outputs = self.pipe.generate(input_ids, 
                                     max_new_tokens=self.max_new_tokens,
                                     temperature=self.temperature,
                                     **kwargs)
        
        out = self.tokenizer.decode(outputs[0])
        
        return out[len(input_text):]


class OpenAIModel(LMMBaseModel):

    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None, openai_key=None, sleep_time=3):
        super(OpenAIModel, self).__init__(model, max_new_tokens, temperature, system_prompt)
        self.openai_key = openai_key
        self.sleep_time = sleep_time

        if self.temperature > 0:
            raise Warning("Temperature is not 0, so that the results may not be reproducable!")

        if self.sleep_time > 0:
            raise Warning("We suggest to set sleep time > 0 (i.e., 5).")

    def sleep(self, seconds):
        import time
        time.sleep(seconds)

    def predict(self, input_text):
        
        from openai import OpenAI
        client = OpenAI(api_key=self.openai_key)
        
        if isinstance(input_text, list):
            messages = input_text
        elif isinstance(input_text, dict):
            messages = [input_text]
        else:
            messages = [{"role": "user", "content": input_text}]
        
        retry_count = 0
        while retry_count < 3:
            try:
                response = client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=self.temperature,
                )
                result = response.choices[0].message.content
                return result
                
            except Exception as e:
                print(e)
                print("Retrying...")
                self.sleep(self.sleep_time)
                retry_count += 1