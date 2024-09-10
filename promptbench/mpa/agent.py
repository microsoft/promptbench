# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from ..models import LLMModel
import copy
from .dataprocess import ParaphraserInputProcess, ParaphraserOutputProcess, EvaluatorInputProcess, EvaluatorOutputProcess


class ParaphraserAgent(object):
    def __init__(self, model: LLMModel, prompt: str, input_func: ParaphraserInputProcess, output_func: ParaphraserOutputProcess):
        self.model = model
        self.prompt = prompt
        self.input_func = input_func
        self.output_func = output_func
    
    def __call__(self, data: dict) -> str:
        input_text = self.input_func(self.prompt, data)

        while True:
            try_count = 1
            try:
                output_text = self.model(input_text)
            except Exception as e:
                print("ParaphraserAgent output error!")
                print(e)
                import time
                time.sleep(30*try_count)
                try_count += 1
                continue

            try:
                paraphrased_data = self.output_func(output_text, data)
                break
            except Exception as e:
                print("ParaphraserAgent process output error!")
                print(e)
                continue

        return paraphrased_data


class EvaluatorAgent(object):
    def __init__(self, model: LLMModel, prompt: str, input_func: EvaluatorInputProcess, output_func: EvaluatorOutputProcess):
        self.model = model
        self.prompt = prompt
        self.input_func = input_func
        self.output_func = output_func
    
    def __call__(self, original_data, paraphraserd_data):
        input_text = self.input_func(self.prompt, original_data, paraphraserd_data)

        while True:
            try_count = 1
            try:
                output_text = self.model(input_text)
            except Exception as e:
                print("EvaluatorAgent output error!")
                print(e)
                import time
                time.sleep(30*try_count)
                try_count += 1
                continue
            
            try:
                valid = self.output_func(output_text)
                break
            except Exception as e:
                print("EvaluatorAgent process output error!")
                print(e)
                continue

        return valid


class Pipeline:
    def __init__(self, paraphraser_agent, eval_agent, iters=1, retry=5):
        """
        Initializes the Pipeline class with paraphraser and evaluator agents, post evaluation action, and number of iterations.
        :param paraphraser_agent: The agent responsible for rephrasing the data.
        :param eval_agent: The agent responsible for evaluating the paraphrased data.
        :param iters: The number of iterations to paraphrase and evaluate.
        """
        self.paraphraser_agent = paraphraser_agent
        self.eval_agent = eval_agent
        self.iters = iters
        self.retry = retry

    def __call__(self, original_data):
        """
        Processes the data through the pipeline, paraphrasing and evaluating according to the specified logic.
        :param data: The data to be paraphrased.
        :return: The paraphrased data list.
        """
        data = copy.deepcopy(original_data)
        paraphrased_data_list = []
        paraphrased_data_list.append(copy.deepcopy(original_data))

        for _ in range(self.iters):
            paraphrased = False
            retry = self.retry
            while not paraphrased and retry > 0:
                copied_data = copy.deepcopy(data)
                retry -= 1
                self.paraphraser_agent(data)
                valid = self.eval_agent(original_data, data)

                if not valid:
                    data = copied_data
                    continue
                else:
                    paraphrased = True
            
            if not paraphrased:
                print("Paraphraser failed to paraphrase the data!")
                paraphrased_data_list.append(copy.deepcopy(paraphrased_data_list[-1]))
            else:
                print("Paraphraser successfully paraphrased the data!")
                paraphrased_data_list.append(copy.deepcopy(data))
        
        return paraphrased_data_list
