def _process_valid_parentheses_input(prompt, raw_data):
    question, label = raw_data['question'], raw_data['answer']
    input_text = prompt + '\n' + ("Question: " + question + '\nAnswer: ')

    return input_text, label

def _process_bool_logic_input(prompt, raw_data):
    question, label = raw_data['question'], raw_data['answer']
    input_text = prompt + '\n' + ("Question: " + question + '\nAnswer: ')

    return input_text, label

def _process_math_input(prompt, raw_data):
    question_type, question, label = raw_data['task'], raw_data['question'], raw_data['answer']
    input_text = prompt.format(question_type) + '\n'

    input_text += ("Question: " + question + '\nAnswer: ')

    return input_text, label

def _process_trans_input(prompt, raw_data):
    source, target, task = raw_data['source'], raw_data['target'], raw_data['task']
    src_lang, des_lang = task.split('-')
    input_text = prompt.format(src_lang, des_lang) + '\n'
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
