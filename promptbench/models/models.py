# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
from abc import ABC
import torch

class LMMBaseModel(ABC):
    """
    Abstract base class for language model interfaces.

    This class provides a common interface for various language models and includes methods for prediction.

    Parameters:
    -----------
    model : str
        The name of the language model.
    max_new_tokens : int
        The maximum number of new tokens to be generated.
    temperature : float, optional
        The temperature for text generation (default is 0).

    Methods:
    --------
    predict(input_text, **kwargs)
        Generates a prediction based on the input text.
    __call__(input_text, **kwargs)
        Shortcut for predict method.
    """
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
    """
    Language model class for the Phi model.

    Inherits from LMMBaseModel and sets up the Phi language model for use.

    Parameters:
    -----------
    model : str
        The name of the Phi model.
    max_new_tokens : int
        The maximum number of new tokens to be generated.
    temperature : float, optional
        The temperature for text generation (default is 0).
    system_prompt : str, optional
        The system prompt to be used (default is None).
    """
    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None):
        super(PhiModel, self).__init__(model, max_new_tokens, temperature)
        from transformers import AutoTokenizer, AutoModelForCausalLM
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto", device_map="auto")
        self.pipe = AutoModelForCausalLM.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto", device_map="auto")
    
    def predict(self, input_text, **kwargs):
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

        outputs = self.pipe.generate(input_ids, 
                                     max_new_tokens=self.max_new_tokens, 
                                     temperature=self.temperature,
                                     **kwargs)
        
        out = self.tokenizer.decode(outputs[0])
        return out[len(input_text):]

class T5Model(LMMBaseModel):
    """
    Language model class for the T5 model.

    Inherits from LMMBaseModel and sets up the T5 language model for use.

    Parameters:
    -----------
    model : str
        The name of the T5 model.
    max_new_tokens : int
        The maximum number of new tokens to be generated.
    temperature : float, optional
        The temperature for text generation (default is 0).
    system_prompt : str, optional
        The system prompt to be used (default is None).
    """
    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None):
        super(T5Model, self).__init__(model, max_new_tokens, temperature)
        from transformers import T5Tokenizer, T5ForConditionalGeneration
        
        # TODO: implement system_prompt
        self.tokenizer = T5Tokenizer.from_pretrained(
            self.model, device_map="auto")
        self.pipe = T5ForConditionalGeneration.from_pretrained(
            self.model, device_map="auto")


class UL2Model(LMMBaseModel):
    """
    Language model class for the UL2 model.

    Inherits from LMMBaseModel and sets up the UL2 language model for use.

    Parameters:
    -----------
    model : str
        The name of the UL2 model.
    max_new_tokens : int
        The maximum number of new tokens to be generated.
    temperature : float, optional
        The temperature for text generation (default is 0).
    system_prompt : str, optional
        The system prompt to be used (default is None).
    """
    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None):
        super(UL2Model, self).__init__(model, max_new_tokens, temperature)
        from transformers import AutoTokenizer, T5ForConditionalGeneration

        # TODO: implement system_prompt

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model, device_map="auto")
        self.pipe = T5ForConditionalGeneration.from_pretrained(
            self.model, device_map="auto", torch_dtype=torch.bfloat16)


class LlamaModel(LMMBaseModel):
    """
    Language model class for the Llama model.

    Inherits from LMMBaseModel and sets up the Llama language model for use.

    Parameters:
    -----------
    model : str
        The name of the Llama model.
    max_new_tokens : int
        The maximum number of new tokens to be generated.
    temperature : float, optional
        The temperature for text generation (default is 0).
    system_prompt : str, optional
        The system prompt to be used (default is None).
    model_dir : str, optional
        The directory containing the model files (default is None).
    """
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
        self.pipe = LlamaForCausalLM.from_pretrained(model_dir, device_map="auto", torch_dtype=torch.float16)

    def predict(self, input_text, **kwargs):
        input_text = f"<s>[INST] <<SYS>>{self.system_prompt}<</SYS>>\n{input_text}[/INST]"
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
    """
    Language model class for the Vicuna model.

    Inherits from LMMBaseModel and sets up the Vicuna language model for use.

    Parameters:
    -----------
    model : str
        The name of the Vicuna model.
    max_new_tokens : int
        The maximum number of new tokens to be generated.
    temperature : float, optional
        The temperature for text generation (default is 0).
    system_prompt : str, optional
        The system prompt to be used (default is None).
    model_dir : str, optional
        The directory containing the model files (default is None).
    """
    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None, model_dir=None):
        super(VicunaModel, self).__init__(model, max_new_tokens, temperature, system_prompt)

        # TODO: implement system_prompt

        from transformers import AutoModelForCausalLM, AutoTokenizer

        self.tokenizer = AutoTokenizer.from_pretrained(model_dir, device_map="auto", use_fast=False)
        self.pipe = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto", torch_dtype=torch.float16)

    def predict(self, input_text, **kwargs):
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
        outputs = self.pipe.generate(input_ids, 
                                     max_new_tokens=self.max_new_tokens,
                                     temperature=self.temperature,
                                     **kwargs)
        
        out = self.tokenizer.decode(outputs[0])
        
        return out[len(input_text):]


class OpenAIModel(LMMBaseModel):
    """
    Language model class for interfacing with OpenAI's GPT models.

    Inherits from LMMBaseModel and sets up a model interface for OpenAI GPT models.

    Parameters:
    -----------
    model : str
        The name of the OpenAI model.
    max_new_tokens : int
        The maximum number of new tokens to be generated.
    temperature : float, optional
        The temperature for text generation (default is 0).
    system_prompt : str, optional
        The system prompt to be used (default is None).
    openai_key : str, optional
        The OpenAI API key (default is None).
    sleep_time : int, optional
        The sleep time between inference calls (default is 3).

    Methods:
    --------
    sleep(seconds)
        Sleep for the specified number of seconds.
    predict(input_text)
        Predicts the output based on the given input text using the OpenAI model.
    """
    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None, openai_key=None, sleep_time=3):
        super(OpenAIModel, self).__init__(model, max_new_tokens, temperature)
        self.openai_key = openai_key
        self.sleep_time = sleep_time

        if self.temperature > 0:
            raise Warning("Temperature is not 0, so that the results may not be reproducable!")

        if self.sleep_time == 0:
            raise Warning("We suggest to set sleep time > 0 (i.e., 5).")

    def sleep(self, seconds):
        import time
        time.sleep(seconds)

    def predict(self, input_text, **kwargs):
        
        from openai import OpenAI
        client = OpenAI(api_key=self.openai_key)
        
        if isinstance(input_text, list):
            messages = input_text
        elif isinstance(input_text, dict):
            messages = [input_text]
        else:
            messages = [{"role": "user", "content": input_text}]
        
        # extra parameterss
        n = kwargs['n'] if 'n' in kwargs else 1
        temperature = kwargs['temperature'] if 'temperature' in kwargs else self.temperature
        max_new_tokens = kwargs['max_new_tokens'] if 'max_new_tokens' in kwargs else self.max_new_tokens
        
        retry_count = 0
        while retry_count < 3:
            try:
                response = client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_new_tokens,
                    n=n,
                )
                # for i, choice in enumerate(response.choices):
                #     print(str(i) + ':' + choice.message.content)
                
                if n > 1:
                    result = [choice.message.content for choice in response.choices]
                else:
                    result = response.choices[0].message.content
                    
                return result
                
            except Exception as e:
                print(e)
                print("Retrying...")
                self.sleep(self.sleep_time)
                retry_count += 1
                

class PaLMModel(LMMBaseModel):
    """
    Language model class for interfacing with PaLM models.

    Inherits from LMMBaseModel and sets up a model interface for PaLM models.

    Parameters:
    -----------
    model : str
        The name of the PaLM model.
    max_new_tokens : int
        The maximum number of new tokens to be generated.
    temperature : float, optional
        The temperature for text generation (default is 0).
    system_prompt : str, optional
        The system prompt to be used (default is None).
    model_dir : str, optional
        The directory containing the model files (default is None).
    """
    def __init__(self, model, max_new_tokens, temperature=0, system_prompt=None, palm_key=None, sleep_time=3):
        super(PaLMModel, self).__init__(model, max_new_tokens, temperature)
        self.palm_key = palm_key
        self.sleep_time = sleep_time
    
    def predict(self, input_text, **kwargs):
        import google.generativeai as palm 
        
        palm.configure(api_key=self.palm_key)
        models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        model = models[0].name
        
        n = kwargs['n'] if 'n' in kwargs else 1
        temperature = kwargs['temperature'] if 'temperature' in kwargs else self.temperature
        max_new_tokens = kwargs['max_new_tokens'] if 'max_new_tokens' in kwargs else self.max_new_tokens
        
        completion = palm.generate_text(
            model=model,
            prompt=input_text,
            temperature=temperature,
            candidate_count = n,
            max_output_tokens=max_new_tokens,
        )
        
        if n > 1:
            result = [cand.output for cand in completion.candidates]
        else:
            result = completion.result
        
        print(result)
        return result
        
        