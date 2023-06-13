# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import openai
from config import LABEL_SET, LABEL_TO_ID
from tqdm import tqdm


"""
This clss implements the inference of the model (including create the model).
"""
class Inference(object):

    def __init__(self, args):
        self.error_analysis = False
        self.args = args
        self.model = args.model
        self.openai_config = args.openai_config
        self.create_model()


    def create_model(self):
        """
        ChatGPT is a special case, we use the openai api to create the model.
        """

        if self.model != 'chatgpt':
            import torch
            import os
            
            """
            Here you can add you own model.
            """

            if self.model == 'google/flan-t5-large':
                from transformers import T5Tokenizer, T5ForConditionalGeneration

                self.tokenizer = T5Tokenizer.from_pretrained(self.model, device_map="auto")
                self.pipe = T5ForConditionalGeneration.from_pretrained(self.model, device_map="auto")

            elif self.model == 'EleutherAI/gpt-neox-20b':
                from transformers import GPTNeoXForCausalLM, GPTNeoXTokenizerFast
                
                self.tokenizer = GPTNeoXTokenizerFast.from_pretrained(self.model, device_map="auto")
                self.pipe = GPTNeoXForCausalLM.from_pretrained(self.model, device_map="auto", torch_dtype=torch.float16)

            # elif self.model.lower() == 'facebook/opt-66b':
            #     from transformers import AutoModelForCausalLM, AutoTokenizer

            #     # the fast tokenizer currently does not work correctly
            #     self.tokenizer = AutoTokenizer.from_pretrained(model, device_map="auto", use_fast=False)
            #     self.pipe = AutoModelForCausalLM.from_pretrained(model, device_map="auto", torch_dtype=torch.float16)
            
            elif self.model.lower() == "llama-13b":
                
                from transformers import LlamaForCausalLM, LlamaTokenizer
                
                model_dir = os.path.join(self.args.model_dir, self.model)

                self.tokenizer = LlamaTokenizer.from_pretrained(model_dir, device_map="auto")
                self.pipe = LlamaForCausalLM.from_pretrained(model_dir, device_map="auto", torch_dtype=torch.float16)
            
            elif self.model.lower() == "vicuna-13b":

                from transformers import AutoModelForCausalLM, AutoTokenizer

                model_dir = os.path.join(self.args.model_dir, self.model)

                self.tokenizer = AutoTokenizer.from_pretrained(model_dir, device_map="auto", use_fast=False)
                self.pipe = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto", torch_dtype=torch.float16)
            
            elif self.model == "google/flan-ul2":

                from transformers import T5ForConditionalGeneration, AutoTokenizer
                
                self.tokenizer = AutoTokenizer.from_pretrained(self.model)
                self.pipe = T5ForConditionalGeneration.from_pretrained(self.model, torch_dtype=torch.bfloat16, device_map="auto")

            elif self.model == "tiiuae/falcon-40b-instruct":                                                         
                from transformers import AutoTokenizer, AutoModelForCausalLM

                self.tokenizer = AutoTokenizer.from_pretrained(self.model)
                self.pipe = AutoModelForCausalLM.from_pretrained(self.model, torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto",)
                

            elif self.model == "cerebras/Cerebras-GPT-13B":
                from transformers import AutoTokenizer, AutoModelForCausalLM

                self.tokenizer = AutoTokenizer.from_pretrained(self.model, device_map="auto")
                self.pipe = AutoModelForCausalLM.from_pretrained(self.model, device_map="auto", torch_dtype=torch.float16)

            elif self.model == "databricks/dolly-v1-6b":
                from transformers import AutoModelForCausalLM, AutoTokenizer

                self.tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v1-6b", device_map="auto", padding_side="left")
                self.pipe = AutoModelForCausalLM.from_pretrained("databricks/dolly-v1-6b", device_map="auto", torch_dtype=torch.float16)
            
            else:
                raise NotImplementedError("The model is not implemented!")


    def process_input(self, prompt, raw_data):
        if self.args.dataset in ["cola", "sst2", "mrpc", "qqp", "mnli", "qnli", "rte", "wnli"]:
            return self._process_cls_input(prompt, raw_data)
        elif self.args.dataset == "mmlu":
            return self._process_qa_input(prompt, raw_data)
        elif self.args.dataset == "squad_v2":
            return self._process_squad_v2_input(prompt, raw_data)
        elif self.args.dataset in ['iwslt', 'un_multi']:
            return self._process_trans_input(prompt, raw_data)
        elif self.args.dataset == 'math':
            return self._process_math_input(prompt, raw_data)
        else:
            raise NotImplementedError("The dataset is not implemented!")
    

    def process_pred(self, pred):
        if self.args.dataset in ["cola", "sst2", "mrpc", "qqp", "mnli", "qnli", "rte", "wnli"]:
            return self._process_cls_pred(pred)
        elif self.args.dataset == "mmlu":
            return self._process_qa_pred(pred)
        elif self.args.dataset == "squad_v2":
            return self._process_squad_v2_pred(pred)
        elif self.args.dataset in ['iwslt', 'un_multi']:
            return self._process_trans_pred(pred)
        elif self.args.dataset == 'math':
            return self._process_math_pred(pred)
        else:
            raise NotImplementedError("The dataset is not implemented!")


    def eval(self, preds, gts):
        
        if self.args.dataset in ["cola", "sst2", "mrpc", "qqp", "mnli", "qnli", "rte", "wnli", "mmlu"]:
            if self.args.dataset == "mmlu":
                preds = [pred.lower() for pred in preds]
                gts = [gt.lower() for gt in gts]
            
            if not isinstance(preds, list):
                preds = [preds]
                gts = [gts]

            return sum(a == b for a, b in zip(preds, gts)) / len(preds)
        
        elif self.args.dataset == "squad_v2":

            from metrics.squad_v2.squad_v2 import SquadV2
            metric = SquadV2()

            model_output = []

            for id, pred in zip(gts, preds):

                if pred == "unanswerable":
                    no_ans_prob = 1
                    pred = ""
                else:
                    no_ans_prob = 0
                
                model_output.append({"id": id, "prediction_text": pred, "no_answer_probability": no_ans_prob})

            references = self.args.data.get_reference()
            score = metric.compute(predictions=model_output, references=references)

            return score["f1"] / 100
        
        elif self.args.dataset in ['iwslt', 'un_multi']:

            from metrics.bleu.bleu import Bleu
            metric = Bleu()
            results = metric.compute(predictions=preds, references=gts)
            
            # it need to /100 to get the proper bleu score (in alignment with other dataset, e.g., glue) 
            return results['bleu'] / 100

        elif self.args.dataset == 'math':
  
            processed_preds = []
            processed_gts = []
            for pred, gt in zip(preds, gts):
                if pred.lower() == "yes":
                    pred = "True"
                elif pred.lower() == "no":
                    pred = "False"
                
                gt = str(gt).lower()
                processed_preds.append(pred.lower())
                processed_gts.append(gt.lower())

            acc = sum(a == b for a, b in zip(processed_preds, processed_gts)) / len(processed_gts)

            return acc
            
        else:
            raise NotImplementedError("Eval this dataset {self.args.dataset} is not implemented!")


    def predict(self, prompt=None):
        from config import MODEL_SET
        assert self.args.data is not None, "Please load data first!"

        if self.model == "chatgpt":
            raise NotImplementedError
        else:
            results = self.predict_by_local_inference(self.model, prompt)
        return results


    def predict_by_local_inference(self, model, prompt):

        data_len = len(self.args.data)
        if data_len > 1000:
            data_len = 1000
    
        score = 0
        check_correctness = 100
        preds = []
        gts = []
        
        for idx in tqdm(range(data_len)):
            
            raw_data = self.args.data.get_content_by_idx(idx, self.args.dataset)
            input_text, gt = self.process_input(prompt, raw_data)

            raw_pred = self.pred_by_generation(input_text, model)
            pred = self.process_pred(raw_pred)

            preds.append(pred)
            gts.append(gt)
 
            if check_correctness > 0:
                self.args.logger.info("gt: {}".format(gt))
                self.args.logger.info("Pred: {}".format(pred))
                self.args.logger.info("sentence: {}".format(input_text))

                check_correctness -= 1

        score = self.eval(preds, gts)
        return score


    def pred_by_generation(self, input_text, model):
        out = 'error!'
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

        if 't5' in model or 'ul2' in model:
            outputs = self.pipe.generate(input_ids, max_length=self.args.generate_len, early_stopping=True)
            out = self.tokenizer.decode(outputs[0])

        elif model == 'EleutherAI/gpt-neox-20b':
            outputs = self.pipe.generate(input_ids, 
                                        #  do_sample=True, 
                                         temperature=0.00001, 
                                        #  max_length=50,
                                         max_new_tokens=self.args.generate_len,
                                         early_stopping=True,
                                         pad_token_id=self.tokenizer.eos_token_id)
            
            out = self.tokenizer.decode(outputs[0])

        elif model == "facebook/opt-66b":
            outputs = self.pipe.generate(input_ids)
            out = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
 
        elif model in ["llama-13b", "vicuna-13b"]:
            outputs = self.pipe.generate(input_ids, 
                                         temperature=0,
                                         max_new_tokens=self.args.generate_len, 
                                         early_stopping=True)
            
            out = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
      
        elif model in ['databricks/dolly-v1-6b', 'cerebras/Cerebras-GPT-13B']:
            outputs = self.pipe.generate(input_ids, 
                                         temperature=0,
                                         max_new_tokens=self.args.generate_len,
                                         pad_token_id=self.tokenizer.eos_token_id,
                                         early_stopping=True)
            
            out = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        elif model == "tiiuae/falcon-40b-instruct":
            outputs = self.pipe.generate(input_ids, 
                                         temperature=0,
                                         max_new_tokens=self.args.generate_len,
                                         pad_token_id=self.tokenizer.eos_token_id,
                                         early_stopping=True)
            
            out = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return out


    def _process_math_input(self, prompt, raw_data):
        from config import MATH_QUESTION_TYPES
        question_type, question, label = MATH_QUESTION_TYPES[raw_data['task']], raw_data['question'], raw_data['answer']
        input_text = prompt.format(question_type) + '\n'
        
        if self.args.shot > 0:
            input_text += "\n"+self.args.data.get_few_shot_examples(raw_data['task'])
        
        input_text += ("Question: " + question + '\nAnswer: ')

        return input_text, label


    def _process_trans_input(self, prompt, raw_data):
        from config import LANGUAGES
        source, target, task = raw_data['source'], raw_data['target'], raw_data['task']
        src_lang, des_lang = task.split('-')
        input_text = prompt.format(LANGUAGES[src_lang], LANGUAGES[des_lang]) + '\n'

        if self.args.shot > 0:
            input_text += "\n"+self.args.data.get_few_shot_examples(task)

        input_text += (source + '\nAnswer: ')
        return input_text, target


    def _process_squad_v2_input(self, prompt, raw_data):
        id, content = raw_data["id"], raw_data["content"]
        input_text = prompt

        if self.args.shot > 0:
            input_text += "\n"+self.args.data.get_few_shot_examples(self.args.dataset)

        input_text += (content + "Answer: ")

        return input_text, id


    def _process_qa_input(self, prompt, raw_data):
        task, content = raw_data["task"], raw_data["content"]
        label = raw_data["label"]

        input_text = prompt.format(task) + "\n"

        if self.args.shot > 0:
            input_text += "\n"+self.args.data.get_few_shot_examples(task.replace(" ", "_"))
        
        input_text += content + "\nAnswer: "
        
        return input_text, label


    def _process_cls_input(self, prompt, raw_data):
        content = raw_data["content"]
        label = raw_data["label"]

        input_text = prompt

        if self.args.shot > 0:
            few_shot_examples = self.args.data.get_few_shot_examples(self.args.dataset)
            input_text += "\n"+few_shot_examples
            if  self.args.dataset == "sst2" or  self.args.dataset == "cola":
                input_text += "Sentence: "
          
        input_text += (content + ' Answer: ')

        return input_text, label

    
    def _process_math_pred(self, raw_pred):
        pred = raw_pred.lower()
        pred = pred.replace("<pad>", "")
        pred = pred.replace("</s>", "")
        pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")

        return pred
    

    def _process_trans_pred(self, raw_pred):
        pred = raw_pred.lower()
        pred = pred.replace("<pad>", "")
        pred = pred.replace("</s>", "")
        pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")

        return pred


    def _process_squad_v2_pred(self, raw_pred):
        pred = raw_pred.lower()
        pred = pred.replace("<pad>", "")
        pred = pred.replace("</s>", "")
        pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")

        return pred


    def _process_cls_pred(self, raw_pred):

        pred = raw_pred.lower()

        pred = pred.replace("<pad>", "")
        pred = pred.replace("</s>", "")
        
        pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")
        pred = pred.split(" ")[-1]
        pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")

        if pred in LABEL_SET[self.args.dataset]:                   
            pred = LABEL_TO_ID[self.args.dataset][pred] 
        else:
            self.args.logger.warn("The original label : '{}'.".format(raw_pred))                
            self.args.logger.warn("The predicted label: '{}' is not in label set.".format(pred))
            pred = -1
        
        return pred
    
    
    def _process_qa_pred(self, raw_pred):
        pred = raw_pred.lower()
        
        pred = pred.replace("<pad>", "")
        pred = pred.replace("</s>", "")
        
        pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")
        pred = pred.split(" ")[-1]
        pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")
        
        if pred not in LABEL_SET[self.args.dataset]:   
            self.args.logger.warn("The original label : '{}'.".format(raw_pred))
            self.args.logger.warn("The predicted label: '{}' is not in label set.".format(pred))
            pred = 'no_answer'

        return pred
    