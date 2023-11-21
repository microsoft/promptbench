from .dataset import *


class DatasetLoader:
    SUPPORTED_DATASETS = [
        "cola", "sst2", "qqp", "mnli", "mnli_matched", "mnli_mismatched", 
        "qnli", "wnli", "rte", "mrpc", "mmlu", "squad_v2", "un_multi", 
        "iwslt", "math", "bool_logic", "valid_parentheses", 
        'gsm8k', "csqa", "bigbench_date", "bigbench_object_tracking"
        # todo gsm8k
    ]

    @staticmethod
    def dataset_list():
        """
        Return a list of all supported datasets.
        """
        return DatasetLoader.SUPPORTED_DATASETS

    @staticmethod
    def load_dataset(dataset_name, *args):
        """
        Load and return the specified dataset.

        This function acts as a factory method, returning the appropriate dataset object 
        based on the provided dataset name. Note that 'un_multi' and 'iwslt' require 
        additional arguments to specify the languages used in the dataset.
        
        The supported languages are: 
        LANGUAGES = {
            'de': 'German',
            'en': 'English',
            'fr': 'French',
        }

        Args:
            dataset_name (str): The name of the dataset to load.
            *args: Additional arguments required by specific datasets.

        Returns:
            Dataset object corresponding to the given dataset_name.

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
            return UnMulti(args[0])  # First argument specifies a configuration for 'un_multi'
        elif dataset_name == 'iwslt':
            return IWSLT(args[0])    # First argument specifies a configuration for 'iwslt'
        elif dataset_name == 'math':
            return Math()
        elif dataset_name == 'bool_logic':
            return BoolLogic()
        elif dataset_name == 'valid_parentheses':
            return ValidParentheses()
        elif dataset_name == 'gsm8k':
            return GSM8K()
        elif dataset_name == 'csqa':
            return CSQA()
        elif 'bigbench' in dataset_name:
            return BigBench(dataset_name)
        else:
            # If the dataset name doesn't match any known datasets, raise an error
            raise NotImplementedError(f"Dataset '{dataset_name}' is not supported.")

