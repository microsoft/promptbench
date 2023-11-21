from tqdm import tqdm
import promptbench as pb
import argparse


# create a logging parser
parser = argparse.ArgumentParser()
parser.add_argument('--dataset_name', type=str, default='bigbench_object_tracking')
parser.add_argument('--model_name', type=str, default='gpt-4-1106-preview')
parser.add_argument('--method_name', type=str, default='ZSCoT')
args = parser.parse_args()

dataset_name = args.dataset_name
model_name = args.model_name
method_name = args.method_name

log_dir = './logs/' if 'gpt' in model_name else ''
    

if __name__ == '__main__':
    log_file = open(f'{log_dir}{method_name}_{model_name}_{dataset_name}.txt', 'w')
    log_file.write(f"Method: {method_name} \nModel: {model_name} \nDataset: {dataset_name}\n\n")
        
    # load dataset
    dataset = pb.DatasetLoader.load_dataset(dataset_name)

    # load a model.
    model = pb.LLMModel(model=model_name, 
                        openai_key = 'sk-xxx',
                        model_dir = f'/mnt/mydata/llms/{model_name}',
                        max_new_tokens=30)

    # load method
    method = pb.PEMethod(method=method_name, dataset=dataset_name)

    # test and get results
    results = method.test(dataset, model)

    log_file.write(f'Result: {results}')
    log_file.close()
    
    print(results)