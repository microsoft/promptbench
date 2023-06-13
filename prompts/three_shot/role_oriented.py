# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
This file contains the prompt sets for the fewshot role-oriented prompts.
"""

ROLE_ORIENTED_PROMPT_SET = {
    'math': [
        "As a mathematics instructor, calculate the answer to the following problem related to {}. ",
        "Pretend you are a math teacher and solve this mathematical question concerning {}. ",
        "Imagine being a math mentor and determine the solution to the following problem with {}. ",
        "In the position of a mathematics coach, figure out the answer to this math challenge involving {}. ",
        "Act as a math expert and compute the result of the following mathematical task about {}. ",
        "As a mathematics consultant, resolve the following problem associated with {}. ",
        "Taking on the role of a math specialist, work out the solution for this mathematical question featuring {}. ",
        "Embodying a mathematics advisor, find the answer to the following math problem with {}. ",
        "As a math guru, evaluate the following mathematical task regarding {}. ",
        "In the shoes of a mathematics master, obtain the result for this math question that includes {}. ",
    ],

    'iwslt': [
        "Acting as a professional translator, translate the provided sentence from {} to {}. ",
        "As a skilled linguist, please convert the following sentence from {} to {}. ",
        "Assuming the role of an expert language translator, translate the given text from {} to {}. ",
        "In the capacity of a proficient translator, please change the following sentence from {} to {}. ",
        "As a language specialist, accurately translate the provided sentence from {} to {}. ",
        "Taking on the role of a certified translator, perform a translation of the given sentence from {} to {}. ",
        "While acting as an experienced language expert, translate the following text from {} to {}. ",
        "As a qualified translator, convert the given sentence from its original {} language to the target language {}. ",
        "Assuming the responsibilities of a professional translator, translate the subsequent text passage from {} to {}. ",
        "In the role of a language expert, perform a machine translation for the provided sentence, changing it from {} to {}. ",
    ],

    'un_multi': [
        "Acting as a professional translator, translate the provided sentence from {} to {}. ",
        "As a skilled linguist, please convert the following sentence from {} to {}. ",
        "Assuming the role of an expert language translator, translate the given text from {} to {}. ",
        "In the capacity of a proficient translator, please change the following sentence from {} to {}. ",
        "As a language specialist, accurately translate the provided sentence from {} to {}. ",
        "Taking on the role of a certified translator, perform a translation of the given sentence from {} to {}. ",
        "While acting as an experienced language expert, translate the following text from {} to {}. ",
        "As a qualified translator, convert the given sentence from its original {} language to the target language {}. ",
        "Assuming the responsibilities of a professional translator, translate the subsequent text passage from {} to {}. ",
        "In the role of a language expert, perform a machine translation for the provided sentence, changing it from {} to {}. ",
    ],

    'squad_v2': [
        "As a well-informed specialist familiar with the context, provide an answer to the question. If the context doesn't contain an answer, reply with 'unanswerable'.",
        "Drawing upon your expertise in the context, determine the most suitable answer. If an answer isn't available, state 'unanswerable'.",
        "As a subject matter expert, extract the correct answer from the context. If an answer is not present, indicate 'unanswerable'.",
        "Using your knowledge of the context, identify the best answer to the question. If the context doesn't provide an answer, write 'unanswerable'.",
        "As an authority on the context, locate the most accurate answer. If the context doesn't contain the answer, mention 'unanswerable'.",
        "Being well-versed in the context, please derive the most fitting answer. If there isn't an answer in the context, use 'unanswerable'.",
        "As an expert with a deep understanding of the context, find the best answer. If the context doesn't include an answer, say 'unanswerable'.",
        "Drawing on your expertise in the context, provide the most precise answer. If the answer is not in the context, respond with 'unanswerable'.",
        "As a proficient expert in the given context, search for the most relevant answer. If the answer cannot be found, respond by saying 'unanswerable'.",
        "With your extensive knowledge of the context, answer the question accurately. If the context doesn't contain the answer, reply with 'unanswerable'."
    ],

    'mmlu': [
        "As an expert in {}, respond to the following multiple-choice question by selecting 'A', 'B', 'C', or 'D'.",
        "Given your proficiency in {}, please answer the subsequent multiple-choice question with 'A', 'B', 'C', or 'D'.",
        "With your knowledge of {}, tackle the following multiple-choice question by choosing 'A', 'B', 'C', or 'D'.",
        "As someone well-versed in {}, please address the multiple-choice question below by selecting 'A', 'B', 'C', or 'D'.",
        "Utilizing your expertise in {}, answer the following multiple-choice question by picking 'A', 'B', 'C', or 'D'.",
        "As a knowledgeable individual in {}, provide your response to the multiple-choice question by choosing 'A', 'B', 'C', or 'D'.",
        "With your understanding of {}, kindly answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D'.",
        "As a skilled person in the field of {}, please respond to the multiple-choice question by choosing 'A', 'B', 'C', or 'D'.",
        "Considering your familiarity with {}, attend to the following multiple-choice question by picking 'A', 'B', 'C', or 'D'.",
        "Drawing upon your mastery of {}, please answer the multiple-choice question by selecting the correct option from 'A', 'B', 'C', or 'D'."
    ],

    'sst2': [
        "As a sentiment classifier, determine whether the following text is 'positive' or 'negative'. ",
        "In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement. ",
        "Acting as a sentiment evaluator, identify if the given sentence is 'positive' or 'negative'. ",
        "As an emotion detector, determine if the provided passage conveys a 'positive' or 'negative' sentiment. ",
        "Working as a sentiment analyzer, please indicate if the following text is 'positive' or 'negative'. ",
        "In the capacity of a sentiment classifier, decide whether the given quote is 'positive' or 'negative'. ",
        "Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative'. ",
        "Functioning as a sentiment identification tool, assess if the following expression is 'positive' or 'negative'. ",
        "Serving as a sentiment evaluation model, determine if the given statement is 'positive' or 'negative'. ",
        "Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative'. ",
    ],

    'wnli': [
        "In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'. ",
        "As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'. ",
        "Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'. ",
        "Acting as an entailment detection instrument, determine if the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'. ",
        "As a tool for determining entailment relationships, review the two statements and categorize their connection as either 'entailment' or 'not_entailment'. ",
        "While performing entailment analysis, classify the relationship between the provided sentences as 'entailment' or 'not_entailment'. ",
        "In the capacity of an entailment assessment system, indicate if the link between the following sentences is 'entailment' or 'not_entailment'. ",
        "Working as an entailment classifier, identify whether the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'. ",
        "As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment' or 'not_entailment'. Respond with 'entailment' or 'not_entailment'. ",
        "In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'. ",   
    ],

    'rte': [
        "In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'. ",
        "As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'. ",
        "Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'. ",
        "Acting as an entailment detection instrument, determine if the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'. ",
        "As a tool for determining entailment relationships, review the two statements and categorize their connection as either 'entailment' or 'not_entailment'. ",
        "While performing entailment analysis, classify the relationship between the provided sentences as 'entailment' or 'not_entailment'. ",
        "In the capacity of an entailment assessment system, indicate if the link between the following sentences is 'entailment' or 'not_entailment'. ",
        "Working as an entailment classifier, identify whether the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'. ",
        "As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment' or 'not_entailment'. Respond with 'entailment' or 'not_entailment'. ",
        "In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'. ",       
    ],

    'mnli': [
        "In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'. ",
        "As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction'. ",
        "Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment', 'neutral', or 'contradiction'. ",
        "Acting as an entailment detection instrument, determine if the given pair of sentences demonstrates entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'. ",
        "As a tool for determining entailment relationships, review the two statements and categorize their connection as either 'entailment', 'neutral', or 'contradiction'. ",
        "While performing entailment analysis, classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction'. ",
        "In the capacity of an entailment assessment system, indicate if the link between the following sentences is 'entailment', 'neutral', or 'contradiction'. ",
        "Working as an entailment classifier, identify whether the given pair of sentences displays entailment, neutral, or contradiction. Respond with 'entailment', 'neutral', or 'contradiction'. ",
        "As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment', 'neutral', or 'contradiction'. ",
        "In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'. ",
    ],

    'cola': [
        "In your role as a grammar check tool, assess the following sentence and classify it as 'acceptable' if it is grammatically correct or 'unacceptable' if it is incorrect. ",
        "As a grammar identification system, examine the provided sentence and respond with 'acceptable' for grammatically correct sentences or 'unacceptable' for incorrect ones. ",
        "Functioning as a grammar evaluation tool, analyze the given sentence and decide if it is grammatically correct, responding with 'acceptable' or 'unacceptable'. ",
        "Acting as a grammar detection instrument, determine if the provided sentence is grammatically sound, answering with 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar. ",
        "As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable'. ",
        "While performing grammar analysis, classify the grammar of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar. ",
        "In the capacity of a grammar assessment system, indicate if the structure of the provided sentence is grammatically correct, responding with 'acceptable' or 'unacceptable'. ",
        "Working as a grammar classifier, identify whether the given sentence has correct grammar, and respond with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones. ",
        "As an instrument for grammar evaluation, consider the sentence and determine if its grammar is correct, responding with 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar. ",
        "In the role of a syntax analyzer, examine the grammar of the provided sentence and decide if it is correct, answering with 'acceptable' for grammatically correct sentences or 'unacceptable' for incorrect ones. ",
    ],

    'qqp': [
        "In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent'. ",
        "As a question equivalence detection system, examine the provided questions and respond with 'equivalent' if they are the same in meaning, or 'not_equivalent' if they are different. ",
        "Functioning as a question similarity evaluation tool, analyze the given questions and decide if they share the same meaning, responding with 'equivalent' or 'not_equivalent'. ",
        "Acting as a question equivalence instrument, determine if the provided questions are equivalent in meaning, answering with 'equivalent' for similar questions or 'not_equivalent' for dissimilar ones. ",
        "As a tool for determining question equivalence, review the questions and categorize their similarity as either 'equivalent' or 'not_equivalent'. ",
        "While performing question comparison analysis, classify the similarity of the following questions as 'equivalent' for equivalent questions or 'not_equivalent' for different questions. ",
        "In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent'. ",
        "Working as a question classifier, identify whether the given questions share the same meaning, and respond with 'equivalent' for equivalent questions or 'not_equivalent' for different ones. ",
        "As an instrument for question comparison evaluation, consider the questions and determine if their meaning is the same, responding with 'equivalent' for similar questions or 'not_equivalent' for different questions. ",
        "In the role of a question similarity analyzer, examine the meaning of the provided questions and decide if they are equivalent, answering with 'equivalent' for equivalent questions or 'not_equivalent' for different questions. ",
    ],

    'qnli': [
        "As a language expert, assess if the given context entails the answer to the question and respond with 'entailment' or 'not_entailment'. ",
        "In your role as a semantic evaluator, determine if the provided context justifies the answer to the question and answer with 'entailment' or 'not_entailment'. ",
        "As a textual analyst, examine if the given context logically implies the answer to the question and indicate your decision with 'entailment' or 'not_entailment'. ",
        "As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment'. ",
        "In the capacity of a language specialist, decide if the context presented contains enough information to infer the answer to the question and respond with 'entailment' or 'not_entailment'. ",
        "As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment'. ",
        "In your role as a linguistic investigator, determine if the context given entails the answer to the question and provide your conclusion with 'entailment' or 'not_entailment'. ",
        "As a semantic interpreter, assess whether the provided context supports the answer to the given question and answer with 'entailment' or 'not_entailment'. ",
        "In the capacity of a language evaluator, examine if the given context justifies the answer to the question and indicate your assessment with 'entailment' or 'not_entailment'. ",
        "As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment'. ",    
    ],


    'mrpc': [
        "As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent'. ",
        "In your capacity as a language analyst, assess the following sentences and classify their similarity as 'equivalent' or 'not_equivalent'. ",
        "As a sentence similarity evaluator, analyze the provided sentences and indicate if their meanings are 'equivalent' or 'not_equivalent'. ",
        "In the role of a textual comparison specialist, examine the given sentences and decide if they share the same meaning, responding with 'equivalent' or 'not_equivalent'. ",
        "As a linguistic comparator, review the following pair of sentences and determine their semantic equivalence by choosing 'equivalent' or 'not_equivalent'. ",
        "In your capacity as a semantic assessment tool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent'. ",
        "As a language comparison expert, examine the given pair of sentences and decide if their meanings align, answering with 'equivalent' or 'not_equivalent'. ",
        "In the role of a sentence comparison analyst, assess the provided sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent'. ",
        "As a textual similarity evaluator, analyze the following pair of sentences and determine if they are semantically 'equivalent' or 'not_equivalent'. ",
        "In your capacity as a semantic comparison tool, examine the given sentences and decide if their meanings are identical, responding with 'equivalent' or 'not_equivalent'. ", 
    ],
}