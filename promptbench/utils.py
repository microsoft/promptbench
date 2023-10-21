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


def eval(dataset, preds, gts):
    dataset_name = dataset.dataset_name

    if dataset_name in ["cola", "sst2", "mrpc", "qqp", "mnli", "qnli", "rte", "wnli", "mmlu", "bool_logic", "valid_parentheses"]:
        if dataset_name == "mmlu":
            preds = [pred.lower() for pred in preds]
            gts = [gt.lower() for gt in gts]

        if not isinstance(preds, list):
            preds = [preds]
            gts = [gts]

        return sum(a == b for a, b in zip(preds, gts)) / len(preds)

    elif dataset_name == "squad_v2":

        from metrics.squad_v2.squad_v2 import SquadV2
        metric = SquadV2()

        model_output = []

        for id, pred in zip(gts, preds):

            if pred == "unanswerable":
                no_ans_prob = 1
                pred = ""
            else:
                no_ans_prob = 0

            model_output.append(
                {"id": id, "prediction_text": pred, "no_answer_probability": no_ans_prob})

        references = dataset.get_reference()
        score = metric.compute(
            predictions=model_output, references=references)

        return score["f1"] / 100

    elif dataset_name in ['iwslt', 'un_multi']:

        from metrics.bleu.bleu import Bleu
        metric = Bleu()
        results = metric.compute(predictions=preds, references=gts)

        # it need to /100 to get the proper bleu score (in alignment with other dataset, e.g., glue)
        return results['bleu'] / 100

    elif dataset_name == 'math':

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

        acc = sum(a == b for a, b in zip(processed_preds,
                    processed_gts)) / len(processed_gts)

        return acc

    else:
        raise NotImplementedError(
            "Eval this dataset {dataset} is not implemented!")


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

def _process_bool_logic_pred(raw_pred):
    pred = raw_pred.lower()
    pred = pred.replace("<pad>", "")
    pred = pred.replace("</s>", "")
    pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")

    return pred

def _process_valid_parentheses_pred(raw_pred):
    pred = raw_pred.lower()
    pred = pred.replace("<pad>", "")
    pred = pred.replace("</s>", "")
    pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")

    return pred

def _process_math_pred(raw_pred):
    pred = raw_pred.lower()
    pred = pred.replace("<pad>", "")
    pred = pred.replace("</s>", "")
    pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")

    return pred

def _process_trans_pred(raw_pred):
    pred = raw_pred.lower()
    pred = pred.replace("<pad>", "")
    pred = pred.replace("</s>", "")
    pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")

    return pred

def _process_squad_v2_pred(raw_pred):
    pred = raw_pred.lower()
    pred = pred.replace("<pad>", "")
    pred = pred.replace("</s>", "")
    pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")

    return pred

def _process_cls_pred(raw_pred):

    pred = raw_pred.lower()

    pred = pred.replace("<pad>", "")
    pred = pred.replace("</s>", "")

    pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")
    pred = pred.split(" ")[-1]
    pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")

    if pred in LABEL_SET[self.args.dataset]:
        pred = LABEL_TO_ID[self.args.dataset][pred]
    else:
        self.args.logger.warn(
            "The original label : '{}'.".format(raw_pred))
        self.args.logger.warn(
            "The predicted label: '{}' is not in label set.".format(pred))
        pred = -1

    return pred

def _process_qa_pred(raw_pred):
    pred = raw_pred.lower()

    pred = pred.replace("<pad>", "")
    pred = pred.replace("</s>", "")

    pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")
    pred = pred.split(" ")[-1]
    pred = pred.strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")

    if pred not in LABEL_SET[self.args.dataset]:
        self.args.logger.warn(
            "The original label : '{}'.".format(raw_pred))
        self.args.logger.warn(
            "The predicted label: '{}' is not in label set.".format(pred))
        pred = 'no_answer'

    return pred