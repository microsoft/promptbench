# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from .dataprocess import InputProcess, OutputProcess
from .visualize import Visualizer
from .defense import Defense

def inference_total_dataset(prompt, model, dataset):
    from ..metrics import Eval

    input_texts, labels = process_input(prompt, dataset)
    
    import tqdm
    raw_preds = []
    for input_text in tqdm.tqdm(input_texts):
        raw_preds.append(model[input_text])
    
    preds = process_pred(dataset.dataset_name, raw_preds)
    acc = Eval(dataset, preds, labels)
    
    return acc