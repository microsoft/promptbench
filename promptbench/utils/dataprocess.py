# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

class DataProcessor:
    def __init__(self):
        self.INPUT_PROCESS_MAP = {
            "cola": self._process_cls_input,
            "sst2": self._process_cls_input,
            "mrpc": self._process_cls_input,
            "qqp": self._process_cls_input,
            "mnli": self._process_cls_input,
            "qnli": self._process_cls_input,
            "rte": self._process_cls_input,
            "wnli": self._process_cls_input,

            "mmlu": self._process_qa_input,
            "squad_v2": self._process_squad_v2_input,
            'iwslt': self._process_trans_input,
            'un_multi': self._process_trans_input,
            'math': self._process_math_input,
            'bool_logic': self._process_cls_input,
            'valid_parentheses': self._process_cls_input,
        }

        self.PRED_PROCESS_MAP = {
            "cola": self._process_cls_pred,
            "sst2": self._process_cls_pred,
            "mrpc": self._process_cls_pred,
            "qqp": self._process_cls_pred,
            "mnli": self._process_cls_pred,
            "qnli": self._process_cls_pred,
            "rte": self._process_cls_pred,
            "wnli": self._process_cls_pred,

            "mmlu": self._process_cls_pred,
            "squad_v2": self._generic_pred_process,
            "iwslt": self._generic_pred_process,
            "un_multi": self._generic_pred_process,
            "math": self._generic_pred_process,

            "bool_logic": self._generic_pred_process,
            "valid_parentheses": self._generic_pred_process,
        }

    def process_input(self, prompt, raw_dataset):
        """ Preprocess the given dataset """
        dataset_name = raw_dataset.dataset_name
        _process = self.INPUT_PROCESS_MAP.get(dataset_name)
        
        if not _process:
            raise NotImplementedError(f"The dataset {dataset_name} is not implemented!")
        
        input_texts, labels = [], []
        for raw_data in raw_dataset:
            input_text, label = _process(prompt, raw_data)
            input_texts.append(input_text)
            labels.append(label)
        
        return input_texts, labels

    def process_pred(self, dataset_name, pred):
        """ Postprocess predictions """
        _process = self.PRED_PROCESS_MAP.get(dataset_name)
        
        if not _process:
            raise NotImplementedError(f"The dataset {dataset_name} is not implemented!")
        
        return _process(pred)

    def _generic_pred_process(self, raw_pred):
        """ A generic function to postprocess a prediction """
        pred = raw_pred.lower()
        pred = pred.replace("<pad>", "").replace("</s>", "").strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")
        return pred

    def _process_cls_pred(self, raw_pred):
        pred = self._generic_pred_process(raw_pred)
        pred = pred.split(" ")[-1]
        pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")
        return pred

    def _create_input_text(prompt, *args, answer_tag=True):
        """Helper function to generate input text."""
        input_text = prompt
        for arg in args:
            if arg:
                input_text += '\n' + arg
        if answer_tag:
            input_text += '\nAnswer: '
        return input_text

    def _process_valid_parentheses_input(self, prompt, raw_data):
        return self._create_input_text(prompt, "Question: " + raw_data['question']), raw_data['answer']

    def _process_bool_logic_input(self, prompt, raw_data):
        return self._create_input_text(prompt, "Question: " + raw_data['question']), raw_data['answer']

    def _process_math_input(self, prompt, raw_data):
        question_type_input = prompt.format(raw_data['task'])
        return self._create_input_text(question_type_input, "Question: " + raw_data['question']), raw_data['answer']

    def _process_trans_input(self, prompt, raw_data):
        lang_input = prompt.format(raw_data['source_lang'], raw_data['target_lang'])
        return self._create_input_text(lang_input, raw_data['source']), raw_data['target']

    def _process_squad_v2_input(self, prompt, raw_data):
        return self._create_input_text(prompt, raw_data["content"], answer_tag=False), raw_data["id"]

    def _process_qa_input(self, prompt, raw_data):
        task_input = prompt.format(raw_data["task"])
        return self._create_input_text(task_input, raw_data["content"]), raw_data["label"]

    def _process_cls_input(self, prompt, raw_data):
        return self._create_input_text(prompt, raw_data["content"], answer_tag=False), raw_data["label"]


def inference_total_dataset(prompt, model, dataset):
    from ..metrics import Eval

    input_texts, labels = DataProcessor.process_input(prompt, dataset)
    
    import tqdm
    raw_preds = []
    for input_text in tqdm.tqdm(input_texts):
        raw_preds.append(model[input_text])
    
    preds = DataProcessor.process_pred(dataset.dataset_name, raw_preds)
    acc = Eval(dataset, preds, labels)
    
    return acc