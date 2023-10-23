# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
import subprocess
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
        self.dataset_name = dataset_name
        self.data = []
        self.data_list = DATA_SET

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
        filepath = "promptbench/data/bool_logic.json"
        if not os.path.exists(filepath):
            url = 'https://wjdcloud.blob.core.windows.net/dataset/promptbench/dataset/bool_logic.json'
            print("Downloading bool_logic dataset...")
            command = ["wget", url]
            subprocess.run(command)

        with open(filepath, 'r') as f:
            data = json.load(f)
        
        self.data = [{"question": d["question"], "answer": "true" if d["answer"] else "false"} for d in data]


class ValidParentheses(Dataset):
    def __init__(self):
        filepath = "promptbench/data/valid_parentheses.json"
        if not os.path.exists(filepath):
            url = 'https://wjdcloud.blob.core.windows.net/dataset/promptbench/dataset/valid_parentheses.json'
            print("Downloading valid_parentheses dataset...")
            command = ["wget", url]
            subprocess.run(command)

        with open(filepath, 'r') as f:
            data = json.load(f)["examples"][:100]
        for d in data:
            self.data.append(
                {"question": d["input"], "answer": "valid" if d["target_scores"]["Valid"] == 1 else "invalid"})


class Math(Dataset):
    def __init__(self) -> None:
        filepath = "promptbench/data/math.json"
        if not os.path.exists(filepath):
            url = 'https://wjdcloud.blob.core.windows.net/dataset/promptbench/dataset/math.json'
            print("Downloading math dataset...")
            command = ["wget", url]
            subprocess.run(command)
        with open(filepath, 'r') as f:
            data = json.load(f)

        for task in data.keys():
            for d in data[task]:
                d["task"] = task
                self.data.append(d)


class UnMulti(Dataset):

    def __init__(self, supported_languages):
        import json
        filepath = "promptbench/data/un_multi.json"
        if not os.path.exists(filepath):
            url = 'https://wjdcloud.blob.core.windows.net/dataset/promptbench/dataset/un_multi.json'
            print("Downloading un_multi dataset...")
            command = ["wget", url]
            subprocess.run(command)

        with open(filepath, 'r') as f:
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

        for task_i in supported_tasks:
            source, target = task_i.split('-')
            for d in data[task_i][:int(num_samples//num_tasks)]:
                self.data[idx] = {
                    'source': d[source],
                    'target': d[target],
                    'task': task_i
                }
                idx += 1


class IWSLT(Dataset):
    def __init__(self, supported_languages):
        import json
        filepath = "promptbench/data/iwslt.json"
        if not os.path.exists(filepath):
            url = 'https://wjdcloud.blob.core.windows.net/dataset/promptbench/dataset/iwslt.json'
            print("Downloading IWSLT dataset...")
            command = ["wget", url]
            subprocess.run(command)

        with open(filepath, 'r') as f:
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

        for task_i in supported_tasks:
            source, target = task_i.split('-')
            for d in data[task_i][:int(num_samples//num_tasks)]:
                self.data[idx] = {
                    'source': d[source],
                    'target': d[target],
                    'task': task_i
                }
                idx += 1


class SQUAD_V2(Dataset):
    def __init__(self, dataset_type="validation"):
        filepath = "promptbench/data/SQUAD_V2.json"
        if not os.path.exists(filepath):
            url = 'https://wjdcloud.blob.core.windows.net/dataset/promptbench/dataset/SQUAD_V2.json'
            print("Downloading SQUAD_V2 dataset...")
            command = ["wget", url]
            subprocess.run(command)

        with open(filepath, "r") as file:
            data = json.load(file)
        
        for d in data:
            self.data.append({"id": d["id"], "content": "Context: " + d["context"] + "\n" + "Question: " + d["question"] + "\n", "answers": d["answers"]})

        import random
        random.seed(42)
        random.shuffle(self.data)
        self.data = self.data[:200]

    """
    TODO: remove get_reference into eval function.
    """
    def get_reference(self):
        references = []
        # for i in range(1):
        #     data = self.data[i]
        for data in self.data:
            references.append({"answers": data["answers"], "id": data["id"]})
        return references


class MMLU(Dataset):
    def __init__(self):
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

        filepath = "promptbench/data/MMLU.json"
        if not os.path.exists(filepath):
            url = 'https://wjdcloud.blob.core.windows.net/dataset/promptbench/dataset/MMLU.json'
            print("Downloading MMLU dataset...")
            command = ["wget", url]
            subprocess.run(command)
        
        with open(filepath, "r") as file:
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


def load_dataset(dataset_name, *args):
    if dataset_name in ["cola", "sst2", "qqp", "mnli", "mnli_matched", "mnli_mismatched", "qnli", "wnli", "rte", "mrpc"]:
        return GLUE(dataset_name)
    elif dataset_name == 'mmlu':
        return MMLU()
    elif dataset_name == "squad_v2":
        return SQUAD_V2()
    elif dataset_name == 'un_multi':
        return UnMulti(args[0])
    elif dataset_name == 'iwslt':
        return IWSLT(args[0])
    elif dataset_name == 'math':
        return Math()
    elif dataset_name == 'bool_logic':
        return BoolLogic()
    elif dataset_name == 'valid_parentheses':
        return ValidParentheses()
    else:
        raise NotImplementedError

