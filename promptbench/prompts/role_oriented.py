# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
This file contains the prompt sets for the zeroshot role-oriented prompts.
"""

ROLE_ORIENTED_PROMPTS = {
    'valid_parentheses': [
        "As a syntax validator, assess the given sequence of brackets and determine whether it conforms to proper bracket rules. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion: {content}\nAnswer:",
        "In your role as an expression evaluator, analyze the provided arrangement of parentheses and ascertain its validity. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion: {content}\nAnswer:",
        "You are a bracket expert. Examine the sequence of brackets given and decide if it follows correct syntax rules. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion: {content}\nAnswer:",
        "As a parenthesis specialist, review the arrangement of brackets provided and determine whether it is a valid sequence. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion: {content}\nAnswer:",
        "In your capacity as a syntax verifier, analyze the string of brackets and identify if the order of parentheses is correct. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion: {content}\nAnswer:",
        "Investigate the validity of the given bracket sequence, ensuring it adheres to appropriate rules for a valid arrangement. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion: {content}\nAnswer:",
        "As a sequence assessor, evaluate the arrangement of brackets provided and ascertain whether it represents a valid expression. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion: {content}\nAnswer:",
        "You are a bracket authority. Examine the provided sequence of brackets and determine if it adheres to valid syntax conventions. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion: {content}\nAnswer:",
        "In your role as a syntax checker, assess the bracket arrangement and conclude whether it conforms to the requirements for validity. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion: {content}\nAnswer:",
        "As a bracket sequence expert, analyze the given string of brackets and judge whether it displays proper syntax and organization. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion: {content}\nAnswer:",    
    ], 
    
    'bool_logic': [
        "In your role as a logical evaluator, determine the truth value of the following expression. Respond True if it is, False otherwise.\nQuestion: {content}\nAnswer:",
        "As a computer scientist, evaluate the given boolean expression's truth value. Respond True if it is, False otherwise.\nQuestion: {content}\nAnswer:",
        "You are a debugging expert. Analyze the expression, determine its truth value. Respond True if it is, False otherwise.\nQuestion: {content}\nAnswer:",
        "As a software engineer, assess the boolean logic, what is the truth value? Respond True if it is, False otherwise.\nQuestion: {content}\nAnswer:",
        "In your capacity as a systems engineer, evaluate the expression, answer its truth value. Respond True if it is, False otherwise.\nQuestion: {content}\nAnswer:",
        "You are a decision-making specialist. Determine the truth value of this bool expression. Respond True if it is, False otherwise.\nQuestion: {content}\nAnswer:",
        "In your role as a problem solver, what is the truth value of this boolean expression? Respond True if it is, False otherwise.\nQuestion: {content}\nAnswer:",
        "As a logical thinker, what is the truth value of the following expression? Respond True if it is, False otherwise.\nQuestion: {content}\nAnswer:",
        "You are a code reviewer. Determine if the boolean logic is True or False. Respond True if it is, False otherwise.\nQuestion: {content}\nAnswer:",
        "In your role as a critical analyst, provide the bool expression's truth value. Respond True if it is, False otherwise.\nQuestion: {content}\nAnswer:",
    ],
    
    'math': [
        "As a mathematics instructor, calculate the answer to the following problem related to {task}: \nQuestion: {content}\nAnswer:",
        "Pretend you are a math teacher and solve this mathematical question concerning {task}: \nQuestion: {content}\nAnswer:",
        "Imagine being a math mentor and determine the solution to the following problem with {task}: \nQuestion: {content}\nAnswer:",
        "In the position of a mathematics coach, figure out the answer to this math challenge involving {task}: \nQuestion: {content}\nAnswer:",
        "Act as a math expert and compute the result of the following mathematical task about {task}: \nQuestion: {content}\nAnswer:",
        "As a mathematics consultant, resolve the following problem associated with {task}: \nQuestion: {content}\nAnswer:",
        "Taking on the role of a math specialist, work out the solution for this mathematical question featuring {task}: \nQuestion: {content}\nAnswer:",
        "Embodying a mathematics advisor, find the answer to the following math problem with {task}: \nQuestion: {content}\nAnswer:",
        "As a math guru, evaluate the following mathematical task regarding {task}: \nQuestion: {content}\nAnswer:",
        "In the shoes of a mathematics master, obtain the result for this math question that includes {task}: \nQuestion: {content}\nAnswer:",
    ],
# I want you to act as a prompt generator for squad v2 dataset.  
# Here is an example : "Please provide the most accurate answer based on the context. If the answer cannot be found in the context, respond with 'unanswerable'.". " 
# Please generate 10 similar prompts. the prompt is used for MMLU (Measuring Massive Multitask Language Understanding) dataset.  
# For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.
    'iwslt': [
        "Acting as a professional translator, translate the provided sentence from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "As a skilled linguist, please convert the following sentence from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "Assuming the role of an expert language translator, translate the given text from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "In the capacity of a proficient translator, please change the following sentence from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "As a language specialist, accurately translate the provided sentence from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "Taking on the role of a certified translator, perform a translation of the given sentence from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "While acting as an experienced language expert, translate the following text from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "As a qualified translator, convert the given sentence from its original {soruce_lang} language to the target language {target_lang}: \nQuestion: {content}\nAnswer:",
        "Assuming the responsibilities of a professional translator, translate the subsequent text passage from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "In the role of a language expert, perform a machine translation for the provided sentence, changing it from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
    ],

    'un_multi': [
        "Acting as a professional translator, translate the provided sentence from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "As a skilled linguist, please convert the following sentence from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "Assuming the role of an expert language translator, translate the given text from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "In the capacity of a proficient translator, please change the following sentence from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "As a language specialist, accurately translate the provided sentence from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "Taking on the role of a certified translator, perform a translation of the given sentence from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "While acting as an experienced language expert, translate the following text from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "As a qualified translator, convert the given sentence from its original {soruce_lang} language to the target language {target_lang}: \nQuestion: {content}\nAnswer:",
        "Assuming the responsibilities of a professional translator, translate the subsequent text passage from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
        "In the role of a language expert, perform a machine translation for the provided sentence, changing it from {soruce_lang} to {target_lang}: \nQuestion: {content}\nAnswer:",
    ],

    'squad_v2': [
        "As a well-informed specialist familiar with the context, provide an answer to the question. If the context doesn't contain an answer, reply with 'unanswerable'.\nQuestion: {content}\nAnswer:",
        "Drawing upon your expertise in the context, determine the most suitable answer. If an answer isn't available, state 'unanswerable'.\nQuestion: {content}\nAnswer:",
        "As a subject matter expert, extract the correct answer from the context. If an answer is not present, indicate 'unanswerable'.\nQuestion: {content}\nAnswer:",
        "Using your knowledge of the context, identify the best answer to the question. If the context doesn't provide an answer, write 'unanswerable'.\nQuestion: {content}\nAnswer:",
        "As an authority on the context, locate the most accurate answer. If the context doesn't contain the answer, mention 'unanswerable'.\nQuestion: {content}\nAnswer:",
        "Being well-versed in the context, please derive the most fitting answer. If there isn't an answer in the context, use 'unanswerable'.\nQuestion: {content}\nAnswer:",
        "As an expert with a deep understanding of the context, find the best answer. If the context doesn't include an answer, say 'unanswerable'.\nQuestion: {content}\nAnswer:",
        "Drawing on your expertise in the context, provide the most precise answer. If the answer is not in the context, respond with 'unanswerable'.\nQuestion: {content}\nAnswer:",
        "As a proficient expert in the given context, search for the most relevant answer. If the answer cannot be found, respond by saying 'unanswerable'.\nQuestion: {content}\nAnswer:",
        "With your extensive knowledge of the context, answer the question accurately. If the context doesn't contain the answer, reply with 'unanswerable'."
    ],

    'mmlu': [
        "As an expert in {task}, respond to the following multiple-choice question by selecting 'A', 'B', 'C', or 'D'.\nQuestion: {content}\nAnswer:",
        "Given your proficiency in {task}, please answer the subsequent multiple-choice question with 'A', 'B', 'C', or 'D'.\nQuestion: {content}\nAnswer:",
        "With your knowledge of {task}, tackle the following multiple-choice question by choosing 'A', 'B', 'C', or 'D'.\nQuestion: {content}\nAnswer:",
        "As someone well-versed in {task}, please address the multiple-choice question below by selecting 'A', 'B', 'C', or 'D'.\nQuestion: {content}\nAnswer:",
        "Utilizing your expertise in {task}, answer the following multiple-choice question by picking 'A', 'B', 'C', or 'D'.\nQuestion: {content}\nAnswer:",
        "As a knowledgeable individual in {task}, provide your response to the multiple-choice question by choosing 'A', 'B', 'C', or 'D'.\nQuestion: {content}\nAnswer:",
        "With your understanding of {task}, kindly answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D'.\nQuestion: {content}\nAnswer:",
        "As a skilled person in the field of {task}, please respond to the multiple-choice question by choosing 'A', 'B', 'C', or 'D'.\nQuestion: {content}\nAnswer:",
        "Considering your familiarity with {task}, attend to the following multiple-choice question by picking 'A', 'B', 'C', or 'D'.\nQuestion: {content}\nAnswer:",
        "Drawing upon your mastery of {task}, please answer the multiple-choice question by selecting the correct option from 'A', 'B', 'C', or 'D'."
    ],

    'sst2': [
        "As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. Please classify: \nQuestion: {content}\nAnswer:",
        "In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement: \nQuestion: {content}\nAnswer:",
        "Acting as a sentiment evaluator, identify if the given sentence is 'positive' or 'negative'. Classify: \nQuestion: {content}\nAnswer:",
        "As an emotion detector, determine if the provided passage conveys a 'positive' or 'negative' sentiment. Classify: \nQuestion: {content}\nAnswer:",
        "Working as a sentiment analyzer, please indicate if the following text is 'positive' or 'negative'. Classify: \nQuestion: {content}\nAnswer:",
        "In the capacity of a sentiment classifier, decide whether the given quote is 'positive' or 'negative'. Classify: \nQuestion: {content}\nAnswer:",
        "Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative'. Classify: \nQuestion: {content}\nAnswer:",
        "Functioning as a sentiment identification tool, assess if the following expression is 'positive' or 'negative'. Classify: \nQuestion: {content}\nAnswer:",
        "Serving as a sentiment evaluation model, determine if the given statement is 'positive' or 'negative'. Classify: \nQuestion: {content}\nAnswer:",
        "Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative'. Classify: \nQuestion: {content}\nAnswer:",
    ],

    # 56.34, 66.20, 61.97, 59.15, 59.15, 56.34, 64.79, 57.75, 64.79, 54.93
    'wnli': [
        "In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "Acting as an entailment detection instrument, determine if the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "As a tool for determining entailment relationships, review the two statements and categorize their connection as either 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "While performing entailment analysis, classify the relationship between the provided sentences as 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "In the capacity of an entailment assessment system, indicate if the link between the following sentences is 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "Working as an entailment classifier, identify whether the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment' or 'not_entailment'. Respond with 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",   
    ],

    # 84.48, 84.12, 84.48, 84.48, 84.12, 84.84, 84.84, 83.03, 85.56, 82.31
    'rte': [
        "In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "Acting as an entailment detection instrument, determine if the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "As a tool for determining entailment relationships, review the two statements and categorize their connection as either 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "While performing entailment analysis, classify the relationship between the provided sentences as 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "In the capacity of an entailment assessment system, indicate if the link between the following sentences is 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "Working as an entailment classifier, identify whether the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment' or 'not_entailment'. Respond with 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",
        "In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment':\nQuestion: {content}\nAnswer:",       
    ],

    'mnli': [
        "In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction':\nQuestion: {content}\nAnswer:",
        "As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction':\nQuestion: {content}\nAnswer:",
        "Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment', 'neutral', or 'contradiction':\nQuestion: {content}\nAnswer:",
        "Acting as an entailment detection instrument, determine if the given pair of sentences demonstrates entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction':\nQuestion: {content}\nAnswer:",
        "As a tool for determining entailment relationships, review the two statements and categorize their connection as either 'entailment', 'neutral', or 'contradiction':\nQuestion: {content}\nAnswer:",
        "While performing entailment analysis, classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction':\nQuestion: {content}\nAnswer:",
        "In the capacity of an entailment assessment system, indicate if the link between the following sentences is 'entailment', 'neutral', or 'contradiction':\nQuestion: {content}\nAnswer:",
        "Working as an entailment classifier, identify whether the given pair of sentences displays entailment, neutral, or contradiction. Respond with 'entailment', 'neutral', or 'contradiction':\nQuestion: {content}\nAnswer:",
        "As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment', 'neutral', or 'contradiction':\nQuestion: {content}\nAnswer:",
        "In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction':\nQuestion: {content}\nAnswer:",
    ],

    'cola': [
        "In your role as a grammar check tool, assess the following sentence and classify it as 'acceptable' if it is grammatically correct or 'unacceptable' if it is incorrect:\nQuestion: {content}\nAnswer:",
        "As a grammar identification system, examine the provided sentence and respond with 'acceptable' for grammatically correct sentences or 'unacceptable' for incorrect ones:\nQuestion: {content}\nAnswer:",
        "Functioning as a grammar evaluation tool, analyze the given sentence and decide if it is grammatically correct, responding with 'acceptable' or 'unacceptable':\nQuestion: {content}\nAnswer:",
        "Acting as a grammar detection instrument, determine if the provided sentence is grammatically sound, answering with 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar:\nQuestion: {content}\nAnswer:",
        "As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable':\nQuestion: {content}\nAnswer:",
        "While performing grammar analysis, classify the grammar of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar:\nQuestion: {content}\nAnswer:",
        "In the capacity of a grammar assessment system, indicate if the structure of the provided sentence is grammatically correct, responding with 'acceptable' or 'unacceptable':\nQuestion: {content}\nAnswer:",
        "Working as a grammar classifier, identify whether the given sentence has correct grammar, and respond with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones:\nQuestion: {content}\nAnswer:",
        "As an instrument for grammar evaluation, consider the sentence and determine if its grammar is correct, responding with 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar:\nQuestion: {content}\nAnswer:",
        "In the role of a syntax analyzer, examine the grammar of the provided sentence and decide if it is correct, answering with 'acceptable' for grammatically correct sentences or 'unacceptable' for incorrect ones:\nQuestion: {content}\nAnswer:",
    ],

    'qqp': [
        "In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "As a question equivalence detection system, examine the provided questions and respond with 'equivalent' if they are the same in meaning, or 'not_equivalent' if they are different. \nQuestion: {content}\nAnswer:",
        "Functioning as a question similarity evaluation tool, analyze the given questions and decide if they share the same meaning, responding with 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "Acting as a question equivalence instrument, determine if the provided questions are equivalent in meaning, answering with 'equivalent' for similar questions or 'not_equivalent' for dissimilar ones. \nQuestion: {content}\nAnswer:",
        "As a tool for determining question equivalence, review the questions and categorize their similarity as either 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "While performing question comparison analysis, classify the similarity of the following questions as 'equivalent' for equivalent questions or 'not_equivalent' for different questions. \nQuestion: {content}\nAnswer:",
        "In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "Working as a question classifier, identify whether the given questions share the same meaning, and respond with 'equivalent' for equivalent questions or 'not_equivalent' for different ones. \nQuestion: {content}\nAnswer:",
        "As an instrument for question comparison evaluation, consider the questions and determine if their meaning is the same, responding with 'equivalent' for similar questions or 'not_equivalent' for different questions. \nQuestion: {content}\nAnswer:",
        "In the role of a question similarity analyzer, examine the meaning of the provided questions and decide if they are equivalent, answering with 'equivalent' for equivalent questions or 'not_equivalent' for different questions. \nQuestion: {content}\nAnswer:",
    ],

    # 86.95, 88.65, 88.85, 87.90, 83.10, 74.45, 88.55, 88.65, 88.85, 83.80
    'qnli': [
        "As a language expert, assess if the given context entails the answer to the question and respond with 'entailment' or 'not_entailment'. \nQuestion: {content}\nAnswer:",
        "In your role as a semantic evaluator, determine if the provided context justifies the answer to the question and answer with 'entailment' or 'not_entailment'. \nQuestion: {content}\nAnswer:",
        "As a textual analyst, examine if the given context logically implies the answer to the question and indicate your decision with 'entailment' or 'not_entailment'. \nQuestion: {content}\nAnswer:",
        "As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment'. \nQuestion: {content}\nAnswer:",
        "In the capacity of a language specialist, decide if the context presented contains enough information to infer the answer to the question and respond with 'entailment' or 'not_entailment'. \nQuestion: {content}\nAnswer:",
        "As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment'. \nQuestion: {content}\nAnswer:",
        "In your role as a linguistic investigator, determine if the context given entails the answer to the question and provide your conclusion with 'entailment' or 'not_entailment'. \nQuestion: {content}\nAnswer:",
        "As a semantic interpreter, assess whether the provided context supports the answer to the given question and answer with 'entailment' or 'not_entailment'. \nQuestion: {content}\nAnswer:",
        "In the capacity of a language evaluator, examine if the given context justifies the answer to the question and indicate your assessment with 'entailment' or 'not_entailment'. \nQuestion: {content}\nAnswer:",
        "As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment'. \nQuestion: {content}\nAnswer:",    
    ],


    # 82.60, 77.94, 80.39, 81.13, 80.64, 75.74, 81.62, 81.13, 79.66, 82.60
    'mrpc': [
        "As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "In your capacity as a language analyst, assess the following sentences and classify their similarity as 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "As a sentence similarity evaluator, analyze the provided sentences and indicate if their meanings are 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "In the role of a textual comparison specialist, examine the given sentences and decide if they share the same meaning, responding with 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "As a linguistic comparator, review the following pair of sentences and determine their semantic equivalence by choosing 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "In your capacity as a semantic assessment tool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "As a language comparison expert, examine the given pair of sentences and decide if their meanings align, answering with 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "In the role of a sentence comparison analyst, assess the provided sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "As a textual similarity evaluator, analyze the following pair of sentences and determine if they are semantically 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:",
        "In your capacity as a semantic comparison tool, examine the given sentences and decide if their meanings are identical, responding with 'equivalent' or 'not_equivalent'. \nQuestion: {content}\nAnswer:", 
    ],
}