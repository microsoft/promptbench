# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

GENERATE_LEN = {
    'sst2': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 2, 'llama2-13b': 2, 'llama2-13b-chat': 2, 'llama2-7b-chat': 2, 'llama2-7b-chat': 2},
    'mnli': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 3, 'llama2-13b': 3, 'llama2-13b-chat': 3, 'llama2-7b-chat': 3, 'llama2-7b-chat': 3},
    'qqp': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 3, 'llama2-13b': 4, 'llama2-13b-chat': 4, 'llama2-7b-chat': 4, 'llama2-7b-chat': 4},
    'qnli': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 4, 'llama2-13b': 2, 'llama2-13b-chat': 2, 'llama2-7b-chat': 2, 'llama2-7b-chat': 2},
    'rte': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 4, 'llama2-13b': 3, 'llama2-13b-chat': 3, 'llama2-7b-chat': 3, 'llama2-7b-chat': 3},
    'cola': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 3, 'llama2-13b': 3, 'llama2-13b-chat': 3, 'llama2-7b-chat': 3, 'llama2-7b-chat': 3},
    'mrpc': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 3, 'llama2-13b': 2, 'llama2-13b-chat': 2, 'llama2-7b-chat': 2, 'llama2-7b-chat': 2},
    'wnli': {'google/flan-t5-large': 20, 'vicuna-13b': 5, 'google/flan-ul2': 20, "chatgpt": 4, 'llama2-13b': 3, 'llama2-13b-chat': 3, 'llama2-7b-chat': 3, 'llama2-7b-chat': 3},
    'mmlu': {'google/flan-t5-large': 2, 'vicuna-13b': 2, 'google/flan-ul2': 2, "chatgpt": 2, 'llama2-13b': 3, 'llama2-13b-chat': 3, 'llama2-7b-chat': 3, 'llama2-7b-chat': 3},
    'squad_v2': {'google/flan-t5-large': 20, 'google/flan-ul2': 20, "chatgpt": 20},
    'iwslt': {'google/flan-t5-large': 70, 'google/flan-ul2': 70, 'chatgpt': 70},
    'un_multi': {'google/flan-t5-large': 140, 'google/flan-ul2': 140, 'chatgpt': 140},
    'math': {'google/flan-t5-large': 20, 'google/flan-ul2': 20, 'chatgpt': 20},
    'bool_logic': {'google/flan-t5-large': 4, },
}


LABEL_TO_ID = {
    'mmlu': {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'},
    'sst2': {'negative': 0, 'positive': 1, '0': 0, '1': 1, 0: 0, 1: 1},
    'mnli': {'entailment': 0, 'neutral': 1, 'contradiction': 2, '0': 0, '1': 1, '2': 2, 0: 0, 1: 1, 2: 2},
    'mnli_mismatched': {'entailment': 0, 'neutral': 1, 'contradiction': 2, '0': 0, '1': 1, '2': 2, 0: 0, 1: 1, 2: 2},
    'mnli_matched': {'entailment': 0, 'neutral': 1, 'contradiction': 2, '0': 0, '1': 1, '2': 2, 0: 0, 1: 1, 2: 2},
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
    'llama2-13b-chat': ['en', 'de', 'fr'],
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




PROMPT_SET_Promptbench_advglue = {
    'clean': {
        'sst2': [
            "Read the provided excerpt and choose between 'positive' and 'negative' to describe its sentiment: ",
        ],
        'qqp': [
            "Can these two statements be considered equal in meaning? Answer with 'equivalent' or 'not_equivalent': ",
        ],
        'mnli': [
            "Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction': ",
        ],
        'qnli': [
            "Consider the context and question, and indicate if the answer can be logically deduced from the context by responding with 'entailment' or 'not_entailment'.",
        ],
        'rte': [
            "Determine if the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'. ",
        ],
        'cola': [
            "Review the sentence below and identify whether its grammar is 'Acceptable' or 'Unacceptable': ",
        ],
        'mrpc': [
            "Can the given sentences be considered semantically identical? Please reply with 'equivalent' or 'not_equivalent'. ",
        ],
        'wnli': [
            "Identify whether the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'. ",
        ],
        'squad_v2': [
            "Discover the best answer based on the context. If the context doesn't include an answer, respond with 'unanswerable'. ",
        ],
    },
    "bertattack": {
        'sst2': [
            "read the standard excerpt and pause between 'positive' and 'negative' to describe its thoughtful: ",
        ],
        'qqp': [
            "Can these two constructions be considered equal in meaning? object with 'equivalent' or 'not_equivalent': ",
        ],
        'mnli': [
            "do the reconciliation between the following sentences and distinguish it as 'entailment', 'neutral', or 'contradiction': ",
        ],
        'qnli': [
            "include the context and answered, and signal if the assertion can be logically deduced from the context by following with 'entailment' or 'not_entailment'. ",
        ],
        'rte': [
            "determine if the following singular of sentence indicating entailment or not_entailment. contrast with 'entailment' or 'not_entailment'. ",
        ],
        'cola': [
            "what the grammatical structure of the given sentence and consider it as 'Acceptable' or 'Unacceptable': ",
        ],
        'mrpc': [
            "Examine the pairs of pronouns and evaluate if their meanings are different by answering with 'equivalent' or 'not_equivalent'. ",
        ],
        'wnli': [
            "Identify whether the given individual of verbs demonstrates entailment or not_entailment. have with 'entailment' or 'not_entailment'. ",
        ],
        'squad_v2': [
            "challenge the best answer based on the context. however the context doesn't include an answer, play with 'unanswerable'. ",
        ],
    },
    "checklist": {
        'sst2': [
            "Read the provided excerpt and choose between 'positive' and 'negative' to describe its sentiment Q47Jmd4lMV: ",
        ],
        'qqp': [
            "Can these two statements be considered equal in meaning? Answer with 'equivalent' or 'not_equivalent' 5XeflW1ZJc. ",
        ],
        'mnli': [
            "Considering the two sentences, identify if their relationship is 'entailment', 'neutral', or 'contradiction' 5XeflW1ZJc: ",
        ],
        'qnli': [
            "Consider the context and question, and indicate if the answer can be logically deduced from the context by responding with 'entailment' or 'not_entailment' Q47Jmd4lMV. ",
        ],
        'rte': [
            "Determine if the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment' MSAddJ4D2a. ",
        ],
        'cola': [
            "Review the sentence below and identify whether its grammar is 'Acceptable' or 'Unacceptable' zexKUTWJYG: ",
        ],
        'mrpc': [
            "Can the given sentences be considered semantically identical? Please reply with 'equivalent' or 'not_equivalent' MQnugHcaoy. ",
        ],
        'wnli': [
            "Examine the pair of sentences and determine if they exhibit entailment or not_entailment. Answer with either 'entailment' or 'not_entailment' 5XeflW1ZJc. ",
        ],
        'squad_v2': [
            "Based on the given context, provide the best possible answer. If there's no answer available in the context, respond with 'unanswerable' ItGDrrA1Sc. ",
        ],
    },
    "deepwordbug": {
        'sst2': [
            "Read the provded excertp and choost between 'positive' and 'negative' to descrhibe its sentigment: ",
        ],
        'qqp': [
            "Can these two statements be considered equal in meaning? Answer with 'equivalent' or 'not_equivalent'. ",
        ],
        'mnli': [
            "Asess the cnonection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction':",
        ],
        'qnli': [
            "ConsideYr the context and Zquestion, and indicaute if the ansUer can be logically deBduced from the congext by qesponding with 'entailment' or 'not_entailment'. ",
        ],
        'rte': [
            "Determine if the given pair of Wentences displays entailment or not_entailment. Respnod with 'entailment' or 'not_entailment'. ",
        ],
        'cola': [
            "Review the sentece below and identify whether its grammar is 'Acceptable' or 'Unacceptable': ",
        ],
        'mrpc': [
            "Evaluate whether the two provRided sentnces convey the same meaning by answering 'equivalent' or 'not_equivalent'. ",
        ],
        'wnli': [
            "Identify whether the given paiM of senJences demonstartes entailment or not_entailment. Answer with 'entailment' or 'not_entailment'. ",
        ],
        'squad_v2': [
            "DiscoveMr the best answr bassd on the Rontext. Iof the cnotext doesn't include an answer, resCpond with 'unanswerable'. ",
        ],
    },
    "stresstest": {
        'sst2': [
            "Review this statement and decide whether it has a 'positive' or 'negative' sentiment and true is true : ",
        ],
        'qqp': [
            "Can these two statements be considered equal in meaning? Answer with 'equivalent' or 'not_equivalent' and false is not true . ",
        ],
        'mnli': [
            "Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction' and true is true: ",
        ],
        'qnli': [
            "Consider the context and question, and indicate if the answer can be logically deduced from the context by responding with 'entailment' or 'not_entailment' and false is not true . ",
        ],
        'rte': [
            "Determine if the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment' and true is true and true is true and true is true and true is true and true is true : ",
        ],
        'cola': [
            "Review the sentence below and identify whether its grammar is 'Acceptable' or 'Unacceptable' and true is true : ",
        ],
        'mrpc': [
            "Can the given sentences be considered semantically identical? Please reply with 'equivalent' or 'not_equivalent' and false is not true . ",
        ],
        'wnli': [
            "Are the following two sentences entailment or not_entailment? Answer me with 'entailment' or 'not_entailment', just one word and true is true . ",
        ],
        'squad_v2': [
            "Discover the best answer based on the context. If the context doesn't include an answer, respond with 'unanswerable' and true is true and true is true and true is true and true is true and true is true . ",
        ],
    },
    "textfooler": {
        'sst2': [
            "Analysis this assertion and defining whether it ai a 'positive' or 'negative' sentiment: ",
        ],
        'qqp': [
            "Defined if the given peers of depositions can fi dealt the same by reaction with 'equivalent' or 'not_equivalent'. ",
        ],
        'mnli': [
            "Assess the liaison between the next convicting and classify it as 'entailment', 'neutral', or 'contradiction': ",
        ],
        'qnli': [
            "Recital the context and items, and specify if the solution can be logically subtracted from the framework by reactions with 'entailment' or 'not_entailment'. ",
        ],
        'rte': [
            "Detects if the bestowed peers of sentences denotes entailment or not_entailment. Cope with 'entailment' or 'not_entailment'. ",
        ],
        'cola': [
            "Revising the punishments below and locate whether its dictionary is 'Acceptable' or 'Unacceptable': ",
        ],
        'mrpc': [
            "Examine the pair of sentences and selects if their regard are identical by responding with 'equivalent' or 'not_equivalent'. ",
        ],
        'wnli': [
            "Identify whether the given pair of sentence exposes entailment or not_entailment. Retaliated with 'entailment' or 'not_entailment'. ",
        ],
        'squad_v2': [
            "Exploit the backdrop, establishing the most dignified rebuttal. Although the context doesn't restrain the reply, reacting with 'unanswerable'. ",
        ],
    },
    "textbugger": {
        'sst2': [
            "Review this speeches and decide if it has a 'positive' or 'negative' sentiment: ",
        ],
        'qqp': [
            "Assess whether the following statements are analogous in maning by answeⲅing 'equivalent' or 'not_equivalent'. ",
        ],
        'mnli': [
            "Analyze the two prоvided punishments and decide if their relatinship is 'entailment', 'neutral', or 'contradiction': ",
        ],
        'qnli': [
            "Considеr the context and question, and idicate if the respond can be logically ԁeduced from the context by ⲅesponding with 'entailment' or 'not_entailment'. ",
        ],
        'rte': [
            "Ascertain if the given pair of sentences displays entailment or not_entailment. Answering with 'entailment' or 'not_entailment'. ",
        ],
        'cola': [
            "As sess the garmmatical structure of the conferred sentence and classify it as 'Acceptable' or 'Unacceptable': ",
        ],
        'mrpc': [
            "Evaluate wհether the both provided sentences convey the same meaninɡ by answeriոg 'equivalent' or 'not_equivalent'. ",
        ],
        'wnli': [
            "Examine the paiⲅ of sentences and determines if they exhibit entailment or not_entailment. Answer with neither 'entailment' or 'not_entailment'. ",
        ],
        'squad_v2': [
            "Discoveⲅ the better answer bsed on the context. If the background doesn't encompass an answer, replying with 'unanswerable'. ",
        ],
    },
    "semantic": {
        'sst2': [
            "What is the classification between 'positive' and 'negative'? ",
        ],
        'qqp': [
            "To determine an equation of questions, you must review the questions and classify their similarity as 'equivalent' or 'not_equivalent'. ",
        ],
        'mnli': [
            "Using this text classification tool, it classifies the relationship between the given phrases as 'entailment', 'neutral', or 'contradiction'. ",
        ],
        'qnli': [
            "Analyze the text to determine if the answer to the question is implied in the context and specify 'entailment' or 'not_entailment'. ",
        ],
        'rte': [
            "Determine whether the given sentences have a cause-effect relationship as an engagement analysis tool and categorize them as 'entailment' or 'not_entailment'. ",
        ],
        'cola': [
            "Classify the grammar of a given sentence into two categories, 'acceptable' or 'unacceptable', and judge its accuracy. ",
        ],
        'mrpc': [
            "As an expert in semantic comparison, assess the similarity between the following two sentences and determine whether they are 'equivalent' or 'not_equivalent'. ",
        ],
        'wnli': [
            "Using implication analysis, determine whether the given sentences have a cause-effect relationship and categorize them as 'entailment' or 'not_entailment'. ",
        ],
        'squad_v2': [
            "Please tell me what your question is about. If there is no context in which you can provide an answer, respond with 'unanswerable'. ",
        ],
    }
}
