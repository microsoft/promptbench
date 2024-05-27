

import promptbench as pb
from tqdm import tqdm
import torch

# print all supported datasets in promptbench
print('All supported datasets: ')
print(pb.SUPPORTED_DATASETS)

# print all supported models in promptbench
print('All supported models: ')
print(pb.SUPPORTED_MODELS)


# load a dataset, sst2, for instance.
# if the dataset is not available locally, it will be downloaded automatically.
def sentiment_classification_example():
    print("sentiment_classification_example")

    print("Loading dataset sst2")
    dataset = pb.DatasetLoader.load_dataset("sst2")

    print("The first 5 examples")
    print(dataset[:5])

    # Prompt API supports a list, so you can pass multiple prompts at once.
    prompts = pb.Prompt(["Classify the sentence as positive or negative: {content}",
                         "Determine the emotion of the following sentence as positive or negative: {content}"
                         ])

    # load a model, flan-t5-large, for instance.
    model = pb.LLMModel(model='google/flan-t5-large', max_new_tokens=10, temperature=0.0001, dtype=torch.float32, device='cpu')

    print("Finished download.")

    def proj_func(pred):
        mapping = {
            "positive": 1,
            "negative": 0
        }
        return mapping.get(pred, -1)

    print("Running evaluation.")
    for prompt in prompts:
        preds = []
        labels = []
        for data in tqdm(dataset[:3]):
            # process input
            input_text = pb.InputProcess.basic_format(prompt, data)
            print(f"Input text: {input_text}")
            label = data['label']
            print(f"Label: {label}")
            raw_pred = model(input_text)
            print(f"Raw Prediction: {raw_pred}")
            # process output - classification
            pred = pb.OutputProcess.cls(raw_pred, proj_func)
            preds.append(pred)
            labels.append(label)

        # evaluate classification
        score = pb.Eval.compute_cls_accuracy(preds, labels)
        print(f"{score:.3f}, {prompt}")


sentiment_classification_example()
