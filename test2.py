from tqdm import tqdm
import promptbench as pb

dataset_name = "bigbench_date"
model_name = "gpt-3.5-turbo"
method_name = "ZSCoT"

# load dataset
dataset = pb.DatasetLoader.load_dataset(dataset_name)

# load a model.
model = pb.LLMModel(model=model_name, 
                    openai_key = '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',
                    max_new_tokens=30)

# load method
method = pb.PEMethod(method=method_name, dataset=dataset_name)

# test and get results
results = method.test(dataset, model)

print(results)


# TODO: logging module