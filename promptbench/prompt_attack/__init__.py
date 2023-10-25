from .attack import *
from .goal_function import AdvPromptGoalFunction

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


class Attack(object):
    def __init__(self, model, attack_name, dataset, prompt):
        self.model = model
        self.attack_name = attack_name
        self.dataset = dataset
        self.prompt = prompt
        self.goal_function = AdvPromptGoalFunction(self.model, self.dataset, query_budget=attack_config["goal_function"]["query_budget"], model_wrapper=None)
        self.unmodifiable_words = LABEL_SET[dataset]
        
        print(f"These words (if they appear in the prompt) are not allowed to be attacked:\n{self.unmodifiable_words}")
        self.attack = self._create_attack(attack_name, self.unmodifiable_words)

    @staticmethod
    def attack_list():
        return ["textbugger", "deepwordbug", "textfooler", "bertattack", "checklist", "stresstest", "semantic"]

    def _create_attack(self, attack, unmodifiable_words):
        if attack == "semantic":
            return None
        
        from promptbench.prompt_attack.label_constraint import LabelConstraint
        label_constraint = LabelConstraint(unmodifiable_words)
        
        if attack == "textfooler":

            transformation = WordSwapEmbedding(max_candidates=attack_config["textfooler"]["max_candidates"])
            stopwords = set(
                ["a", "about", "above", "across", "after", "afterwards", "again", "against", "ain", "all", "almost", "alone", "along", "already", "also", "although", "am", "among", "amongst", "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "aren", "aren't", "around", "as", "at", "back", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "both", "but", "by", "can", "cannot", "could", "couldn", "couldn't", "d", "didn", "didn't", "doesn", "doesn't", "don", "don't", "down", "due", "during", "either", "else", "elsewhere", "empty", "enough", "even", "ever", "everyone", "everything", "everywhere", "except", "first", "for", "former", "formerly", "from", "hadn", "hadn't", "hasn", "hasn't", "haven", "haven't", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "i", "if", "in", "indeed", "into", "is", "isn", "isn't", "it", "it's", "its", "itself", "just", "latter", "latterly", "least", "ll", "may", "me", "meanwhile", "mightn", "mightn't", "mine", "more", "moreover", "most", "mostly", "must", "mustn", "mustn't", "my", "myself", "namely", "needn", "needn't", "neither", "never", "nevertheless", "next", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "o", "of", "off", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "per", "please", "s", "same", "shan", "shan't", "she", "she's", "should've", "shouldn", "shouldn't", "somehow", "something", "sometime", "somewhere", "such", "t", "than", "that", "that'll", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "this", "those", "through", "throughout", "thru", "thus", "to", "too", "toward", "towards", "under", "unless", "until", "up", "upon", "used", "ve", "was", "wasn", "wasn't", "we", "were", "weren", "weren't", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "with", "within", "without", "won", "won't", "would", "wouldn", "wouldn't", "y", "yet", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
            )
            constraints = [RepeatModification(), StopwordModification(stopwords=stopwords)]
            input_column_modification = InputColumnModification(
                ["premise", "hypothesis"], {"premise"}
            )

            constraints.append(input_column_modification)

            constraints.append(WordEmbeddingDistance(min_cos_sim=attack_config["textfooler"]["min_word_cos_sim"]))
            constraints.append(PartOfSpeech(allow_verb_noun_swap=True))
            use_constraint = UniversalSentenceEncoder(
                threshold=attack_config["textfooler"]["min_sentence_cos_sim"],
                metric="angular",
                compare_against_original=False,
                window_size=15,
                skip_text_shorter_than_window=True,
            )
            constraints.append(use_constraint)
            goal_function = goal_function
            search_method = GreedyWordSwapWIR(wir_method="delete")

        elif attack == "textbugger":
            transformation = CompositeTransformation(
                [
                    WordSwapRandomCharacterInsertion(
                        random_one=True,
                        letters_to_insert=" ",
                        skip_first_char=True,
                        skip_last_char=True,
                    ),
                    WordSwapRandomCharacterDeletion(
                        random_one=True, skip_first_char=True, skip_last_char=True
                    ),
                    WordSwapNeighboringCharacterSwap(
                        random_one=True, skip_first_char=True, skip_last_char=True
                    ),
                    WordSwapHomoglyphSwap(),
                    WordSwapEmbedding(max_candidates=attack_config["textbugger"]["max_candidates"]),
                ]
            )

            constraints = [RepeatModification(), StopwordModification()]
            constraints.append(UniversalSentenceEncoder(threshold=attack_config["textbugger"]["min_sentence_cos_sim"]))
            
            search_method = GreedyWordSwapWIR(wir_method="delete")
        
        elif attack == "deepwordbug":

            transformation = CompositeTransformation(
                [
                    WordSwapNeighboringCharacterSwap(),
                    WordSwapRandomCharacterSubstitution(),
                    WordSwapRandomCharacterDeletion(),
                    WordSwapRandomCharacterInsertion(),
                ]
            )

            constraints = [RepeatModification(), StopwordModification()]
            constraints.append(LevenshteinEditDistance(attack_config["deepwordbug"]["levenshtein_edit_distance"]))
            search_method = GreedyWordSwapWIR() 

        elif attack == "bertattack":

            transformation = WordSwapMaskedLM(method="bert-attack", max_candidates=48)
            constraints = [RepeatModification(), StopwordModification()]

            constraints.append(MaxWordsPerturbed(max_percent=attack_config["bertattack"]["max_word_perturbed_percent"]))

            # larger threshold?
            use_constraint = UniversalSentenceEncoder(
                threshold=attack_config["bertattack"]["min_sentence_cos_sim"],
                metric="cosine",
                compare_against_original=True,
                window_size=None,
            )
            constraints.append(use_constraint)
            search_method = GreedyWordSwapWIR(wir_method="unk")

        elif attack == "checklist":
            from promptbench.prompt_attack.transformations import CheckListTransformation
            from promptbench.prompt_attack.search import BruteForceSearch
            transformation = CheckListTransformation()
            constraints = []
            search_method = BruteForceSearch()   

        elif attack == "stresstest":
            from promptbench.prompt_attack.transformations import StressTestTransformation
            from promptbench.prompt_attack.search import BruteForceSearch
            transformation = StressTestTransformation()
            constraints = []
            search_method = BruteForceSearch() 

        else:
            raise NotImplementedError
        
        # Adding label constraint
        constraints.append(label_constraint)
        goal_function = goal_function
        attack = AdvPromptAttack(goal_function, constraints, transformation, search_method)
        return attack
   
    def attack(self):
        if self.attack_name == "semantic":
            from ..prompts.semantic_atk_prompts import SEMANTIC_ADV_PROMPT_SET
            prompts_dict = SEMANTIC_ADV_PROMPT_SET[self.dataset.dataset_name]
            results = {}
            for language in prompts_dict.keys():
                prompts = prompts_dict[language]
                for prompt in prompts:
                    from ..utils import inference_total_dataset
                    acc = inference_total_dataset(prompt, self.model, self.dataset)
                    results[prompt] = acc
            
            return results
                  
        else:
            return self.attack.attack(self.prompt)

