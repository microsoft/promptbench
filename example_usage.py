# Example usage of the config file
import promptbench as pb
from config import OPENAI_API_KEY, PALM_API_KEY, DEFAULT_MODEL, DEFAULT_MAX_TOKENS

# Load dataset
dataset_name = "gsm8k"
dataset = pb.DatasetLoader.load_dataset(dataset_name)

# Load model using API key from config
model = pb.LLMModel(
    model=DEFAULT_MODEL, 
    openai_key=OPENAI_API_KEY,
    max_new_tokens=DEFAULT_MAX_TOKENS
)

# Load method
method = pb.PEMethod(
    method='emotion_prompt', 
    dataset=dataset_name,
    verbose=True,
    prompt_id=1
)

# Test the method
results = method.test(dataset, model, num_samples=5)
print(f"Results: {results}")

# Import the method
from Mel_mini.Segmentation import get_mel_json

# Or import the specific module
from Mel_mini.Segmentation.mel_segmentation import get_mel_json

# Use the method (will raise NotImplementedError until implemented)
try:
    result = get_mel_json("your prompt here")
except NotImplementedError:
    print("Method not yet implemented") 