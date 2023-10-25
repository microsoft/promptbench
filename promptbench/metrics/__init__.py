# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""
Example usage:

from promptbench.metrics import Eval
eval = Eval()
score = eval(dataset, preds, gts)
"""

class Eval:

    BLEU_NORMALIZATION_FACTOR = 100
    SQUAD_V2_NORMALIZATION_FACTOR = 100
    
    def __call__(self, dataset, preds, gts):
        """Main evaluation method to compute metrics based on dataset type.

        Args:
            dataset: The dataset object.
            preds: A list of model predictions.
            gts: A list of ground truth values.

        Returns:
            The computed evaluation metric (e.g., accuracy, F1, BLEU).
        """
        dataset_name = dataset.dataset_name

        dataset_eval_mapping = {
            "cola": self._compute_simple_accuracy,
            "sst2": self._compute_simple_accuracy,
            "mrpc": self._compute_simple_accuracy,
            "qqp": self._compute_simple_accuracy,
            "mnli": self._compute_simple_accuracy,
            "qnli": self._compute_simple_accuracy,
            "rte": self._compute_simple_accuracy,
            "wnli": self._compute_simple_accuracy,
            "mmlu": self._compute_simple_accuracy,
            "bool_logic": self._compute_simple_accuracy,
            "valid_parentheses": self._compute_simple_accuracy,
            "squad_v2": self._compute_squad_v2,
            "iwslt": self._compute_bleu,
            "un_multi": self._compute_bleu,
            "math": self._compute_math_accuracy,
        }

        if dataset_name not in dataset_eval_mapping:
            raise NotImplementedError(f"Eval for dataset {dataset_name} is not implemented!")

        return dataset_eval_mapping[dataset_name](dataset, preds, gts)

    def _compute_simple_accuracy(self, dataset, preds, gts):
        """Compute simple accuracy for a given dataset, predictions, and ground truths.

        It normalizes the predictions and ground truths to lowercase.
        """
        preds = [pred.lower() for pred in preds]
        gts = [gt.lower() for gt in gts]

        if not isinstance(preds, list):
            preds = [preds]
            gts = [gts]

        return sum(a == b for a, b in zip(preds, gts)) / len(preds)

    def _compute_squad_v2(self, dataset, preds, gts):
        """Compute F1 score for the SQuAD V2 dataset based on model predictions and ground truths."""

        from .squad_v2.squad_v2 import SquadV2
        metric = SquadV2()

        model_output = []
        for id, pred in zip(gts, preds):
            no_ans_prob = 1 if pred == "unanswerable" else 0
            pred = "" if pred == "unanswerable" else pred
            model_output.append({"id": id, "prediction_text": pred, "no_answer_probability": no_ans_prob})

        references = [{"answers": data["answers"], "id": data["id"]} for data in dataset]

        score = metric.compute(predictions=model_output, references=references)

        return score["f1"] / self.SQUAD_V2_NORMALIZATION_FACTOR

    def _compute_bleu(self, dataset, preds, gts):
        """Compute BLEU score for translation tasks based on model predictions and ground truths."""

        from .bleu.bleu import Bleu
        metric = Bleu()
        results = metric.compute(predictions=preds, references=gts)
        return results['bleu'] / self.BLEU_NORMALIZATION_FACTOR

    def _compute_math_accuracy(self, dataset, preds, gts):
        """Compute accuracy for the 'math' dataset by normalizing certain prediction values."""

        processed_preds = []
        processed_gts = []
        
        for pred, gt in zip(preds, gts):
            pred = "True" if pred.lower() == "yes" else ("False" if pred.lower() == "no" else pred)
            gt = str(gt).lower()
            processed_preds.append(pred.lower())
            processed_gts.append(gt)

        return sum(a == b for a, b in zip(processed_preds, processed_gts)) / len(processed_gts)
