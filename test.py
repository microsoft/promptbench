# from promptbench.dataload import load_dataset
# dataset = load_dataset('sst2')
# # dataset = load_dataset('iwslt', ['en', 'de'])
# print(dataset[0])

from promptbench.metrics import Eval
eval = Eval()
print(eval)