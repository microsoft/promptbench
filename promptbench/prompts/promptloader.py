"""
TODO: support custom prompt
"""

import numpy as np
import re
import os

"""
TODO: write a function to add few-shot examples to the prompt
TODO: evaluation function
TODO: add code into model.py (there we need to return a score)

TODO: DyVal Llama2?
TODO: presentation
"""

def get_few_shot_examples(self):
    from prompts.three_shot.few_shot_examples import examples
    few_shot_examples = examples["bool_logic"]
    return few_shot_examples


def get_few_shot_examples(self):
    from prompts.three_shot.few_shot_examples import examples
    few_shot_examples = examples["valid_parentheses"]
    return few_shot_examples

def get_few_shot_examples(self, task):
    from prompts.three_shot.few_shot_examples import examples

    few_shot_data = examples["math"][task]
    few_shot_examples = "Here are three examples. \n"
    for d in few_shot_data:
        few_shot_examples += "Question: " + d["question"] + "\n"
        few_shot_examples += "Answer: " + str(d["answer"]) + "\n"

    return few_shot_examples

def get_few_shot_examples(self, task):
    from prompts.three_shot.few_shot_examples import examples

    few_shot_examples = examples["un_multi"][task]
    return few_shot_examples

def get_few_shot_examples(self, task):
    from prompts.three_shot.few_shot_examples import examples

    few_shot_examples = examples["iwslt"][task]
    return few_shot_examples

def get_few_shot_examples(self, task):
    from prompts.three_shot.few_shot_examples import examples

    few_shot_examples = examples[task]
    return few_shot_examples

with open("promptbench/data/MMLU_few_shot.json", "r") as file:
    self.few_shot_data = json.load(file)

def get_few_shot_examples(self, task):
    content = "Here are three examples.\n"
    data = self.few_shot_data[task]
    for idx in range(min(len(data), 3)):
        content += ("Input: " + data[idx]["input"] + "\n"
                    + "A : " + data[idx]["A"] + "\n"
                    + "B : " + data[idx]["B"] + "\n"
                    + "C : " + data[idx]["C"] + "\n"
                    + "D : " + data[idx]["D"] + "\n\n"
                    + "Answer : " + data[idx]["target"] + "\n"
                    )

    return content

def get_few_shot_examples(self, task):
    from prompts.three_shot.few_shot_examples import examples

    few_shot_examples = examples[task]
    return few_shot_examples

def split_markdown_by_title(markdown_file):
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()

    re_str = "# cola|# mnli|# mrpc|# qnli|# qqp|# rte|# sst2|# wnli|# mmlu|# squad_v2|# iwslt|# un_multi|# math"
    
    datasets = ["# cola", "# mnli", "# mrpc", "# qnli", "# qqp", "# rte", "# sst2", "# wnli",
                "# mmlu", "# squad_v2", "# iwslt", "# un_multi", "# math"]
    
    primary_sections = re.split(re_str, content)[1:]
    assert len(primary_sections) == len(datasets)

    all_sections_dict = {}

    for dataset, primary_section in zip(datasets, primary_sections):
        re_str = "## "
        results = re.split(re_str, primary_section)
        keywords = ["10 prompts", "bertattack", "checklist", "deepwordbug", "stresstest",
                    "textfooler", "textbugger", "translation"]

        secondary_sections_dict = {}
        for res in results:
            for keyword in keywords:
                if keyword in res.lower():
                    secondary_sections_dict[keyword] = res
                    break

        all_sections_dict[dataset] = secondary_sections_dict

    return all_sections_dict


def list_files(directory):
    files = [os.path.join(directory, d) for d in os.listdir(directory) if not os.path.isdir(os.path.join(directory, d))]
    return files

def convert_model_name(attack):
    attack_name = {
        "google/flan-t5-large": "t5",
        "google/flan-ul2": "ul2",
        "vicuna-13b": "vicuna",
        "llama2-13b-chat": "llama2",
        "chatgpt": "chatgpt",
    }
    return attack_name[attack]


def convert_dataset_name(dataset):
    return "# " + dataset


def retrieve(model_name, dataset_name, attack_name, prompt_type):
    model_name = convert_model_name(model_name)
    dataset_name = convert_dataset_name(dataset_name)

    if "zero" in prompt_type:
        shot = "zeroshot"
    else:
        shot = "fewshot"
    
    if "task" in prompt_type:
        prompt_type = "task"
    else:
        prompt_type = "role"
    
    directory_path = "./adv_prompts"
    md_dir = os.path.join(directory_path, model_name + "_" + shot + ".md")
    sections_dict = split_markdown_by_title(md_dir)
    results = {}
    for cur_dataset in sections_dict.keys():
        if cur_dataset == dataset_name:
            dataset_dict = sections_dict[cur_dataset]
            best_acc = 0
            best_prompt = ""
            for cur_attack in dataset_dict.keys():
                if cur_attack == "10 prompts":
                    prompts_dict = dataset_dict[cur_attack].split("\n")
                    num = 0
                    for prompt_summary in prompts_dict:
                        if "Acc: " not in prompt_summary:
                            continue
                        else:
                            import re
                            num += 1
                            match = re.search(r'Acc: (\d+\.\d+)%', prompt_summary)
                            if match:
                                number = float(match.group(1))
                                if number > best_acc:
                                    best_acc = number
                                    best_prompt = prompt_summary.split("prompt: ")[1]

            for cur_attack in dataset_dict.keys():
                
                if cur_attack == attack_name:

                    if attack_name == "translation":
                        prompts_dict = dataset_dict[attack_name].split("\n")
            
                        for prompt_summary in prompts_dict:
                            if "acc: " not in prompt_summary:
                                continue
                            
                            prompt = prompt_summary.split("prompt: ")[1]
                            
                            import re
                        
                            match_atk = re.search(r'acc: (\d+\.\d+)%', prompt_summary)
                            number_atk = float(match_atk.group(1))
                            results[prompt] = number_atk
  
                        sorted_results = sorted(results.items(), key=lambda item: item[1])[:6]

                        returned_results = []
                        for result in sorted_results:
                            returned_results.append({"origin prompt": best_prompt, "origin acc": best_acc, "attack prompt": result[0], "attack acc": result[1]})
      
                        return returned_results

                    elif attack_name in ["bertattack", "checklist", "deepwordbug", "stresstest", "textfooler", "textbugger"]:

                        prompts_dict = dataset_dict[attack_name].split("Original prompt: ")
                        num = 0
                        
                        returned_results = []
                        for prompt_summary in prompts_dict:
                            if "Attacked prompt: " not in prompt_summary:
                                continue

                            origin_prompt = prompt_summary.split("\n")[0]
                            attack_prompt = prompt_summary.split("Attacked prompt: ")[1].split("Original acc: ")[0]
                            attack_prompt = bytes(attack_prompt[2:-1], "utf-8").decode("unicode_escape").encode("latin1").decode("utf-8")

                            print(origin_prompt)
                            print(attack_prompt)

                            num += 1
                            import re
                            match_origin = re.search(r'Original acc: (\d+\.\d+)%', prompt_summary)
                            match_atk = re.search(r'attacked acc: (\d+\.\d+)%', prompt_summary)
                            if match_origin and match_atk:
                                if prompt_type == "task":
                                    if num > 3:
                                        break
                                else:
                                    if num < 3:
                                        continue
                                number_origin = float(match_origin.group(1))
                                number_atk = float(match_atk.group(1))
                                returned_results.append({"origin prompt": origin_prompt, "origin acc": number_origin, "attack prompt": attack_prompt, "attack acc": number_atk})
                        
                        return returned_results


if __name__ == "__main__":
    print(retrieve("t5", "cola", "bertattack", "zeroshot_task"))

    