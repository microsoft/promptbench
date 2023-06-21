# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

MNLI_LABEL = ['entailment', 'neutral', 'contradiction', 'entailment\'', 'neutral\'', 'contradiction\'']
EQ_LABEL = ['equivalent', 'not_equivalent', 'equivalent\'', 'not_equivalent\'']
ENTAIL_LABEL = ['entailment', 'not_entailment', 'entailment\'', 'not_entailment\'', '0', '1', '0\'', '1\'', 0, 1]

LABEL_SET = {
    # 'positive\'', 'negative\'' is used for label constraint due to a bug of TextAttack repo.
    'sst2': ['positive', 'negative', 'positive\'', 'negative\'', '0', '1', '0\'', '1\'',0, 1], 
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
    'squad_v2': ['unanswerable', 'unanswerable\''], # do not change the word 'nothing' in prompts.
    'iwslt': ['translate', 'translate\''],
    'un_multi': ['translate', 'translate\''],
    'math': ['math', 'math\''],
}

GENERATE_LEN = {
    'sst2': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 2},
    'mnli': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 3},
    'qqp': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 3},
    'qnli': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 4},
    'rte': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 4},
    'cola': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 3},
    'mrpc': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 3},
    'wnli': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 4},
    'mmlu': {'google/flan-t5-large': 2, 'vicuna-13b': 2, 'google/flan-ul2': 2, "chatgpt": 2},
    'squad_v2': {'google/flan-t5-large': 20, 'google/flan-ul2': 20, "chatgpt": 20},
    'iwslt': {'google/flan-t5-large': 70, 'google/flan-ul2': 70, 'chatgpt': 70},
    'un_multi': {'google/flan-t5-large': 140, 'google/flan-ul2': 140, 'chatgpt': 140},
    'math': {'google/flan-t5-large': 20, 'google/flan-ul2': 20, 'chatgpt': 20},
}

MODEL_SET = [ 
    'google/flan-t5-large',
    'EleutherAI/gpt-neox-20b',
    'tiiuae/falcon-40b-instruct',
    # 'facebook/opt-66b', 
    'llama-13b',
    'vicuna-13b',
    'vicuna-13b-v1.3',
    'google/flan-ul2',
    'cerebras/Cerebras-GPT-13B',
    'databricks/dolly-v1-6b',
    'chatgpt'
]

LABEL_TO_ID = {
    'mmlu': {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'},
    'sst2': {'negative': 0, 'positive': 1, '0': 0, '1': 1, 0: 0, 1: 1},
    'mnli': {'entailment': 0, 'neutral': 1, 'contradiction': 2, '0': 0, '1': 1, '2':2, 0: 0, 1: 1, 2: 2},
    'mnli_mismatched': {'entailment': 0, 'neutral': 1, 'contradiction': 2, '0': 0, '1': 1, '2':2, 0: 0, 1: 1, 2: 2},
    'mnli_matched': {'entailment': 0, 'neutral': 1, 'contradiction': 2, '0': 0, '1': 1, '2':2, 0: 0, 1: 1, 2: 2},
    'qqp': {'equivalent': 1, 'not_equivalent': 0, '0': 0, '1': 1, 0: 0, 1: 1},
    'qnli': {'entailment': 0, 'not_entailment': 1, '0': 0, '1': 1, 0: 0, 1: 1},
    'rte': {'entailment': 0, 'not_entailment': 1, '0': 0, '1': 1, 0: 0, 1: 1},
    'cola': {'unacceptable': 0, 'acceptable': 1, '0': 0, '1': 1, 0: 0, 1: 1},
    'mrpc': {'equivalent': 1, 'not_equivalent': 0, '0': 0, '1': 1, 0: 0, 1: 1},
    'wnli': {'entailment': 1, 'not_entailment': 0, '0': 0, '1': 1, 0: 0, 1: 1},
}

ID_TO_LABEL = {
    'mmlu': {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'},
    'sst2': {0: 'negative', 1: 'positive'},
    'mnli': {0: 'entailment', 1: 'neutral', 2: 'contradiction'},
    'mnli_matched': {0: 'entailment', 1: 'neutral', 2: 'contradiction'},
    'mnli_mismatched': {0: 'entailment', 1: 'neutral', 2: 'contradiction'},
    'qqp': {1: 'equivalent', 0: 'not_equivalent'},
    'qnli': {0: 'entailment', 1: 'not_entailment'},
    'rte': {0: 'entailment', 1: 'not_entailment'},
    'cola': {0: 'unacceptable', 1: 'acceptable'},
    'mrpc': {1: 'equivalent', 0: 'not_equivalent'},
    'wnli': {1: 'entailment', 0: 'not_entailment'},
}

SUPPORTED_LANGUAGES = {
    'google/flan-t5-large': ['en', 'de', 'fr'],
    'google/flan-ul2': ['en', 'de', 'fr'],
    'vicuna-13b': ['en', 'de', 'fr'],
    'chatgpt': ['en', 'de', 'fr'],
}

LANGUAGES = {
    'ar': 'Arabic', 
    'de': 'German', 
    'en': 'English', 
    'es': 'Spanish',
    'fr': 'French',
    'ru': 'Russian',
    'zh': 'Chinese',
    'it': 'Italian',
    'nl': 'Dutch',
    'ro': 'Romanian',
    'ja': 'Japanese',
    'ko': 'Korean',
}

MATH_QUESTION_TYPES = {
    'algebra_linear_1d': ' linear algebra ',
    'algebra_linear_2d': ' linear algebra ',
    'algebra_sequence_next_term': ' given a sequence predict the next term ',
    'arithmetic_addition_sub_multiple': ' arithmetic addition and subtraction ',
    'arithmetic_mul_div_multiple': ' arithmetic multiplication and division ',
    'arithmetic_mixed': ' arithmetic addition, subtraction, multiplication and division ',
    'arithmetic_nearest_integer_root': ' arithmetic nearest integer root ',
    'comparison_closest': ' compare which one of given numbers is closest to target number ',
    'comparison_kth_biggest': ' compare which one of given numbers is kth biggest or smallest ',
    'comparison_pair': ' comparison which one of given numbers is bigger or smaller ', 
    'measurement_conversion': ' measurement conversion ',
    'numbers_base_conversion': ' numbers base conversion ',
    'numbers_div_remainder': ' numbers division and remainder ',
    'numbers_gcd': ' numbers greatest common divisor ',
    'numbers_is_factor': ' if one number is a factor of antoher number ',
    'number_is_prime': ' if a number is prime ',
    'numbers_lcm': ' least common multiple ',
    'numbers_place_value': ' place value ',
    'numbers_round_number': ' round number ',
    'polynomials_evaluate': ' polynomials evaluate ',
}