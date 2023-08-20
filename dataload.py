# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from config import *
import json
from datasets import load_dataset


"""
====================================================================================================
3 functions need to be implemented.

__init__(): load data from file or other sources.

get_content_by_idx(): return a dict with relevant informations.

get_few_shot_examples(): return a string with few-shot examples.

====================================================================================================
"""

class Dataset(object):
    def __init__(self):
        self.data = None

    def __len__(self):
        assert self.data is not None, "self.data is None. Please load data first."
        return len(self.data)

    def get_content_by_idx(self, idx, *args):  
        raise NotImplementedError("get_content_by_idx() must be implemented in the subclass.")
    
    def get_few_shot_examples(self, task):
        raise NotImplementedError("get_few_shot_examples() must be implemented in the subclass.")

class BoolLogic(Dataset):
    def __init__(self):
        import json
        with open("data/bool_logic.json", 'r') as f:
            data = json.load(f)
        self.data = [{"question": d["question"], "answer": "true" if d["answer"] else "false"} for d in data]
            
    def get_content_by_idx(self, idx, *args):
        return self.data[idx]
    
    def get_few_shot_examples(self):
        from prompts.three_shot.few_shot_examples import examples
        few_shot_examples = examples["bool_logic"]
        return few_shot_examples


class ValidParentheses(Dataset):
    def __init__(self):
        self.data = []
        import json
        with open("data/valid_parentheses.json", 'r') as f:
            data = json.load(f)["examples"][:100]
        for d in data:
            self.data.append({"question": d["input"], "answer": "valid" if d["target_scores"]["Valid"] == 1 else "invalid"})

    def get_content_by_idx(self, idx, *args):
        return self.data[idx]
    
    def get_few_shot_examples(self):
        from prompts.three_shot.few_shot_examples import examples
        few_shot_examples = examples["valid_parentheses"]
        return few_shot_examples
        
        
class Math(Dataset):
    def __init__(self) -> None:
        from data.math import math_dataset
        self.data = []
        for task in math_dataset.keys():
            for d in math_dataset[task]:
                d["task"] = task
                self.data.append(d)

    def get_content_by_idx(self, idx, *args):
        return self.data[idx]

    def get_few_shot_examples(self, task):
        from prompts.three_shot.few_shot_examples import examples
            
        few_shot_data = examples["math"][task]
        few_shot_examples = "Here are three examples. \n"
        for d in few_shot_data:
            few_shot_examples += "Question: " + d["question"] + "\n"
            few_shot_examples += "Answer: " + str(d["answer"]) + "\n"

        return few_shot_examples
        

class UnMulti(Dataset):

    def __init__(self, data_path, supported_languages):
        import json
        with open(data_path, 'r') as f:
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
    
    def get_content_by_idx(self, idx, task=None):
        return self.data[idx]
    
    def get_few_shot_examples(self, task):
        from prompts.three_shot.few_shot_examples import examples
            
        few_shot_examples = examples["un_multi"][task]
        return few_shot_examples


class IWSLT(UnMulti):
    def get_few_shot_examples(self, task):
        from prompts.three_shot.few_shot_examples import examples

        few_shot_examples = examples["iwslt"][task]
        return few_shot_examples


class SQUAD_V2(Dataset):
    def __init__(self, dataset_type="validation"):
        # self.data = []
        # data = load_dataset("squad_v2")[dataset_type]
        # random.seed(42)
        # random_indices = random.sample(range(len(data)), 1000)
        # self.data = data.select(random_indices)
        with open("data/SQUAD_V2.json", "r") as file:
            self.data = json.load(file)
        
        import random
        random.seed(42)
        random.shuffle(self.data)
        self.data = self.data[:200]

    def get_content_by_idx(self, idx, *args):
        content = "Context: " + self.data[idx]["context"] + "\n" \
                  "Question: " + self.data[idx]["question"] + "\n"

        return {"id": self.data[idx]["id"], "content": content}

    def get_reference(self):
        references = []
        # for i in range(1):
        #     data = self.data[i]
        for data in self.data:
            references.append({"answers": data["answers"], "id": data["id"]})
        return references

    def get_few_shot_examples(self, task):
        from prompts.three_shot.few_shot_examples import examples
            
        few_shot_examples = examples[task]
        return few_shot_examples


class MMLU(Dataset):
    def __init__(self, dataset_type="validation"):
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
        
        with open("data/MMLU.json", "r") as file:
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
        
        with open("data/MMLU_few_shot.json", "r") as file:
            self.few_shot_data = json.load(file)        
    

    def get_content_by_idx(self, idx, *args):
        return self.data[idx]
    
    def get_few_shot_examples(self, task):
        content = "Here are three examples.\n"
        data = self.few_shot_data[task]
        for idx in range(min(len(data), 3)):
            content +=  ("Input: " + data[idx]["input"] + "\n" \
                        + "A : " + data[idx]["A"] + "\n" \
                        + "B : " + data[idx]["B"] + "\n" \
                        + "C : " + data[idx]["C"] + "\n" \
                        + "D : " + data[idx]["D"] + "\n\n" \
                        + "Answer : " + data[idx]["target"] + "\n" \
                        )

        return content
            

class GLUE(Dataset):
    def __init__(self, task, dataset_type="validation"):
        
        self.supported_tasks = ["sst2", "cola", "qqp", "mnli", "mnli_matched", "mnli_mismatched", "qnli", "wnli", "rte", "mrpc"]
        assert task in self.supported_tasks

        self.task = task
        self.dataset_type = dataset_type
        
        if self.task == "mnli":
            from datasets import concatenate_datasets
            matched = load_dataset('glue', 'mnli')["validation_matched"]
            mismatched = load_dataset("glue", "mnli")["validation_mismatched"]
            self.data = concatenate_datasets([matched, mismatched])
        else:
            self.data = load_dataset("glue", task)[dataset_type]

    def get_few_shot_examples(self, task):
        from prompts.three_shot.few_shot_examples import examples
            
        few_shot_examples = examples[task]
        return few_shot_examples

    def get_content_by_idx(self, idx, task, *args):
        if task == "sst2" or task == "cola":
            content = self.data[idx]['sentence']
        elif task == 'qqp':
            content = 'Question 1: ' + self.data[idx]['question1'] + ' Question 2: ' + self.data[idx]['question2']
        elif  task == 'mnli' or task == 'mnli_matched' or task == 'mnli_mismatched':
            content = 'Premise: ' + self.data[idx]['premise'] + ' Hypothesis: ' + self.data[idx]['hypothesis']
        elif task == 'qnli':
            content = 'Question: ' + self.data[idx]['question'] + ' Context: ' + self.data[idx]['sentence']
        elif task == 'rte' or task == 'mrpc' or task == "wnli":
            content = 'Sentence 1: ' + self.data[idx]['sentence1'] + ' Sentence 2: ' + self.data[idx]['sentence2']
        else:
            raise NotImplementedError
        
        label = self.data[idx]['label']
        
        return {"content": content, "label": label}


def create_dataset(dataset_name, *args):
    if dataset_name in ["cola", "sst2", "qqp", "mnli", "mnli_matched", "mnli_mismatched", "qnli", "wnli", "rte", "mrpc"]:
        return GLUE(dataset_name)
    elif dataset_name == 'mmlu':
        return MMLU()
    elif dataset_name == "squad_v2":
        return SQUAD_V2()
    elif dataset_name == 'un_multi':
        return UnMulti("data/un_multi.json", args[0])
    elif dataset_name == 'iwslt':
        return IWSLT("data/iwslt.json", args[0])
    elif dataset_name == 'math':
        return Math()
    elif dataset_name == 'bool_logic':
        return BoolLogic()
    elif dataset_name == 'valid_parentheses':
        return ValidParentheses()
    else:
        raise NotImplementedError

if __name__ == "__main__":
    dataset = ValidParentheses()
    # dataset = BoolLogic()
    d = dataset.get_content_by_idx(0)
    print(type(d['answer']))
    print(d)