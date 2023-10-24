"""
TODO: how to process the prediction of different tasks. Using <<<>>>?
"""

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