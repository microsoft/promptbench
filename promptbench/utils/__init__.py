def inference_total_dataset(prompt, model, dataset):
    from ..process import process_input, process_pred
    from ..metrics import eval

    input_texts, labels = process_input(prompt, dataset)
    
    import tqdm
    raw_preds = []
    for input_text in tqdm.tqdm(input_texts):
        raw_preds.append(model[input_text])
    
    preds = process_pred(dataset.dataset_name, raw_preds)
    acc = eval(dataset, preds, labels)
    
    return acc
