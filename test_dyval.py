# import spacy

# # Load the English Language Model
# nlp = spacy.load("en_core_web_sm")

# # Sample sentence
# sentence = "The quick brown fox jumps over the lazy dog."
# doc = nlp(sentence)

# # Extracting the syntax tree
# for token in doc:
#     print(f"{token.text:10} {token.dep_:10} {token.head.text:10} {token.head.pos_:10} {[(child.text, child.dep_) for child in token.children]}")


import spacy
import random

nlp = spacy.load("en_core_web_sm")

# Example pools of words
nouns_pool = ["dog", "car", "apple", "beach"]
verbs_pool = ["run", "drive", "eat", "play"]
adjectives_pool = ["quick", "red", "sweet", "sunny"]

def replace_word(token):
    if token.pos_ == "NOUN":
        return random.choice(nouns_pool)
    elif token.pos_ == "VERB":
        return random.choice(verbs_pool)
    elif token.pos_ == "ADJ":
        return random.choice(adjectives_pool)
    else:
        return token.text  # No replacement for other types of words

def generate_sentence(sentence):
    doc = nlp(sentence)
    new_sentence = " ".join(replace_word(token) for token in doc)
    return new_sentence

original_sentence = "The quick brown fox jumps over the lazy dog."
modified_sentence = generate_sentence(original_sentence)
print(modified_sentence)
