import argparse
import os
import logging
import pretty_errors

from promptbench.config import *
from promptbench.dataload import create_dataset
from promptbench.inference import Inference
from promptbench.prompt_attack.attack import *
from promptbench.prompt_attack.goal_function import AdvPromptGoalFunction
from promptbench.config import MODEL_SET, DATA_SET, ATTACK_SET

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
    def __init__(self, model, attack_name, unmodifiable_words, dataset, prompt):
        self.model = model
        self.attack_name = attack_name
        self.dataset = dataset
        self.prompt = prompt
        self.goal_function = self._create_goal_function()
        self.attack = self._create_attack(attack_name, unmodifiable_words)

    @staticmethod
    def attack_name_list():
        return ["textbugger", "deepwordbug", "textfooler", "bertattack", "checklist", "stresstest", "semantic"]

    def _create_goal_function(self):
        return AdvPromptGoalFunction(inference=self.model, query_budget=attack_config["goal_function"]["query_budget"], model_wrapper=None)

    def _create_attack(self, attack, unmodifiable_words):
        if attack == "semantic":
            return None
        
        from promptbench.config import LABEL_SET
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
            pass
        else:
            return self.attack.attack(self.prompt)