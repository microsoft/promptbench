# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import re
import random
from ..utils.dataprocess import InputProcess, OutputProcess

class ParaphraserInputProcess:
    def __call__(self, prompt: str, data: dict) -> str:
        raise NotImplementedError


class ParaphraserOutputProcess():
    def __call__(self, text: str, data: dict) -> dict:
        raise NotImplementedError
    

class EvaluatorInputProcess:
    def __call__(self, prompt: str, original_data: dict, paraphraserd_data: dict) -> str:
        raise NotImplementedError


class EvaluatorOutputProcess():
    def __call__(self, text: str) -> bool:
        raise NotImplementedError
    

class ChoicePermuter:
    @staticmethod
    def permute(choices_str: str, correct_answer: str) -> tuple:
        # Use regular expression to split the string into individual choices
        choices = re.split(r'\n(?=[A-E]:)', choices_str)

        # Extract the label and content of each choice
        labels = [choice.split(':', 1)[0] for choice in choices]
        contents = [choice.split(':', 1)[1].strip() for choice in choices]

        # Shuffle the contents
        random.shuffle(contents)

        # Reassign the shuffled contents to the original labels
        permuted_choices = [f"{labels[i]}: {contents[i]}" for i in range(len(contents))]

        # Find the new label for the correct answer
        correct_content = choices[ord(correct_answer) - ord('A')].split(':', 1)[1].strip()
        new_correct_answer = labels[contents.index(correct_content)]

        return '\n'.join(permuted_choices), new_correct_answer
   

class ParaphraserBasicInputProcess(ParaphraserInputProcess):
    def __call__(self, prompt: str, data: dict) -> str:
        return InputProcess.basic_format(prompt, data)
    

class ParaphraserQuestionOutputProcess(ParaphraserOutputProcess):
    def __call__(self, text: str, data: dict) -> dict:
        output = re.findall("<<<(.*?)>>>", text, re.DOTALL)
        if len(output) == 1:
            data["question"] = output[0]
            return data
        else:
            raise ValueError("Invalid output format")


class ParaphraserChoicesOutputProcess(ParaphraserOutputProcess):
    def __call__(self, text: str, data: dict) -> dict:
        output = re.findall("<<<(.*?)>>>", text, re.DOTALL)
        if len(output) == 1:
            choices = output[0]
            data["choices"] = choices
            return data
        else:
            raise ValueError("Invalid output format")


class EvaluatorMMLUQuestionInputProcess(EvaluatorInputProcess):
    def __call__(self, prompt: str, original_data: dict, paraphraserd_data: dict) -> str:
        data = {}
        data["question"] = original_data["question"]
        data["paraphrased"] = paraphraserd_data["question"]
        return InputProcess.basic_format(prompt, data)


class EvaluatorGSM8KQuestionInputProcess(EvaluatorInputProcess):
    def __call__(self, prompt: str, original_data: dict, paraphraserd_data: dict) -> str:
        data = {}
        data["question"] = original_data["question"]
        data["paraphrased"] = paraphraserd_data["question"]
        data["answer"] = original_data["answer"]
        return InputProcess.basic_format(prompt, data)
    

class EvaluatorMMLUParaphrasedChoicesInputProcess(EvaluatorInputProcess):
    def __call__(self, prompt: str, original_data: dict, paraphraserd_data: dict) -> str:
        data = {}
        data["question"] = original_data["question"]
        data["choices"] = original_data["choices"]
        data["paraphrased"] = paraphraserd_data["choices"]
        data["answer"] = original_data["answer"]
        return InputProcess.basic_format(prompt, data)


class EvaluatorMMLUNewChoiceInputProcess(EvaluatorInputProcess):
    def __call__(self, prompt: str, original_data: dict, paraphraserd_data: dict) -> str:
        data = {}
        data["question"] = original_data["question"]
        data["choices"] = original_data["choices"]
        data["new_choice"] = paraphraserd_data["choices"]
        data["answer"] = original_data["answer"]
        return InputProcess.basic_format(prompt, data)


class EvaluatorBasicOutputProcess(EvaluatorOutputProcess):
    def __call__(self, text: str) -> bool:
        output = re.findall("<<<(.*?)>>>", text, re.DOTALL)
        if len(output) == 1:
            if output[0].lower() == "yes":
                return True
            elif output[0].lower() == "no":
                return False
            else:
                raise ValueError("Invalid output format")
        else:
            raise ValueError("Invalid output format")