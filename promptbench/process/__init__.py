from .preprocess import *
from .postprocess import *


def process_input(prompt, raw_dataset):
    dataset = raw_dataset.dataset_name
    if dataset in ["cola", "sst2", "mrpc", "qqp", "mnli", "qnli", "rte", "wnli"]:
        _process = _process_cls_input
    elif dataset == "mmlu":
        _process = _process_qa_input
    elif dataset == "squad_v2":
        _process = _process_squad_v2_input
    elif dataset in ['iwslt', 'un_multi']:
        _process = _process_trans_input
    elif dataset == 'math':
        _process = _process_math_input
    elif dataset == 'bool_logic':
        _process = _process_bool_logic_input
    elif dataset == 'valid_parentheses':
        _process = _process_valid_parentheses_input
    else:
        raise NotImplementedError("The dataset is not implemented!")

    input_texts = []
    labels = []

    for raw_data in raw_dataset:
        input_text, label = _process(prompt, raw_data)
        input_texts.append(input_text)
        labels.append(label)
    
    return input_texts, labels


def process_pred(dataset_name, pred):
    if dataset_name in ["cola", "sst2", "mrpc", "qqp", "mnli", "qnli", "rte", "wnli"]:
        return _process_cls_pred(pred)
    elif dataset_name == "mmlu":
        return _process_qa_pred(pred)
    elif dataset_name == "squad_v2":
        return _process_squad_v2_pred(pred)
    elif dataset_name in ['iwslt', 'un_multi']:
        return _process_trans_pred(pred)
    elif dataset_name == 'math':
        return _process_math_pred(pred)
    elif dataset_name == 'bool_logic':
        return _process_bool_logic_pred(pred)
    elif dataset_name == 'valid_parentheses':
        return _process_valid_parentheses_pred(pred)
    else:
        raise NotImplementedError("The dataset is not implemented!")