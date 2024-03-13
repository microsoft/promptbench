# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from .dataset import *

SUPPORTED_DATASETS = [
    "sst2", "cola", "qqp",
    "mnli", "mnli_matched", "mnli_mismatched",
    "qnli", "wnli", "rte", "mrpc",
    "mmlu", "squad_v2", "un_multi", "iwslt2017", "math",
    "bool_logic", "valid_parentheses",
    "gsm8k", "csqa", "bigbench_date", "bigbench_object_tracking",
    "last_letter_concat", "numersense", "qasc",
    "bbh", "drop", "arc-easy", "arc-challenge",
]

SUPPORTED_DATASETS_VLM = [
    "vqav2", "nocaps", "science_qa", 
    "math_vista", "ai2d", "mmmu", "chart_qa"
]

class DatasetLoader:
    
    @staticmethod
    def load_dataset(dataset_name, task=None, supported_languages=None):
        """
        Load and return the specified dataset.

        This function acts as a factory method, returning the appropriate dataset object 
        based on the provided dataset name. 
        'math', 'un_multi' and 'iwslt' require additional arguments to specify the languages used in the dataset.

        Args:
            dataset_name (str): The name of the dataset to load.
            task: str: Additional arguments required by 'math'. 
                        Please visit https://huggingface.co/datasets/math_dataset/ to see the supported tasks for math.
            supported_languages: list: Additional arguments required by 'iwslt'. 
                                Please visit https://huggingface.co/datasets/iwslt2017 to see the supported languages for iwslt.
                                e.g. supported_languages=['de-en', 'ar-en'] for German-English and Arabic-English translation.
        Returns:
            Dataset object corresponding to the given dataset_name.
            The dataset object is an instance of a list, each element is a dictionary. Please refer to each dataset's documentation for details.

        Raises:
            NotImplementedError: If the dataset_name does not correspond to any known dataset.
        """        
        # GLUE datasets
        if dataset_name in ["cola", "sst2", "qqp", "mnli", "mnli_matched", "mnli_mismatched", 
                            "qnli", "wnli", "rte", "mrpc"]:
            return GLUE(dataset_name)
        elif dataset_name == 'mmlu':
            return MMLU()
        elif dataset_name == "squad_v2":
            return SQUAD_V2()
        elif dataset_name == 'un_multi':
            return UnMulti()
        elif dataset_name == 'iwslt2017':
            return IWSLT(supported_languages)
        elif dataset_name in 'math':
            return Math(task)
        elif dataset_name == 'bool_logic':
            return BoolLogic()
        elif dataset_name == 'valid_parentheses':
            return ValidParentheses()
        elif dataset_name == 'gsm8k':
            return GSM8K()
        elif dataset_name == 'csqa':
            return CSQA()
        elif dataset_name == 'qasc':
            return QASC()
        elif 'bigbench' in dataset_name:
            return BigBench(dataset_name)
        elif dataset_name == 'bbh':
            return BBH()
        elif dataset_name == 'drop':
            return DROP()
        elif dataset_name == 'arc-easy':
            return ARC('ARC-Easy')
        elif dataset_name == 'arc-challenge':
            return ARC('ARC-Challenge')
        elif dataset_name == 'vqav2':
            return VQAv2()
        elif dataset_name =='nocaps':
            return NoCaps()
        elif dataset_name =='math_vista':
            return MathVista()
        elif dataset_name == 'ai2d':
            return AI2D()
        elif dataset_name == 'mmmu':
            return MMMU()
        elif dataset_name == 'chart_qa':
            return ChartQA()
        elif dataset_name == 'science_qa':
            return ScienceQA()
        else:
            # If the dataset name doesn't match any known datasets, raise an error
            raise NotImplementedError(f"Dataset '{dataset_name}' is not supported.")

