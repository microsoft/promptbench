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