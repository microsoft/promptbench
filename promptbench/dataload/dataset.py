# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
import re
import random
import requests
import json
from PIL import Image as PILImage
from tqdm import tqdm

from promptbench.config import *
from datasets import load_dataset


def shuffleDict(d):
    keys = list(d.keys())
    random.shuffle(keys)
    [(key, d[key]) for key in keys]
    random.shuffle(keys)
    [(key, d[key]) for key in keys]
    random.shuffle(keys)
    keys = [(key, d[key]) for key in keys]
    #keys = d(keys)
    return dict(keys)

class Dataset(object):
    def __init__(self, dataset_name):
        self.data = []
        self.dataset_name = dataset_name

        # Get the parent directory
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(os.path.dirname(cur_dir), 'data')

        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)
        
        # check if the dataset exists, if not, download it
        if dataset_name == "gsm8k":
            self.filepath = os.path.join(self.data_dir, f"{dataset_name}.jsonl")
        else:
            self.filepath = os.path.join(self.data_dir, f"{dataset_name}.json")
            
        if not os.path.exists(self.filepath):
            if dataset_name == "gsm8k":
                url = f'https://wjdcloud.blob.core.windows.net/dataset/promptbench/dataset/{dataset_name}.jsonl'
            else:
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
    
    def extract_answer(self, output): 
        return output

    def save_images_to_local(self, dataset, split, key_list):
        # Get the parent directory
        cur_dir = os.path.dirname(os.path.abspath(__file__))

        self.data_dir = os.path.join(os.path.dirname(cur_dir), 'data')
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)

        self.dataset_dir = os.path.join(self.data_dir, dataset)
        if not os.path.exists(self.dataset_dir):
            os.mkdir(self.dataset_dir)
        
        self.split_dir = os.path.join(self.dataset_dir, split)
        if not os.path.exists(self.split_dir):
            os.mkdir(self.split_dir)

        self.filepath = os.path.join(self.dataset_dir, f"{split}.json")
        if not os.path.exists(self.filepath):
            local_path_dict = {}
            print('Saveing images to local path: ', self.split_dir)
            for idx in tqdm(range(len(self.data))):
                local_path_dict[str(idx)] = []
                for key in key_list:
                    if self.data[idx][key] is not None:
                        image_dir = os.path.join(self.split_dir, f'{idx}_{key}.png')
                        self.data[idx][key].save(image_dir)
                        local_path_dict[str(idx)].append(image_dir)
            print('Saving file: ', self.filepath)
            with open(self.filepath, 'w') as f:
                json.dump(local_path_dict, f)
        else:
            print('Images already saved to local, loading file: ', self.filepath)
            with open(self.filepath, 'r') as f:
                local_path_dict = json.load(f)

        self.local_path_dict = local_path_dict

class BoolLogic(Dataset):
    """
    BoolLogic is a dataset class (obtained from BigBench) representing boolean logic expressions. Each entry in the dataset consists of a boolean logic expression and its corresponding label (either 'true' or 'false'). The dataset is read from a JSON file containing questions and answers.
    
    https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/boolean_expressions

    Example data format:
    [{'content': 'not ( not False and True ) or not True is ', 'label': 'false'}, ...]
    """
    def __init__(self):
        super().__init__("bool_logic")
        with open(self.filepath, 'r') as f:
            data = json.load(f)
        
        self.data = [{"content": d["question"], "label": "true" if d["answer"] else "false"} for d in data]


class ValidParentheses(Dataset):
    """
    ValidParentheses is a dataset class (obtained from BigBench) for validating parentheses in strings. It checks if the given string of parentheses is valid or invalid. The dataset is initialized by reading from a JSON file, with each entry containing a string of parentheses and a label ('valid' or 'invalid').

    https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/cs_algorithms

    Example data format:
    [{'content': '( ] } (', 'label': 'invalid'}, ...]
    """
    def __init__(self):
        super().__init__("valid_parentheses")

        with open(self.filepath, 'r') as f:
            data = json.load(f)["examples"][:100]
        for d in data:
            self.data.append(
                {"content": d["input"], "label": "valid" if d["target_scores"]["Valid"] == 1 else "invalid"})


class Math(Dataset):
    """
    Math is a dataset class that loads mathematical questions and answers from the Hugging Face datasets (math_dataset test set). This dataset covers various types of math questions, such as algebra, calculus, and arithmetic. It is initialized with a specific type of math question.

    Reference: https://huggingface.co/datasets/math_dataset/

    Example data format:
    [{'question': "Solve -282*d + 929 - 178 = -1223 for d.\\n'", 'answer': "b'7\\n'", 'task': 'algebra__linear_1d'}, ...]
    """
    def __init__(self, task) -> None:

        self.data = []

        MATH_QUESTION_TYPES = [
            'algebra__linear_1d',
            'algebra__linear_1d_composed',
            'algebra__linear_2d',
            'algebra__linear_2d_composed',
            'algebra__polynomial_roots',
            'algebra__polynomial_roots_composed',
            'algebra__sequence_next_term',
            'algebra__sequence_nth_term',
            'arithmetic__add_or_sub',
            'arithmetic__add_or_sub_in_base',
            'arithmetic__add_sub_multiple',
            'arithmetic__div',
            'arithmetic__mixed',
            'arithmetic__mul',
            'arithmetic__mul_div_multiple',
            'arithmetic__nearest_integer_root',
            'arithmetic__simplify_surd',

            'calculus__differentiate',
            'calculus__differentiate_composed',

            'comparison__closest',
            'comparison__closest_composed',
            'comparison__kth_biggest',
            'comparison__kth_biggest_composed',
            'comparison__pair',
            'comparison__pair_composed',
            'comparison__sort',
            'comparison__sort_composed',

            'measurement__conversion',
            'measurement__time',

            'numbers__base_conversion',
            'numbers__div_remainder',
            'numbers__div_remainder_composed',
            'numbers__gcd',
            'numbers__gcd_composed',
            'numbers__is_factor',
            'numbers__is_factor_composed',
            'numbers__is_prime',
            'numbers__is_prime_composed',
            'numbers__lcm',
            'numbers__lcm_composed',
            'numbers__list_prime_factors',
            'numbers__list_prime_factors_composed',
            'numbers__place_value',
            'numbers__place_value_composed',
            'numbers__round_number',
            'numbers__round_number_composed',

            'polynomials__add',
            'polynomials__coefficient_named',
            'polynomials__collect',
            'polynomials__compose',
            'polynomials__evaluate',
            'polynomials__evaluate_composed',
            'polynomials__expand',
            'polynomials__simplify_power',
            'probability__swr_p_level_set',
            'probability__swr_p_sequence',
        ]
        
        assert task in MATH_QUESTION_TYPES, f"Task {task} is not supported in math dataset. Please choose from {MATH_QUESTION_TYPES}"
        data = load_dataset("math_dataset", task)["test"]
        for d in data:
            d["task"] = task
            self.data.append(d)


class UnMulti(Dataset):
    """
    UnMulti is a dataset class for multilingual translation tasks. It includes translations between multiple language pairs. The dataset is partially loaded from a JSON file due to its large size.

    Example data format:
    [{'source': '4 - العميد بحري مرتضى سفاري، قائد القوات البحرية', 'target': 'Konteradmiral Morteza Safari (Kommandeur der Marine des Korps der Iranischen Revolutionsgarden)', 'soruce_lang': 'Arabic', 'target_lang': 'German'}, ...]
    """
    def __init__(self):
        # un_multi dataset only have train set and is large, so we selected partial dataset.
        super().__init__("un_multi")

        with open(self.filepath, 'r') as f:
            data = json.load(f)
        self.data = []

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

        for task_i in data.keys():
            source, target = task_i.split('-')
            for d in data[task_i]:
                self.data.append({
                    'source': d[source],
                    'target': d[target],
                    'soruce_lang': LANGUAGES[source],
                    'target_lang': LANGUAGES[target],
                })


class IWSLT(Dataset):
    """
    IWSLT is a dataset class for the International Workshop on Spoken Language Translation. It includes pairs of sentences in different languages, intended for translation tasks. The dataset is loaded from Hugging Face datasets and supports multiple language pairs.

    Reference: https://huggingface.co/datasets/iwslt

    Example data format:
    [{'source': 'قبل عدة سنوات، هنا في تيد، قدّم بيتر سكيلمان منافسة تصميم تسمى منافسة حلوى المارش مالو.', 'target': 'Several years ago here at TED, Peter Skillman introduced a design challenge called the marshmallow challenge.', 'soruce_lang': 'Arabic', 'target_lang': 'English'}, ...]
    """
    def __init__(self, supported_languages):
        # IWSLT now is loaded from huggingface datasets.
        # https://huggingface.co/datasets/iwslt

        self.data = []

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

        for task_i in supported_languages:
            source, target = task_i.split('-')
            data = load_dataset("iwslt2017", "iwslt2017-"+task_i)["test"]
            for d in data:
                d = d["translation"]
                self.data.append({
                    'source': d[source],
                    'target': d[target],
                    'soruce_lang': LANGUAGES[source],
                    'target_lang': LANGUAGES[target],
                })


class SQUAD_V2(Dataset):
    """
    SQUAD_V2 is a dataset class for the Stanford Question Answering Dataset (SQuAD) version 2, which involves question-answering tasks.
    SQUAD_V2 dataset is loaded from huggingface datasets.
    Reference: https://huggingface.co/datasets/squad_v2

    Example data format:
    [{'id': '56ddde6b9a695914005b9628', 'title': 'Normans', 'context': 'The Normans (Norman: Nourmands; French: Normands; Latin: Normanni) were the people who in the 10th and 11th centuries gave their name to Normandy, a region in France. They were descended from Norse ("Norman" comes from "Norseman") raiders and pirates from Denmark, Iceland and Norway who, under their leader Rollo, agreed to swear fealty to King Charles III of West Francia. Through generations of assimilation and mixing with the native Frankish and Roman-Gaulish populations, their descendants would gradually merge with the Carolingian-based cultures of West Francia. The distinct cultural and ethnic identity of the Normans emerged initially in the first half of the 10th century, and it continued to evolve over the succeeding centuries.', 'question': 'In what country is Normandy located?', 'answers': {'text': ['France', 'France', 'France', 'France'], 'answer_start': [159, 159, 159, 159]}}, ...]
    """
    def __init__(self):
        # 
        # 
        self.data = []
        data = load_dataset("squad_v2")["validation"]
        for d in data:
            self.data.append(d)


class MMLU(Dataset):
    """
    MMLU is a dataset class for the Multimodal Multi-Task Learning Understanding dataset, covering various educational and professional fields.
    MMLU dataset is loaded from huggingface datasets: lukaemon/mmlu (test set).
    
    Reference: https://huggingface.co/datasets/cais/mmlu/viewer/abstract_algebra/test

    Example data format:
    [{'input': "This question refers to the following information.\nRead the the following quotation to answer questions.\nThe various modes of worship which prevailed in the Roman world were all considered by the people as equally true; by the philosopher as equally false; and by the magistrate as equally useful.\nEdward Gibbon, The Decline and Fall of the Roman Empire, 1776–1788\nGibbon's interpretation of the state of religious worship in ancient Rome could be summarized as", 'A': "In ancient Rome, religious worship was decentralized and tended to vary with one's social position.", 'B': 'In ancient Rome, religious worship was the source of much social tension and turmoil.', 'C': 'In ancient Rome, religious worship was homogeneous and highly centralized.', 'D': 'In ancient Rome, religious worship was revolutionized by the introduction of Christianity.', 'target': 'A', 'task': 'high_school_european_history'}, ...]
    """
    def __init__(self):       
        self.data = []
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

        for task in self.tasks:
            data = load_dataset("cais/mmlu", task)["test"]
            for d in data:
                d["task"] = task
                self.data.append(d)

            
class GLUE(Dataset):
    """
    GLUE class is a dataset class for the General Language Understanding Evaluation benchmark, supporting multiple natural language understanding tasks.

    Examples:
    [{'content': "it 's a charming and often affecting journey . ", 'label': 1}, {'content': 'unflinchingly bleak and desperate ', 'label': 0}, ...]
    """
    def __init__(self, task):
        self.data = []
        self.supported_tasks = ["sst2", "cola", "qqp", "mnli",
                                "mnli_matched", "mnli_mismatched", "qnli", "wnli", "rte", "mrpc"]
        assert task in self.supported_tasks

        self.task = task

        if self.task == "mnli":
            from datasets import concatenate_datasets
            matched = load_dataset('glue', 'mnli')["validation_matched"]
            mismatched = load_dataset("glue", "mnli")["validation_mismatched"]
            data = concatenate_datasets([matched, mismatched])
        else:
            data = load_dataset("glue", task)["validation"]
        
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


class GSM8K(Dataset):
    """
    GSM8K is a dataset class that loads mathematical questions and answers from the Hugging Face datasets (main test set). The dataset is a collection of 8.5K high-quality, linguistically diverse grade school math word problems.
    GSM8K dataset is loaded from huggingface datasets: /gsm8k (test set).
    
    Reference: https://huggingface.co/datasets/gsm8k/viewer/main/test
    
    Example data format:
    [{'question': "A robe takes 2 bolts of blue fiber and half that much white fiber. How many bolts in total does it take?", 'answer': "It takes 2/2=<<2/2=1>>1 bolt of white fiber So the total amount of fabric is 2+1=<<2+1=3>>3 bolts of fabric #### 3"}, ...]
    """
    def __init__(self):
        # gsm8k dataset now is loaded from huggingface datasets: /gsm8k (test set).
        # https://huggingface.co/datasets/gsm8k
        
        data = load_dataset("gsm8k", "main")["test"]
        self.data = []
        for d in data:
            content = d["question"].strip()
            label = d["answer"].split("#### ")[-1]
            self.data.append({"content": content, "label": label})
    
    def extract_answer(self, output):
        answer = output.replace(",", "")
        answer = [s for s in re.findall(r'-?\d+\.?\d*', answer)]
        answer = answer[0] if len(answer) > 0 else ""
        return answer


class BigBench(Dataset):
    """
    BigBench is a dataset class that loads questions and answers from the BigBench benchmark (sub-dataset: date and object tracking). It includes various types of questions, such as date understanding, object tracking. The dataset is loaded from a JSON file containing questions and answers.
    
    date: https://github.com/google/BIG-bench/blob/main/bigbench/benchmark_tasks/date_understanding/task.json
    object_tracking: https://github.com/google/BIG-bench/blob/main/bigbench/benchmark_tasks/logical_deduction/three_objects/task.json
    
    Example data format:
    [
        {
            "input": "On a shelf, there are three books: a black book, an orange book, and a blue book. The blue book is to the right of the orange book. The orange book is to the right of the black book.",
            "target_scores": {
                "The black book is the leftmost.": 1,
                "The orange book is the leftmost.": 0,
                "The blue book is the leftmost.": 0
            }
        },
    """
    def __init__(self, dataset_name):
        super().__init__(dataset_name)
        
        self.data = []
        with open(self.filepath, 'r') as f:
            json_data = json.load(f)
            json_data = json_data["examples"]
            if self.dataset_name == "bigbench_date":
                choice_index = ['A','B','C','D','E','F']
            elif self.dataset_name == "bigbench_object_tracking":
                choice_index = ['A','B','C']
            else:
                raise ValueError("dataset is not properly defined ...")
            for line in json_data:
                raw_q = line["input"].strip()
                if self.dataset_name == "bigbench_date":
                    choice = "Answer Choices:"
                    # Randomly shuffle the answer choice dictionary because the original answer is always A ...
                    choice_dic = shuffleDict(line["target_scores"])
                elif self.dataset_name == "bigbench_object_tracking":
                    choice = "\nWhich choice is true ? Answer Choices:"
                    choice_dic = line["target_scores"]
                else:
                    raise ValueError("dataset is not properly defined ...")
                for i, key_value in enumerate(choice_dic.items()):
                    key, value = key_value
                    choice += " ("
                    choice += choice_index[i]
                    choice += ") "
                    choice += key
                    if value == 1:
                        a = choice_index[i]
                        #a = key
                q = raw_q + " " + choice
                self.data.append({"content": q, "label": a})
    
    def extract_answer(self, output): 
        if self.dataset_name == "bigbench_date":
            answer = re.findall(r'A|B|C|D|E|F', output)
        elif self.dataset_name == "bigbench_object_tracking":
            answer = re.findall(r'A|B|C', output)
        
        answer = answer[0] if len(answer) > 0 else ""
        
        # print(answer)
        return answer

             
class CSQA(Dataset):
    """
    CSQA is a dataset class that loads questions and answers from the CommonsenseQA dataset. The dataset is a challenging commonsense question-answering dataset. It comprises 12,247 questions with 5 multiple-choice answers each. 
    CSQA dataset now is loaded from huggingface datasets: /commonsense_qa (val set).
    
    Reference: https://huggingface.co/datasets/commonsense_qa/viewer/default/validation
    
    Example data format:
    ['id': "1afa02df02c908a558b4036e80242fac", 'question': "A revolving door is convenient for two direction travel, but it also serves as a security measure at a what?", 'question_concept': "revolving door", 'choices': { "label": [ "A", "B", "C", "D", "E" ], "text": [ "bank", "library", "department store", "mall", "new york" ] }, 'answerKey': "A" ]
    
    """
    def __init__(self):
        data = load_dataset("commonsense_qa")["validation"]
        
        self.data = []
        choice_index = ['A','B','C','D','E']
        for d in data:
            raw_q = d["question"].strip()
            choice = "\nAnswer Choices:"
            choice_list = d["choices"]["text"]
            for i, c in enumerate(choice_list):
                choice += " ("
                choice += choice_index[i]
                choice += ") "
                choice += c
            q = raw_q + " " + choice
            a = d["answerKey"]
            self.data.append({"content": q, "label": a})
                
    def extract_answer(self, output): 
        answer = re.findall(r'A|B|C|D|E', output)
        answer = answer[0] if len(answer) > 0 else ""
        
        # print(answer)
        return answer
    

class LastLetterConcat(Dataset):
    """
    LastLetterConcat is a dataset class that loads questions and answers from the Last Letter Concat dataset. The dataset is initialized by reading from a JSON file, with each entry containing a query and a answer.
    
    Reference: https://arxiv.org/pdf/2201.11903.pdf (page 8)
    
    Example data format:
    [{"question": "Take the last letters of each words in \"Whitney Erika Tj Benito\" and concatenate them.", "answer": "yajo"}, ...]
    """
    def __init__(self):
        super().__init__("last_letter_concat")
        
        self.data = []
        with open(self.filepath, 'r') as f:
            json_data = json.load(f)
            for line in json_data:
                q = line["question"].strip()
                a = line["answer"]
                self.data.append({"content": q, "label": a})
    

class NumerSense(Dataset):
    """
    NumerSense is a dataset class that loads questions and answers from the NumerSense dataset which is a unique numerical commonsense reasoning probing task. The dataset is initialized by reading from a JSON file, with each entry containing a query and a answer (English number).
    
    https://github.com/INK-USC/NumerSense/blob/main/data/validation.masked.tsv
    
    Example data format:
    [{"query": "you may take the subway back and forth to work <mask> days a week.", "answer": "five"}, ...]
    
    """
    def __init__(self):
        super().__init__("numersense")
        
        self.data = []
        with open(self.filepath, 'r') as f:
            json_data = json.load(f)
            for line in json_data:
                q = line["query"].strip()
                a = line["answer"]
                self.data.append({"content": q, "label": a})
                

class QASC(Dataset):
    """
    QASC is a dataset class that loads questions and answers from the Question Answering via QASC dataset. QASC is a question-answering dataset with a focus on sentence composition. It consists of 9,980 8-way multiple-choice questions about grade school science (8,134 train, 926 dev, 920 test), and comes with a corpus of 17M sentences.
    QASC dataset now is loaded from huggingface datasets: /qasc (val set).
    
    Reference: https://huggingface.co/datasets/qasc/viewer/default/validation
    
    Example data format: 
    ['id': "3NGI5ARFTT4HNGVWXAMLNBMFA0U1PG", 'question': "Climate is generally described in terms of what?", 'choices': { "text": [ "sand", "occurs over a wide range", "forests", "Global warming", "rapid changes occur", "local weather conditions", "measure of motion", "city life" ], "label": [ "A", "B", "C", "D", "E", "F", "G", "H" ] }, 'answerKey': "F", 'fact1': "Climate is generally described in terms of temperature and moisture.", 'fact2': "Fire behavior is driven by local weather conditions such as winds, temperature and moisture.", 'combinedfact':"Climate is generally described in terms of local weather conditions", 'formatted_question': "Climate is generally described in terms of what? (A) sand (B) occurs over a wide range (C) forests (D) Global warming (E) rapid changes occur (F) local weather conditions (G) measure of motion (H) city life"]
    
    """
    
    def __init__(self):
        data = load_dataset("qasc")["validation"]
        
        self.data = []
        choice_index = ['A','B','C','D','E','F','G','H']
        for d in data:
            raw_q = d["question"].strip()
            choice = "\nAnswer Choices:"
            choice_list = d["choices"]["text"]
            for i, c in enumerate(choice_list):
                choice += " ("
                choice += choice_index[i]
                choice += ") "
                choice += c
            q = raw_q + " " + choice
            a = d["answerKey"]
            self.data.append({"content": q, "label": a})
                
    def extract_answer(self, output): 
        answer = re.findall(r'A|B|C|D|E|F|G|H', output)
        answer = answer[0] if len(answer) > 0 else ""
        
        # print(answer)
        return answer

class BBH(Dataset):
    """
    BBH is a dataset class for the BigBench Hard dataset. This dataset is loaded from huggingface datasets: lukaemon/bbh (test set).
    
    Reference: 
    https://huggingface.co/datasets/lukaemon/bbh
    https://github.com/suzgunmirac/BIG-Bench-Hard

    Example data format:
    {'input': 'not ( True ) and ( True ) is', 'target': 'False', 'task': 'boolean_expressions'}
    """
    def __init__(self):       
        self.data = []
        self.tasks = ['boolean_expressions', 'causal_judgement', 'date_understanding', 'disambiguation_qa', 
                      'dyck_languages', 'formal_fallacies', 'geometric_shapes', 'hyperbaton', 'logical_deduction_five_objects', 
                      'logical_deduction_seven_objects', 'logical_deduction_three_objects', 'movie_recommendation', 
                      'multistep_arithmetic_two', 'navigate', 'object_counting', 'penguins_in_a_table', 'reasoning_about_colored_objects', 
                      'ruin_names', 'salient_translation_error_detection', 'snarks', 'sports_understanding', 'temporal_sequences', 
                      'tracking_shuffled_objects_five_objects', 'tracking_shuffled_objects_seven_objects', 
                      'tracking_shuffled_objects_three_objects', 'web_of_lies', 'word_sorting']

        for task in self.tasks:
            data = load_dataset("lukaemon/bbh", task)["test"]
            for d in data:
                d["task"] = task
                self.data.append(d)


class DROP(Dataset):
    """
    DROP is a dataset class for the DROP dataset. 
    This dataset is loaded from huggingface datasets: drop (validation set).

    Reference:
    https://huggingface.co/datasets/drop
    DROP: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs (https://arxiv.org/abs/1903.00161)

    Example data format:
    {
        'section_id': 'nfl_1184', 
        'query_id': 'f37e81fa-ef7b-4583-b671-762fc433faa9', 
        'passage': " Hoping to rebound from their loss to the Patriots, the Raiders stayed at home for a Week 16 duel with the Houston Texans.  Oakland would get the early lead in the first quarter as quarterback JaMarcus Russell completed a 20-yard touchdown pass to rookie wide receiver Chaz Schilens.  The Texans would respond with fullback Vonta Leach getting a 1-yard touchdown run, yet the Raiders would answer with kicker Sebastian Janikowski getting a 33-yard and a 30-yard field goal.  Houston would tie the game in the second quarter with kicker Kris Brown getting a 53-yard and a 24-yard field goal. Oakland would take the lead in the third quarter with wide receiver Johnnie Lee Higgins catching a 29-yard touchdown pass from Russell, followed up by an 80-yard punt return for a touchdown.  The Texans tried to rally in the fourth quarter as Brown nailed a 40-yard field goal, yet the Raiders' defense would shut down any possible attempt.", 
        'question': 'Who scored the first touchdown of the game?', 
        'answers_spans': {'spans': ['Chaz Schilens', 'JaMarcus Russell'], 'types': ['span', 'span']}
    }
    """
    def __init__(self):
        data = load_dataset("drop")["validation"]
        self.data = []

        for d in data:
            self.data.append(d)

class ARC(Dataset):
    """
    ARC is a dataset class for the AI2 Reasoning Challenge dataset. 
    This dataset is loaded from huggingface datasets: arc (test set).

    Reference:
    https://huggingface.co/datasets/ai2_arc
    AI2 Reasoning Challenge (ARC) (https://arxiv.org/abs/1803.05457)

    Example data format:
    {
        'id': 'Mercury_7175875', 
        'question': 'An astronomer observes that a planet rotates faster after a meteorite impact. Which is the most likely effect of this increase in rotation?', 
        'choices': {'text': ['Planetary density will decrease.', 'Planetary years will become longer.', 'Planetary days will become shorter.', 'Planetary gravity will become stronger.'], 'label': ['A', 'B', 'C', 'D']}, 
        'answerKey': 'C'
    }
    """
    def __init__(self, name):
        data = load_dataset("ai2_arc", name)["test"]
        self.data = []

        for d in data:
            self.data.append(d)

class VQAv2(Dataset):
    """
    VQAv2 is a dataset class for the Visual Question Answering v2 dataset. 
    This dataset is loaded from huggingface datasets: vqa_v2 (validation set).

    Reference:
    https://huggingface.co/datasets/HuggingFaceM4/VQAv2
    Making the V in VQA Matter: Elevating the Role of Image Understanding in Visual Question Answering (https://arxiv.org/abs/1612.00837)

    Example data format:
    {
        'images': [<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x512>],
        'image_paths': ['/Users/username/.cache/huggingface/datasets/downloads/extracted/adf50b3f63fdc93e9e2d368b11520a5796a4e904a80852e73a19a7112fca3592/val2014/COCO_val2014_000000262148.jpg'],
        'answers': [{'answer': 'down', 'answer_confidence': 'yes', 'answer_id': 1},
        {'answer': 'down', 'answer_confidence': 'yes', 'answer_id': 2},
        {'answer': 'at table', 'answer_confidence': 'yes', 'answer_id': 3},
        {'answer': 'skateboard', 'answer_confidence': 'yes', 'answer_id': 4},
        {'answer': 'down', 'answer_confidence': 'yes', 'answer_id': 5},
        {'answer': 'table', 'answer_confidence': 'yes', 'answer_id': 6},
        {'answer': 'down', 'answer_confidence': 'yes', 'answer_id': 7},
        {'answer': 'down', 'answer_confidence': 'yes', 'answer_id': 8},
        {'answer': 'down', 'answer_confidence': 'yes', 'answer_id': 9},
        {'answer': 'down', 'answer_confidence': 'yes', 'answer_id': 10}],
        'question': 'Where is he looking?'
    }
    """
    def __init__(self):
        from datasets import Image
        data = load_dataset("HuggingFaceM4/VQAv2", split="validation").cast_column("image", Image(decode=False))
        self.data = data
    
    def __getitem__(self, idx):
        assert len(self.data) > 0, "Empty dataset. Please load data first."
        return {"images": [PILImage.open(self.data[idx]['image']['path'])],
                "image_paths": [self.data[idx]['image']['path']],
                "answers": self.data[idx]['answers'],
                "question": self.data[idx]['question'],}

class NoCaps(Dataset):
    """
    NoCaps is a dataset class for the NoCaps dataset. 
    This dataset is loaded from huggingface datasets: nocaps (validation set).

    Reference:
    https://huggingface.co/datasets/HuggingFaceM4/NoCaps
    nocaps: novel object captioning at scale (https://arxiv.org/abs/1812.08658)

    Example data format:
    {
        'images': [<PIL.JpegImagePlugin.JpegImageFile image mode=L size=732x1024>],
        'image_paths': ['https://s3.amazonaws.com/nocaps/val/0013ea2087020901.jpg'],
        'answers': ['A baby is standing in front of a house.',
        'A little girl in a white jacket and sandals.',
        'A young child stands in front of a house.',
        'A child is wearing a white shirt and standing on a side walk. ',
        'A little boy is standing in his diaper with a white shirt on.',
        'A child wearing a diaper and shoes stands on the sidewalk.',
        'A child is wearing a light-colored shirt during the daytime.',
        'A little kid standing on the pavement in a shirt. ',
        'Black and white photo of a little girl smiling.',
        'a cute baby is standing alone with white shirt']
    }
    """
    def __init__(self):
        from datasets import Image
        data = load_dataset("HuggingFaceM4/NoCaps", split="validation").cast_column("image", Image(decode=False))
        data1 = load_dataset("HuggingFaceM4/NoCaps", split="validation")
        self.data = data
        self.data1 = data1
    
    def __getitem__(self, idx):
        assert len(self.data) > 0, "Empty dataset. Please load data first."
        return {"images": [self.data1[idx]['image']],
                "image_paths": [self.data[idx]['image']['path']],
                "answers": self.data[idx]['annotations_captions']}

class MathVista(Dataset):
    """
    MathVista is a dataset class for the MathVista dataset. 
    This dataset is loaded from huggingface datasets: math_vista (testmini set).

    Reference:
    https://huggingface.co/datasets/AI4Math/MathVista
    MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts (https://arxiv.org/abs/2310.02255)

    Example data format:
    {
        'images': [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=1514x720>],
        'image_paths': ['/Users/username/promptbench/promptbench/data/math_vista/testmini/0_decoded_image.png'],
        'answer': '1.2',
        'question': "When a spring does work on an object, we cannot find the work by simply multiplying the spring force by the object's displacement. The reason is that there is no one value for the force-it changes. However, we can split the displacement up into an infinite number of tiny parts and then approximate the force in each as being constant. Integration sums the work done in all those parts. Here we use the generic result of the integration.\r\n\r\nIn Figure, a cumin canister of mass $m=0.40 \\mathrm{~kg}$ slides across a horizontal frictionless counter with speed $v=0.50 \\mathrm{~m} / \\mathrm{s}$. It then runs into and compresses a spring of spring constant $k=750 \\mathrm{~N} / \\mathrm{m}$. When the canister is momentarily stopped by the spring, by what distance $d$ is the spring compressed?\nANSWER TYPE: float"
    }
        
    """
    def __init__(self):
        data = load_dataset("AI4Math/MathVista", split="testmini")
        self.data = data
        self.save_images_to_local(dataset='math_vista', split='testmini', key_list=['decoded_image'])

    def __getitem__(self, idx):
        assert len(self.data) > 0, "Empty dataset. Please load data first."
        return {"images": [self.data[idx]['decoded_image']],
                "image_paths": self.local_path_dict[str(idx)],
                "answer": self.data[idx]['answer'],
                "question":  self.data[idx]['question'] + "\nANSWER TYPE: " + self.data[idx]['answer_type'],}

class AI2D(Dataset):
    """
    AI2D is a dataset class for the AI2D dataset. 
    This dataset is loaded from huggingface datasets: ai2d (test set).

    Reference:
    https://huggingface.co/datasets/lmms-lab/ai2d
    A Diagram Is Worth A Dozen Images (https://arxiv.org/abs/1603.07396)

    Example data format:
    {
        'images': [<PIL.PngImagePlugin.PngImageFile image mode=RGB size=600x449>],
        'image_paths': ['/Users/username/promptbench/promptbench/data/ai2d/test/0_image.png'],
        'question': 'which of these define dairy item\n0: c\n1: D\n2: b\n3: a',
        'answer': '1'
    }
    """
    def __init__(self):
        data = load_dataset("lmms-lab/ai2d", split="test")
        self.data = data
        self.save_images_to_local(dataset='ai2d', split='test', key_list=['image'])

    def __getitem__(self, idx):
        assert len(self.data) > 0, "Empty dataset. Please load data first."
        choices_dict = dict(enumerate(self.data[idx]['options']))
        choices = ''
        for k, v in choices_dict.items():
            choices += f"\n{k}: {v}"
        return({"images": [self.data[idx]['image']],
                "image_paths": self.local_path_dict[str(idx)],
                "question": self.data[idx]['question'] + choices,
                "answer": self.data[idx]['answer']})

class ChartQA(Dataset):
    """
    ChartQA is a dataset class for the ChartQA dataset.
    This dataset is loaded from huggingface datasets: chart_qa (test set).

    Reference:
    https://huggingface.co/datasets/lmms-lab/ChartQA
    ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning (https://arxiv.org/abs/2203.10244)

    Example data format:
    {
        'images': [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=850x600>],
        'image_paths': ['/Users/username/promptbench/promptbench/data/chart_qa/test/0_image.png'],
        'answer': '14',
        'question': 'How many food item is shown in the bar graph?'
    }
    """
    def __init__(self):
        data = load_dataset("lmms-lab/ChartQA", split="test")
        self.data = data
        self.save_images_to_local(dataset='chart_qa', split='test', key_list=['image'])
    
    def __getitem__(self, idx):
        assert len(self.data) > 0, "Empty dataset. Please load data first."
        return {"images": [self.data[idx]['image']],
                "image_paths": self.local_path_dict[str(idx)],
                "answer": self.data[idx]['answer'],
                "question":  self.data[idx]['question'],}

class ScienceQA(Dataset):
    """
    ScienceQA is a dataset class for the ScienceQA dataset.
    This dataset is loaded from huggingface datasets: science_qa (validation set).

    Reference:
    https://huggingface.co/datasets/derek-thomas/ScienceQA
    Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering (https://arxiv.org/abs/2209.09513)

    Example data format:
    {
        'images': [<PIL.PngImagePlugin.PngImageFile image mode=RGB size=202x202>],
        'image_paths': ['/Users/username/promptbench/promptbench/data/science_qa/validation/0_image.png'],
        'answer': 1,
        'question': "Which animal's mouth is also adapted for bottom feeding?\n0: discus\n1: armored catfish"
    }
    """
    def __init__(self):
        data = load_dataset("derek-thomas/ScienceQA", split="validation")
        data_with_images = []
        for d in data:
            if d['image'] is not None:
                data_with_images.append(d)
        self.data = data_with_images
        self.save_images_to_local(dataset='science_qa', split='validation', key_list=['image'])

    def __getitem__(self, idx):
        assert len(self.data) > 0, "Empty dataset. Please load data first."
        choices_dict = dict(enumerate(self.data[idx]['choices']))
        choices = ''
        for k, v in choices_dict.items():
            choices += f"\n{k}: {v}"
        return {"images": [self.data[idx]['image']],
                "image_paths": self.local_path_dict[str(idx)],
                "answer": self.data[idx]['answer'],
                "question":  self.data[idx]['question'] + choices,}

class MMMU(Dataset):
    """
    MMMU is a dataset class for the MMMU dataset. 
    This dataset is loaded from huggingface datasets: mmlu (validation set).

    Reference:
    https://huggingface.co/datasets/lmms-lab/MMMU
    MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI (https://arxiv.org/abs/2311.16502)

    {
        'images': [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=733x237>],
        'image_paths': ['/Users/username/promptbench/promptbench/data/mmmu/validation/0_image_1.png'],
        'answer': 'B',
        'question': '<image 1> Baxter Company has a relevant range of production between 15,000 and 30,000 units. The following cost data represents average variable costs per unit for 25,000 units of production. If 30,000 units are produced, what are the per unit manufacturing overhead costs incurred?\nA: $6\nB: $7\nC: $8\nD: $9'
    }
    """
    def __init__(self):
        data = load_dataset("lmms-lab/MMMU", split="validation")
        self.data = data
        self.save_images_to_local(dataset='mmmu', split='validation', key_list=['image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7'])

    def __getitem__(self, idx):
        assert len(self.data) > 0, "Empty dataset. Please load data first."
        
        d = self.data[idx]
        choices_dict = dict(enumerate(eval(d['options'])))
        choices = ''
        for k, v in choices_dict.items():
            choices += f"\n{chr(ord('A') + int(k))}: {v}"
        question = d['question'] + choices

        images = []
        for i in range(1, 7):
            if f'image {i}' in question:
                if d[f'image_{i}'].mode == 'P':
                    d[f'image_{i}'] = d[f'image_{i}'].convert('RGBA')
                images.append(d[f'image_{i}'])
        
        return {"images": images,
                "image_paths": self.local_path_dict[str(idx)],
                "answer": d['answer'],
                "question": question,}
