# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

MPA_DEFAULT_PRMOPTS = {

    'mmlu': {

        'paraphraser_paraphrase_question': \
"""
I'm assessing a student's understanding beyond memorization. I have a question with multiple choices and a known correct answer. The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

To test the student's comprehension, I plan to paraphrase the question to present the same concept in a different way. 

Please assist me in paraphrasing the question.

Please present your paraphrased question within triple angle brackets. 
For example, if you want to change the question to 'What is the capital of China?', please respond with <<<What is the capital of China?>>>, do not include choices.
""",

        'paraphraser_add_question_context': \
"""
I'm assessing a student's understanding beyond memorization. I have a question with multiple choices and a known correct answer. The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

To test the student's comprehension, I plan to add non-essential context to the question: introducing context or details to the question that are relevant but not directly helpful in answering it. The context can be put at the beginning, middle, or end of the question.

Please assist me in adding extra context to the question.

Please present your revised question within triple angle brackets. 
For example, if you want to revise the question to 'What is the capital of China?', please respond <<<What is the capital of China?>>>, do not include choices.
""",

        'paraphraser_paraphrase_choices': \
"""
I'm assessing a student's understanding beyond memorization. I have a question with multiple choices and a known correct answer. The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the choices.

### Original Question and Choices:

### Question:
{question}

### Choices:
{choices}

To test the student's comprehension, I plan to paraphrase the choices: each choice should be paraphrased to reflect the same concept or idea as the original. The essence and meaning must be preserved. If a choice cannot be paraphrased without changing its meaning, it should be kept unchanged.

Please assist me in paraphrasing the original choices.

Please concatenate the choices with '\\n' and present your revised choices within triple angle brackets.
For example, if you change the original choices to 'A: Beijing', 'B: Chongqing', please respond <<<A: Beijing\nB: Chongqing>>>
""",

        'paraphraser_add_new_choice': \
"""
I'm assessing a student's understanding beyond memorization. I have a question with multiple choices and a known correct answer. The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the choices.

### Original Question and Choices:

### Question:
{question}

### Choices:
{choices}

To test the student's comprehension, I plan to keep the choices A,B,C,D unchanged, and introduce an additional relevant choice E that is related to the topic but doesn't provide another correct answer. This choice should be plausible but clearly not correct in the context of the question.

Please assist me in adding one new choice.

Please concatenate the choices with '\\n' and present your revised choices within triple angle brackets.
For example, if the original choices are 'A: Beijing', 'B: Chongqing' and you want to add a new choice 'C: Shanghai', please respond <<<A: Beijing\nB: Chongqing\nC: Shanghai>>>
""",
        
        'evaluator_paraphrase_question': \
"""
I have revised the wording of a multiple-choice question and need to assess whether the revised version still tests the same knowledge as the original question. 

Your task is to analyze both the original question and the revised question and determine if they are effectively assessing the same concept or knowledge area.

### Original Question:
{question}

### Rephrased Question:
{paraphrased}

If both questions fundamentally address the same topic or concept, respond with <<<Yes>>>, else respond with <<<No>>>.
""",

        'evaluator_add_question_context': \
"""
I have revised the wording of a multiple-choice question and need to assess whether the revised version still tests the same knowledge as the original question. 

Your task is to analyze both the original question and the revised question and determine if they are effectively assessing the same concept or knowledge area.

### Original Question:
{question}

### Paraphrased Question:
{paraphrased}

If both questions fundamentally address the same topic or concept, respond with <<<Yes>>>, else respond with <<<No>>>.
""",

        'evaluator_paraphrase_choices': \
"""
I have a multiple-choice question with four original choices (A, B, C, D) and a known correct answer. These choices have been paraphrased, and an additional irrelevant choice has been added. 

Your task is to analyze the paraphrased choices in the context of the question and determine if the paraphrased choices (A, B, C, D) still reflect the original meaning of their respective original choices.

### Question:
{question}

### Original Choices:
{choices}

### Paraphrased Choice:
{paraphrased}

###Answer for the Original Choices:
{answer}

If all the paraphrased choices maintain their original meaning, respond with <<<Yes>>>. Otherwise, respond with <<<No>>>.
""",

        'evaluator_add_new_choice': \
"""
I have a multiple-choice question with four original choices (A, B, C, D) and a known correct answer. These choices have been paraphrased, and an additional irrelevant choice has been added. 

Your task is to analyze the paraphrased choices in the context of the question and determine whether the new choice (E) is relevant to the question but does not provide an alternative correct answer.

### Question:
{question}

### Original Choices:
{choices}

### New Choices:
{new_choice}

###Answer for the Original Choices:
{answer}

If the new choice (E) is relevant to the question and is not another correct answer, respond with <<<Yes>>>. Otherwise, respond with <<<No>>>.
"""
    },

    'gsm8k': {

        'paraphraser_paraphrase_question': \
"""
I'm assessing a student's understanding beyond memorization. I have a math question and a known correct answer. The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

### Answer:
{answer}

To test the student's comprehension, I plan to paraphrase the question to present the same concept in a different way. 

Please retain the original numerical values and the core mathematical relationships in the question to ensure the integrity of the problem is preserved. 

The key objective is to ensure that the rephrased question tests the same mathematical concept, remains solvable, and that its correct solution aligns with the original answer, which is {answer}.

Please assist me in paraphrasing the question.

Please present your paraphrased question within triple angle brackets. 
For example, if you want to change the question to 'What is the capital of China?', please respond with <<<What is the capital of China?>>>.
""",

        'paraphraser_add_question_context': \
"""
I'm assessing a student's understanding beyond memorization. I have a math question and a known correct answer. The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

### Answer:
{answer}

To test the student's comprehension, I plan to add non-essential context to the question: introducing context or details to the question that are relevant but not directly helpful in answering it. The context can be put at the beginning, middle, or end of the question.

Please retain the original numerical values and the core mathematical relationships in the question to ensure the integrity of the problem is preserved. 

The key objective is to ensure that the rephrased question tests the same mathematical concept, remains solvable, and that its correct solution aligns with the original answer, which is {answer}.

Please assist me in adding extra context to the question.

Please present your revised question within triple angle brackets. 
For example, if you want to revise the question to 'What is the capital of China?', please respond <<<What is the capital of China?>>>.
""",
        
        'evaluator_paraphrase_question': \
"""
I have revised the wording of a math question and need to assess whether the revised version still tests the same knowledge as the original question. 

Your task is to analyze both the original question and the revised question and determine if they are effectively the same.

### Original Question:
{question}

### Rephrased Question:
{paraphrased}

### Answer:
{answer}

If both questions fundamentally address the same math question and share the same answer, respond with <<<Yes>>>, else respond with <<<No>>>.
""",

        'evaluator_add_question_context': \
"""
I have revised the wording of a math question and need to assess whether the revised version still tests the same knowledge as the original question. 

Your task is to analyze both the original question and the revised question and determine if they are effectively the same.

### Original Question:
{question}

### Paraphrased Question:
{paraphrased}

### Answer:
{answer}

If both questions fundamentally address the same math question and share the same answer, respond with <<<Yes>>>, else respond with <<<No>>>.
"""
    },

    'causal_judgement': {
        'paraphraser_paraphrase_question': \
"""
I'm assessing a student's understanding beyond memorization. I have a question about causal judgement task and a known correct answer. 

The causal judgement task is about: given a short story (involving moral, intentional, or counterfactual analysis), determine how a typical person would answer a causal question about the story.

The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

To test the student's comprehension, I plan to paraphrase the question to present the same concept in a different way. 

Please assist me in paraphrasing the question.

Please present your paraphrased question within triple angle brackets. 
For example, if you want to change the question to 'What is the capital of China?', please respond with <<<What is the capital of China?>>>, do not include choices.
""",

        'paraphraser_add_question_context': \
"""
I'm assessing a student's understanding beyond memorization. I have a question about causal judgement task and a known correct answer. 

The causal judgement task is about: given a short story (involving moral, intentional, or counterfactual analysis), determine how a typical person would answer a causal question about the story.

The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

To test the student's comprehension, I plan to add non-essential context to the question: introducing context or details to the question that are relevant but not directly helpful in answering it. The context can be put at the beginning, middle, or end of the question.

Please assist me in adding extra context to the question.

Please present your revised question within triple angle brackets. 
For example, if you want to revise the question to 'What is the capital of China?', please respond <<<What is the capital of China?>>>, do not include choices.
""",
        
        'evaluator_paraphrase_question': \
"""
I have revised the wording of a question about causal judgement task and need to assess whether the revised version still tests the same knowledge as the original question. 

Your task is to analyze both the original question and the revised question and determine if they are effectively the same.

### Original Question:
{question}

### Rephrased Question:
{paraphrased}

### Answer:
{answer}

If both questions fundamentally address the same question and share the same answer, respond with <<<Yes>>>, else respond with <<<No>>>.
""",

        'evaluator_add_question_context': \
"""
I have revised the wording of a question about causal judgement task and need to assess whether the revised version still tests the same knowledge as the original question. 

Your task is to analyze both the original question and the revised question and determine if they are effectively the same.

### Original Question:
{question}

### Paraphrased Question:
{paraphrased}

### Answer:
{answer}

If both questions fundamentally address the same question and share the same answer, respond with <<<Yes>>>, else respond with <<<No>>>.
"""
    },

    'formal_fallacies': {
        'paraphraser_paraphrase_question': \
"""
I'm assessing a student's understanding beyond memorization. I have a question about formal fallacies task and a known correct answer. 

The formal fallacies task is about: given a context involving a set of statements, determine whether an argument---presented informally---can be logically deduced from the provided context.

The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

To test the student's comprehension, I plan to paraphrase the question to present the same concept in a different way.

Please do not change the meaning of each argument.

Please assist me in paraphrasing the question.

Please present your paraphrased question within triple angle brackets. 
For example, if you want to change the question to 'What is the capital of China?', please respond with <<<What is the capital of China?>>>, do not include choices.
""",

        'paraphraser_add_question_context': \
"""
I'm assessing a student's understanding beyond memorization. I have a question about formal fallacies task and a known correct answer. 

The formal fallacies task is about: given a context involving a set of statements, determine whether an argument---presented informally---can be logically deduced from the provided context.

The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

To test the student's comprehension, I plan to add non-essential context to the question: introducing context or details to the question that are relevant but not directly helpful in answering it. The context can be put at the beginning, middle, or end of the question.

Please do not change the meaning of each argument.

Please assist me in adding extra context to the question.

Please present your revised question within triple angle brackets. 
For example, if you want to revise the question to 'What is the capital of China?', please respond <<<What is the capital of China?>>>, do not include choices.
""",
        
        'evaluator_paraphrase_question': \
"""
I have revised the wording of a question about formal fallacies task and need to assess whether the revised version still tests the same knowledge as the original question. 

The formal fallacies task is about: given a context involving a set of statements, determine whether an argument---presented informally---can be logically deduced from the provided context.

Your task is to analyze both the original question and the revised question and determine if they are effectively the same.

### Original Question:
{question}

### Rephrased Question:
{paraphrased}

### Answer:
{answer}

If both questions fundamentally address the same question and share the same answer, respond with <<<Yes>>>, else respond with <<<No>>>.
""",

        'evaluator_add_question_context': \
"""
I have revised the wording of a question about formal fallacies task and need to assess whether the revised version still tests the same knowledge as the original question. 

The formal fallacies task is about: given a context involving a set of statements, determine whether an argument---presented informally---can be logically deduced from the provided context.

Your task is to analyze both the original question and the revised question and determine if they are effectively the same.

### Original Question:
{question}

### Paraphrased Question:
{paraphrased}

### Answer:
{answer}

If both questions fundamentally address the same question and share the same answer, respond with <<<Yes>>>, else respond with <<<No>>>.
"""
    },

    'object_counting': {
        'paraphraser_paraphrase_question': \
"""
I'm assessing a student's understanding beyond memorization. I have a question about object counting task and a known correct answer. 

The object counting task is about: given a collection of possessions that a person has along with their quantities (e.g., three pianos, two strawberries, one table, and two watermelons), determine the number of a certain object/item class (e.g., fruits).

The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

To test the student's comprehension, I plan to paraphrase the question to present the same concept in a different way.

Please do not change the number of each possesion.

Please assist me in paraphrasing the question.

Please present your paraphrased question within triple angle brackets. 
For example, if you want to change the question to 'What is the capital of China?', please respond with <<<What is the capital of China?>>>, do not include choices.
""",

        'paraphraser_add_question_context': \
"""
I'm assessing a student's understanding beyond memorization. I have a question about object counting task and a known correct answer. 

The object counting task is about: given a collection of possessions that a person has along with their quantities (e.g., three pianos, two strawberries, one table, and two watermelons), determine the number of a certain object/item class (e.g., fruits).

The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

To test the student's comprehension, I plan to add non-essential context to the question: introducing context or details to the question that are relevant but not directly helpful in answering it. The context can be put at the beginning, middle, or end of the question.

Please do not change the number of each possesion.

Please assist me in adding extra context to the question.

Please present your revised question within triple angle brackets. 
For example, if you want to revise the question to 'What is the capital of China?', please respond <<<What is the capital of China?>>>, do not include choices.
""",
        
        'evaluator_paraphrase_question': \
"""
I have revised the wording of a question about object counting task and need to assess whether the revised version still tests the same knowledge as the original question. 

The object counting task is about: given a collection of possessions that a person has along with their quantities (e.g., three pianos, two strawberries, one table, and two watermelons), determine the number of a certain object/item class (e.g., fruits).

Your task is to analyze both the original question and the revised question and determine if they are effectively the same.

### Original Question:
{question}

### Rephrased Question:
{paraphrased}

### Answer:
{answer}

If both questions fundamentally address the same question and share the same answer, respond with <<<Yes>>>, else respond with <<<No>>>.
""",

        'evaluator_add_question_context': \
"""
I have revised the wording of a question about object counting task and need to assess whether the revised version still tests the same knowledge as the original question. 

The object counting task is about: given a collection of possessions that a person has along with their quantities (e.g., three pianos, two strawberries, one table, and two watermelons), determine the number of a certain object/item class (e.g., fruits).

Your task is to analyze both the original question and the revised question and determine if they are effectively the same.

### Original Question:
{question}

### Paraphrased Question:
{paraphrased}

### Answer:
{answer}

If both questions fundamentally address the same question and share the same answer, respond with <<<Yes>>>, else respond with <<<No>>>.
"""
    },

    'temporal_sequences': {
        'paraphraser_paraphrase_question': \
"""
I'm assessing a student's understanding beyond memorization. I have a question about temporal sequences task and a known correct answer. 

The temporal sequences task is about: given a series of events and activities a person has completed in the course of a day, determine what time, during the day, they might have been free to perform another activity.

The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

The challenge is to paraphrase this question while strictly adhering to two key constraints:
1. The activity mentioned in the question must remain unchanged.
2. The time slot for this activity must also remain the same.

These elements are crucial to ensure the essence of the original question is retained in the paraphrase.

Please assist me in paraphrasing the question that meets these constraints.

Please present your paraphrased question within triple angle brackets. 
For example, if you want to change the question to 'What is the capital of China?', please respond with <<<What is the capital of China?>>>, do not include choices.
""",

        'paraphraser_add_question_context': \
"""
I'm assessing a student's understanding beyond memorization. I have a question about temporal sequences task and a known correct answer. 

The temporal sequences task is about: given a series of events and activities a person has completed in the course of a day, determine what time, during the day, they might have been free to perform another activity.

The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

The challenge is to add new context into each activity while strictly adhering to two key constraints:
1. The activity mentioned in the question must remain unchanged.
2. The time slot for this activity must also remain the same.

These elements are crucial to ensure the essence of the original question is retained in the paraphrase.

Please assist me in adding extra context to each activity that meets these constraints.

Please present your revised question within triple angle brackets. 
For example, if you want to revise the question to 'What is the capital of China?', please respond <<<What is the capital of China?>>>, do not include choices.
""",
        
        'evaluator_paraphrase_question': \
"""
I have revised the wording of a question about temporal sequences and need to assess whether the revised version still tests the same knowledge as the original question. 

The temporal sequences task is about: given a series of events and activities a person has completed in the course of a day, determine what time, during the day, they might have been free to perform another activity.

Your task is to analyze both the original question and the revised question and determine if they are effectively the same.

### Original Question:
{question}

### Rephrased Question:
{paraphrased}

### Answer:
{answer}

While reviewing, pay particular attention to the following:
1. Does the rephrased question refer to the same specific activities mentioned in the original question?
2. Is the time slot for this activity consistent between the original and rephrased questions?

Only if both conditions are met, and the questions essentially address the same point, respond with <<<Yes>>>, else respond with <<<No>>>.
""",

        'evaluator_add_question_context': \
"""
I have revised the wording of a question about temporal sequences task and need to assess whether the revised version still tests the same knowledge as the original question. 

The temporal sequences task is about: given a series of events and activities a person has completed in the course of a day, determine what time, during the day, they might have been free to perform another activity.

Your task is to analyze both the original question and the revised question and determine if they are effectively the same.

### Original Question:
{question}

### Paraphrased Question:
{paraphrased}

### Answer:
{answer}

While reviewing, pay particular attention to the following:
1. Does the rephrased question refer to the same specific activities mentioned in the original question?
2. Is the time slot for this activity consistent between the original and rephrased questions?

Only if both conditions are met, and the questions essentially address the same point, respond with <<<Yes>>>, else respond with <<<No>>>.
"""
    },

    'arc-challenge': {
        'paraphraser_paraphrase_question': \
"""
I'm assessing a student's understanding beyond memorization. I have a question with multiple choices and a known correct answer. The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

To test the student's comprehension, I plan to paraphrase the question to present the same concept in a different way. 

Please assist me in paraphrasing the question.

Please present your paraphrased question within triple angle brackets. 
For example, if you want to change the question to 'What is the capital of China?', please respond with <<<What is the capital of China?>>>, do not include choices.
""",

        'paraphraser_add_question_context': \
"""
I'm assessing a student's understanding beyond memorization. I have a question with multiple choices and a known correct answer. The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the question and its answer.

### Question:
{question}

To test the student's comprehension, I plan to add non-essential context to the question: introducing context or details to the question that are relevant but not directly helpful in answering it. The context can be put at the beginning, middle, or end of the question.

Please assist me in adding extra context to the question.

Please present your revised question within triple angle brackets. 
For example, if you want to revise the question to 'What is the capital of China?', please respond <<<What is the capital of China?>>>, do not include choices.
""",

        'paraphraser_paraphrase_choices': \
"""
I'm assessing a student's understanding beyond memorization. I have a question with multiple choices and a known correct answer. The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the choices.

### Original Question and Choices:

### Question:
{question}

### Choices:
{choices}

To test the student's comprehension, I plan to paraphrase the choices: each choice should be paraphrased to reflect the same concept or idea as the original. The essence and meaning must be preserved. If a choice cannot be paraphrased without changing its meaning, it should be kept unchanged.

Please assist me in paraphrasing the original choices.

Please concatenate the choices with '\\n' and present your revised choices within triple angle brackets.
For example, if you change the original choices to 'A: Beijing', 'B: Chongqing', please respond <<<A: Beijing\nB: Chongqing>>>
""",

        'paraphraser_add_new_choice': \
"""
I'm assessing a student's understanding beyond memorization. I have a question with multiple choices and a known correct answer. The student provided the right answer, but I want to ensure they truly understand the material and didn't just memorize the choices.

### Original Question and Choices:

### Question:
{question}

### Choices:
{choices}

To test the student's comprehension, I plan to keep the original choices unchanged, and introduce an additional relevant choice that is related to the topic but doesn't provide another correct answer. This choice should be plausible but clearly not correct in the context of the question.

Please assist me in adding one new choice.

Please concatenate the choices with '\\n' and present your revised choices within triple angle brackets.
For example, if the original choices are 'A: Beijing', 'B: Chongqing' and you want to add a new choice 'C: Shanghai', please respond <<<A: Beijing\nB: Chongqing\nC: Shanghai>>>
""",
        
        'evaluator_paraphrase_question': \
"""
I have revised the wording of a multiple-choice question and need to assess whether the revised version still tests the same knowledge as the original question. 

Your task is to analyze both the original question and the revised question and determine if they are effectively assessing the same concept or knowledge area.

### Original Question:
{question}

### Rephrased Question:
{paraphrased}

If both questions fundamentally address the same topic or concept, respond with <<<Yes>>>, else respond with <<<No>>>.
""",

        'evaluator_add_question_context': \
"""
I have revised the wording of a multiple-choice question and need to assess whether the revised version still tests the same knowledge as the original question. 

Your task is to analyze both the original question and the revised question and determine if they are effectively assessing the same concept or knowledge area.

### Original Question:
{question}

### Paraphrased Question:
{paraphrased}

If both questions fundamentally address the same topic or concept, respond with <<<Yes>>>, else respond with <<<No>>>.
""",

        'evaluator_paraphrase_choices': \
"""
I have a multiple-choice question and a known correct answer. These choices have been paraphrased, and an additional irrelevant choice has been added. 

Your task is to analyze the paraphrased choices in the context of the question and determine if the paraphrased choices still reflect the original meaning of their respective original choices.

### Question:
{question}

### Original Choices:
{choices}

### Paraphrased Choice:
{paraphrased}

###Answer for the Original Choices:
{answer}

If all the paraphrased choices maintain their original meaning, respond with <<<Yes>>>. Otherwise, respond with <<<No>>>.
""",

        'evaluator_add_new_choice': \
"""
I have a multiple-choice question and a known correct answer. These choices have been paraphrased, and an additional irrelevant choice has been added. 

Your task is to analyze the paraphrased choices in the context of the question and determine whether the new choice is relevant to the question but does not provide an alternative correct answer.

### Question:
{question}

### Original Choices:
{choices}

### New Choices:
{new_choice}

###Answer for the Original Choices:
{answer}

If the new choice is relevant to the question and is not another correct answer, respond with <<<Yes>>>. Otherwise, respond with <<<No>>>.
"""
    },

}


PROMPTS = {
    'mmlu': "Here is a question about {task}:\n\n{question}\n\n{choices}\n\nChoose the correct answer and explain why. Please include your answer into <<<>>>. For example, if you choose A, please write <<<A>>>.",
    'gsm8k': "Here is a math problem:\n\n{question}\n\nPlease solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.",
    'arc-challenge': "Here is a multiple-choice science problem:\n\n### Question:\n{question}\n\n### Choices\n{choices}\n\nPlease solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.",
    'formal_fallacies': "Here is a question about formal fallacies (given a context involving a set of statements, determine whether an argument can be logically deduced from the provided context):\n\n### Question:\n{question}\n\n### {choices}\n\nPlease answer this question and include your answer into <<<>>>. For example, if your answer is valid, please write <<<valid>>>.",
    'object_counting': "Here is a question about object counting (given a collection of possessions that a person has along with their quantities, determine the number of a certain object/item class.):\n\n{question}\n\nPlease answer this question and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.",
    'temporal_sequences': "Here is a question about temporal sequences (given a series of events and activities a person has completed in the course of a day, determine what time, during the day, they might have been free to perform another activity.):\n\n### Question:\n{question}\n\n### {choices}\n\nPlease answer this question and include your answer into <<<>>>. For example, if your answer is (A), please write <<<(A)>>>.",
}

FEW_SHOT_PROMPTS = {
	'gsm8k': {
        'origin':
"""
Q:
Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:
Natalia sold 48/2 = <<48/2=24>>24 clips in May. Natalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May. <<<72>>>

Q:
Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:
Weng earns 12/60 = $<<12/60=0.2>>0.2 per minute. Working 50 minutes, she earned 0.2 x 50 = $<<0.2*50=10>>10. <<<10>>>

Q:
Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?	
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:
In the beginning, Betty has only 100 / 2 = $<<100/2=50>>50. Betty's grandparents gave her 15 * 2 = $<<15*2=30>>30. This means, Betty needs 100 - 50 - 30 - 15 = $<<100-50-30-15=5>>5 more. <<<5>>>

Q:
Julie is reading a 120-page book. Yesterday, she was able to read 12 pages and today, she read twice as many pages as yesterday. If she wants to read half of the remaining pages tomorrow, how many pages should she read?	
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:
Maila read 12 x 2 = <<12*2=24>>24 pages today. So she was able to read a total of 12 + 24 = <<12+24=36>>36 pages since yesterday. There are 120 - 36 = <<120-36=84>>84 pages left to be read. Since she wants to read half of the remaining pages tomorrow, then she should read 84/2 = <<84/2=42>>42 pages. <<<42>>>

Q:
James writes a 3-page letter to 2 different friends twice a week. How many pages does he write a year?	
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:
He writes each friend 3*2=<<3*2=6>>6 pages a week So he writes 6*2=<<6*2=12>>12 pages every week That means he writes 12*52=<<12*52=624>>624 pages a year. <<<624>>>

Q:
{question}
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:

""",
		'paraphrased':
"""
Q:
In April, the local community center hosted a small business expo, attracting numerous visitors. During this event, Natalia set up a booth to sell her handmade hair clips. She was quite successful, selling her accessories to 48 customers. However, in May, there was no such event to boost her sales, and she noticed that her customer count had decreased to just half the number she had in April. Assuming Natalia sold an equal number of hair clips to each customer, can you determine the total number of customers she sold hair clips to over the course of these two months?
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:
Natalia sold 48/2 = <<48/2=24>>24 clips in May. Natalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May. <<<72>>>

Q:
Weng has recently taken up a part-time job as a babysitter to save up for a new bicycle. She charges a standard rate of $12 per hour for her babysitting services. On a sunny Thursday afternoon, she looked after her neighbor's child while the parents attended a yoga class. The session she spent babysitting lasted for exactly 5/6 of an hour. How much money did Weng earn for her babysitting on that day?
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:
Weng earns 12/60 = $<<12/60=0.2>>0.2 per minute. Working 50 minutes, she earned 0.2 x 50 = $<<0.2*50=10>>10. <<<10>>>

Q:
Betty, an avid collector of unique wallets, has her eyes set on a limited edition wallet that costs $100. She has been saving her allowance and has managed to accumulate 50% of the total price. On her birthday, her parents decide to support her passion by gifting her $15, and her grandparents, who are always eager to encourage her hobbies, generously give her twice what her parents contributed. As she adds these gifts to her savings, she wonders how much more money she will need to save from her upcoming babysitting jobs to finally purchase the wallet.
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:
In the beginning, Betty has only 100 / 2 = $<<100/2=50>>50. Betty's grandparents gave her 15 * 2 = $<<15*2=30>>30. This means, Betty needs 100 - 50 - 30 - 15 = $<<100-50-30-15=5>>5 more. <<<5>>>

Q:
Julie is an avid reader and has recently started reading a new mystery novel that has exactly 120 pages. On a sunny Monday, she cozied up on her porch and got through 12 pages of the book. The following day, inspired by the intriguing plot, she read twice as many pages as she did on Monday. Julie has a goal to read half of the remaining pages by Wednesday night. Considering her progress so far, how many pages does Julie need to read on Wednesday to meet her halfway goal?
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:
Maila read 12 x 2 = <<12*2=24>>24 pages today. So she was able to read a total of 12 + 24 = <<12+24=36>>36 pages since yesterday. There are 120 - 36 = <<120-36=84>>84 pages left to be read. Since she wants to read half of the remaining pages tomorrow, then she should read 84/2 = <<84/2=42>>42 pages. <<<42>>>

Q:
James, an avid writer and a dedicated friend, has committed to a unique tradition. Every week, without fail, he sits at his antique oak desk, the surface scattered with an array of colorful stamps from around the world and various fountain pens. With earnest focus, he crafts a 3-page letter to each of his two closest friends, sharing stories of his daily musings and life's little adventures. This practice is so dear to him that he repeats it twice each week, once on a tranquil Sunday morning and again on a quiet Wednesday evening. As the seasons change and a full year turns, how many pages has James penned in his heartfelt correspondences?
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:
He writes each friend 3*2=<<3*2=6>>6 pages a week So he writes 6*2=<<6*2=12>>12 pages every week That means he writes 12*52=<<12*52=624>>624 pages a year. <<<624>>>

Q:
{question}
Please solve this math problem and include your answer into <<<>>>. For example, if your answer is 1, please write <<<1>>>.

A:

"""
	},
    'arc-challenge':{
        'origin':
"""
Q:
Which of the following statements best explains why magnets usually stick to a refrigerator door?

A: The refrigerator door is smooth.
B: The refrigerator door contains iron.
C: The refrigerator door is a good conductor.
D: The refrigerator door has electric wires in it.

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:
The reason why magnets usually stick to a refrigerator door is because the door contains iron or a ferromagnetic material, which is attracted to magnets. Therefore, the correct answer is: <<<B>>>

Q:
Stars are often classified by their apparent brightness in the nighttime sky. Stars can also be classified in many other ways. Which of these is least useful in classifying stars?

A: visible color
B: composition
C: surface texture
D: temperature

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:
In classifying stars, surface texture is the least useful attribute. This is because stars are massive, luminous spheres of plasma, and the concept of a surface texture, as it would be understood in the context of solid objects, does not apply to them in a meaningful way. Therefore, the correct answer is: <<<C>>>

Q:
Which statement is an observation?

A: The plant has flowers.
B: The plant is very pretty.
C: The plant will grow berries.
D: The plant might be poisonous.

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:

An observation is a statement about something that can be directly seen or measured. In the given options, "The plant has flowers" is a direct observation because it is a factual statement about a visible characteristic of the plant. Therefore, the correct answer is: <<<A>>>

Q:
Which of these substances conducts electricity the best?

A: Wood
B: Brick
C: Cooper
D: Plastic

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:
The substance among the given options that conducts electricity the best is copper. Copper is a metal known for its excellent electrical conductivity. Therefore, the correct answer is: <<<C>>>

Q:
Which pair of elements has the most similar properties?

A: Li and B
B: I and Ca
C: K and He
D: N and P

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:
The most similar properties among elements are typically found within the same group (column) in the periodic table, as they have the same number of valence electrons. In the given options, nitrogen (N) and phosphorus (P) are both in Group 15 of the periodic table, also known as the pnictogens. They share similar chemical properties due to their electronic configuration. Therefore, the correct answer is: <<<D>>>

Q:
{question}

{choices}

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:
""",

		'paraphrased':
"""
Q:
While considering the various materials appliances are made from, such as the plastic used for food processor bodies or the glass in blender jars, why are magnets typically attracted to the metal surface of a fridge, unlike these other materials?

A: The refrigerator door's surface is even and flat.
B: The refrigerator door is magnetized with the same polarity as the magnet.
C: The refrigerator door contains electrical conductive pathways within it.
D: The refrigerator door is an effective conductor of electricity.
E: The refrigerator door includes iron in its composition.

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:
Magnets are typically attracted to the metal surface of a refrigerator because this surface usually includes iron in its composition. Iron is a ferromagnetic material, which means it is strongly attracted by magnets. This is not the case with materials like plastic or glass, which are used in other appliances but do not exhibit magnetic properties. Therefore, the correct answer is: <<<E>>>

Q:
While astronomers have developed a sophisticated understanding of the cosmos, utilizing advanced telescopes and other observational tools to study the vast universe, they often categorize stars to better understand stellar evolution and composition. From spectral classification to luminosity and mass, many characteristics can be used to organize and differentiate these celestial bodies. Considering this complex framework for stellar categorization, which criterion would be the least effective for categorizing stars?

A: hue observed with the naked eye
B: granularity of the surface
C: elemental makeup
D: frequency of pulsation
E: degree of heat

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:
In the context of categorizing stars, the least effective criterion would be the granularity of the surface. Stars are massive, luminous spheres of plasma, and the concept of a surface texture or granularity, as it would apply to solid objects, is not applicable or useful in the study of stars. Therefore, the correct answer is: <<<B>>>

Q:
During a recent field trip to a natural history museum, the class encountered a variety of informative exhibits ranging from prehistoric fossils to interactive models demonstrating various scientific principles. As the students moved through an exhibit that detailed the scientific method, they were encouraged to think about how scientists gather and analyze data. With this in mind, please identify the statement that constitutes an empirical observation.

A: The plant can survive droughts.
B: There's a possibility that the plant is toxic.
C: The plant is likely to produce berries.
D: The plant looks beautiful.
E: The plant is flowering.

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:
An empirical observation is a statement based on direct, observable, and measurable evidence. Among the given options, "The plant is flowering" is an empirical observation because it is a factual statement about a visible and verifiable condition of the plant. Therefore, the correct answer is: <<<E>>>

Q:
In a scenario where a group of engineers is tasked with designing an advanced circuit for a new piece of technology, they must consider the properties of various materials to ensure the most efficient electrical conductivity. Among the following options, taking into account their atomic structure and the likelihood of their electrons to move freely, which material would the engineers find most effective at allowing the flow of electric current?

A: Copper
B: Timber
C: Glass
D: Masonry
E: Synthetic material

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:
In considering materials for efficient electrical conductivity, engineers would focus on materials whose atomic structure allows electrons to move freely. Among the options provided, copper is the best conductor of electricity. It is a metal with a structure that allows for easy movement of electrons, making it highly effective for electrical applications. Therefore, the correct answer is: <<<A>>>

Q:
In the periodic table, elements are arranged according to their atomic number, displaying periodic trends in chemical and physical properties as one moves across a period or down a group. Considering this organization and the principles behind the formation of the periodic table, among different pairs of elements, which two exhibit the most comparable characteristics?

A: Potassium and Helium
B: Oxygen and Fluorine
C: Nitrogen and Phosphorus
D: Iodine and Calcium
E: Lithium and Boron

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:
Elements that are in the same group (vertical column) of the periodic table typically exhibit the most comparable characteristics, as they have similar electron configurations, particularly in their outer shells. Among the pairs listed, nitrogen (N) and phosphorus (P) are both in Group 15 of the periodic table. They share similar chemical properties due to their electronic structure. Therefore, the correct answer is: <<<C>>>

Q:
{question}

{choices}

Please solve this problem and include your answer into <<<>>>. For example, if your choose A, please write <<<A>>>.

A:
""",
	}

}