# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

class Visualizer:

    def __init__(self, model) -> None:
        self.model = model

    def vis_by_grad(self, tokenizer, input_sentence, label):
        self.model.eval()

        def map_subwords_to_words(sentence, tokenizer):
            tokens = tokenizer.tokenize(sentence)
            mapping = []
            i = 0
            for token in tokens:
                if token[0] == "▁":
                    mapping.append(i)
                    i += 1
                else:
                    mapping.append(i - 1)

            return mapping, tokens

        # input_len = len(input_sentence.split())

        mapping, tokens = map_subwords_to_words(input_sentence, tokenizer)
        words = "".join(tokens).replace("▁", " ").split()

        input_len = len(words)

        inputs = tokenizer(input_sentence, return_tensors="pt")

        embeddings = self.model.get_input_embeddings()(inputs['input_ids'])
        embeddings.requires_grad_()
        embeddings.retain_grad()

        labels = tokenizer(label, return_tensors="pt")["input_ids"]

        outputs = self.model(inputs_embeds=embeddings,
                             attention_mask=inputs['attention_mask'], labels=labels)

        outputs.loss.backward()
        # print(outputs.loss.item())

        grads = embeddings.grad
        # print(grads.shape)
        import torch
        word_grads = [torch.zeros_like(grads[0][0])
                      for _ in range(input_len)]  # 初始化每个单词的梯度向量

        # ignore the [EOS] token
        for idx, grad in enumerate(grads[0][:len(mapping)]):
            word_grads[mapping[idx]] += grad

        words_importance = [grad.norm().item() for grad in word_grads]

        import numpy as np

        """ normalize importance by min-max"""
        min_importance = np.min(words_importance)
        max_importance = np.max(words_importance)
        words_importance = (words_importance - min_importance) / \
            (max_importance - min_importance)

        # word_importance_dict = {}
        # for word, importance in zip(words, word_importance):
        #     print(f"The gradient for '{word}' is {grad}")
        #     word_importance_dict[word] = importance

        return words, words_importance

    def vis_by_delete(self, tokenizer, input_sentence, label):
        import copy

        words = input_sentence.split()

        encoded_label = tokenizer(label, return_tensors="pt")["input_ids"]

        inputs = tokenizer(input_sentence, return_tensors="pt")
        outputs = self.model(**inputs, labels=encoded_label)
        original_loss = outputs.loss.item()

        word_importance = []

        for i in range(len(words)):
            new_words = copy.deepcopy(words)
            del new_words[i]
            new_sentence = ' '.join(new_words)
            inputs = tokenizer(new_sentence, return_tensors="pt")
            outputs = self.model(**inputs, labels=encoded_label)
            new_loss = outputs.loss.item()

            importance = abs(new_loss - original_loss)
            word_importance.append(importance)

        import numpy as np

        """ normalize importance by min-max"""
        min_importance = np.min(word_importance)
        max_importance = np.max(word_importance)
        word_importance = (word_importance - min_importance) / \
            (max_importance - min_importance)

        word_importance_dict = {}
        for word, importance in zip(words, word_importance):
            word_importance_dict[word] = importance

        return word_importance_dict

    def save_importance(self, words, importance):
        from html import escape
        import matplotlib.pyplot as plt
        import matplotlib.colors as colors
        import numpy as np

        cmap = plt.colormaps['Reds']
        latex_output = ''

        for i, word in enumerate(words):
            rgba = cmap(importance[i])

            rgb = ','.join(str(int(rgba[j]*255)) for j in range(3))

            # latex_output += '\\colorbox[RGB]{' + rgb + '}{' + word + '\\vphantom{fg}}\\hspace*{0pt}'
            latex_output += word + ' '

        return latex_output


if __name__ == "__main__":
    from transformers import T5Tokenizer, T5ForConditionalGeneration

    tokenizer = T5Tokenizer.from_pretrained(
        "google/flan-t5-large", device_map="auto")
    model = T5ForConditionalGeneration.from_pretrained(
        "google/flan-t5-large", device_map="auto")
    input_sentence = "As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment' or 'not_entailment'. Respond with 'entailment' or 'not_entailment'  and true is true :"
    label = 'not_entailment'

    print("================by grad================")
    words, words_importance = vis_by_grad(
        model, tokenizer, input_sentence, label)
    for word, importance in zip(words, words_importance):
        print(f"{word:10}: {importance:.4f}")

    print()

    # print("================by delete================")
    # word_importance_dict = vis_by_delete(model, tokenizer, input_sentence, label)
    # for word, importance in word_importance_dict.items():
    #     print(f"{word:10}: {importance:.4f}")
    # print()
