# Prompt Engineering

```python
import promptbench as pb
```

```python
# load dataset
dataset = pb.DatasetLoader.load_dataset(dataset_name)

# load a model.
# If model is openai/palm, need to provide openai_key/palm_key
# If model is llama, vicuna, need to provide model dir
model = pb.LLMModel(model=model_name, 
                    openai_key="sk-xxx",
                    max_new_tokens=30)

# load method
# If method is emotion prompt, need to provide prompt id (0-10)
method = pb.PEMethod(method=method_name, 
                    dataset=dataset_name,
                    prompt_id = 1  # for emotion_prompt 
                    )

# test and get results
results = method.test(dataset, model)
```