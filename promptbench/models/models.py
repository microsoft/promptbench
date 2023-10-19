# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

LLAMA_MODELS = [
    'llama2-7b',
    'llama2-7b-chat',
    'llama2-13b',
    'llama2-13b-chat',
    'llama2-70b',
    'llama2-70b-chat',
]

GPT_MODELS = [
    'gpt-3.5-turbo',
    'gpt-4',
]

VICUNA_MODELS = [
    'vicuna-7b',
    'vicuna-13b',
    'vicuna-13b-v1.3',
]

UL2_MODELS = [
    'google/flan-ul2',
]

MODEL_LIST = {
    't5': ['google/flan-t5-large'],
    'llama': LLAMA_MODELS,
    'gpt': GPT_MODELS,
    'vicuna': VICUNA_MODELS,
    'ul2': UL2_MODELS,
}


class LMMBaseModel(object):

    def __init__(self, **kwargs):
        self.model = kwargs.get('model', 'google/flan-t5-large')
        self.gen_len = kwargs.get('gen_len', 5)

    def predict(self, input_text, **kwargs):
        raise NotImplementedError("The model is not implemented!")

    def __call__(self, input_text, **kwargs):
        return self.predict(input_text, **kwargs)


class LLMModel(object):

    def __init__(self, **kwargs):
        self.model = kwargs.get('model', None)
        self.infer_model = self.create_model(**kwargs)

    def create_model(self, **kwargs):
        if self.model == 'google/flan-t5-large':
            return T5Model(**kwargs)
        elif self.model in LLAMA_MODELS:
            return LlamaModel(**kwargs)
        elif self.model in GPT_MODELS:
            return OpenaiModel(**kwargs)
        elif self.model in VICUNA_MODELS:
            return VicunaModel(**kwargs)
        elif self.model in UL2_MODELS:
            return UL2Model(**kwargs)
        else:
            raise ValueError("The model is not supported!")

    @staticmethod
    def model_list():
        return MODEL_LIST

    def __call__(self, **kwargs):
        return self.infer_model


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
            input_ids, max_new_tokens=self.gen_len)
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
            input_ids, max_new_tokens=self.gen_len)
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
            input_ids, max_new_tokens=self.gen_len)
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
            input_ids, max_new_tokens=self.gen_len)
        out = self.tokenizer.decode(outputs[0])
        return out


class OpenaiModel(LMMBaseModel):

    def __init__(self, **kwargs):
        super(OpenaiModel, self).__init__(**kwargs)
        self.openai_key = kwargs.get('openai_key', None)
        self.temperature = kwargs.get('temperature', 0.0)
        if not self.openai_key:
            raise ValueError("openai_key is required for openai model!")

    def sleep(self, seconds):
        import random
        import time
        time.sleep(seconds + random.random())

    def predict(self, input_text, sleep=3):
        self.sleep(sleep if sleep > 0 else 0)
        import openai
        openai.api_key = self.openai_key
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": input_text},
                ],
                temperature=self.temperature,
            )
            result = response['choices'][0]['message']['content']
        except Exception as e:
            print(e)
            result = 'error!'
        return result

    def __call__(self, input_text, sleep=3, **kwargs):
        return self.predict(input_text, sleep, **kwargs)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='vicuna-7b')
    parser.add_argument('--model_dir', type=str,
                        default='/home/jindwang/mine/vicuna-7b')
    args = parser.parse_args()
    model = LLMModel(model=args.model,
                     model_dir=args.model_dir)()
    print(model('The quick brown fox jumps over the lazy dog'))