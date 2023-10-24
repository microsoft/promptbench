from .dataload import *

def load_dataset(dataset_name, *args):
    if dataset_name in ["cola", "sst2", "qqp", "mnli", "mnli_matched", "mnli_mismatched", "qnli", "wnli", "rte", "mrpc"]:
        return GLUE(dataset_name)
    elif dataset_name == 'mmlu':
        return MMLU()
    elif dataset_name == "squad_v2":
        return SQUAD_V2()
    elif dataset_name == 'un_multi':
        return UnMulti(args[0])
    elif dataset_name == 'iwslt':
        return IWSLT(args[0])
    elif dataset_name == 'math':
        return Math()
    elif dataset_name == 'bool_logic':
        return BoolLogic()
    elif dataset_name == 'valid_parentheses':
        return ValidParentheses()
    else:
        raise NotImplementedError