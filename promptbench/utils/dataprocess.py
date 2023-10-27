# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

class InputProcess:
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
    def general(raw_pred):
        """
        General processing for predictions using the base prediction process.

        Parameters:
        - raw_pred (str): The raw prediction text.

        Returns:
        - str: The processed prediction text.
        """
        return OutputProcess._base_pred_process(raw_pred)

    @staticmethod
    def cls(raw_pred):
        """
        Processes the prediction by taking the last word after basic processing.

        Parameters:
        - raw_pred (str): The raw prediction text.

        Returns:
        - str: The last word from the processed prediction text.
        """
        pred = OutputProcess._base_pred_process(raw_pred)
        return pred.split(" ")[-1]

    @staticmethod
    def pattern_split(raw_pred, pattern):
        """
        Processes the prediction by splitting it based on a provided pattern
        and taking the last part.

        Parameters:
        - raw_pred (str): The raw prediction text.
        - pattern (str): The pattern to split the prediction text on.

        Returns:
        - str: The last part of the prediction text after splitting.
        """
        return OutputProcess._base_pred_process(raw_pred.split(pattern)[-1])

    @staticmethod
    def pattern_re(raw_pred, pattern):
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
        return OutputProcess._base_pred_process(match.group(1) if match else raw_pred)
