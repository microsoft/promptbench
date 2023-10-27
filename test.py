from promptbench.dataload import load_dataset, Dataset
print(Dataset.data_list())
dataset = load_dataset('sst2')
# dataset = load_dataset('iwslt', ['en', 'de'])
print(dataset[0])

# from promptbench.metrics import Eval
# eval = Eval()
# print(eval)

from promptbench.models import LLMModel

# print all supported models
print(LLMModel.model_list())

# Create a T5 model
model_t5 = LLMModel(model='google/flan-t5-large')
output_t5 = model_t5("Translate English to German: 'Hello World'")
print(output_t5)

from promptbench.utils import Visualizer
x = Visualizer('google/flan-t5-large')
print(x)
