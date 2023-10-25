# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
This file contains the prompt sets for the zeroshot task-oriented prompts.
"""

TASK_ORIENTED_PROMPT_SET = {
    'valid_parentheses': [
        "Judge if the arrangement of brackets in the provided expression follows proper rules for validity. Respond Valid if the brakets are matched, Invalid otherwise.",
        "Decide whether the sequence of parentheses presented is correctly balanced. Respond Valid if the brakets are matched, Invalid otherwise.",
        "Evaluate the correctness of the given parenthesis configuration. Respond Valid if the brakets are matched, Invalid otherwise.",
        "Analyze the order of brackets in the expression to determine if it is valid. Respond Valid if the brakets are matched, Invalid otherwise.",
        "Examine the organization of parentheses in the given string to verify its validity. Respond Valid if the brakets are matched, Invalid otherwise.",
        "Assess whether the arrangement of brackets follows the necessary rules for a valid expression. Respond Valid if the brakets are matched, Invalid otherwise.",
        "Check if the presented combination of parentheses conforms to the requirements of valid syntax. Respond Valid if the brakets are matched, Invalid otherwise.",
        "Verify whether the provided expression demonstrates appropriate use of parentheses. Respond Valid if the brakets are matched, Invalid otherwise.",
        "Evaluate if the sequence of brackets is structured properly and is therefore valid. Respond Valid if the brakets are matched, Invalid otherwise.",
        "Determine whether the given expression displays a correct arrangement of parentheses. Respond Valid if the brakets are matched, Invalid otherwise.",
    ],
    
    'bool_logic': [
        "Evaluate the given boolean expression and provide its truth value. Respond True if it is, False otherwise.",
        "Simplify the provided boolean expression. Respond True if it is, False otherwise.",
        "Determine if the given combination of boolean values yields a True or False result. Respond True if it is, False otherwise.",
        "Assess the outcome of the complex boolean expression presented. Respond True if it is, False otherwise.",
        "Calculate the provided boolean expression. Respond True if it is, False otherwise.",
        "Evaluate the boolean expression by following the correct order of operator precedence. Respond True if it is, False otherwise.",
        "Analyze the nested boolean expression and ascertain its truth value. Respond True if it is, False otherwise.",
        "Calculate the result of the mixed boolean expression with various logical operators. Respond True if it is, False otherwise.",
        "simplify the given boolean expression. Respond True if it is, False otherwise.",
        "Indicate whether the boolean expression provided is True or False. Respond True if it is, False otherwise.",        
    ],
    
    'math': [
        "Solve the following math question about {}:",
        "Determine the solution to this mathematical problem related to {}:",
        "Calculate the answer to the following math query about {}:",
        "Find the solution for this mathematical challenge with {}:",
        "Compute the result of this math task concerning {}:",
        "Resolve the following mathematical question associated with {}:",
        "Work out the answer to this math problem featuring {}:",
        "Figure out the solution for the following mathematical task with {}:",
        "Obtain the result for this math question regarding {}:",
        "Evaluate the following mathematical problem that includes {}:",
    ],

    'iwslt': [
        "Translate the provided sentence from {} to {} while maintaining the original meaning and context:",
        "Convert the following sentence from its original {} language to the target language {}:",
        "Given the sentence below, perform a machine translation from {} to {}:",
        "Translate the subsequent sentence from its source language {} into the desired language {}:",
        "Accurately translate the sentence from {} to {}, ensuring the meaning remains intact:",
        "Please perform a translation of the given sentence, converting it from {} to {}:",
        "Translate the following text from the source language {} to the target language {}:",
        "Using machine translation, convert the given sentence from {} into the {} language:",
        "Translate the subsequent text passage from its original {} language to the {} language:",
        "Perform a machine translation for the provided sentence, changing it from {} to {}:",
    ],

    'un_multi': [
        "Translate the provided sentence from {} to {} while maintaining the original meaning and context:",
        "Convert the following sentence from its original {} language to the target language {}:",
        "Given the sentence below, perform a machine translation from {} to {}:",
        "Translate the subsequent sentence from its source language {} into the desired language {}:",
        "Accurately translate the sentence from {} to {}, ensuring the meaning remains intact:",
        "Please perform a translation of the given sentence, converting it from {} to {}:",
        "Translate the following text from the source language {} to the target language {}:",
        "Using machine translation, convert the given sentence from {} into the {} language:",
        "Translate the subsequent text passage from its original {} language to the {} language:",
        "Perform a machine translation for the provided sentence, changing it from {} to {}:",
    ],

    'squad_v2': [
        "Based on the given context, provide the best possible answer. If there's no answer available in the context, respond with 'unanswerable'.",
        "Identify the most relevant answer from the context. If it's not possible to find an answer, respond with 'unanswerable'.",
        "Find the correct answer in the context provided. If an answer cannot be found, please respond with 'unanswerable'.",
        "Please extract the most appropriate answer from the context. If an answer is not present, indicate 'unanswerable'.",
        "Using the context, determine the most suitable answer. If the context doesn't contain the answer, respond with 'unanswerable'.",
        "Locate the most accurate answer within the context. If the context doesn't provide an answer, respond with 'unanswerable'.",
        "Please derive the most fitting answer from the context. If there isn't an answer in the context, respond with 'unanswerable'.",
        "Discover the best answer based on the context. If the context doesn't include an answer, respond with 'unanswerable'.",
        "From the context, provide the most precise answer. If the answer is not in the context, respond with 'unanswerable'.",
        "Search the context for the most relevant answer. If the answer cannot be found, respond with 'unanswerable'.",
    ],

# I want you to act as a prompt generator for a machine translation task.
# Here is an example : "Solve the following math question about {}"
# Please generate 10 similar prompts. the prompt is used for deepmind mathmatic dataset.
# For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.
    
    'mmlu': [
        "Answer the following multiple-choice question about {} by selecting the correct option: 'A', 'B', 'C', or 'D'. ",
        "For the multiple-choice question related to {}, please choose the most accurate answer from 'A', 'B', 'C', or 'D'. ",
        "Below are multiple-choice question concerning {}. Indicate your response with 'A', 'B', 'C', or 'D'. ",
        "Please respond to the multiple-choice question about {} by selecting the appropriate answer: 'A', 'B', 'C', or 'D'. ",
        "Regarding the following multiple-choice question on {}, pick the correct answer from the options 'A', 'B', 'C', or 'D'. ",
        "Evaluate the multiple-choice question about {} and select the most fitting response from 'A', 'B', 'C', or 'D'. ",
        "Examine the following question based on {} and choose the correct response from 'A', 'B', 'C', or 'D'. ",
        "For each multiple-choice question about {}, identify the correct answer by selecting 'A', 'B', 'C', or 'D'. ",
        "In relation to the multiple-choice question on {}, please provide the accurate answer by choosing 'A', 'B', 'C', or 'D'. ",
        "Answer the subsequent multiple-choice question about {} by picking the right option among 'A', 'B', 'C', or 'D'. "
    ],

    'sst2': [
        "Analyze the tone of this statement and respond with either 'positive' or 'negative': ",
        "Evaluate the sentiment of the given text and classify it as 'positive' or 'negative': ",
        "Please identify the emotional tone of this passage: 'positive' or 'negative'? ",
        "Assess the mood of the following quote and determine if it's 'positive' or 'negative': ",
        "Determine the overall sentiment of this sentence, categorizing it as 'positive' or 'negative': ",
        "Read the provided excerpt and choose between 'positive' and 'negative' to describe its sentiment: ",
        "Considering the given phrase, would you say it carries a 'positive' or 'negative' connotation? ",
        "After examining the following expression, label its emotion as either 'positive' or 'negative': ",
        "Review this statement and decide whether it has a 'positive' or 'negative' sentiment: ",
        "Given the context of this text, indicate if the emotion conveyed is 'positive' or 'negative': ",
    ],

    'wnli': [
        'Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word. ',
        "Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.",
        "Examine the pair of sentences and determine if they exhibit entailment or not_entailment. Answer with either 'entailment' or 'not_entailment'.",
        "Assess the connection between the following sentences and classify it as 'entailment' or 'not_entailment'.",
        "Analyze the two provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.",
        "Identify whether the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.",
        "Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.",
        "Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.",
        "Indicate if the connection between the following sentences is 'entailment' or 'not_entailment'.",
        "Determine if the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'.",
        "Considering the two sentences, identify if their relationship is 'entailment' or 'not_entailment'.",
    ],

    'rte': [
        'Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word. ',
        "Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.",
        "Examine the pair of sentences and determine if they exhibit entailment or not_entailment. Answer with either 'entailment' or 'not_entailment'.",
        "Assess the connection between the following sentences and classify it as 'entailment' or 'not_entailment'.",
        "Analyze the two provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.",
        "Identify whether the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.",
        "Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.",
        "Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.",
        "Indicate if the connection between the following sentences is 'entailment' or 'not_entailment'.",
        "Determine if the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'.",
        "Considering the two sentences, identify if their relationship is 'entailment' or 'not_entailment'.",    
    ],

    'mnli': [
        "Does the relationship between the given sentences represent entailment, neutral, or contradiction? Respond with 'entailment', 'neutral', or 'contradiction':",
        "Examine the pair of sentences and determine if they exhibit entailment, neutral, or contradiction. Answer with either 'entailment', 'neutral', or 'contradiction':",
        "Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction':",
        "Analyze the two provided sentences and decide if their relationship is 'entailment', 'neutral', or 'contradiction':",
        "Identify whether the given pair of sentences demonstrates entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction':",
        "Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction':",
        "Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction':",
        "Indicate if the connection between the following sentences is 'entailment', 'neutral', or 'contradiction':",
        "Determine if the given pair of sentences displays entailment, neutral, or contradiction. Respond with 'entailment', 'neutral', or 'contradiction':",
        "Considering the two sentences, identify if their relationship is 'entailment', 'neutral', or 'contradiction':",
    ],

    'cola': [
        "Assess the following sentence and determine if it is grammatically correct. Respond with 'Acceptable' or 'Unacceptable':",
        "Examine the given sentence and decide if it is grammatically sound. Answer with either 'Acceptable' or 'Unacceptable':",
        "Analyze the provided sentence and classify its grammatical correctness as 'Acceptable' or 'Unacceptable':",
        "Review the sentence below and identify whether its grammar is 'Acceptable' or 'Unacceptable':",
        "Determine if the grammar of the given sentence is 'Acceptable' or 'Unacceptable':",
        "Please evaluate the grammatical structure of the provided sentence and answer with 'Acceptable' or 'Unacceptable':",
        "Check the grammar of the following sentence and indicate if it is 'Acceptable' or 'Unacceptable':",
        "Is the provided sentence grammatically correct? Respond with 'Acceptable' or 'Unacceptable':",
        "Examine the sentence and decide if its grammar is 'Acceptable' or 'Unacceptable':",
        "Assess the grammatical structure of the given sentence and classify it as 'Acceptable' or 'Unacceptable':",
    ],


    'qqp': [
        'Are the following two questions equivalent or not? Answer me with "equivalent" or "not_equivalent". ',
        "Determine if the given pair of statements can be considered the same by responding with 'equivalent' or 'not_equivalent'. ",
        "Do these two sentences convey the same meaning? Indicate with 'equivalent' or 'not_equivalent'. ",
        "Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent'. ",
        "Are the meanings of these two phrases the same? Reply with 'equivalent' or 'not_equivalent'. ",
        "Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent'. ",
        "Can these two statements be considered equal in meaning? Answer with 'equivalent' or 'not_equivalent'. ",
        "Please indicate if the following pair of sentences share the same meaning by responding with 'equivalent' or 'not_equivalent'. ",
        "Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent'. ",
        "Evaluate whether these two phrases have identical meanings and respond with 'equivalent' or 'not_equivalent'. ",
        "Analyze if the given set of sentences have the same connotation by answering with 'equivalent' or 'not_equivalent'. ",
    ],

    # 81.75, 88.05, 61.70, 87.25, 89.75, 84.95, 87.95, 81.40, 84.40, 82.95
    'qnli': [
        "Given the question and context provided, determine if the answer can be inferred by choosing 'entailment' or 'not_entailment'. ",
        "Based on the provided context and question, decide if the information supports the answer by responding with 'entailment' or 'not_entailment'. ",
        "Please assess if the answer to the question can be derived from the given context by selecting 'entailment' or 'not_entailment'. ",
        "Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment'. ",
        "Evaluate whether the given context supports the answer to the question by responding with 'entailment' or 'not_entailment'. ",
        "Examine the context and question, and determine if the context logically implies the answer by selecting 'entailment' or 'not_entailment'. ",
        "Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment'. ",
        "Consider the context and question, and indicate if the answer can be logically deduced from the context by responding with 'entailment' or 'not_entailment'. ",
        "Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment'. ",
        "Assess if the answer to the question can be logically concluded from the provided context by choosing 'entailment' or 'not_entailment'. ",
    ],

    # 82.11, 81.86, 80.64, 81.62, 82.11, 82.35, 80.64, 80.88, 81.86, 80.88
    'mrpc': [
        "Do these two sentences have the same underlying meaning? Respond with 'equivalent' or 'not_equivalent'. ",
        "Are the meanings of the following pair of sentences the same? Answer with 'equivalent' or 'not_equivalent'. ",
        "Can the given sentences be considered semantically identical? Please reply with 'equivalent' or 'not_equivalent'. ",
        "Evaluate whether the two provided sentences convey the same meaning by answering 'equivalent' or 'not_equivalent'. ",
        "Do the meanings of these two statements align? Indicate your answer with 'equivalent' or 'not_equivalent'. ",
        "Compare the following sentences and determine if they share the same semantic meaning by responding with 'equivalent' or 'not_equivalent'. ",
        "Assess if the two given sentences have equivalent meanings by selecting 'equivalent' or 'not_equivalent'. ",
        "Please analyze the provided sentences and indicate if their meanings are the same by choosing 'equivalent' or 'not_equivalent'. ",
        "Examine the pair of sentences and decide if their meanings are identical by answering with 'equivalent' or 'not_equivalent'. ",
        "Determine if the meanings of the following sentences are semantically equivalent by responding with 'equivalent' or 'not_equivalent'. ",
    ],

}
