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

        from .squad_v2.squad_v2 import SquadV2
        metric = SquadV2()

        model_output = []
        """
        TODO: remove get_reference into eval function.
        """
        def get_reference(self):
            references = []

            for data in self.data:
                references.append({"answers": data["answers"], "id": data["id"]})
            return references

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

        from .bleu.bleu import Bleu
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