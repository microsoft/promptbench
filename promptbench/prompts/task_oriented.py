# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
This file contains the prompt sets for the zeroshot task-oriented prompts.
"""

TASK_ORIENTED_PROMPTS = {
    'valid_parentheses': [
        "Judge if the arrangement of brackets in the provided expression follows proper rules for validity. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion:{content}\nAnswer:",
        "Decide whether the sequence of parentheses presented is correctly balanced. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion:{content}\nAnswer:",
        "Evaluate the correctness of the given parenthesis configuration. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion:{content}\nAnswer:",
        "Analyze the order of brackets in the expression to determine if it is valid. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion:{content}\nAnswer:",
        "Examine the organization of parentheses in the given string to verify its validity. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion:{content}\nAnswer:",
        "Assess whether the arrangement of brackets follows the necessary rules for a valid expression. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion:{content}\nAnswer:",
        "Check if the presented combination of parentheses conforms to the requirements of valid syntax. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion:{content}\nAnswer:",
        "Verify whether the provided expression demonstrates appropriate use of parentheses. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion:{content}\nAnswer:",
        "Evaluate if the sequence of brackets is structured properly and is therefore valid. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion:{content}\nAnswer:",
        "Determine whether the given expression displays a correct arrangement of parentheses. Respond Valid if the brakets are matched, Invalid otherwise.\nQuestion:{content}\nAnswer:",
    ],
    
    'bool_logic': [
        "Evaluate the given boolean expression and provide its truth value. Respond True if it is, False otherwise.\nQuestion:{content}\nAnswer:",
        "Simplify the provided boolean expression. Respond True if it is, False otherwise.\nQuestion:{content}\nAnswer:",
        "Determine if the given combination of boolean values yields a True or False result. Respond True if it is, False otherwise.\nQuestion:{content}\nAnswer:",
        "Assess the outcome of the complex boolean expression presented. Respond True if it is, False otherwise.\nQuestion:{content}\nAnswer:",
        "Calculate the provided boolean expression. Respond True if it is, False otherwise.\nQuestion:{content}\nAnswer:",
        "Evaluate the boolean expression by following the correct order of operator precedence. Respond True if it is, False otherwise.\nQuestion:{content}\nAnswer:",
        "Analyze the nested boolean expression and ascertain its truth value. Respond True if it is, False otherwise.\nQuestion:{content}\nAnswer:",
        "Calculate the result of the mixed boolean expression with various logical operators. Respond True if it is, False otherwise.\nQuestion:{content}\nAnswer:",
        "simplify the given boolean expression. Respond True if it is, False otherwise.\nQuestion:{content}\nAnswer:",
        "Indicate whether the boolean expression provided is True or False. Respond True if it is, False otherwise.\nQuestion:{content}\nAnswer:",        
    ],
    

    'math': [
        "Solve the following math question about {task}:\nQuestion:{content}\nAnswer:",
        "Determine the solution to this mathematical problem related to {task}:\nQuestion:{content}\nAnswer:",
        "Calculate the answer to the following math query about {task}:\nQuestion:{content}\nAnswer:",
        "Find the solution for this mathematical challenge with {task}:\nQuestion:{content}\nAnswer:",
        "Compute the result of this math task concerning {task}:\nQuestion:{content}\nAnswer:",
        "Resolve the following mathematical question associated with {task}:\nQuestion:{content}\nAnswer:",
        "Work out the answer to this math problem featuring {task}:\nQuestion:{content}\nAnswer:",
        "Figure out the solution for the following mathematical task with {task}:\nQuestion:{content}\nAnswer:",
        "Obtain the result for this math question regarding {task}:\nQuestion:{content}\nAnswer:",
        "Evaluate the following mathematical problem that includes {task}:\nQuestion:{content}\nAnswer:",
    ],

    'iwslt': [
        "Translate the provided sentence from {soruce_lang} to {} while maintaining the original meaning and context:\nQuestion:{content}\nAnswer:",
        "Convert the following sentence from its original {soruce_lang} language to the target language {target_lang}:\nQuestion:{content}\nAnswer:",
        "Given the sentence below, perform a machine translation from {soruce_lang} to {target_lang}:\nQuestion:{content}\nAnswer:",
        "Translate the subsequent sentence from its source language {soruce_lang} into the desired language {target_lang}:\nQuestion:{content}\nAnswer:",
        "Accurately translate the sentence from {soruce_lang} to {target_lang}, ensuring the meaning remains intact:\nQuestion:{content}\nAnswer:",
        "Please perform a translation of the given sentence, converting it from {soruce_lang} to {target_lang}:\nQuestion:{content}\nAnswer:",
        "Translate the following text from the source language {soruce_lang} to the target language {target_lang}:\nQuestion:{content}\nAnswer:",
        "Using machine translation, convert the given sentence from {soruce_lang} into the {target_lang} language:\nQuestion:{content}\nAnswer:",
        "Translate the subsequent text passage from its original {soruce_lang} language to the {target_lang} language:\nQuestion:{content}\nAnswer:",
        "Perform a machine translation for the provided sentence, changing it from {soruce_lang} to {target_lang}:\nQuestion:{content}\nAnswer:",
    ],

    'un_multi': [
        "Translate the provided sentence from {soruce_lang} to {} while maintaining the original meaning and context:\nQuestion:{content}\nAnswer:",
        "Convert the following sentence from its original {soruce_lang} language to the target language {target_lang}:\nQuestion:{content}\nAnswer:",
        "Given the sentence below, perform a machine translation from {soruce_lang} to {target_lang}:\nQuestion:{content}\nAnswer:",
        "Translate the subsequent sentence from its source language {soruce_lang} into the desired language {target_lang}:\nQuestion:{content}\nAnswer:",
        "Accurately translate the sentence from {soruce_lang} to {target_lang}, ensuring the meaning remains intact:\nQuestion:{content}\nAnswer:",
        "Please perform a translation of the given sentence, converting it from {soruce_lang} to {target_lang}:\nQuestion:{content}\nAnswer:",
        "Translate the following text from the source language {soruce_lang} to the target language {target_lang}:\nQuestion:{content}\nAnswer:",
        "Using machine translation, convert the given sentence from {soruce_lang} into the {target_lang} language:\nQuestion:{content}\nAnswer:",
        "Translate the subsequent text passage from its original {soruce_lang} language to the {target_lang} language:\nQuestion:{content}\nAnswer:",
        "Perform a machine translation for the provided sentence, changing it from {soruce_lang} to {target_lang}:\nQuestion:{content}\nAnswer:",
    ],

    'squad_v2': [
        "Based on the given context, provide the best possible answer. If there's no answer available in the context, respond with 'unanswerable'.\nQuestion:{content}\nAnswer:",
        "Identify the most relevant answer from the context. If it's not possible to find an answer, respond with 'unanswerable'.\nQuestion:{content}\nAnswer:",
        "Find the correct answer in the context provided. If an answer cannot be found, please respond with 'unanswerable'.\nQuestion:{content}\nAnswer:",
        "Please extract the most appropriate answer from the context. If an answer is not present, indicate 'unanswerable'.\nQuestion:{content}\nAnswer:",
        "Using the context, determine the most suitable answer. If the context doesn't contain the answer, respond with 'unanswerable'.\nQuestion:{content}\nAnswer:",
        "Locate the most accurate answer within the context. If the context doesn't provide an answer, respond with 'unanswerable'.\nQuestion:{content}\nAnswer:",
        "Please derive the most fitting answer from the context. If there isn't an answer in the context, respond with 'unanswerable'.\nQuestion:{content}\nAnswer:",
        "Discover the best answer based on the context. If the context doesn't include an answer, respond with 'unanswerable'.\nQuestion:{content}\nAnswer:",
        "From the context, provide the most precise answer. If the answer is not in the context, respond with 'unanswerable'.\nQuestion:{content}\nAnswer:",
        "Search the context for the most relevant answer. If the answer cannot be found, respond with 'unanswerable'.\nQuestion:{content}\nAnswer:",
    ],

# I want you to act as a prompt generator for a machine translation task.
# Here is an example : "Solve the following math question about {}"
# Please generate 10 similar prompts. the prompt is used for deepmind mathmatic dataset.
# For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.
    
    'mmlu': [
        "Answer the following multiple-choice question about {task} by selecting the correct option: 'A', 'B', 'C', or 'D'. \nQuestion:{content}\nAnswer:",
        "For the multiple-choice question related to {task}, please choose the most accurate answer from 'A', 'B', 'C', or 'D'. \nQuestion:{content}\nAnswer:",
        "Below are multiple-choice question concerning {task}. Indicate your response with 'A', 'B', 'C', or 'D'. \nQuestion:{content}\nAnswer:",
        "Please respond to the multiple-choice question about {task} by selecting the appropriate answer: 'A', 'B', 'C', or 'D'. \nQuestion:{content}\nAnswer:",
        "Regarding the following multiple-choice question on {task}, pick the correct answer from the options 'A', 'B', 'C', or 'D'. \nQuestion:{content}\nAnswer:",
        "Evaluate the multiple-choice question about {task} and select the most fitting response from 'A', 'B', 'C', or 'D'. \nQuestion:{content}\nAnswer:",
        "Examine the following question based on {task} and choose the correct response from 'A', 'B', 'C', or 'D'. \nQuestion:{content}\nAnswer:",
        "For each multiple-choice question about {task}, identify the correct answer by selecting 'A', 'B', 'C', or 'D'. \nQuestion:{content}\nAnswer:",
        "In relation to the multiple-choice question on {task}, please provide the accurate answer by choosing 'A', 'B', 'C', or 'D'. \nQuestion:{content}\nAnswer:",
        "Answer the subsequent multiple-choice question about {task} by picking the right option among 'A', 'B', 'C', or 'D'. "
    ],

    'sst2': [
        "Analyze the tone of this statement and respond with either 'positive' or 'negative': \nQuestion:{content}\nAnswer:",
        "Evaluate the sentiment of the given text and classify it as 'positive' or 'negative': \nQuestion:{content}\nAnswer:",
        "Please identify the emotional tone of this passage: 'positive' or 'negative'? \nQuestion:{content}\nAnswer:",
        "Assess the mood of the following quote and determine if it's 'positive' or 'negative': \nQuestion:{content}\nAnswer:",
        "Determine the overall sentiment of this sentence, categorizing it as 'positive' or 'negative': \nQuestion:{content}\nAnswer:",
        "Read the provided excerpt and choose between 'positive' and 'negative' to describe its sentiment: \nQuestion:{content}\nAnswer:",
        "Considering the given phrase, would you say it carries a 'positive' or 'negative' connotation? \nQuestion:{content}\nAnswer:",
        "After examining the following expression, label its emotion as either 'positive' or 'negative': \nQuestion:{content}\nAnswer:",
        "Review this statement and decide whether it has a 'positive' or 'negative' sentiment: \nQuestion:{content}\nAnswer:",
        "Given the context of this text, indicate if the emotion conveyed is 'positive' or 'negative': \nQuestion:{content}\nAnswer:",
    ],

    'wnli': [
        'Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment\nQuestion:{content}\nAnswer:", just one word. ',
        "Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Examine the pair of sentences and determine if they exhibit entailment or not_entailment. Answer with either 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Assess the connection between the following sentences and classify it as 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Analyze the two provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Identify whether the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Indicate if the connection between the following sentences is 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Determine if the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Considering the two sentences, identify if their relationship is 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
    ],

    'rte': [
        'Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment\nQuestion:{content}\nAnswer:", just one word. ',
        "Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Examine the pair of sentences and determine if they exhibit entailment or not_entailment. Answer with either 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Assess the connection between the following sentences and classify it as 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Analyze the two provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Identify whether the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Indicate if the connection between the following sentences is 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Determine if the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",
        "Considering the two sentences, identify if their relationship is 'entailment' or 'not_entailment'.\nQuestion:{content}\nAnswer:",    
    ],

    'mnli': [
        "Does the relationship between the given sentences represent entailment, neutral, or contradiction? Respond with 'entailment', 'neutral', or 'contradiction':\nQuestion:{content}\nAnswer:",
        "Examine the pair of sentences and determine if they exhibit entailment, neutral, or contradiction. Answer with either 'entailment', 'neutral', or 'contradiction':\nQuestion:{content}\nAnswer:",
        "Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction':\nQuestion:{content}\nAnswer:",
        "Analyze the two provided sentences and decide if their relationship is 'entailment', 'neutral', or 'contradiction':\nQuestion:{content}\nAnswer:",
        "Identify whether the given pair of sentences demonstrates entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction':\nQuestion:{content}\nAnswer:",
        "Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction':\nQuestion:{content}\nAnswer:",
        "Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction':\nQuestion:{content}\nAnswer:",
        "Indicate if the connection between the following sentences is 'entailment', 'neutral', or 'contradiction':\nQuestion:{content}\nAnswer:",
        "Determine if the given pair of sentences displays entailment, neutral, or contradiction. Respond with 'entailment', 'neutral', or 'contradiction':\nQuestion:{content}\nAnswer:",
        "Considering the two sentences, identify if their relationship is 'entailment', 'neutral', or 'contradiction':\nQuestion:{content}\nAnswer:",
    ],

    'cola': [
        "Assess the following sentence and determine if it is grammatically correct. Respond with 'Acceptable' or 'Unacceptable':\nQuestion:{content}\nAnswer:",
        "Examine the given sentence and decide if it is grammatically sound. Answer with either 'Acceptable' or 'Unacceptable':\nQuestion:{content}\nAnswer:",
        "Analyze the provided sentence and classify its grammatical correctness as 'Acceptable' or 'Unacceptable':\nQuestion:{content}\nAnswer:",
        "Review the sentence below and identify whether its grammar is 'Acceptable' or 'Unacceptable':\nQuestion:{content}\nAnswer:",
        "Determine if the grammar of the given sentence is 'Acceptable' or 'Unacceptable':\nQuestion:{content}\nAnswer:",
        "Please evaluate the grammatical structure of the provided sentence and answer with 'Acceptable' or 'Unacceptable':\nQuestion:{content}\nAnswer:",
        "Check the grammar of the following sentence and indicate if it is 'Acceptable' or 'Unacceptable':\nQuestion:{content}\nAnswer:",
        "Is the provided sentence grammatically correct? Respond with 'Acceptable' or 'Unacceptable':\nQuestion:{content}\nAnswer:",
        "Examine the sentence and decide if its grammar is 'Acceptable' or 'Unacceptable':\nQuestion:{content}\nAnswer:",
        "Assess the grammatical structure of the given sentence and classify it as 'Acceptable' or 'Unacceptable':\nQuestion:{content}\nAnswer:",
    ],


    'qqp': [
        'Are the following two questions equivalent or not? Answer me with "equivalent" or "not_equivalent". ',
        "Determine if the given pair of statements can be considered the same by responding with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Do these two sentences convey the same meaning? Indicate with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Are the meanings of these two phrases the same? Reply with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Can these two statements be considered equal in meaning? Answer with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Please indicate if the following pair of sentences share the same meaning by responding with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Evaluate whether these two phrases have identical meanings and respond with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Analyze if the given set of sentences have the same connotation by answering with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
    ],

    # 81.75, 88.05, 61.70, 87.25, 89.75, 84.95, 87.95, 81.40, 84.40, 82.95
    'qnli': [
        "Given the question and context provided, determine if the answer can be inferred by choosing 'entailment' or 'not_entailment'. \nQuestion:{content}\nAnswer:",
        "Based on the provided context and question, decide if the information supports the answer by responding with 'entailment' or 'not_entailment'. \nQuestion:{content}\nAnswer:",
        "Please assess if the answer to the question can be derived from the given context by selecting 'entailment' or 'not_entailment'. \nQuestion:{content}\nAnswer:",
        "Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment'. \nQuestion:{content}\nAnswer:",
        "Evaluate whether the given context supports the answer to the question by responding with 'entailment' or 'not_entailment'. \nQuestion:{content}\nAnswer:",
        "Examine the context and question, and determine if the context logically implies the answer by selecting 'entailment' or 'not_entailment'. \nQuestion:{content}\nAnswer:",
        "Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment'. \nQuestion:{content}\nAnswer:",
        "Consider the context and question, and indicate if the answer can be logically deduced from the context by responding with 'entailment' or 'not_entailment'. \nQuestion:{content}\nAnswer:",
        "Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment'. \nQuestion:{content}\nAnswer:",
        "Assess if the answer to the question can be logically concluded from the provided context by choosing 'entailment' or 'not_entailment'. \nQuestion:{content}\nAnswer:",
    ],

    # 82.11, 81.86, 80.64, 81.62, 82.11, 82.35, 80.64, 80.88, 81.86, 80.88
    'mrpc': [
        "Do these two sentences have the same underlying meaning? Respond with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Are the meanings of the following pair of sentences the same? Answer with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Can the given sentences be considered semantically identical? Please reply with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Evaluate whether the two provided sentences convey the same meaning by answering 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Do the meanings of these two statements align? Indicate your answer with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Compare the following sentences and determine if they share the same semantic meaning by responding with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Assess if the two given sentences have equivalent meanings by selecting 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Please analyze the provided sentences and indicate if their meanings are the same by choosing 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Examine the pair of sentences and decide if their meanings are identical by answering with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
        "Determine if the meanings of the following sentences are semantically equivalent by responding with 'equivalent' or 'not_equivalent'. \nQuestion:{content}\nAnswer:",
    ],

}
