import promptbench as pb
from promptbench.models import LLMModel
from promptbench.dyval import *

import argparse
import os
import logging

def create_logger(log_path):

    logging.getLogger().handlers = []

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    return logger

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="phi-1.5", choices=pb.SUPPORTED_MODELS)
    parser.add_argument("--dataset", type=str, default="arithmetic", choices=pb.dyval.DYVAL_DATASETS)
    
    parser.add_argument("--output_dir", type=str, default="./", help="Logs and result directory")

    parser.add_argument("--model_path", type=str, default="../llama2-13b", help="Model path")
    parser.add_argument("--temp", type=float, default=0, help="Temperature for sampling")
    parser.add_argument("--max_new_tokens", type=float, default=100, help="Ratio relative to the input token count to determine the maximum tokens the LLM can produce")

    parser.add_argument("--shot", type=int, default=0, help="Number of few-shot examples to generate")
    parser.add_argument("--cot", action='store_true', help="Chain of thought")
    parser.add_argument("--least2most", action='store_true', help="Least to most prompting")
    parser.add_argument("--ape", action='store_true', help="Automatic Prompting Engeneering")
    parser.add_argument("--skic", action='store_true', help="SKill in Context prompting")

    parser.add_argument("--num_samples", type=int, default=3, help="Number of samples to generate")

    parser.add_argument("--num_nodes_per_sample", type=int, default=10, help="Number of nodes per sample (for GeneralDAG)")
    parser.add_argument("--min_links_per_node", type=int, default=1, help="Minimum number of links per node (for GeneralDAG)")
    parser.add_argument("--max_links_per_node", type=int, default=4, help="Maximum number of links per node (for GeneralDAG)")

    parser.add_argument("--depth", type=int, default=2, help="Depth of the DAG (for TreeDAG)")
    parser.add_argument("--num_children_per_node", type=int, default=2, help="Number of children per node (for TreeDAG)")
    parser.add_argument("--extra_links_per_node", type=int, default=0, help="Number of extra links per node (for TreeDAG)")
    
    parser.add_argument("--add_rand_desc", type=int, default=0, help="Add random descriptions to the DAG")
    parser.add_argument("--delete_desc", type=int, default=0, help="Randomly delete descriptions from the DAG")
    parser.add_argument("--add_cycles", type=int, default=0, help="Add cycles to the DAG")

    parser.add_argument("--num_dags", type=int, default=1, help="Number of coefficient to be replaced in linear equation task")

    args = parser.parse_args()
    return args


def inference(logger, prompt, dataset, model):

    score = {}

    for order in ["topological", "reversed", "random"]:
        data = dataset[order]
        preds = []
        answers = []
        
        for d in data:
            input_text = pb.InputProcess.basic_format(prompt, d)
            raw_pred = model(input_text)
            pred = process_dyval_preds(raw_pred)
            preds.append(pred)
            answers.append(d["answers"])

            logger.info(f"Input: {input_text}")
            logger.info(f"Raw Pred: {raw_pred}")
            logger.info(f"Pred: {pred}")
            logger.info(f"Answer: {d['answers']}")
            logger.info("\n")

        score[order] = evaluate(dataset.dataset_type, preds, answers)

    return score


def main(args):

    save_dir = args.dataset + "_" + args.model.replace("/", "_") + "/"

    LOGS_DIR = os.path.join(args.output_dir, "logs_test/" + save_dir)
    RESULTS_DIR = os.path.join(args.output_dir, "results_test/" + save_dir)

    for DIR in [LOGS_DIR, RESULTS_DIR]:
        if not os.path.isdir(DIR):
            os.makedirs(DIR)
    
    file_name =  "max_new_tokens" + str(args.max_new_tokens)[:3] + "_shot" + str(args.shot)
    if args.cot:
        file_name += "_cot"
    elif args.least2most:
        file_name += "_least2most"
    elif args.ape:
        file_name += "_ape"
    elif args.skic:
        file_name += "_skic"

    if args.dataset in ["arithmetic", "linear_equation", "bool_logic", "deductive_logic", "abductive_logic"]:
        file_name += "_depth" + str(args.depth) + "_children" + str(args.num_children_per_node) + "_extra" + str(args.extra_links_per_node)
    elif args.dataset in ["reachability", "max_sum_path"]:
        file_name +=  "_nodes" + str(args.num_nodes_per_sample) + "_min" + str(args.min_links_per_node) + "_max" + str(args.max_links_per_node)
    file_name += "_rand" + str(args.add_rand_desc) + "_delete" + str(args.delete_desc) + "_cycles" + str(args.add_cycles)
 
    logger = create_logger(LOGS_DIR+file_name+".log")
    logger.info(args)
    if args.ape:
        prompts = APE_PROMPTS[args.dataset]
    elif args.skic:
        prompts = SKIC_PROMPTS[args.dataset]
    else:
        prompts = DYVAL_PROMPTS[args.dataset]

    dataset = DyValDataset(args.dataset, 
                           False,
                           args.num_samples,
                           args.num_nodes_per_sample,
                           args.min_links_per_node,
                           args.max_links_per_node,
                           args.depth, 
                           args.num_children_per_node,
                           args.extra_links_per_node,
                           args.add_rand_desc,
                           args.delete_desc,
                           args.add_cycles)
    
    results = {}
    model = LLMModel(args.model, 
                     args.max_new_tokens, 
                     args.temp, 
                     args.model_path, 
                     openai_key="",
                     sleep_time=3)

    for prompt in prompts:
        if args.cot:
            prompt = prompt + "\nLet's think step by step."
        if args.shot:
            prompt = dataset.get_fewshot_examples(args.shot) + "\n\nQ:\n" + prompt
        if args.least2most:
            l2m_example = LEAST2MOST_EXAMPLES[args.dataset][0]
            l2m_prompt = l2m_example + "\nQ:\n"
            prompt = l2m_prompt + prompt
        if args.ape or args.skic:
            suffix = SUFFIX[args.dataset][0]
            prompt = prompt + suffix
            # dataset.data["descriptions"] = {"random": dataset["descriptions"]["random"]}

        score = inference(logger, prompt, dataset, model)
        results[prompt] = score
        logger.info("\n")
        logger.info("=====================================================================================")
        logger.info(f"Prompt: {prompt}")
        for order in score.keys():
            logger.info(f"Order: {order}, Score: {score[order]}")
        
        logger.info("=====================================================================================")
        logger.info("\n")
    
    for prompt, score in results.items():
        with open(RESULTS_DIR+file_name+".txt", "a+") as f:
            f.write("\n")
            f.write("=====================================================================================\n")
            f.write(f"Prompt: {prompt}\n")
            for order in score.keys():
                f.write(f"Order: {order}, Score: {score[order]}\n")
            f.write("=====================================================================================\n")

if __name__ == "__main__":
    args = get_args()
    main(args)