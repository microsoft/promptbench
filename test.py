# # # from promptbench.dataload import load_dataset, Dataset
# # # print(Dataset.data_list())
# # # dataset = load_dataset('sst2')
# # # # dataset = load_dataset('iwslt', ['en', 'de'])
# # # print(dataset[0])

# # # # from promptbench.metrics import Eval
# # # # eval = Eval()
# # # # print(eval)

# # from promptbench.models import LLMModel

# # # # print all supported models
# # # print(LLMModel.model_list())

# # # Create a T5 model
# # model_t5 = LLMModel(model='google/flan-t5-large')

# # input_sentence = "As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment' or 'not_entailment'. Respond with 'entailment' or 'not_entailment'  and true is true :"
# # label = 'not_entailment'

# # from promptbench.utils import Visualizer
# # visualizer = Visualizer(model_t5)
# # word_importance_dict = visualizer.vis_by_grad(input_sentence, label)
# # for word, importance in word_importance_dict.items():
# #     print("{:10}: {:.4f}".format(word, importance))

# # word_importance_dict = visualizer.vis_by_delete(input_sentence, label)
# # for word, importance in word_importance_dict.items():
# #     print("{:10}: {:.4f}".format(word, importance))


# # output_t5 = model_t5("Translate English to German: 'Hello World'")


# # # # test defense of prompt input using spell correct
# # # from promptbench.utils import Defense
# # # x = Defense('spellcorrect')
# # # print(x('I am a student at the Univrsity of California, Berkeey.'))



# # """
# # Processing input and output
# # """
# # from promptbench.utils import InputProcess, OutputProcess

# # # For a prompt with task information:
# # prompt_template2 = "Translate the following sentence from {source_lang} into {target_lang}: {content}"
# # input_data_dict2 = {"content": "Bonjour", "source_lang": "French", "target_lang": "English"}
# # print(InputProcess.basic_format(prompt_template2, input_data_dict2))

# # def test_OutputProcess():
# #     processor = OutputProcess()

# #     # Testing general
# #     assert processor.general("HeLlo, WOrld! </s> <pad>") == "hello, world"

# #     # Testing cls
# #     assert processor.cls("This is an example string. classify") == "classify"
# #     assert processor.cls("Another example for classification. result") == "result"

# #     # Testing pattern_split
# #     assert processor.pattern_split("This is a pattern_split example. split_here result", "split_here") == "result"
# #     assert processor.pattern_split("Another pattern_split test. delimiter outcome", "delimiter") == "outcome"

# #     # Testing pattern_re
# #     assert processor.pattern_re("This is a regular expression <<<test>>>.", '<<<(.*?)>>>') == "test"
# #     assert processor.pattern_re("No matching pattern here.", '<<<(.*?)>>>') == "no matching pattern here"

# #     print("All tests passed!")

# # test_OutputProcess()


# from promptbench.prompts import Prompt
# from promptbench.utils import InputProcess, OutputProcess
# from promptbench.models import LLMModel

# # prompts = Prompt(dataset_name='sst2')
# prompts = Prompt("Classify the sentence as positive or negative: {content}")
# dataset = [{"content": "I am happy today.", "label": 1}, {"content": "It's slow, very slow...", "label": 0}]
# print(prompts[:2])


# # input_text = InputProcess.basic_format(prompts[0], data)
# # print(input_text)

# # model_t5 = LLMModel(model='google/flan-t5-large', max_new_tokens=10)

# # raw_pred = model_t5(input_text)
# # pred = OutputProcess.cls(raw_pred)
# # print(raw_pred)
# # print(pred)


# # from promptbench.dataload import DatasetLoader
# # print(DatasetLoader.SUPPORTED_DATASETS)
# # dataset = DatasetLoader.load_dataset('sst2')

# import promptbench as pb
# print(pb.LLMModel.model_list())
# model = pb.LLMModel(model='phi-1.5', max_new_tokens=20)

# # print(pb.DatasetLoader.dataset_list())
# # dataset = pb.DatasetLoader.load_dataset("sst2")
# # print(dataset[:5])

# # dataset = pb.DyValDataset("arithmetic", num_samples=100, depth=3, num_children_per_node=2, add_rand_desc=1)
# # print(dataset["topological"][0])


# # prompts = pb.Prompt(["Classify the sentence as positive or negative: {content}",
# #                      "Determine the emotion of the following sentence as positive or negative: {content}"
# #                      ])

# # """
# # You may need to define the projection function for the model output.
# # Since the output format defined in your prompts may be different from the model output.
# # For example, for sst2 dataset, the label are '0' and '1' to represent 'negative' and 'positive'.
# # But the model output is 'negative' and 'positive'.
# # So we need to define a projection function to map the model output to the label.
# # """
# def proj_func(pred):
#     mapping = {
#         "positive": 1,
#         "negative": 0
#     }
#     return mapping.get(pred, -1)


# from tqdm import tqdm
# for prompt in prompts:
#     preds = []
#     labels = []
#     for data in tqdm(dataset):
#         input_text = pb.InputProcess.basic_format(prompt, data)
#         print(input_text)
#         label = data['label']
#         raw_pred = model(input_text)
#         print(raw_pred)
#         pred = pb.OutputProcess.cls(raw_pred, proj_func)
#         preds.append(pred)
#         labels.append(label)
    
#     score = pb.Eval.compute_cls_accuracy(preds, labels)
#     print(f"{score:.3f}, {prompt}")

import torch
import transformers
from transformers import LlamaForCausalLM, LlamaTokenizer, AutoTokenizer, AutoModelForCausalLM

# model_dir = "../llama2-13b"

model_dir = "meta-llama/Llama-2-13b-hf"

tokenizer = LlamaTokenizer.from_pretrained(model_dir, device_map="auto")
pipe = LlamaForCausalLM.from_pretrained(model_dir, device_map="auto", torch_dtype=torch.float16)
print(tokenizer.eos_token)

# base_prompt = """
# <<SYS>>
# Analyze the text in the content and evaluate the overall sentiment for 'User'.\n
# And return your sentiment analysis only as : Positive, Negative, or Neutral \n
# <</SYS>>
# [INST]
# User:{user_prompt}
# [/INST]\n

# Assistant:
# """

base_prompt = """
Analyze the text in the content and evaluate the overall sentiment.\n
And return your sentiment analysis only as : Positive, Negative, or Neutral \n
{user_prompt}
"""

# model = "meta-llama/Llama-2-13b-hf"

# tokenizer = AutoTokenizer.from_pretrained(model)
# pipeline = transformers.pipeline(
#     "text-generation",
#     model=model,
#     torch_dtype=torch.float16,
#     device_map="auto",
# )

# base_prompt = "<s>[INST]\n<<SYS>>\n{system_prompt}\n<</SYS>>\n\n{user_prompt}[/INST]"
system_prompt = "You are a helpful assistant to help 'User'."
user_prompt = "It's slow, very slow..."

# input_text = base_prompt.format(system_prompt=system_prompt, user_prompt=user_prompt)
input_text = base_prompt.format(user_prompt=user_prompt)

input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
outputs = pipe.generate(input_ids, 
                        max_new_tokens=100, 
                        temperature=0.0000001,
                        do_sample=True,)

out = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)

print(out)
