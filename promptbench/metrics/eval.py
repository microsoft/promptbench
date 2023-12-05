# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

class Eval:
    """
    A utility class for computing various evaluation metrics.

    This class provides static methods to compute metrics such as classification accuracy, SQuAD V2 F1 score, BLEU score, and math accuracy.

    Attributes:
    -----------
    BLEU_NORMALIZATION_FACTOR : int
        The normalization factor for the BLEU score.
    SQUAD_V2_NORMALIZATION_FACTOR : int
        The normalization factor for the SQuAD V2 F1 score.

    Methods:
    --------
    compute_cls_accuracy(preds, gts)
        Computes classification accuracy.
    compute_squad_v2_f1(preds, gts, dataset)
        Computes the F1 score for the SQuAD V2 dataset.
    compute_bleu(preds, gts)
        Computes the BLEU score for translation tasks.
    compute_math_accuracy(dataset, preds, gts)
        Computes accuracy for math dataset.
    """
    BLEU_NORMALIZATION_FACTOR = 100
    SQUAD_V2_NORMALIZATION_FACTOR = 100
    
    @staticmethod
    def compute_cls_accuracy(preds, gts):
        """
        Computes classification accuracy based on predictions and ground truths.

        Parameters:
        -----------
        preds : list
            A list of predictions.
        gts : list
            A list of ground truths.

        Returns:
        --------
        float
            The classification accuracy.
        """
        try:
            preds = [str(pred).lower() for pred in preds]
            gts = [str(gt).lower() for gt in gts]
        except AttributeError:
            print("Something in either preds or gts can not be convert to a string.")
            
        if not isinstance(preds, list):
            preds = [preds]
            gts = [gts]

        return sum(a == b for a, b in zip(preds, gts)) / len(preds)

    @staticmethod
    def compute_squad_v2_f1(preds, gts, dataset):
        """
        Computes the F1 score for the SQuAD V2 dataset.

        Parameters:
        -----------
        preds : list
            A list of predictions.
        gts : list
            A list of ground truth IDs.
        dataset : list
            The dataset containing the SQuAD V2 data.

        Returns:
        --------
        float
            The F1 score for the SQuAD V2 dataset.
        """
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

    @staticmethod
    def compute_bleu(preds, gts):
        """
        Computes the BLEU score for translation tasks.

        Parameters:
        -----------
        preds : list
            A list of predictions.
        gts : list
            A list of ground truth translations.

        Returns:
        --------
        float
            The BLEU score.
        """
        from .bleu.bleu import Bleu
        metric = Bleu()
        results = metric.compute(predictions=preds, references=gts)
        return results['bleu'] / self.BLEU_NORMALIZATION_FACTOR

    @staticmethod
    def compute_math_accuracy(self, dataset, preds, gts):
        """
        Computes accuracy for the 'math' dataset.

        Parameters:
        -----------
        dataset : list
            The dataset containing math data.
        preds : list
            A list of predictions.
        gts : list
            A list of ground truths.

        Returns:
        --------
        float
            The math accuracy.
        """
        processed_preds = []
        processed_gts = []
        
        for pred, gt in zip(preds, gts):
            pred = "True" if pred.lower() == "yes" else ("False" if pred.lower() == "no" else pred)
            gt = str(gt).lower()
            processed_preds.append(pred.lower())
            processed_gts.append(gt)

        return sum(a == b for a, b in zip(processed_preds, processed_gts)) / len(processed_gts)
