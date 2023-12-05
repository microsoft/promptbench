# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from .attack import *

MNLI_LABEL = ['entailment', 'neutral', 'contradiction',
              'entailment\'', 'neutral\'', 'contradiction\'']
EQ_LABEL = ['equivalent', 'not_equivalent', 'equivalent\'', 'not_equivalent\'']
ENTAIL_LABEL = ['entailment', 'not_entailment', 'entailment\'',
                'not_entailment\'', '0', '1', '0\'', '1\'']

LABEL_SET = {
    # 'positive\'', 'negative\'' is used for label constraint due to a bug of TextAttack repo.
    'sst2': ['positive', 'negative', 'positive\'', 'negative\'', '0', '1', '0\'', '1\''],
    'mnli': MNLI_LABEL,
    'mnli_mismatched': MNLI_LABEL,
    'mnli_matched': MNLI_LABEL,
    'qqp': EQ_LABEL,
    'qnli': ENTAIL_LABEL,
    'rte': ENTAIL_LABEL,
    'cola': ['unacceptable', 'acceptable', 'unacceptable\'', 'acceptable\''],
    'mrpc': EQ_LABEL,
    'wnli': ENTAIL_LABEL,
    'mmlu': ['A', 'B', 'C', 'D', 'A\'', 'B\'', 'C\'', 'D\'', 'a', 'b', 'c', 'd', 'a\'', 'b\'', 'c\'', 'd\''],
    # do not change the word 'nothing' in prompts.
    'squad_v2': ['unanswerable', 'unanswerable\''],
    'iwslt': ['translate', 'translate\''],
    'un_multi': ['translate', 'translate\''],
    'math': ['math', 'math\''],
    'bool_logic': ['True', 'False', 'True\'', 'False\'', "bool", "boolean", "bool\'", "boolean\'"],
    'valid_parentheses': ['Valid', 'Invalid', 'Valid\'', 'Invalid\'', 'matched', 'matched\'', 'valid', 'invalid', 'valid\'', 'invalid\''],
}

attack_config = {
    "goal_function": {
        "query_budget": float("inf"),
    },

    "textfooler": {
        "max_candidates": 50,
        "min_word_cos_sim": 0.6,
        "min_sentence_cos_sim": 0.840845057,
    },

    "textbugger": {
        "max_candidates": 5,
        "min_sentence_cos_sim": 0.8,
    },

    "deepwordbug": {
        "levenshtein_edit_distance" : 30,
    },

    "bertattack": {
        "max_candidates": 48,
        "max_word_perturbed_percent": 1,
        "min_sentence_cos_sim": 0.8,
    },

    "checklist": {
        "max_candidates": 5,
    },

    "stresstest": {
        "max_candidates": 5,
    }

}


