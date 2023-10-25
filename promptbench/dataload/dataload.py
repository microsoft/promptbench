# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
import requests
import json

from promptbench.config import *
from datasets import load_dataset


DATA_SET = [
    "sst2", "cola", "qqp",
    "mnli", "mnli_matched", "mnli_mismatched",
    "qnli", "wnli", "rte", "mrpc",
    "mmlu", "squad_v2", "un_multi", "iwslt", "math",
    "bool_logic", "valid_parentheses"
]

class Dataset(object):
    def __init__(self, dataset_name):
        self.data = []
        self.data_list = DATA_SET

        # Get the parent directory
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(cur_dir)

        # Construct the path to the data directory in A
        self.data_dir = os.path.join(parent_dir, 'data')

        # check if the data path exists
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)
        
        # check if the dataset exists, if not, download it
        self.filepath = os.path.join(self.data_dir, f"{dataset_name}.json")
        if not os.path.exists(self.filepath):
            url = f'https://wjdcloud.blob.core.windows.net/dataset/promptbench/dataset/{dataset_name}.json'
            print(f"Downloading {dataset_name} dataset...")
            response = requests.get(url)
            with open(self.filepath, 'wb') as f:
                f.write(response.content)


    def __len__(self):
        assert len(self.data) > 0, "Empty dataset. Please load data first."
        return len(self.data)

    def __getitem__(self, idx):
        assert len(self.data) > 0, "Empty dataset. Please load data first."
        return self.data[idx]

    @staticmethod
    def data_list(self):
        return self.data_list


class BoolLogic(Dataset):
    def __init__(self):
        super().__init__("bool_logic")
        with open(self.filepath, 'r') as f:
            data = json.load(f)
        
        self.data = [{"content": d["question"], "label": "true" if d["answer"] else "false"} for d in data]


class ValidParentheses(Dataset):
    def __init__(self):
        super().__init__("valid_parentheses")

        with open(self.filepath, 'r') as f:
            data = json.load(f)["examples"][:100]
        for d in data:
            self.data.append(
                {"content": d["input"], "label": "valid" if d["target_scores"]["Valid"] == 1 else "invalid"})


class Math(Dataset):
    def __init__(self) -> None:
        super().__init__("math")
        
        with open(self.filepath, 'r') as f:
            data = json.load(f)
        
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
        
        for task in data.keys():
            for d in data[task]:
                d["task"] = MATH_QUESTION_TYPES[task]
                self.data.append(d)


class UnMulti(Dataset):

    def __init__(self, supported_languages):
        super().__init__("un_multi")

        with open(self.filepath, 'r') as f:
            data = json.load(f)
        self.data = dict()

        idx = 0
        supported_tasks = []
        for task_i in data.keys():
            source, target = task_i.split('-')
            if source in supported_languages and target in supported_languages:
                supported_tasks.append(task_i)

        num_tasks = len(supported_tasks)
        num_samples = 100

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

        for task_i in supported_tasks:
            source, target = task_i.split('-')
            for d in data[task_i][:int(num_samples//num_tasks)]:
                self.data[idx] = {
                    'source': d[source],
                    'target': d[target],
                    'soruce_lang': LANGUAGES[source],
                    'target_lang': LANGUAGES[target],
                }
                idx += 1


class IWSLT(Dataset):
    def __init__(self, supported_languages):
        super().__init__("iwslt")

        with open(self.filepath, 'r') as f:
            data = json.load(f)
        self.data = dict()

        idx = 0
        supported_tasks = []
        for task_i in data.keys():
            source, target = task_i.split('-')
            if source in supported_languages and target in supported_languages:
                supported_tasks.append(task_i)

        num_tasks = len(supported_tasks)
        num_samples = 100

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

        for task_i in supported_tasks:
            source, target = task_i.split('-')
            for d in data[task_i][:int(num_samples//num_tasks)]:
                self.data[idx] = {
                    'source': d[source],
                    'target': d[target],
                    'soruce_lang': LANGUAGES[source],
                    'target_lang': LANGUAGES[target],
                }
                idx += 1


class SQUAD_V2(Dataset):
    def __init__(self):
        super().__init__("squad_v2")
        with open(self.filepath, "r") as file:
            data = json.load(file)
        
        for d in data:
            self.data.append({"id": d["id"], "content": "Context: " + d["context"] + "\n" + "Question: " + d["question"] + "\n", "answers": d["answers"]})

        import random
        random.seed(42)
        random.shuffle(self.data)
        self.data = self.data[:200]


class MMLU(Dataset):
    def __init__(self):
        super().__init__("mmlu")
        self.tasks = ['high_school_european_history', 'business_ethics', 'clinical_knowledge', 'medical_genetics',
                      'high_school_us_history', 'high_school_physics', 'high_school_world_history', 'virology',
                      'high_school_microeconomics', 'econometrics', 'college_computer_science', 'high_school_biology',
                      'abstract_algebra', 'professional_accounting', 'philosophy', 'professional_medicine', 'nutrition',
                      'global_facts', 'machine_learning', 'security_studies', 'public_relations', 'professional_psychology',
                      'prehistory', 'anatomy', 'human_sexuality', 'college_medicine', 'high_school_government_and_politics',
                      'college_chemistry', 'logical_fallacies', 'high_school_geography', 'elementary_mathematics', 'human_aging',
                      'college_mathematics', 'high_school_psychology', 'formal_logic', 'high_school_statistics', 'international_law',
                      'high_school_mathematics', 'high_school_computer_science', 'conceptual_physics', 'miscellaneous', 'high_school_chemistry',
                      'marketing', 'professional_law', 'management', 'college_physics', 'jurisprudence', 'world_religions', 'sociology',
                      'us_foreign_policy', 'high_school_macroeconomics', 'computer_security', 'moral_scenarios', 'moral_disputes',
                      'electrical_engineering', 'astronomy', 'college_biology']
        
        with open(self.filepath, "r") as file:
            self.raw_data = json.load(file)

        cnt = {}
        self.data = []

        for task in self.tasks:
            cnt[task] = 0

        for d in self.raw_data:
            task = d["task"].replace(" ", "_")
            if cnt[task] < 10:
                self.data.append(d)
                cnt[task] += 1


class GLUE(Dataset):
    def __init__(self, task, dataset_type="validation"):
        self.data = []
        self.supported_tasks = ["sst2", "cola", "qqp", "mnli",
                                "mnli_matched", "mnli_mismatched", "qnli", "wnli", "rte", "mrpc"]
        assert task in self.supported_tasks

        self.task = task
        self.dataset_type = dataset_type

        if self.task == "mnli":
            from datasets import concatenate_datasets
            matched = load_dataset('glue', 'mnli')["validation_matched"]
            mismatched = load_dataset("glue", "mnli")["validation_mismatched"]
            data = concatenate_datasets([matched, mismatched])
        else:
            data = load_dataset("glue", task)[dataset_type]
        
        for d in data:
            if task == "sst2" or task == "cola":
                content = d['sentence']
            elif task == 'qqp':
                content = 'Question 1: ' + \
                    d['question1'] + ' Question 2: ' + \
                    d['question2']
            elif task == 'mnli' or task == 'mnli_matched' or task == 'mnli_mismatched':
                content = 'Premise: ' + \
                    d['premise'] + ' Hypothesis: ' + \
                    d['hypothesis']
            elif task == 'qnli':
                content = 'Question: ' + \
                    d['question'] + ' Context: ' + \
                    d['sentence']
            elif task == 'rte' or task == 'mrpc' or task == "wnli":
                content = 'Sentence 1: ' + \
                    d['sentence1'] + ' Sentence 2: ' + \
                    d['sentence2']
            else:
                raise NotImplementedError

            self.data.append({"content": content, "label": d['label']})            



