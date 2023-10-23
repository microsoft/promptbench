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

def _process_valid_parentheses_input(prompt, raw_data):
    question, label = raw_data['question'], raw_data['answer']
    input_text = prompt + '\n' + ("Question: " + question + '\nAnswer: ')

    return input_text, label

def _process_bool_logic_input(prompt, raw_data):
    question, label = raw_data['question'], raw_data['answer']
    input_text = prompt + '\n' + ("Question: " + question + '\nAnswer: ')

    return input_text, label

def _process_math_input(prompt, raw_data):
    from config import MATH_QUESTION_TYPES
    question_type, question, label = MATH_QUESTION_TYPES[raw_data['task']], raw_data['question'], raw_data['answer']
    input_text = prompt.format(question_type) + '\n'

    input_text += ("Question: " + question + '\nAnswer: ')

    return input_text, label

def _process_trans_input(prompt, raw_data):
    from config import LANGUAGES
    source, target, task = raw_data['source'], raw_data['target'], raw_data['task']
    src_lang, des_lang = task.split('-')
    input_text = prompt.format(LANGUAGES[src_lang], LANGUAGES[des_lang]) + '\n'
    input_text += (source + '\nAnswer: ')
    return input_text, target

def _process_squad_v2_input(prompt, raw_data):
    id, content = raw_data["id"], raw_data["content"]
    input_text = prompt + content + "Answer: "

    return input_text, id

def _process_qa_input(prompt, raw_data):
    task, content = raw_data["task"], raw_data["content"]
    label = raw_data["label"]
    input_text = prompt.format(task) + "\n" + content + "\nAnswer: "
    return input_text, label

def _process_cls_input(prompt, raw_data):
    content = raw_data["content"]
    label = raw_data["label"]
    input_text = prompt + content + ' Answer: '
    
    return input_text, label
