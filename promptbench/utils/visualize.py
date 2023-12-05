# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from ..models import LLMModel
import torch
import numpy as np
import copy

class Visualizer:
    def __init__(self, model: LLMModel) -> None:
        """
        Initialize the Visualizer class.

        Parameters:
        - model (LLMModel): The model to visualize.

        Attributes:
        - model: The inference pipeline of the provided model.
        - tokenizer (Tokenizer): Tokenizer associated with the model.
        """
        self.model = model.infer_model.pipe
        self.tokenizer = model.infer_model.tokenizer

    def _map_subwords_to_words(self, sentence: str):
        """
        Convert a sentence into tokens and map subword tokens to their corresponding words.

        Parameters:
        - sentence (str): The input sentence.

        Returns:
        - mapping (list): List mapping subword tokens to word indices.
        - tokens (list): Tokenized version of the input sentence.
        """
        tokens = self.tokenizer.tokenize(sentence)
        mapping = []
        word_idx = 0
        for token in tokens:
            if token.startswith("▁"):
                mapping.append(word_idx)
                word_idx += 1
            else:
                mapping.append(word_idx - 1)
        return mapping, tokens

    def _normalize_importance(self, word_importance):
        """
        Normalize importance values of words in a sentence using min-max scaling.

        Parameters:
        - word_importance (list): List of importance values for each word.

        Returns:
        - list: Normalized importance values for each word.
        """
        min_importance = np.min(word_importance)
        max_importance = np.max(word_importance)
        return (word_importance - min_importance) / (max_importance - min_importance)

    def vis_by_grad(self, input_sentence: str, label: str) -> dict:
        """
        Visualize word importance in an input sentence based on gradient information.

        This method uses the gradients of the model's outputs with respect to its 
        input embeddings to estimate word importance.

        Parameters:
        - input_sentence (str): The input sentence.
        - label (str): The target label.

        Returns:
        - dict: Dictionary with words as keys and their normalized importance as values.
        """        
        self.model.eval()

        mapping, tokens = self._map_subwords_to_words(input_sentence)
        words = "".join(tokens).replace("▁", " ").split()

        inputs = self.tokenizer(input_sentence, return_tensors="pt")
        embeddings = self.model.get_input_embeddings()(inputs['input_ids'])
        embeddings.requires_grad_()
        embeddings.retain_grad()

        labels = self.tokenizer(label, return_tensors="pt")["input_ids"]
        outputs = self.model(inputs_embeds=embeddings, attention_mask=inputs['attention_mask'], labels=labels)
        outputs.loss.backward()

        grads = embeddings.grad
        word_grads = [torch.zeros_like(grads[0][0]) for _ in range(len(words))]  # Initialize gradient vectors for each word

        # Aggregate gradients for each word
        for idx, grad in enumerate(grads[0][:len(mapping)]):
            word_grads[mapping[idx]] += grad

        words_importance = [grad.norm().item() for grad in word_grads]
        normalized_importance = self._normalize_importance(words_importance)

        return dict(zip(words, normalized_importance))

    def vis_by_delete(self, input_sentence: str, label: str) -> dict:
        """
        Visualize word importance in an input sentence by deletion method.

        For each word in the sentence, the method deletes it and measures the 
        change in the model's output. A higher change indicates higher importance.

        Parameters:
        - input_sentence (str): The input sentence.
        - label (str): The target label.

        Returns:
        - dict: Dictionary with words as keys and their normalized importance as values.
        """        
        words = input_sentence.split()
        encoded_label = self.tokenizer(label, return_tensors="pt")["input_ids"]
        inputs = self.tokenizer(input_sentence, return_tensors="pt")
        original_loss = self.model(**inputs, labels=encoded_label).loss.item()

        word_importance = []
        for i in range(len(words)):
            new_words = copy.deepcopy(words)
            del new_words[i]
            new_sentence = ' '.join(new_words)
            inputs = self.tokenizer(new_sentence, return_tensors="pt")
            new_loss = self.model(**inputs, labels=encoded_label).loss.item()

            importance = abs(new_loss - original_loss)
            word_importance.append(importance)

        normalized_importance = self._normalize_importance(word_importance)

        return dict(zip(words, normalized_importance))
    


