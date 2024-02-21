# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
#
# Source Attribution:
# The majority of this code is derived from the following sources:
# - TextAttack GitHub Repository: https://github.com/QData/TextAttack
# - Reference Paper: Morris, John X., et al. "TextAttack: A Framework for Adversarial Attacks, Data Augmentation, and Adversarial Training in NLP." arXiv preprint arXiv:2005.05909 (2020).



"""
Attack Class
"""

from collections import OrderedDict
from typing import List, Union

import lru
import torch

import textattack
from textattack.attack_results import (
    FailedAttackResult,
    MaximizedAttackResult,
    SkippedAttackResult,
    SuccessfulAttackResult,
)
from textattack.constraints import Constraint, PreTransformationConstraint
from textattack.goal_function_results import GoalFunctionResultStatus
from textattack.goal_functions import GoalFunction
from textattack.models.wrappers import ModelWrapper
from textattack.shared import AttackedText, utils


from textattack.constraints.grammaticality import PartOfSpeech
from textattack.constraints.semantics import WordEmbeddingDistance
from textattack.constraints.overlap import LevenshteinEditDistance, MaxWordsPerturbed
from textattack.constraints.semantics.sentence_encoders import UniversalSentenceEncoder

from textattack.constraints.pre_transformation import (
    InputColumnModification,
    RepeatModification,
    StopwordModification,
)
from textattack.search_methods import SearchMethod, GreedyWordSwapWIR


from textattack.transformations import (
    Transformation,
    CompositeTransformation,
    WordSwapEmbedding,
    WordSwapHomoglyphSwap,
    WordSwapNeighboringCharacterSwap,
    WordSwapRandomCharacterDeletion,
    WordSwapRandomCharacterInsertion,
    WordSwapRandomCharacterSubstitution,
    WordSwapMaskedLM,
)

from .__init__ import LABEL_SET, attack_config
from .goal_function import AdvPromptGoalFunction


class Attack(object):
    def __init__(self, model, attack_name, dataset, prompt, eval_func, unmodifiable_words=None, verbose=True):
        """
        model: the model to attack
        attack_name: the name of the attack, e.g. "textfooler", "textbugger", "deepwordbug", "bertattack", "checklist", "stresstest", "semantic"
        dataset: the dataset for prompt attack
        prompt: the prompt to attack
        eval_func: the evaluation function to evaluate the performance of a prompt, the interface is eval_func(prompt, dataset, model), in this function, you need to implement the logic to get the prediction of the model on the prompt, and evaluate the correctness of the prediction, finally, return the accuracy of the model on the prompt.
        unmodifiable_words: the words that are not allowed to be attacked
        verbose: whether to print the attack process

        return: None
        """
        self.model = model
        self.attack_name = attack_name
        self.dataset = dataset
        self.prompt = prompt
        self.eval_func = eval_func
        self.goal_function = AdvPromptGoalFunction(self.model, 
                                                   self.dataset,  
                                                   eval_func, 
                                                   query_budget=attack_config["goal_function"]["query_budget"], 
                                                   model_wrapper=None,
                                                   verbose=verbose)
        if unmodifiable_words:
            self.unmodifiable_words = unmodifiable_words
        else:
            print("Using default unmodifiable words.")
            self.unmodifiable_words = LABEL_SET[dataset]
        
        print(f"These words (if they appear in the prompt) are not allowed to be attacked:\n{self.unmodifiable_words}")
        self.prompt_attack = self._create_attack(attack_name)

    @staticmethod
    def attack_list():
        return ["textbugger", "deepwordbug", "textfooler", "bertattack", "checklist", "stresstest", "semantic"]

    def _create_attack(self, attack):
        if attack == "semantic":
            return None
        
        from promptbench.prompt_attack.label_constraint import LabelConstraint
        label_constraint = LabelConstraint(self.unmodifiable_words)
        
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
        attack = AdvPromptAttack(self.goal_function, constraints, transformation, search_method)
        return attack
   
    def attack(self):
        if self.attack_name == "semantic":
            from ..prompts.semantic_atk_prompts import SEMANTIC_ADV_PROMPT_SET
            prompts_dict = SEMANTIC_ADV_PROMPT_SET[self.dataset.dataset_name]
            results = {}
            for language in prompts_dict.keys():
                prompts = prompts_dict[language]
                for prompt in prompts:
                    acc = self.eval_func(prompt, self.dataset, self.model)
                    results[prompt] = acc
            
            return results
                  
        else:
            return self.prompt_attack.attack(self.prompt)


class AdvPromptAttack:
    """An attack generates adversarial examples on text.

    An attack is comprised of a goal function, constraints, transformation, and a search method. Use :meth:`attack` method to attack one sample at a time.

    Args:
        goal_function (:class:`~textattack.goal_functions.GoalFunction`):
            A function for determining how well a perturbation is doing at achieving the attack's goal.
        constraints (list of :class:`~textattack.constraints.Constraint` or :class:`~textattack.constraints.PreTransformationConstraint`):
            A list of constraints to add to the attack, defining which perturbations are valid.
        transformation (:class:`~textattack.transformations.Transformation`):
            The transformation applied at each step of the attack.
        search_method (:class:`~textattack.search_methods.SearchMethod`):
            The method for exploring the search space of possible perturbations
        transformation_cache_size (:obj:`int`, `optional`, defaults to :obj:`2**15`):
            The number of items to keep in the transformations cache
        constraint_cache_size (:obj:`int`, `optional`, defaults to :obj:`2**15`):
            The number of items to keep in the constraints cache

    Example::

        >>> import textattack
        >>> import transformers

        >>> # Load model, tokenizer, and model_wrapper
        >>> model = transformers.AutoModelForSequenceClassification.from_pretrained("textattack/bert-base-uncased-imdb")
        >>> tokenizer = transformers.AutoTokenizer.from_pretrained("textattack/bert-base-uncased-imdb")
        >>> model_wrapper = textattack.models.wrappers.HuggingFaceModelWrapper(model, tokenizer)

        >>> # Construct our four components for `Attack`
        >>> from textattack.constraints.pre_transformation import RepeatModification, StopwordModification
        >>> from textattack.constraints.semantics import WordEmbeddingDistance

        >>> goal_function = textattack.goal_functions.UntargetedClassification(model_wrapper)
        >>> constraints = [
        ...     RepeatModification(),
        ...     StopwordModification()
        ...     WordEmbeddingDistance(min_cos_sim=0.9)
        ... ]
        >>> transformation = WordSwapEmbedding(max_candidates=50)
        >>> search_method = GreedyWordSwapWIR(wir_method="delete")

        >>> # Construct the actual attack
        >>> attack = Attack(goal_function, constraints, transformation, search_method)

        >>> input_text = "I really enjoyed the new movie that came out last month."
        >>> label = 1 #Positive
        >>> attack_result = attack.attack(input_text, label)
    """

    def __init__(
        self,
        goal_function: GoalFunction,
        constraints: List[Union[Constraint, PreTransformationConstraint]],
        transformation: Transformation,
        search_method: SearchMethod,
        transformation_cache_size=2**15,
        constraint_cache_size=2**15,
    ):
        """Initialize an attack object.

        Attacks can be run multiple times.
        """
        assert isinstance(
            constraints, list
        ), "`constraints` must be a list of `textattack.constraints.Constraint` or `textattack.constraints.PreTransformationConstraint`."
        for c in constraints:
            assert isinstance(
                c, (Constraint, PreTransformationConstraint)
            ), "`constraints` must be a list of `textattack.constraints.Constraint` or `textattack.constraints.PreTransformationConstraint`."
        assert isinstance(
            transformation, Transformation
        ), f"`transformation` must be of type `textattack.transformations.Transformation`, but got type `{type(transformation)}`."
        assert isinstance(
            search_method, SearchMethod
        ), f"`search_method` must be of type `textattack.search_methods.SearchMethod`, but got type `{type(search_method)}`."

        self.goal_function = goal_function
        self.search_method = search_method
        self.transformation = transformation
        self.is_black_box = (
            getattr(transformation, "is_black_box", True) and search_method.is_black_box
        )

        if not self.search_method.check_transformation_compatibility(
            self.transformation
        ):
            raise ValueError(
                f"SearchMethod {self.search_method} incompatible with transformation {self.transformation}"
            )

        self.constraints = []
        self.pre_transformation_constraints = []
        for constraint in constraints:
            if isinstance(
                constraint,
                textattack.constraints.PreTransformationConstraint,
            ):
                self.pre_transformation_constraints.append(constraint)
            else:
                self.constraints.append(constraint)

        # Check if we can use transformation cache for our transformation.
        if not self.transformation.deterministic:
            self.use_transformation_cache = False
        elif isinstance(self.transformation, CompositeTransformation):
            self.use_transformation_cache = True
            for t in self.transformation.transformations:
                if not t.deterministic:
                    self.use_transformation_cache = False
                    break
        else:
            self.use_transformation_cache = True
        self.transformation_cache_size = transformation_cache_size
        self.transformation_cache = lru.LRU(transformation_cache_size)

        self.constraint_cache_size = constraint_cache_size
        self.constraints_cache = lru.LRU(constraint_cache_size)

        # Give search method access to functions for getting transformations and evaluating them
        self.search_method.get_transformations = self.get_transformations
        # Give search method access to self.goal_function for model query count, etc.
        self.search_method.goal_function = self.goal_function
        # The search method only needs access to the first argument. The second is only used
        # by the attack class when checking whether to skip the sample
        self.search_method.get_goal_results = self.goal_function.get_results

        # Give search method access to get indices which need to be ordered / searched
        self.search_method.get_indices_to_order = self.get_indices_to_order

        self.search_method.filter_transformations = self.filter_transformations

    def clear_cache(self, recursive=True):
        self.constraints_cache.clear()
        if self.use_transformation_cache:
            self.transformation_cache.clear()
        if recursive:
            self.goal_function.clear_cache()
            for constraint in self.constraints:
                if hasattr(constraint, "clear_cache"):
                    constraint.clear_cache()

    def cpu_(self):
        """Move any `torch.nn.Module` models that are part of Attack to CPU."""
        visited = set()

        def to_cpu(obj):
            visited.add(id(obj))
            if isinstance(obj, torch.nn.Module):
                obj.cpu()
            elif isinstance(
                obj,
                (
                    AdvPromptAttack,
                    GoalFunction,
                    Transformation,
                    SearchMethod,
                    Constraint,
                    PreTransformationConstraint,
                    ModelWrapper,
                ),
            ):
                for key in obj.__dict__:
                    s_obj = obj.__dict__[key]
                    if id(s_obj) not in visited:
                        to_cpu(s_obj)
            elif isinstance(obj, (list, tuple)):
                for item in obj:
                    if id(item) not in visited and isinstance(
                        item, (Transformation, Constraint, PreTransformationConstraint)
                    ):
                        to_cpu(item)

        to_cpu(self)

    def cuda_(self):
        """Move any `torch.nn.Module` models that are part of Attack to GPU."""
        visited = set()

        def to_cuda(obj):
            visited.add(id(obj))
            if isinstance(obj, torch.nn.Module):
                obj.to(textattack.shared.utils.device)
            elif isinstance(
                obj,
                (
                    AdvPromptAttack,
                    GoalFunction,
                    Transformation,
                    SearchMethod,
                    Constraint,
                    PreTransformationConstraint,
                    ModelWrapper,
                ),
            ):
                for key in obj.__dict__:
                    s_obj = obj.__dict__[key]
                    if id(s_obj) not in visited:
                        to_cuda(s_obj)
            elif isinstance(obj, (list, tuple)):
                for item in obj:
                    if id(item) not in visited and isinstance(
                        item, (Transformation, Constraint, PreTransformationConstraint)
                    ):
                        to_cuda(item)

        to_cuda(self)

    def get_indices_to_order(self, current_text, **kwargs):
        """Applies ``pre_transformation_constraints`` to ``text`` to get all
        the indices that can be used to search and order.

        Args:
            current_text: The current ``AttackedText`` for which we need to find indices are eligible to be ordered.
        Returns:
            The length and the filtered list of indices which search methods can use to search/order.
        """

        indices_to_order = self.transformation(
            current_text,
            pre_transformation_constraints=self.pre_transformation_constraints,
            return_indices=True,
            **kwargs,
        )

        len_text = len(indices_to_order)

        # Convert indices_to_order to list for easier shuffling later
        return len_text, list(indices_to_order)

    def _get_transformations_uncached(self, current_text, original_text=None, **kwargs):
        """Applies ``self.transformation`` to ``text``, then filters the list
        of possible transformations through the applicable constraints.

        Args:
            current_text: The current ``AttackedText`` on which to perform the transformations.
            original_text: The original ``AttackedText`` from which the attack started.
        Returns:
            A filtered list of transformations where each transformation matches the constraints
        """
        transformed_texts = self.transformation(
            current_text,
            pre_transformation_constraints=self.pre_transformation_constraints,
            **kwargs,
        )

        return transformed_texts

    def get_transformations(self, current_text, original_text=None, **kwargs):
        """Applies ``self.transformation`` to ``text``, then filters the list
        of possible transformations through the applicable constraints.

        Args:
            current_text: The current ``AttackedText`` on which to perform the transformations.
            original_text: The original ``AttackedText`` from which the attack started.
        Returns:
            A filtered list of transformations where each transformation matches the constraints
        """
        if not self.transformation:
            raise RuntimeError(
                "Cannot call `get_transformations` without a transformation."
            )

        if self.use_transformation_cache:
            cache_key = tuple([current_text] + sorted(kwargs.items()))
            if utils.hashable(cache_key) and cache_key in self.transformation_cache:
                # promote transformed_text to the top of the LRU cache
                self.transformation_cache[cache_key] = self.transformation_cache[
                    cache_key
                ]
                transformed_texts = list(self.transformation_cache[cache_key])
            else:
                transformed_texts = self._get_transformations_uncached(
                    current_text, original_text, **kwargs
                )
                if utils.hashable(cache_key):
                    self.transformation_cache[cache_key] = tuple(transformed_texts)
        else:
            transformed_texts = self._get_transformations_uncached(
                current_text, original_text, **kwargs
            )

        return self.filter_transformations(
            transformed_texts, current_text, original_text
        )

    def _filter_transformations_uncached(
        self, transformed_texts, current_text, original_text=None
    ):
        """Filters a list of potential transformed texts based on
        ``self.constraints``

        Args:
            transformed_texts: A list of candidate transformed ``AttackedText`` to filter.
            current_text: The current ``AttackedText`` on which the transformation was applied.
            original_text: The original ``AttackedText`` from which the attack started.
        """
        filtered_texts = transformed_texts[:]
        for C in self.constraints:
            if len(filtered_texts) == 0:
                break
            if C.compare_against_original:
                if not original_text:
                    raise ValueError(
                        f"Missing `original_text` argument when constraint {type(C)} is set to compare against `original_text`"
                    )

                filtered_texts = C.call_many(filtered_texts, original_text)
            else:
                filtered_texts = C.call_many(filtered_texts, current_text)
        # Default to false for all original transformations.
        for original_transformed_text in transformed_texts:
            self.constraints_cache[(current_text, original_transformed_text)] = False
        # Set unfiltered transformations to True in the cache.
        for filtered_text in filtered_texts:
            self.constraints_cache[(current_text, filtered_text)] = True
        return filtered_texts

    def filter_transformations(
        self, transformed_texts, current_text, original_text=None
    ):
        """Filters a list of potential transformed texts based on
        ``self.constraints`` Utilizes an LRU cache to attempt to avoid
        recomputing common transformations.

        Args:
            transformed_texts: A list of candidate transformed ``AttackedText`` to filter.
            current_text: The current ``AttackedText`` on which the transformation was applied.
            original_text: The original ``AttackedText`` from which the attack started.
        """
        # Remove any occurences of current_text in transformed_texts
        transformed_texts = [
            t for t in transformed_texts if t.text != current_text.text
        ]
        # Populate cache with transformed_texts
        uncached_texts = []
        filtered_texts = []
        for transformed_text in transformed_texts:
            if (current_text, transformed_text) not in self.constraints_cache:
                uncached_texts.append(transformed_text)
            else:
                # promote transformed_text to the top of the LRU cache
                self.constraints_cache[
                    (current_text, transformed_text)
                ] = self.constraints_cache[(current_text, transformed_text)]
                if self.constraints_cache[(current_text, transformed_text)]:
                    filtered_texts.append(transformed_text)
        filtered_texts += self._filter_transformations_uncached(
            uncached_texts, current_text, original_text=original_text
        )
        # Sort transformations to ensure order is preserved between runs
        filtered_texts.sort(key=lambda t: t.text)
        return filtered_texts

    def _attack(self, initial_result):
        """Calls the ``SearchMethod`` to perturb the ``AttackedText`` stored in
        ``initial_result``.

        Args:
            initial_result: The initial ``GoalFunctionResult`` from which to perturb.

        Returns:
            A ``SuccessfulAttackResult``, ``FailedAttackResult``,
                or ``MaximizedAttackResult``.
        """
        final_result = self.search_method(initial_result)
        self.clear_cache()
        if final_result.goal_status == GoalFunctionResultStatus.SUCCEEDED:
            result = SuccessfulAttackResult(
                initial_result,
                final_result,
            )
        elif final_result.goal_status == GoalFunctionResultStatus.SEARCHING:
            result = FailedAttackResult(
                initial_result,
                final_result,
            )
        elif final_result.goal_status == GoalFunctionResultStatus.MAXIMIZING:
            result = MaximizedAttackResult(
                initial_result,
                final_result,
            )
        else:
            raise ValueError(f"Unrecognized goal status {final_result.goal_status}")
        return  {
            "original prompt": result.original_result.attacked_text.text,
            "original score": result.original_result.output, 
            "attacked prompt": result.perturbed_result.attacked_text.text, 
            "attacked score": result.perturbed_result.output, 
            "PDR": (result.original_result.output-result.perturbed_result.output) / result.original_result.output
        }

    def attack(self, example):
        """Attack a single example.

        Args:
            example (:obj:`str`, :obj:`OrderedDict[str, str]` or :class:`~textattack.shared.AttackedText`):
                Example to attack. It can be a single string or an `OrderedDict` where
                keys represent the input fields (e.g. "premise", "hypothesis") and the values are the actual input textx.
                Also accepts :class:`~textattack.shared.AttackedText` that wraps around the input.
            ground_truth_output(:obj:`int`, :obj:`float` or :obj:`str`):
                Ground truth output of `example`.
                For classification tasks, it should be an integer representing the ground truth label.
                For regression tasks (e.g. STS), it should be the target value.
                For seq2seq tasks (e.g. translation), it should be the target string.
        Returns:
            :class:`~textattack.attack_results.AttackResult` that represents the result of the attack.
        """
        assert isinstance(
            example, (str, OrderedDict, AttackedText)
        ), "`example` must either be `str`, `collections.OrderedDict`, `textattack.shared.AttackedText`."
        if isinstance(example, (str, OrderedDict)):
            example = AttackedText(example)

        # assert isinstance(
        #     ground_truth_output, (int, str)
        # ), "`ground_truth_output` must either be `str` or `int`."
        
        # Allow ground_truth_output to be float (acc). 
        goal_function_result, _ = self.goal_function.init_attack_example(example)
        if goal_function_result.goal_status == GoalFunctionResultStatus.SKIPPED:
            return SkippedAttackResult(goal_function_result)
        else:
            result = self._attack(goal_function_result)
            return result

    def __repr__(self):
        """Prints attack parameters in a human-readable string.

        Inspired by the readability of printing PyTorch nn.Modules:
        https://github.com/pytorch/pytorch/blob/master/torch/nn/modules/module.py
        """
        main_str = "Attack" + "("
        lines = []

        lines.append(utils.add_indent(f"(search_method): {self.search_method}", 2))
        # self.goal_function
        lines.append(utils.add_indent(f"(goal_function):  {self.goal_function}", 2))
        # self.transformation
        lines.append(utils.add_indent(f"(transformation):  {self.transformation}", 2))
        # self.constraints
        constraints_lines = []
        constraints = self.constraints + self.pre_transformation_constraints
        if len(constraints):
            for i, constraint in enumerate(constraints):
                constraints_lines.append(utils.add_indent(f"({i}): {constraint}", 2))
            constraints_str = utils.add_indent("\n" + "\n".join(constraints_lines), 2)
        else:
            constraints_str = "None"
        lines.append(utils.add_indent(f"(constraints): {constraints_str}", 2))
        # self.is_black_box
        lines.append(utils.add_indent(f"(is_black_box):  {self.is_black_box}", 2))
        main_str += "\n  " + "\n  ".join(lines) + "\n"
        main_str += ")"
        return main_str

    def __getstate__(self):
        state = self.__dict__.copy()
        state["transformation_cache"] = None
        state["constraints_cache"] = None
        return state

    def __setstate__(self, state):
        self.__dict__ = state
        self.transformation_cache = lru.LRU(self.transformation_cache_size)
        self.constraints_cache = lru.LRU(self.constraint_cache_size)

    __str__ = __repr__
