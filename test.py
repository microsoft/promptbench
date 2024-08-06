import promptbench as pb
from promptbench.prompteval import efficient_eval

prompt_list = [
    "Classify the sentence as positive or negative: {content}",
    "Determine the emotion of the following sentence as positive or negative: {content}",
    "Is the sentiment of this sentence positive or negative? {content}",
    "Identify whether the sentiment in the following sentence is positive or negative: {content}",
    "Assess the sentiment of this statement as either positive or negative: {content}",
    "Evaluate the following sentence and indicate if it is positive or negative: {content}",
    "Judge the emotional tone of this sentence as positive or negative: {content}",
    "Label the sentiment expressed in the sentence as positive or negative: {content}",
    "Decide if the sentiment in this statement is positive or negative: {content}",
    "Analyze the following sentence and determine if it is positive or negative: {content}",
    "Categorize the sentiment of the given sentence as positive or negative: {content}",
    "Tell if the following sentence conveys a positive or negative sentiment: {content}",
    "Discern whether the emotion in the sentence is positive or negative: {content}",
    "Determine if the given sentence expresses a positive or negative sentiment: {content}",
    "Conclude if the emotional tone of this sentence is positive or negative: {content}",
    "Recognize whether the sentiment of the following statement is positive or negative: {content}",
    "Rate the sentiment in this sentence as positive or negative: {content}",
    "Classify the emotional tone of the given sentence as positive or negative: {content}",
    "Identify the sentiment in this sentence and classify it as positive or negative: {content}",
    "Assess if the sentiment of the following statement is positive or negative: {content}",
    "Indicate whether the sentiment of this sentence is positive or negative: {content}",
    "Determine if the sentiment in this sentence is positive or negative: {content}",
    "Judge whether the following sentence has a positive or negative sentiment: {content}",
    "Analyze the emotional tone of the sentence and classify it as positive or negative: {content}",
    "Label the given sentence as having a positive or negative sentiment: {content}",
    "Evaluate whether the sentiment in the following sentence is positive or negative: {content}",
    "Categorize the given sentence based on whether its sentiment is positive or negative: {content}",
    "Determine the emotional quality of the sentence as positive or negative: {content}",
    "Is the emotional tone of this sentence positive or negative? {content}",
    "Discern the sentiment of the given sentence and label it as positive or negative: {content}"
]

def proj_func(pred):
    mapping = {
        "positive": 1,
        "negative": 0
    }
    return mapping.get(pred, -1)

# get dataset
dataset = pb.DatasetLoader.load_dataset("sst2")

# get model
model = pb.LLMModel(model='google/flan-t5-large', max_new_tokens=10, temperature=0.0001, device='cuda')

# efficient evaluation
mean_acc = efficient_eval(model, prompt_list, dataset, proj_func, budget=1200)
print(mean_acc)
