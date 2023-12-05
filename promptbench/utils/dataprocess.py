# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

class InputProcess:
    """
    A utility class for processing input data for language models.

    This class provides static methods to format input data based on given prompt templates and input data dictionaries.

    Methods:
    --------
    basic_format(prompt_template, input_data_dict)
        Combines a prompt template and input data to create a formatted model input.
    """
    @staticmethod
    def basic_format(prompt_template, input_data_dict):
        """
        Combine the prompt and input to create an input for the model.

        Parameters:
        - prompt_template (str): The template for the prompt with placeholders.
        - input_data_dict (dict): Dictionary containing data to fill in the template.

        Returns:
        - str: The combined model input.
        """
        return prompt_template.format(**input_data_dict)

    # Additional input processing methods can be added here.
    # ...

class OutputProcess:
    """
    A utility class for processing raw predictions from language models.

    This class provides static methods for various ways to process and clean up raw prediction text.

    Methods:
    --------
    general(raw_pred, proj_func=None)
        Performs general processing on the raw prediction text.
    cls(raw_pred, proj_func=None)
        Processes the raw prediction text for classification tasks.
    pattern_split(raw_pred, pattern, proj_func=None)
        Splits the raw prediction text based on a pattern.
    pattern_re(raw_pred, pattern, proj_func=None)
        Uses regular expressions to process the raw prediction text.
    """
    
    @staticmethod
    def _base_pred_process(pred):
        """
        Basic processing for predictions which involves lowercasing, 
        removing special tokens and stripping unwanted characters.

        Parameters:
        - pred (str): The raw prediction text.

        Returns:
        - str: The processed prediction text.
        """
        pred = pred.lower().replace("<pad>", "").replace("</s>", "").strip(",._\"\'-+=!?()&^%$#@:\\|\{\}[]<>/`\n\t\r\v\f ")
        return pred

    @staticmethod
    def general(raw_pred, proj_func=None):
        """
        General processing for predictions using the base prediction process.

        Parameters:
        - raw_pred (str): The raw prediction text.

        Returns:
        - str: The processed prediction text.
        """
        pred = OutputProcess._base_pred_process(raw_pred)
        if proj_func:
            pred = proj_func(pred)
        return pred

    @staticmethod
    def cls(raw_pred, proj_func=None):
        """
        Processes the prediction by taking the last word after basic processing.

        Parameters:
        - raw_pred (str): The raw prediction text.

        Returns:
        - str: The last word from the processed prediction text.
        """
        pred = OutputProcess._base_pred_process(raw_pred).split(" ")[-1]
        if proj_func:
            pred = proj_func(pred)
        return pred

    @staticmethod
    def pattern_split(raw_pred, pattern, proj_func=None):
        """
        Processes the prediction by splitting it based on a provided pattern
        and taking the last part.

        Parameters:
        - raw_pred (str): The raw prediction text.
        - pattern (str): The pattern to split the prediction text on.

        Returns:
        - str: The last part of the prediction text after splitting.
        """
        pred = OutputProcess._base_pred_process(raw_pred.split(pattern)[-1])
        if proj_func:
            pred = proj_func(pred)

        return pred   
    
    @staticmethod
    def pattern_re(raw_pred, pattern, proj_func=None):
        """
        Processes the prediction using regular expressions to extract a specific pattern.

        Parameters:
        - raw_pred (str): The raw prediction text.
        - pattern (str): The regular expression pattern to search for.

        Returns:
        - str: The matched pattern from the prediction text, or the original text if no match.
        """
        import re
        match = re.search(pattern, raw_pred)
        if match:
            pred = OutputProcess._base_pred_process(match.group(1))
            if proj_func:
                pred = proj_func(pred)
        else:
            pred = raw_pred
        
        return pred
