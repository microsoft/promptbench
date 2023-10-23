def get_few_shot_examples(self):
    from prompts.three_shot.few_shot_examples import examples
    few_shot_examples = examples["bool_logic"]
    return few_shot_examples


def get_few_shot_examples(self):
    from prompts.three_shot.few_shot_examples import examples
    few_shot_examples = examples["valid_parentheses"]
    return few_shot_examples

def get_few_shot_examples(self, task):
    from prompts.three_shot.few_shot_examples import examples

    few_shot_data = examples["math"][task]
    few_shot_examples = "Here are three examples. \n"
    for d in few_shot_data:
        few_shot_examples += "Question: " + d["question"] + "\n"
        few_shot_examples += "Answer: " + str(d["answer"]) + "\n"

    return few_shot_examples

def get_few_shot_examples(self, task):
    from prompts.three_shot.few_shot_examples import examples

    few_shot_examples = examples["un_multi"][task]
    return few_shot_examples

def get_few_shot_examples(self, task):
    from prompts.three_shot.few_shot_examples import examples

    few_shot_examples = examples["iwslt"][task]
    return few_shot_examples

def get_few_shot_examples(self, task):
    from prompts.three_shot.few_shot_examples import examples

    few_shot_examples = examples[task]
    return few_shot_examples

with open("promptbench/data/MMLU_few_shot.json", "r") as file:
    self.few_shot_data = json.load(file)

def get_few_shot_examples(self, task):
    content = "Here are three examples.\n"
    data = self.few_shot_data[task]
    for idx in range(min(len(data), 3)):
        content += ("Input: " + data[idx]["input"] + "\n"
                    + "A : " + data[idx]["A"] + "\n"
                    + "B : " + data[idx]["B"] + "\n"
                    + "C : " + data[idx]["C"] + "\n"
                    + "D : " + data[idx]["D"] + "\n\n"
                    + "Answer : " + data[idx]["target"] + "\n"
                    )

    return content

def get_few_shot_examples(self, task):
    from prompts.three_shot.few_shot_examples import examples

    few_shot_examples = examples[task]
    return few_shot_examples








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



