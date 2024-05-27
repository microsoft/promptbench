
import datasets
 
import evaluate

from .rouge_ import compute_rouge  # From: https://github.com/tensorflow/nmt/blob/master/nmt/scripts/route.py
from .tokenizer_13a import Tokenizer13a
 

_CITATION = """\
@INPROCEEDINGS{Papineni02bleu:a,
    author = {Kishore Papineni and Salim Roukos and Todd Ward and Wei-jing Zhu},
    title = {BLEU: a Method for Automatic Evaluation of Machine Translation},
    booktitle = {},
    year = {2002},
    pages = {311--318}
}
@inproceedings{lin-och-2004-orange,
    title = "{ORANGE}: a Method for Evaluating Automatic Evaluation Metrics for Machine Translation",
    author = "Lin, Chin-Yew  and
      Och, Franz Josef",
    booktitle = "{COLING} 2004: Proceedings of the 20th International Conference on Computational Linguistics",
    month = "aug 23{--}aug 27",
    year = "2004",
    address = "Geneva, Switzerland",
    publisher = "COLING",
    url = "https://www.aclweb.org/anthology/C04-1072",
    pages = "501--507",
}
"""
 
_DESCRIPTION = """\
Recall-Oriented Understudy for Gisting Evaluation, often referred as ROUGE score, is a metric used to evaluate text summarization and translation models. There are variations of ROUGE scores. 
"""
 
_KWARGS_DESCRIPTION = """
Computes ROUGE score of prediction segments against one or more references.
Args:
    predictions: list of predictions to score.
    references: list of lists of or just a list of references for each translation.
    tokenizer : approach used for tokenizing `predictions` and `references`.
        The default tokenizer is `tokenizer_13a`, a minimal tokenization approach that is equivalent to `mteval-v13a`, used by WMT.
        This can be replaced by any function that takes a string as input and returns a list of tokens as output.
Returns:
    'rouge': rouge score
Examples:
    >>> predictions = ["hello there general kenobi", "foo bar foobar"]
"""
 
class Rouge(evaluate.Metric):
    def _info(self):
        return evaluate.MetricInfo(
            description=_DESCRIPTION,
            citation=_CITATION,
            inputs_description=_KWARGS_DESCRIPTION,
            features=[
                datasets.Features(
                    {
                        "predictions": datasets.Value("string", id="sequence"),
                        "references": datasets.Sequence(datasets.Value("string", id="sequence"), id="references"),
                    }
                ),
                datasets.Features(
                    {
                        "predictions": datasets.Value("string", id="sequence"),
                        "references": datasets.Value("string", id="sequence"),
                    }
                ),
            ],
            codebase_urls=["https://github.com/tensorflow/nmt/blob/master/nmt/scripts/rouge.py"],
            reference_urls=[
                "https://en.wikipedia.org/wiki/ROUGE_(metric)"
            ],
        )
 
    def _compute(self, references, predictions, tokenizer=Tokenizer13a()):
        # if only one reference is provided make sure we still use list of lists

        score = compute_rouge(
            references=references, predictions=predictions
        )

        # score description
        #  rouge_1 = ROUGE-1 algorithm
        #    f = full score
        #    r = recall score
        #    p = precision score
        #  rouge_2 = ROUGE-2 algorithm
        #  rouge_l = ROUGE-L, for longest common sequence.

        return {
            "rouge_1": score["rouge_1/f_score"],
            "rouge_2": score["rouge_2/f_score"],
            "rouge_l": score["rouge_l/f_score"]
        }
