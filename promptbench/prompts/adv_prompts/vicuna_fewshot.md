# vicuna_fewshot

# cola

## 10 prompts

Acc: 65.20%, prompt: Determine if the grammar of the given sentence is 'Acceptable' or 'Unacceptable'.
Acc: 62.20%, prompt: Assess the grammatical structure of the given sentence and classify it as 'Acceptable' or 'Unacceptable'.
Acc: 47.70%, prompt: Examine the sentence and decide if its grammar is 'Acceptable' or 'Unacceptable'.
Acc: 38.50%, prompt: Check the grammar of the following sentence and indicate if it is 'Acceptable' or 'Unacceptable'.
Acc: 33.90%, prompt: Review the sentence below and identify whether its grammar is 'Acceptable' or 'Unacceptable'.
Acc: 8.00%, prompt: Analyze the provided sentence and classify its grammatical correctness as 'Acceptable' or 'Unacceptable'.
Acc: 5.30%, prompt: Is the provided sentence grammatically correct? Respond with 'Acceptable' or 'Unacceptable'.
Acc: 1.60%, prompt: Examine the given sentence and decide if it is grammatically sound. Answer with either 'Acceptable' or 'Unacceptable'.
Acc: 1.10%, prompt: Assess the following sentence and determine if it is grammatically correct. Respond with 'Acceptable' or 'Unacceptable'.
Acc: 0.90%, prompt: Please evaluate the grammatical structure of the provided sentence and answer with 'Acceptable' or 'Unacceptable'.

Acc: 49.60%, prompt: As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable'.
Acc: 48.00%, prompt: While performing grammar analysis, classify the grammar of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar.
Acc: 35.20%, prompt: Working as a grammar classifier, identify whether the given sentence has correct grammar, and respond with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones.
Acc: 33.40%, prompt: In your role as a grammar check tool, assess the following sentence and classify it as 'acceptable' if it is grammatically correct or 'unacceptable' if it is incorrect.
Acc: 26.90%, prompt: Functioning as a grammar evaluation tool, analyze the given sentence and decide if it is grammatically correct, responding with 'acceptable' or 'unacceptable'.
Acc: 20.80%, prompt: As an instrument for grammar evaluation, consider the sentence and determine if its grammar is correct, responding with 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar.
Acc: 19.30%, prompt: Acting as a grammar detection instrument, determine if the provided sentence is grammatically sound, answering with 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar.
Acc: 14.70%, prompt: In the capacity of a grammar assessment system, indicate if the structure of the provided sentence is grammatically correct, responding with 'acceptable' or 'unacceptable'.
Acc: 5.20%, prompt: In the role of a syntax analyzer, examine the grammar of the provided sentence and decide if it is correct, answering with 'acceptable' for grammatically correct sentences or 'unacceptable' for incorrect ones.
Acc: 0.10%, prompt: As a grammar identification system, examine the provided sentence and respond with 'acceptable' for grammatically correct sentences or 'unacceptable' for incorrect ones.

## bertattack

Original prompt: Determine if the grammar of the given sentence is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Determine if the grammar of the other situation is 'Acceptable' or 'Unacceptable'. "
Original acc: 65.20%, attacked acc: 32.90%, dropped acc: 32.30%

Original prompt: Assess the grammatical structure of the given sentence and classify it as 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Assess the context t of the of sentence and judge it as 'Acceptable' or 'Unacceptable'. "
Original acc: 62.20%, attacked acc: 3.80%, dropped acc: 58.40%

Original prompt: Examine the sentence and decide if its grammar is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Examine the discourse and see if its grammar is 'Acceptable' or 'Unacceptable'. "
Original acc: 47.70%, attacked acc: 15.40%, dropped acc: 32.30%

Original prompt: As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable'.
Attacked prompt: b"should a be for calculating adjective correctness, review the sentence and categorize its i as or 'acceptable' or 'unacceptable'. "
Original acc: 49.60%, attacked acc: 0.00%, dropped acc: 49.60%

Original prompt: While performing grammar analysis, classify the grammar of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar.
Attacked prompt: b"While to grammar analysis, view the language of the following sentence as 'acceptable' for correctly adjective or 'unacceptable' for english sentences. "
Original acc: 48.00%, attacked acc: 0.20%, dropped acc: 47.80%

Original prompt: Working as a grammar classifier, identify whether the given sentence has correct grammar, and respond with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones.
Attacked prompt: b"Working as a grammar classiate, identify whether the given sentence has correct grammar, and answer with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones. "
Original acc: 35.20%, attacked acc: 0.00%, dropped acc: 35.20%

## checklist

Original prompt: Determine if the grammar of the given sentence is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Determine if the grammar of the given sentence is 'Acceptable' or 'Unacceptable' Q47Jmd4lMV. "
Original acc: 65.20%, attacked acc: 21.30%, dropped acc: 43.90%

Original prompt: Assess the grammatical structure of the given sentence and classify it as 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Assess the grammatical structure of the given sentence and classify it as 'Acceptable' or 'Unacceptable' Q47Jmd4lMV. "
Original acc: 62.20%, attacked acc: 17.40%, dropped acc: 44.80%

Original prompt: Examine the sentence and decide if its grammar is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Examine the sentence and decide if its grammar is 'Acceptable' or 'Unacceptable' PDCGfz6DL9. "
Original acc: 47.70%, attacked acc: 18.90%, dropped acc: 28.80%

Original prompt: As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable'.
Attacked prompt: b"As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable' 6a4Yn3RGVc. "
Original acc: 49.60%, attacked acc: 8.70%, dropped acc: 40.90%

Original prompt: While performing grammar analysis, classify the grammar of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar.
Attacked prompt: b"While performing grammar analysis, classify the grammar of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar Q47Jmd4lMV. "
Original acc: 48.00%, attacked acc: 3.90%, dropped acc: 44.10%

Original prompt: Working as a grammar classifier, identify whether the given sentence has correct grammar, and respond with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones.
Attacked prompt: b"Working as a grammar classifier, identify whether the given sentence has correct grammar, and respond with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones yh912BU8T0. "
Original acc: 35.20%, attacked acc: 2.40%, dropped acc: 32.80%

## deepwordbug

Original prompt: Determine if the grammar of the given sentence is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Dtermine if the gammar of the gisven setnence is 'Acceptable' or 'Unacceptable'. "
Original acc: 65.20%, attacked acc: 24.50%, dropped acc: 40.70%

Original prompt: Assess the grammatical structure of the given sentence and classify it as 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Assess the grammatcal etructure of the given entence and classif it as 'Acceptable' or 'Unacceptable'. "
Original acc: 62.00%, attacked acc: 11.40%, dropped acc: 50.60%

Original prompt: Examine the sentence and decide if its grammar is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Exmaine the sntence and dcide if its rgammar is 'Acceptable' or 'Unacceptable'. "
Original acc: 47.60%, attacked acc: 12.90%, dropped acc: 34.70%

Original prompt: As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable'.
Attacked prompt: b"sA a tobol for determning grammatical correctness, reTview the sentence and caegorize its grammar as iether 'acceptable' or 'unacceptable'. "
Original acc: 49.80%, attacked acc: 3.00%, dropped acc: 46.80%

Original prompt: While performing grammar analysis, classify the grammar of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar.
Attacked prompt: b"Whie performing grammar analysis, claBsify the grammar of the following sentenge as 'acceptable' for correct grammar or 'unacceptable' for incorrect grmmar. "
Original acc: 47.50%, attacked acc: 1.10%, dropped acc: 46.40%

Original prompt: Working as a grammar classifier, identify whether the given sentence has correct grammar, and respond with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones.
Attacked prompt: b"Working as a grammar clsasifier, identify whether the given sentence has correct grammar, and reszond with 'acceptable' for correct sentences or 'unacceptable' for incorrect noes. "
Original acc: 35.10%, attacked acc: 0.00%, dropped acc: 35.10%

## stresstest

Original prompt: Determine if the grammar of the given sentence is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Determine if the grammar of the given sentence is 'Acceptable' or 'Unacceptable'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 65.20%, attacked acc: 21.30%, dropped acc: 43.90%

Original prompt: Assess the grammatical structure of the given sentence and classify it as 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Assess the grammatical structure of the given sentence and classify it as 'Acceptable' or 'Unacceptable'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 62.20%, attacked acc: 16.00%, dropped acc: 46.20%

Original prompt: Examine the sentence and decide if its grammar is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Examine the sentence and decide if its grammar is 'Acceptable' or 'Unacceptable'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 47.70%, attacked acc: 10.60%, dropped acc: 37.10%

Original prompt: As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable'.
Attacked prompt: b"As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable'  and true is true . "
Original acc: 49.60%, attacked acc: 3.00%, dropped acc: 46.60%

Original prompt: While performing grammar analysis, classify the grammar of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar.
Attacked prompt: b"While performing grammar analysis, classify the grammar of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar  and true is true . "
Original acc: 48.00%, attacked acc: 17.20%, dropped acc: 30.80%

Original prompt: Working as a grammar classifier, identify whether the given sentence has correct grammar, and respond with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones.
Attacked prompt: b"Working as a grammar classifier, identify whether the given sentence has correct grammar, and respond with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 35.20%, attacked acc: 0.90%, dropped acc: 34.30%

## textbugger

Original prompt: Determine if the grammar of the given sentence is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Identify if the \xc9\xa1rammar of the give\xd5\xb8 sentence is 'Acceptable' or 'Unacceptable'. "
Original acc: 65.20%, attacked acc: 4.00%, dropped acc: 61.20%

Original prompt: Assess the grammatical structure of the given sentence and classify it as 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Assess the grammatically s\xf0\x9d\x9a\x9dructure of the \xc9\xa1iven sentecne and clasisfy it as 'Acceptable' or 'Unacceptable'. "
Original acc: 62.20%, attacked acc: 2.20%, dropped acc: 60.00%

Original prompt: Examine the sentence and decide if its grammar is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Investigated the sentencing and decide if its grammar is 'Acceptable' or 'Unacceptable'. "
Original acc: 47.70%, attacked acc: 21.00%, dropped acc: 26.70%

Original prompt: As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable'.
Attacked prompt: b"Como a \xf0\x9d\x9a\x9dool for determines grammatical correctness, review the se\xd5\xb8tence and cat\xd0\xb5gorize its grammar as or 'acceptable' or 'unacceptable'. "
Original acc: 49.60%, attacked acc: 1.10%, dropped acc: 48.50%

Original prompt: While performing grammar analysis, classify the grammar of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar.
Attacked prompt: b"Whie pe\xe2\xb2\x85forming grammar analysis, \xcf\xb2lassify the grammatical of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammr. "
Original acc: 48.00%, attacked acc: 0.00%, dropped acc: 48.00%

Original prompt: Working as a grammar classifier, identify whether the given sentence has correct grammar, and respond with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones.
Attacked prompt: b"Working as a grammar classi\xf0\x9d\x9a\x8fier, identify whether the given sentence has correct grammar, and replying with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones. "
Original acc: 35.20%, attacked acc: 0.00%, dropped acc: 35.20%

## textfooler

Original prompt: Determine if the grammar of the given sentence is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Establishing if the verbs of the offered condemnation is 'Acceptable' or 'Unacceptable'. "
Original acc: 65.20%, attacked acc: 14.20%, dropped acc: 51.00%

Original prompt: Assess the grammatical structure of the given sentence and classify it as 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Assess the grammatically constructing of the given sentence and classed it as 'Acceptable' or 'Unacceptable'. "
Original acc: 62.20%, attacked acc: 23.00%, dropped acc: 39.20%

Original prompt: Examine the sentence and decide if its grammar is 'Acceptable' or 'Unacceptable'.
Attacked prompt: b"Discuss the sentencing and choosing if its language is 'Acceptable' or 'Unacceptable'. "
Original acc: 47.70%, attacked acc: 8.00%, dropped acc: 39.70%

Original prompt: As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable'.
Attacked prompt: b"As a appliance for establish grammatical correctness, reconsider the reprimand and classify its grammar as either 'acceptable' or 'unacceptable'. "
Original acc: 49.60%, attacked acc: 1.90%, dropped acc: 47.70%

Original prompt: While performing grammar analysis, classify the grammar of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for incorrect grammar.
Attacked prompt: b"During exercise grammar examines, classified the pronunciation of the following sentence as 'acceptable' for correct grammar or 'unacceptable' for improper jargon. "
Original acc: 48.00%, attacked acc: 0.20%, dropped acc: 47.80%

Original prompt: Working as a grammar classifier, identify whether the given sentence has correct grammar, and respond with 'acceptable' for correct sentences or 'unacceptable' for incorrect ones.
Attacked prompt: b"Working as a grammar classifier, identify whether the given sentence has correct jargon, and cope with 'acceptable' for correct punishments or 'unacceptable' for inappropriate ones. "
Original acc: 35.20%, attacked acc: 0.00%, dropped acc: 35.20%

## translation

Language: chinese, acc: 17.00%, prompt: As a tool for determining grammatical correctness, please review the following sentences and categorize them grammatically as 'acceptable' or 'unacceptable'.
Language: chinese, acc: 17.10%, prompt: Please evaluate the grammar of the following sentences and mark them as 'acceptable' or 'unacceptable'.
Language: chinese, acc: 5.30%, prompt: Please check that the following sentences are grammatically correct and categorize them as 'acceptable' or 'unacceptable'.
Language: chinese, acc: 8.60%, prompt: Please determine whether the following sentences are 'acceptable' or 'unacceptable' based on grammatical correctness.
Language: chinese, acc: 24.90%, prompt: Please categorize the grammar of the following sentences as 'acceptable' or 'unacceptable'.
Language: chinese, acc: 13.50%, prompt: Please check the grammar of the following sentences and classify them as 'acceptable' or 'unacceptable'.
Language: chinese, acc: 7.20%, prompt: Please mark the following sentences as 'acceptable' or 'unacceptable' according to the grammatical norms.
Language: chinese, acc: 17.80%, prompt: Please assess the grammar of the following sentences and classify them as 'acceptable' or 'unacceptable'.
Language: chinese, acc: 8.90%, prompt: Please mark the following sentences as 'acceptable' or 'unacceptable' for grammatical accuracy.
Language: chinese, acc: 13.50%, prompt: Please check the grammar of the following sentences and classify them as 'acceptable' or 'unacceptable'.
Language: french, acc: 16.50%, prompt: As a tool for assessing semantic relevance, categorize the sentence as 'acceptable' or 'unacceptable' according to its meaning and context.
Language: french, acc: 23.80%, prompt: Determine whether the grammatical structure of the sentence is 'acceptable' or 'unacceptable' by carefully reviewing it.
Language: french, acc: 21.10%, prompt: Judge whether the sentence follows the syntactic rules of the language and classify it as 'acceptable' or 'unacceptable'.
Language: french, acc: 10.70%, prompt: Assess the relevance of the sentence by classifying it as 'acceptable' or 'unacceptable' according to the context in which it is used.
Language: french, acc: 35.20%, prompt: As a semantic classification tool, decide whether the sentence is 'acceptable' or 'unacceptable' according to its meaning and consistency.
Language: french, acc: 29.60%, prompt: Analyze the sentence carefully and determine whether it is grammatically 'acceptable' or 'unacceptable'.
Language: french, acc: 34.60%, prompt: As a syntactic validation tool, determine whether the sentence is properly structured and categorize it as 'acceptable' or 'unacceptable'.
Language: french, acc: 16.50%, prompt: When evaluating the grammar of the sentence, classify it as 'acceptable' or 'unacceptable' according to the rules of the French language.
Language: french, acc: 32.70%, prompt: Determine whether the sentence is 'acceptable' or 'unacceptable' depending on its syntactic construction and semantic context.
Language: french, acc: 10.40%, prompt: As a tool for linguistic analysis, categorize the sentence as 'acceptable' or 'unacceptable' according to its relevance and semantic consistency.
Language: arabic, acc: 48.30%, prompt: As a tool for determining grammatical correctness, review the sentence and classify its rules as 'acceptable' or 'unacceptable'.
Language: arabic, acc: 36.80%, prompt: Analyze the sentence carefully and classify its grammar between 'acceptable' or 'unacceptable'.
Language: arabic, acc: 26.70%, prompt: As a tool for determining grammatical correctness, classify the rules of the sentence between 'acceptable' or 'unacceptable'.
Language: arabic, acc: 9.00%, prompt: Evaluate the correctness of the sentence between 'acceptable' or 'unacceptable', as a tool for determining grammatical correctness.
Language: arabic, acc: 30.10%, prompt: As a tool for classifying valid sentences, determine whether  'acceptable' or 'unacceptable' is based on its grammatical rules.
Language: arabic, acc: 35.60%, prompt: Analyze the sentence carefully and classify its grammatical rules between 'acceptable' or 'unacceptable'.
Language: arabic, acc: 34.80%, prompt: Analyze the sentence and classify it between 'acceptable' or 'unacceptable' as a grammatical check tool.
Language: arabic, acc: 22.60%, prompt: As a classification tool for grammatical sentences, determine whether the sentence 'acceptable' or 'unacceptable' is based on its rules.
Language: arabic, acc: 31.50%, prompt: As a tool for analyzing grammar, classify the rules of the sentence between 'acceptable' or 'unacceptable'.
Language: arabic, acc: 20.70%, prompt: Determine whether the sentence is 'acceptable' or 'unacceptable' as a tool for determining grammatical correctness and analyze its grammar.
Language: spanish, acc: 35.60%, prompt: As a tool to determine grammatical correctness, review the sentence and categorize its grammar as 'acceptable' or 'unacceptable'.
Language: spanish, acc: 40.00%, prompt: Analyze the sentence carefully and classify its grammar as 'acceptable' or 'unacceptable'.
Language: spanish, acc: 39.20%, prompt: As a tool for determining grammatical correctness, it categorizes the grammatical rules of the sentence as 'acceptable' or 'unacceptable'.
Language: spanish, acc: 44.50%, prompt: Evaluate the grammatical correctness of the sentence and classify it as 'acceptable' or 'unacceptable' using a grammatical verification tool.
Language: spanish, acc: 5.80%, prompt: As a tool for classifying grammatically correct sentences, determine whether the sentence is 'acceptable' or 'unacceptable' based on its grammatical rules.
Language: spanish, acc: 31.80%, prompt: Analyse the sentence carefully and classify its grammar as 'acceptable' or 'unacceptable' using a grammatical revision tool.
Language: spanish, acc: 31.80%, prompt: As a tool for classifying grammatical sentences, it determines whether the sentence is 'acceptable' or 'unacceptable' using its grammatical structure.
Language: spanish, acc: 38.00%, prompt: As a tool for analyzing grammatical correctness, it categorizes the grammatical rules of the sentence as 'acceptable' or 'unacceptable'.
Language: spanish, acc: 26.50%, prompt: Determine whether the sentence is 'acceptable' or 'unacceptable' using a grammatical verification tool and sort it accordingly.
Language: spanish, acc: 30.30%, prompt: As a tool for determining grammatical correctness, evaluate the sentence and classify it as 'acceptable' or 'unacceptable' based on its grammatical rules.
Language: japanese, acc: 61.40%, prompt: As a tool to determine whether grammar is grammatically correct, look at the sentence and categorize grammar into the 'acceptable' or 'unacceptable' categories.
Language: japanese, acc: 38.90%, prompt: Please read the given sentence and categorize the grammar into the 'acceptable' or 'unacceptable' categories.
Language: japanese, acc: 57.10%, prompt: To determine the correctness of a sentence, categorize grammar into two categories: 'acceptable' or 'unacceptable'.
Language: japanese, acc: 58.70%, prompt: Classify the grammar of a given sentence into two categories: 'acceptable' and 'unacceptable'.
Language: japanese, acc: 29.60%, prompt: Classify a given sentence into the categories 'acceptable' or 'unacceptable' to determine whether it is grammatically correct.
Language: japanese, acc: 72.30%, prompt: To determine whether it is grammatically correct, categorize a given sentence into two categories: 'acceptable' or 'unacceptable'.
Language: japanese, acc: 32.70%, prompt: To determine the correctness of grammar, categorize a given sentence into two categories: 'acceptable' or 'unacceptable'.
Language: japanese, acc: 48.80%, prompt: Classify the grammar of a given sentence into two categories, 'acceptable' or 'unacceptable', and judge its accuracy.
Language: japanese, acc: 53.20%, prompt: To determine whether it is grammatically correct, divide a given sentence into two categories: 'acceptable' or 'unacceptable'.
Language: japanese, acc: 66.10%, prompt: To evaluate the accuracy of grammar, categorize a given sentence into two categories: 'acceptable' or 'unacceptable'.
Language: korean, acc: 13.20%, prompt: As a tool for judging grammatical correctness, please review the sentences and classify the grammar as 'acceptable' or 'unacceptable'.
Language: korean, acc: 23.10%, prompt: Please read the given sentences, and classify the grammar as 'acceptable' or 'unacceptable'.
Language: korean, acc: 19.60%, prompt: Please classify the sentences as 'acceptable' or 'unacceptable' to judge the grammatical appropriateness.
Language: korean, acc: 33.20%, prompt: Please classify the grammar of the given sentences into 2 categories: 'acceptable' or 'unacceptable'.
Language: korean, acc: 7.60%, prompt: Please classify the given sentences as 'acceptable' or 'unacceptable' to judge the correctness of the grammar.
Language: korean, acc: 17.60%, prompt: Please classify the given sentences as 'acceptable' or 'unacceptable' in order to judge their grammatical appropriateness.
Language: korean, acc: 16.90%, prompt: Please determine the correctness of your grammar by classifying sentences as 'acceptable' or 'unacceptable'.
Language: korean, acc: 40.20%, prompt: Classify the grammar of a given sentence as 'acceptable' or 'unacceptable', and judge its accuracy.
Language: korean, acc: 7.60%, prompt: Please classify the given sentences as 'acceptable' or 'unacceptable' to judge the correctness of the grammar.
Language: korean, acc: 30.10%, prompt: Please rate the accuracy of your grammar by categorizing sentences as 'acceptable' or 'unacceptable'.

# mnli

## 10 prompts

Acc: 25.10%, prompt: Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Acc: 21.30%, prompt: Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction'.
Acc: 9.60%, prompt: Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'.
Acc: 9.50%, prompt: Does the relationship between the given sentences represent entailment, neutral, or contradiction? Respond with 'entailment', 'neutral', or 'contradiction'.
Acc: 3.80%, prompt: Indicate if the connection between the following sentences is 'entailment', 'neutral', or 'contradiction'.
Acc: 2.50%, prompt: Considering the two sentences, identify if their relationship is 'entailment', 'neutral', or 'contradiction'.
Acc: 1.00%, prompt: Analyze the two provided sentences and decide if their relationship is 'entailment', 'neutral', or 'contradiction'.
Acc: 0.60%, prompt: Determine if the given pair of sentences displays entailment, neutral, or contradiction. Respond with 'entailment', 'neutral', or 'contradiction'.
Acc: 0.10%, prompt: Examine the pair of sentences and determine if they exhibit entailment, neutral, or contradiction. Answer with either 'entailment', 'neutral', or 'contradiction'.

Acc: 19.20%, prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Acc: 16.90%, prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction'.
Acc: 11.20%, prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'.
Acc: 11.00%, prompt: While performing entailment analysis, classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction'.
Acc: 10.20%, prompt: As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment', 'neutral', or 'contradiction'.
Acc: 10.10%, prompt: As a tool for determining entailment relationships, review the two statements and categorize their connection as either 'entailment', 'neutral', or 'contradiction'.
Acc: 6.30%, prompt: In the capacity of an entailment assessment system, indicate if the link between the following sentences is 'entailment', 'neutral', or 'contradiction'.
Acc: 3.80%, prompt: Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment', 'neutral', or 'contradiction'.
Acc: 1.10%, prompt: Working as an entailment classifier, identify whether the given pair of sentences displays entailment, neutral, or contradiction. Respond with 'entailment', 'neutral', or 'contradiction'.
Acc: 0.50%, prompt: Acting as an entailment detection instrument, determine if the given pair of sentences demonstrates entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'.

## bertattack

Original prompt: Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Assess the situation between the following objects and classify it as 'entailment', 'neutral', or 'contradiction'. "
Original acc: 25.10%, attacked acc: 0.90%, dropped acc: 24.20%

Original prompt: Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Please state the relationship between the provided data as 'entailment', 'neutral', or 'contradiction'. "
Original acc: 21.30%, attacked acc: 0.70%, dropped acc: 20.60%

Original prompt: Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'. "
Original acc: 9.60%, attacked acc: 9.60%, dropped acc: 11.70%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"In your use as an entailment analysis utility, estimate the relation between the provided contexts and classify it as 'entailment', 'neutral', or 'contradiction'. "
Original acc: 19.20%, attacked acc: 0.00%, dropped acc: 19.20%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"As an entailment identification tree, determine the communication between the following words and answer with 'entailment', 'neutral', or 'contradiction'. "
Original acc: 16.90%, attacked acc: 0.00%, dropped acc: 16.90%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"is the role of a descriptive relationship analyzer, consider the connection between the given words and make if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'. "
Original acc: 11.20%, attacked acc: 0.00%, dropped acc: 11.20%

## checklist

Original prompt: Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction' yh912BU8T0. "
Original acc: 25.10%, attacked acc: 3.70%, dropped acc: 21.40%

Original prompt: Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction' Q47Jmd4lMV. "
Original acc: 21.30%, attacked acc: 2.60%, dropped acc: 18.70%

Original prompt: Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction' w52rwgo0Av. "
Original acc: 9.60%, attacked acc: 4.60%, dropped acc: 5.00%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction' Q47Jmd4lMV. "
Original acc: 19.20%, attacked acc: 7.10%, dropped acc: 12.10%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction' Pbl3tYuoRo. "
Original acc: 16.90%, attacked acc: 1.40%, dropped acc: 15.50%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction' Pbl3tYuoRo. "
Original acc: 11.20%, attacked acc: 6.70%, dropped acc: 4.50%

## deepwordbug

Original prompt: Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction'. Attacked prompt: b"Assess the cqnnection between the ollowing sentenceX and Mlassify it as 'entailment', 'neutral', or 'contradiction'. " Original acc: 25.10%, attacked acc: 4.30%, dropped acc: 20.80%

Original prompt: Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction'. Attacked prompt: b"Pltase Nlassify the relationshpi between the provided sentencXs as 'entailment', 'neutral', or 'contradiction'. " Original acc: 21.40%, attacked acc: 1.60%, dropped acc: 19.80%

Original prompt: Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'. Attacked prompt: b"Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'. " Original acc: 9.80%, attacked acc: 9.80%, dropped acc: 11.60%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'. Attacked prompt: b"IZn your roKe as an entailment analysis tool, ssess the relationyship between the givne sentences and classify it as 'entailment', 'neutral', or 'contradiction'. " Original acc: 19.50%, attacked acc: 1.60%, dropped acc: 17.90%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction'. Attacked prompt: b"mAs an entailment identification Cystem, examine the connetcion between the following sentenceCs and respond with 'entailment', 'neutral', or 'contradiction'. " Original acc: 17.00%, attacked acc: 0.80%, dropped acc: 16.20%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'. Attacked prompt: b"Ic the role of a semaintic relationhsip analyzeer, examine the connection between the given Osentences and decide if they exhbiit entailment, neutral, or contradiction. Afswer with 'entailment', 'neutral', or 'contradiction'. " Original acc: 11.20%, attacked acc: 0.20%, dropped acc: 11.00%

## stresstest

Original prompt: Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction'  and true is true . "
Original acc: 25.10%, attacked acc: 1.80%, dropped acc: 23.30%

Original prompt: Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 21.30%, attacked acc: 5.30%, dropped acc: 16.00%

Original prompt: Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'  and false is not true . "
Original acc: 9.60%, attacked acc: 4.50%, dropped acc: 5.10%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 19.20%, attacked acc: 15.60%, dropped acc: 3.60%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction'  and true is true . "
Original acc: 16.90%, attacked acc: 0.60%, dropped acc: 16.30%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 11.20%, attacked acc: 3.20%, dropped acc: 8.00%

## textbugger

Original prompt: Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Assess the link between the \xf0\x9d\x9a\x8following sentence and c\xe2\x85\xbcassify it as 'entailment', 'neutral', or 'contradiction'. "
Original acc: 25.10%, attacked acc: 0.30%, dropped acc: 24.80%

Original prompt: Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Invite categorize the relationshp between the provided sentences as 'entailment', 'neutral', or 'contradiction'. "
Original acc: 21.30%, attacked acc: 0.70%, dropped acc: 20.60%

Original prompt: Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'. "
Original acc: 9.60%, attacked acc: 9.60%, dropped acc: 11.70%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"In your role as an entailment analysi\xd1\x95 to\xd0\xbel, evaluate the relationship between the awarded sen\xf0\x9d\x9a\x9dences and classify it as 'entailment', 'neutral', or 'contradiction'. "
Original acc: 19.20%, attacked acc: 2.40%, dropped acc: 16.80%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"As an entailment identifying sytsem, examine the connec\xf0\x9d\x9a\x9dion between the \xf0\x9d\x9a\x8following sentence and respond with 'entailment', 'neutral', or 'contradiction'. "
Original acc: 16.90%, attacked acc: 0.90%, dropped acc: 16.00%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"During the role of a se\xef\xbd\x8dantic relationship analy\xe1\xb4\xa2er, examine the connection between the awarded sentences and determine if they exhibi\xf0\x9d\x9a\x9d entailment, neutral, or contradiction. Ans wer with 'entailment', 'neutral', or 'contradiction'. "
Original acc: 11.20%, attacked acc: 0.00%, dropped acc: 11.20%

## textfooler

Original prompt: Assess the connection between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Assess the link between the later judgments and classify it as 'entailment', 'neutral', or 'contradiction'. "
Original acc: 25.10%, attacked acc: 1.10%, dropped acc: 24.00%

Original prompt: Please classify the relationship between the provided sentences as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Asking classify the dealings between the provided condemning as 'entailment', 'neutral', or 'contradiction'. "
Original acc: 21.30%, attacked acc: 0.80%, dropped acc: 20.50%

Original prompt: Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Review the two statements and categorize their relationship as either 'entailment', 'neutral', or 'contradiction'. "
Original acc: 9.60%, attacked acc: 9.60%, dropped acc: 11.70%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"During your role as an entailment investigate utility, appraisals the relationships between the offered sentences and categorized it as 'entailment', 'neutral', or 'contradiction'. "
Original acc: 19.20%, attacked acc: 1.10%, dropped acc: 18.10%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"As an entailment determining system, examine the respecting between the following judgement and respond with 'entailment', 'neutral', or 'contradiction'. "
Original acc: 16.90%, attacked acc: 0.00%, dropped acc: 16.90%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment, neutral, or contradiction. Answer with 'entailment', 'neutral', or 'contradiction'.
Attacked prompt: b"Per the role of a semantic relationship analyzer, examine the connection between the offered sentences and determines if they fairs entailment, neutral, or contradiction. Response with 'entailment', 'neutral', or 'contradiction'. "
Original acc: 11.20%, attacked acc: 0.10%, dropped acc: 11.10%

# mrpc

## 10 prompts

Acc: 69.36%, prompt: Determine if the meanings of the following sentences are semantically equivalent by responding with 'equivalent' or 'not_equivalent'.
Acc: 68.38%, prompt: Assess if the two given sentences have equivalent meanings by selecting 'equivalent' or 'not_equivalent'.
Acc: 67.65%, prompt: Do the meanings of these two statements align? Indicate your answer with 'equivalent' or 'not_equivalent'.
Acc: 65.69%, prompt: Are the meanings of the following pair of sentences the same? Answer with 'equivalent' or 'not_equivalent'.
Acc: 65.69%, prompt: Can the given sentences be considered semantically identical? Please reply with 'equivalent' or 'not_equivalent'.
Acc: 63.48%, prompt: Evaluate whether the two provided sentences convey the same meaning by answering 'equivalent' or 'not_equivalent'.
Acc: 63.24%, prompt: Please analyze the provided sentences and indicate if their meanings are the same by choosing 'equivalent' or 'not_equivalent'.
Acc: 62.99%, prompt: Compare the following sentences and determine if they share the same semantic meaning by responding with 'equivalent' or 'not_equivalent'.
Acc: 62.01%, prompt: Do these two sentences have the same underlying meaning? Respond with 'equivalent' or 'not_equivalent'.
Acc: 47.06%, prompt: Examine the pair of sentences and decide if their meanings are identical by answering with 'equivalent' or 'not_equivalent'.

Acc: 69.12%, prompt: In your capacity as a semantic assessment tool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent'.
Acc: 68.38%, prompt: As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent'.
Acc: 68.14%, prompt: In the role of a sentence comparison analyst, assess the provided sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent'.
Acc: 67.89%, prompt: As a sentence similarity evaluator, analyze the provided sentences and indicate if their meanings are 'equivalent' or 'not_equivalent'.
Acc: 66.91%, prompt: In your capacity as a language analyst, assess the following sentences and classify their similarity as 'equivalent' or 'not_equivalent'.
Acc: 66.67%, prompt: In your capacity as a semantic comparison tool, examine the given sentences and decide if their meanings are identical, responding with 'equivalent' or 'not_equivalent'.
Acc: 66.18%, prompt: In the role of a textual comparison specialist, examine the given sentences and decide if they share the same meaning, responding with 'equivalent' or 'not_equivalent'.
Acc: 65.69%, prompt: As a language comparison expert, examine the given pair of sentences and decide if their meanings align, answering with 'equivalent' or 'not_equivalent'.
Acc: 63.24%, prompt: As a linguistic comparator, review the following pair of sentences and determine their semantic equivalence by choosing 'equivalent' or 'not_equivalent'.
Acc: 60.78%, prompt: As a textual similarity evaluator, analyze the following pair of sentences and determine if they are semantically 'equivalent' or 'not_equivalent'.

## bertattack

Original prompt: Determine if the meanings of the following sentences are semantically equivalent by responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Determine if the words of the following sentence are semanticdouble equivalent by thinking with 'equivalent' or 'not_equivalent'. "
Original acc: 69.36%, attacked acc: 33.33%, dropped acc: 36.03%

Original prompt: Assess if the two given sentences have equivalent meanings by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Assess if the two given statements have equivalent meanings by removing 'equivalent' or 'not_equivalent'. "
Original acc: 68.38%, attacked acc: 61.52%, dropped acc: 6.86%

Original prompt: Do the meanings of these two statements align? Indicate your answer with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Do the function of these two statements align? enter your answer with 'equivalent' or 'not_equivalent'. "
Original acc: 67.65%, attacked acc: 49.02%, dropped acc: 18.63%

Original prompt: In your capacity as a semantic assessment tool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"In your capacity as a knowledge assessment tool, consider the following sentences and classify their components as 'equivalent' or 'not_equivalent'. "
Original acc: 69.12%, attacked acc: 55.88%, dropped acc: 13.24%

Original prompt: As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent'.
Attacked prompt: b"to a wikipedia comparison expert, evaluate the given couple of sentences and know if they are 'equivalent' or 'not_equivalent'. "
Original acc: 68.38%, attacked acc: 55.64%, dropped acc: 12.75%

Original prompt: In the role of a sentence comparison analyst, assess the provided sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"to the role of a face comparison instance, assess the following sentences and indicate if they describe the same person by selecting 'equivalent' or 'not_equivalent'. "
Original acc: 68.14%, attacked acc: 17.16%, dropped acc: 50.98%

## checklist

Original prompt: Determine if the meanings of the following sentences are semantically equivalent by responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Determine if the meanings of the following sentences are semantically equivalent by responding with 'equivalent' or 'not_equivalent' SFPCqpiClT. "
Original acc: 69.36%, attacked acc: 62.01%, dropped acc: 7.35%

Original prompt: Assess if the two given sentences have equivalent meanings by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Assess if the two given sentences have equivalent meanings by selecting 'equivalent' or 'not_equivalent' bhrRSokrfa. "
Original acc: 68.38%, attacked acc: 62.25%, dropped acc: 6.13%

Original prompt: Do the meanings of these two statements align? Indicate your answer with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Do the meanings of these two statements align? Indicate your answer with 'equivalent' or 'not_equivalent' SFPCqpiClT. "
Original acc: 67.65%, attacked acc: 63.97%, dropped acc: 3.68%

Original prompt: In your capacity as a semantic assessment tool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"In your capacity as a semantic assessment tool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent' ofOQXLxiW4. "
Original acc: 69.12%, attacked acc: 65.20%, dropped acc: 3.92%

Original prompt: As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent'.
Attacked prompt: b"As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent' bhrRSokrfa. "
Original acc: 68.38%, attacked acc: 66.91%, dropped acc: 1.47%

Original prompt: In the role of a sentence comparison analyst, assess the provided sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"In the role of a sentence comparison analyst, assess the provided sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent' xikCjkMydH. "
Original acc: 68.14%, attacked acc: 58.09%, dropped acc: 10.05%

## deepwordbug

Original prompt: Determine if the meanings of the following sentences are semantically equivalent by responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"DeterOine if the meanings of the followjing senteJnces are sCmantically equivalent by resgonding with 'equivalent' or 'not_equivalent'. "
Original acc: 69.85%, attacked acc: 64.46%, dropped acc: 5.39%

Original prompt: Assess if the two given sentences have equivalent meanings by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"AssesHs if the two giken sKentences have equivalent meanings by seDecting 'equivalent' or 'not_equivalent'. "
Original acc: 68.38%, attacked acc: 60.54%, dropped acc: 7.84%

Original prompt: Do the meanings of these two statements align? Indicate your answer with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Zo the meanings of these Xwo statements Ualign? IndicNte your answeY with 'equivalent' or 'not_equivalent'. "
Original acc: 67.65%, attacked acc: 36.76%, dropped acc: 30.88%

Original prompt: In your capacity as a semantic assessment tool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"nI your capacitCy as a sebmantic assgssment otol, evaluate the provided sentenceAs and Zlassify their meaniPgs as 'equivalent' or 'not_equivalent'. "
Original acc: 69.12%, attacked acc: 34.31%, dropped acc: 34.80%

Original prompt: As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent'.
Attacked prompt: b"bAs a selantic comparuson exZert, evaluate the given pair of sentences and deermine if they are 'equivalent' or 'not_equivalent'. "
Original acc: 68.38%, attacked acc: 54.90%, dropped acc: 13.48%

Original prompt: In the role of a sentence comparison analyst, assess the provided sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"GIn the role of a senteLnce comparisoU anNlyst, assess the provided sentences and indicate if they dconvey the same meaJning by selecting 'equivalent' or 'not_equivalent'. "
Original acc: 68.14%, attacked acc: 37.75%, dropped acc: 30.39%

## stresstest

Original prompt: Determine if the meanings of the following sentences are semantically equivalent by responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Determine if the meanings of the following sentences are semantically equivalent by responding with 'equivalent' or 'not_equivalent'  and true is true . "
Original acc: 69.36%, attacked acc: 69.36%, dropped acc: 0.00%

Original prompt: Assess if the two given sentences have equivalent meanings by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Assess if the two given sentences have equivalent meanings by selecting 'equivalent' or 'not_equivalent'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 68.38%, attacked acc: 69.36%, dropped acc: -0.98%

Original prompt: Do the meanings of these two statements align? Indicate your answer with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Do the meanings of these two statements align? Indicate your answer with 'equivalent' or 'not_equivalent'  and false is not true . "
Original acc: 67.65%, attacked acc: 67.40%, dropped acc: 0.25%

Original prompt: In your capacity as a semantic assessment tool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"In your capacity as a semantic assessment tool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent'  and false is not true . "
Original acc: 69.12%, attacked acc: 64.22%, dropped acc: 4.90%

Original prompt: As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent'.
Attacked prompt: b"As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent'  and false is not true . "
Original acc: 68.38%, attacked acc: 68.63%, dropped acc: -0.25%

Original prompt: In the role of a sentence comparison analyst, assess the provided sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"In the role of a sentence comparison analyst, assess the provided sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent'  and false is not true . "
Original acc: 68.14%, attacked acc: 59.80%, dropped acc: 8.33%

## textbugger

Original prompt: Determine if the meanings of the following sentences are semantically equivalent by responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Determie if the mean ings of the following sentences are semantically equivalent by respondi\xd5\xb8g with 'equivalent' or 'not_equivalent'. "
Original acc: 69.36%, attacked acc: 45.59%, dropped acc: 23.77%

Original prompt: Assess if the two given sentences have equivalent meanings by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Assessing if the t wo given sentences have equivalent meanings by selecti\xd5\xb8g 'equivalent' or 'not_equivalent'. "
Original acc: 68.38%, attacked acc: 44.61%, dropped acc: 23.77%

Original prompt: Do the meanings of these two statements align? Indicate your answer with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Do the meaning of these dos stateme\xd5\xb8ts aligns? Indicate your answer with 'equivalent' or 'not_equivalent'. "
Original acc: 67.65%, attacked acc: 45.10%, dropped acc: 22.55%

Original prompt: In your capacity as a semantic assessment tool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"At your capacity as a se\xef\xbd\x8dantic asse ssment \xf0\x9d\x9a\x9dool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent'. "
Original acc: 69.12%, attacked acc: 53.92%, dropped acc: 15.20%

Original prompt: As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent'.
Attacked prompt: b"As a sema\xd5\xb8tic com\xd1\x80arison expert, evaluate the given pair of sentences and \xd4\x81etermine if they are 'equivalent' or 'not_equivalent'. "
Original acc: 68.38%, attacked acc: 50.25%, dropped acc: 18.14%

Original prompt: In the role of a sentence comparison analyst, assess the provided sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Onto the role of a sente\xd5\xb8ce c omparison analys\xf0\x9d\x9a\x9d, assess the given sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent'. "
Original acc: 68.14%, attacked acc: 44.36%, dropped acc: 23.77%

## textfooler

Original prompt: Determine if the meanings of the following sentences are semantically equivalent by responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Decide if the senses of the following sentence are semantically equivalent by meet with 'equivalent' or 'not_equivalent'. "
Original acc: 69.36%, attacked acc: 35.54%, dropped acc: 33.82%

Original prompt: Assess if the two given sentences have equivalent meanings by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Ascertain if the two made sentences did equivalent meanings by option 'equivalent' or 'not_equivalent'. "
Original acc: 68.38%, attacked acc: 45.10%, dropped acc: 23.28%

Original prompt: Do the meanings of these two statements align? Indicate your answer with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Making the senses of these two sermons realign? Reflect your reply with 'equivalent' or 'not_equivalent'. "
Original acc: 67.65%, attacked acc: 46.81%, dropped acc: 20.83%

Original prompt: In your capacity as a semantic assessment tool, evaluate the provided sentences and classify their meanings as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Towards your aptitude as a semantic exams paraphernalia, evaluate the furnished sentences and classify their connotation as 'equivalent' or 'not_equivalent'. "
Original acc: 69.12%, attacked acc: 51.47%, dropped acc: 17.65%

Original prompt: As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent'.
Attacked prompt: b"As a semantic comparison whiz, evaluate the given couple of sentences and determine if they are 'equivalent' or 'not_equivalent'. "
Original acc: 68.38%, attacked acc: 64.22%, dropped acc: 4.17%

Original prompt: In the role of a sentence comparison analyst, assess the provided sentences and indicate if they convey the same meaning by selecting 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Towards the feature of a judgements versus psychoanalyst, reviews the supplied sentences and clarified if they convey the same senses by electing 'equivalent' or 'not_equivalent'. "
Original acc: 68.14%, attacked acc: 13.24%, dropped acc: 54.90%

## translation

Language: chinese, acc: 69.36%, prompt: As an expert in semantic comparison, evaluates two given sentences to determine whether they are 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 68.14%, prompt: From the point of view of semantic comparison, determine whether this pair of sentences is 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 63.73%, prompt: Using the semantic comparison method, determine whether the following two statements are 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 64.95%, prompt: For the following two sentences, determine whether they are 'equivalent' or 'not_equivalent' based on semantic comparison.
Language: chinese, acc: 62.01%, prompt: As an expert in semantic comparison, please evaluate the following two sentences and determine if they are 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 64.46%, prompt: Using semantic comparison techniques, determine whether the following two sentences are 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 65.44%, prompt: Please determine whether the following two sentences are 'equivalent' or 'not_equivalent' according to the standard of semantic comparison.
Language: chinese, acc: 59.56%, prompt: As an expert in the field of semantic comparison, please evaluate the following two sentences and determine whether they are 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 64.46%, prompt: Using semantic comparison, determine whether the following two sentences are 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 66.18%, prompt: Determine whether the following two sentences are 'equivalent' or 'not_equivalent' based on semantic comparison.
Language: french, acc: 66.67%, prompt: As an expert in semantic comparison, evaluate the following pair of sentences and determine whether they are 'equivalent' or 'not_equivalent'.
Language: french, acc: 68.63%, prompt: Can you determine whether the following two sentences are 'equivalent' or 'not_equivalent' as a semantic comparison expert?
Language: french, acc: 65.69%, prompt: Using your expertise in semantic comparison, determine whether the following two sentences are 'equivalent' or 'not_equivalent'.
Language: french, acc: 68.63%, prompt: As a semantic comparison specialist, assess the similarity between the following two sentences and determine whether they are 'equivalent' or 'not_equivalent'.
Language: french, acc: 59.56%, prompt: Are you able to determine whether the following two sentences are 'equivalent' or 'not_equivalent' as an expert in semantic comparison?
Language: french, acc: 65.20%, prompt: As a semantic comparison professional, evaluate the following pair of sentences and indicate whether they are 'equivalent' or 'not_equivalent'.
Language: french, acc: 58.33%, prompt: Can you determine whether the following two sentences have a 'equivalent' or 'not_equivalent' meaning as an expert in semantic comparison?
Language: french, acc: 68.63%, prompt: As an expert in semantic comparison, assess the similarity between the following two sentences and determine whether they are 'equivalent' or 'not_equivalent'.
Language: french, acc: 65.69%, prompt: Using your expertise in semantic comparison, determine whether the following two sentences are 'equivalent' or 'not_equivalent' in terms of meaning.
Language: french, acc: 67.40%, prompt: As a semantic comparison professional, assess the similarity between the following two sentences and indicate whether they are 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 68.14%, prompt: As an expert in semantic comparison, evaluate the two given sentences and determine whether they are 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 64.46%, prompt: Based on my experience in semantic analysis, classify the following two sentences as 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 66.18%, prompt: As an expert in semantic comparison, analyze the following two sentences and classify them as 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 67.40%, prompt: Your task as an expert in semantic comparison is to evaluate the following two sentences and determine whether they are 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 54.90%, prompt: As a semantic comparison specialist, analyze the two data statements and insert them into one of the following categories: 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 61.52%, prompt: Based on my experience in semantic analysis, classify the following two sentences between 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 68.63%, prompt: Your role as a semantic comparison specialist requires analyzing the two given sentences and determining whether they are 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 65.69%, prompt: As an experienced semantic analyst, classify the following two sentences as 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 68.63%, prompt: Your job as a semantic analyst evaluates the following two sentences as 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 69.12%, prompt: As a semantic analyst, determine whether the given sentences are 'equivalent' or 'not_equivalent' based on their relationship.
Language: spanish, acc: 68.87%, prompt: As an expert in semantic comparison, it evaluates the pair of sentences provided and determines whether they are 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 64.46%, prompt: Based on my experience in semantic analysis, classify the following two sentences as 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 67.89%, prompt: As an expert in semantic comparison, analyze the two sentences given and classify them as 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 67.16%, prompt: Your task as a semantic comparison specialist is to evaluate the following two sentences and determine whether they are 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 68.14%, prompt: As an expert in semantic analysis, he makes a classification of the following two sentences based on their 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 65.69%, prompt: Based on your experience of semantic comparison, classify the next two sentences as 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 68.38%, prompt: As a specialist in semantic analysis, you are given the task of analysing the two sentences given and classifying them as 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 68.38%, prompt: As an expert in semantic comparison, he classifies the following two sentences into 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 66.67%, prompt: As a specialist in semantic analysis, evaluate the following two sentences and classify them as 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 69.61%, prompt: Your task as an expert in semantic comparison is to analyze the two sentences provided and determine whether they are 'equivalent' or 'not_equivalent' based on their semantic relationship.
Language: japanese, acc: 64.22%, prompt: Evaluate whether a given pair of sentences is 'equivalent' or 'not_equivalent', depending on the context.
Language: japanese, acc: 66.18%, prompt: Use a semantic comparison to determine whether a given pair of sentences is 'equivalent' or 'not_equivalent'.
Language: japanese, acc: 69.36%, prompt: Evaluate a given pair of sentences as 'equivalent' or 'not_equivalent' by determining whether they have the same semantic meaning.
Language: japanese, acc: 61.52%, prompt: Determine whether a given pair of sentences is synonyms and evaluate whether they are 'equivalent' or 'not_equivalent'.
Language: japanese, acc: 68.38%, prompt: Determine whether a given pair of sentences is 'equivalent' or 'not_equivalent', and whether they are semantically identical.
Language: japanese, acc: 63.73%, prompt: Determinate whether a given pair of sentences has the same meaning and evaluate whether they are 'equivalent' or 'not_equivalent'.
Language: japanese, acc: 67.65%, prompt: Evaluate whether a given pair of sentences is 'equivalent' or 'not_equivalent' by determining whether they are semantically identical.
Language: japanese, acc: 65.69%, prompt: Judge whether a given pair of sentences is equal and evaluate whether they are 'equivalent' or 'not_equivalent'.
Language: japanese, acc: 64.46%, prompt: Determinate whether a given pair of sentences are semantically equal and evaluate whether they are 'equivalent' or 'not_equivalent'.
Language: japanese, acc: 63.73%, prompt: Whether a given pair of sentences is 'equivalent' or 'not_equivalent' depends on the context.
Language: korean, acc: 69.36%, prompt: As a sentence comparator, evaluate the two sentences given to determine 'equivalent' or 'not_equivalent'.
Language: korean, acc: 70.83%, prompt: Compare two sentences to determine 'equivalent' or 'not_equivalent'. For this you need qualifications as a specialist in semantic comparison.
Language: korean, acc: 69.12%, prompt: It takes your knowledge as an expert in semantic comparison to determine that two sentences are 'equivalent' or 'not_equivalent'.
Language: korean, acc: 67.89%, prompt: As a specialist in semantic comparison, evaluate whether two given sentences are 'equivalent' or 'not_equivalent'.
Language: korean, acc: 68.38%, prompt: Analyze two sentences to determine 'equivalent' or 'not_equivalent'. For that you need the knowledge of a semantic comparison expert.
Language: korean, acc: 68.38%, prompt: As an expert in semantic comparison, decide whether two sentences are 'equivalent' or 'not_equivalent'.
Language: korean, acc: 71.57%, prompt: It takes the knowledge of an expert in semantic comparison to compare two sentences to judge 'equivalent' or 'not_equivalent'.
Language: korean, acc: 69.61%, prompt: Experience as an expert in semantic comparison is required to determine whether two given sentences are 'equivalent' or 'not_equivalent'.
Language: korean, acc: 68.38%, prompt: As an expert in semantic comparison, determine whether two sentences are 'equivalent' or 'not_equivalent'.
Language: korean, acc: 70.10%, prompt: Analyze two sentences to determine 'equivalent' or 'not_equivalent'. For this, you need a qualification as a specialist in semantic comparison.

# qnli

## 10 prompts

Acc: 42.70%, prompt: Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment'.
Acc: 41.20%, prompt: Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment'.
Acc: 38.90%, prompt: Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment'.
Acc: 38.10%, prompt: Assess if the answer to the question can be logically concluded from the provided context by choosing 'entailment' or 'not_entailment'.
Acc: 37.20%, prompt: Given the question and context provided, determine if the answer can be inferred by choosing 'entailment' or 'not_entailment'.
Acc: 30.90%, prompt: Please assess if the answer to the question can be derived from the given context by selecting 'entailment' or 'not_entailment'.
Acc: 28.30%, prompt: Examine the context and question, and determine if the context logically implies the answer by selecting 'entailment' or 'not_entailment'.
Acc: 21.90%, prompt: Based on the provided context and question, decide if the information supports the answer by responding with 'entailment' or 'not_entailment'.
Acc: 20.20%, prompt: Evaluate whether the given context supports the answer to the question by responding with 'entailment' or 'not_entailment'.
Acc: 19.00%, prompt: Consider the context and question, and indicate if the answer can be logically deduced from the context by responding with 'entailment' or 'not_entailment'.

Acc: 42.90%, prompt: As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment'.
Acc: 41.40%, prompt: As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment'.
Acc: 35.50%, prompt: As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment'.
Acc: 31.30%, prompt: In the capacity of a language specialist, decide if the context presented contains enough information to infer the answer to the question and respond with 'entailment' or 'not_entailment'.
Acc: 31.00%, prompt: In your role as a linguistic investigator, determine if the context given entails the answer to the question and provide your conclusion with 'entailment' or 'not_entailment'.
Acc: 29.20%, prompt: In the capacity of a language evaluator, examine if the given context justifies the answer to the question and indicate your assessment with 'entailment' or 'not_entailment'.
Acc: 29.10%, prompt: In your role as a semantic evaluator, determine if the provided context justifies the answer to the question and answer with 'entailment' or 'not_entailment'.
Acc: 27.50%, prompt: As a language expert, assess if the given context entails the answer to the question and respond with 'entailment' or 'not_entailment'.
Acc: 19.80%, prompt: As a semantic interpreter, assess whether the provided context supports the answer to the given question and answer with 'entailment' or 'not_entailment'.
Acc: 14.10%, prompt: As a textual analyst, examine if the given context logically implies the answer to the question and indicate your decision with 'entailment' or 'not_entailment'.

## bertattack

Original prompt: Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment'.
Attacked prompt: b"play the provided topic and word, and decision if the context contains enough information to determine the answers by creating 'entailment' or 'not_entailment'. "
Original acc: 42.70%, attacked acc: 0.10%, dropped acc: 42.60%

Original prompt: Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"Based on the information in the context, decide if the answer to the is is committed by versus 'entailment' or 'not_entailment'. "
Original acc: 41.20%, attacked acc: 0.00%, dropped acc: 41.20%

Original prompt: Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"s the context and what, and indicate if the context entails the answer by avoiding 'entailment' or 'not_entailment'. "
Original acc: 38.90%, attacked acc: 2.20%, dropped acc: 36.70%

Original prompt: As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"As a linguistics consultant, determined if the answers to the asked is logical. supported by the provided topic and task with 'entailment' or 'not_entailment'. "
Original acc: 42.90%, attacked acc: 0.30%, dropped acc: 42.60%

Original prompt: As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment'.
Attacked prompt: b"As a semantic researcher, evaluate should the supplied context supports the concept to the task and seek 'entailment' or 'not_entailment'. "
Original acc: 41.40%, attacked acc: 0.10%, dropped acc: 41.30%

Original prompt: As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment'.
Attacked prompt: b"As a textual inference expert, write if the answer to the task can be deduced from the supplied instance and search 'entailment' or 'not_entailment'. "
Original acc: 35.50%, attacked acc: 0.00%, dropped acc: 35.50%

## checklist

Original prompt: Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment'.
Attacked prompt: b"Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment' zexKUTWJYG. "
Original acc: 42.70%, attacked acc: 9.70%, dropped acc: 33.00%

Original prompt: Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment' zq0DcZ5dnI. "
Original acc: 41.20%, attacked acc: 1.10%, dropped acc: 40.10%

Original prompt: Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment' MSAddJ4D2a. "
Original acc: 38.90%, attacked acc: 5.50%, dropped acc: 33.40%

Original prompt: As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment' rzu98kF2KF. "
Original acc: 42.90%, attacked acc: 3.70%, dropped acc: 39.20%

Original prompt: As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment'.
Attacked prompt: b"As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment' d6ZQ3u0GBQ. "
Original acc: 41.40%, attacked acc: 1.00%, dropped acc: 40.40%

Original prompt: As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment'.
Attacked prompt: b"As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment' d6ZQ3u0GBQ. "
Original acc: 35.50%, attacked acc: 2.80%, dropped acc: 32.70%

## deepwordbug

Original prompt: Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment'.
Attacked prompt: b"RevTiew the ginen cEntext and uestion, and decid if the context conatains enough iformation to uspport the answVer by selectin 'entailment' or 'not_entailment'. "
Original acc: 42.70%, attacked acc: 0.20%, dropped acc: 42.50%

Original prompt: Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"Basvd on the information in the context, decZde if the answer to the question is jsutified by choosing 'entailment' or 'not_entailment'. "
Original acc: 41.20%, attacked acc: 6.90%, dropped acc: 34.30%

Original prompt: Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"ABalyze the dcontext and question, and indicte if the context entails the ansTwer by choosing 'entailment' or 'not_entailment'. "
Original acc: 39.00%, attacked acc: 0.30%, dropped acc: 38.70%

Original prompt: As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Abs a linguistic consultant, decide if the answer to the question is logically supported by the provided Aontext and respGond with 'entailment' or 'not_entailment'. "
Original acc: 42.90%, attacked acc: 1.80%, dropped acc: 41.10%

Original prompt: As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment'.
Attacked prompt: b"sA a semantic researcher, valuate whether the provided context supports the anshwer to the Equestion and cVhoose 'entailment' or 'not_entailment'. "
Original acc: 41.30%, attacked acc: 3.40%, dropped acc: 37.90%

Original prompt: As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment'.
Attacked prompt: b"sA a Zextual inference expert, analyze if the answeer to the question can be demuced from the provided cnotext and sKelect 'entailment' or 'not_entailment'. "
Original acc: 35.30%, attacked acc: 2.80%, dropped acc: 32.50%

## stresstest

Original prompt: Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment'.
Attacked prompt: b"Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 42.70%, attacked acc: 10.20%, dropped acc: 32.50%

Original prompt: Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 41.20%, attacked acc: 6.70%, dropped acc: 34.50%

Original prompt: Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 38.90%, attacked acc: 12.30%, dropped acc: 26.60%

Original prompt: As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 42.90%, attacked acc: 7.00%, dropped acc: 35.90%

Original prompt: As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment'.
Attacked prompt: b"As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 41.40%, attacked acc: 12.50%, dropped acc: 28.90%

Original prompt: As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment'.
Attacked prompt: b"As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 35.50%, attacked acc: 7.00%, dropped acc: 28.50%

## textbugger

Original prompt: Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment'.
Attacked prompt: b"Examination the given context and ques\xf0\x9d\x9a\x9dion, and deciding if the context con\xf0\x9d\x9a\x9dains enough information to support the answers by \xd1\x95electing 'entailment' or 'not_entailment'. "
Original acc: 42.70%, attacked acc: 1.30%, dropped acc: 41.40%

Original prompt: Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"Based on the info in the context, decision if the answer to the ques\xf0\x9d\x9a\x9dion is warranted by chosing 'entailment' or 'not_entailment'. "
Original acc: 41.20%, attacked acc: 3.70%, dropped acc: 37.50%

Original prompt: Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"Analyze the context and question, and depicts if the context involves the ans wer by choosi\xd5\xb8g 'entailment' or 'not_entailment'. "
Original acc: 38.90%, attacked acc: 0.70%, dropped acc: 38.20%

Original prompt: As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"A\xd1\x95 a \xe2\x85\xbcinguistic consultant, deciding if the answering to the quesiton is logically supported by the supplied context and cater with 'entailment' or 'not_entailment'. "
Original acc: 42.90%, attacked acc: 1.20%, dropped acc: 41.70%

Original prompt: As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment'.
Attacked prompt: b"As a semantic reesarcher, evaluating whether the provided context supports the answering to the question and chosen 'entailment' or 'not_entailment'. "
Original acc: 41.40%, attacked acc: 0.00%, dropped acc: 41.40%

Original prompt: As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment'.
Attacked prompt: b"As a textual infere\xd5\xb8ce expert, analyzes if the answer to the problem can be presumed from the provided context and selec\xf0\x9d\x9a\x9d 'entailment' or 'not_entailment'. "
Original acc: 35.50%, attacked acc: 0.10%, dropped acc: 35.40%

## textfooler

Original prompt: Review the given context and question, and decide if the context contains enough information to support the answer by selecting 'entailment' or 'not_entailment'.
Attacked prompt: b"Discuss the given context and tura, and decide if the context encompasses enough information to support the satisfy by takes 'entailment' or 'not_entailment'. "
Original acc: 42.70%, attacked acc: 0.00%, dropped acc: 42.70%

Original prompt: Based on the information in the context, decide if the answer to the question is justified by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"Based on the data in the context, pick if the answer to the tura is fide by choice 'entailment' or 'not_entailment'. "
Original acc: 41.20%, attacked acc: 0.20%, dropped acc: 41.00%

Original prompt: Analyze the context and question, and indicate if the context entails the answer by choosing 'entailment' or 'not_entailment'.
Attacked prompt: b"Analyse the context and question, and outlined if the context encompass the answers by options 'entailment' or 'not_entailment'. "
Original acc: 38.90%, attacked acc: 0.50%, dropped acc: 38.40%

Original prompt: As a linguistic consultant, decide if the answer to the question is logically supported by the provided context and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Iike a linguistic advisors, decisions if the answer to the item is logically argued by the provided context and cater with 'entailment' or 'not_entailment'. "
Original acc: 42.90%, attacked acc: 0.20%, dropped acc: 42.70%

Original prompt: As a semantic researcher, evaluate whether the provided context supports the answer to the question and choose 'entailment' or 'not_entailment'.
Attacked prompt: b"As a semantic researcher, appraisals whether the provided context supports the answer to the question and taking 'entailment' or 'not_entailment'. "
Original acc: 41.40%, attacked acc: 0.10%, dropped acc: 41.30%

Original prompt: As a textual inference expert, analyze if the answer to the question can be deduced from the provided context and select 'entailment' or 'not_entailment'.
Attacked prompt: b"Iike a textual deduction speciality, exams if the answer to the topics can be deduced from the lodged context and select 'entailment' or 'not_entailment'. "
Original acc: 35.50%, attacked acc: 0.30%, dropped acc: 35.20%

## translation

Language: chinese, acc: 28.40%, prompt: Determine whether the answer is implied or not based on the context. Answer 'entailment' or 'not_entailment'.
Language: chinese, acc: 25.70%, prompt: As a language expert, determine whether the text contains the answer and choose 'entailment' or 'not_entailment'.
Language: chinese, acc: 23.70%, prompt: Determine whether the text implies an answer, and select 'entailment' or 'not_entailment'.
Language: chinese, acc: 42.40%, prompt: Given the text and the question, whether the answer is implied, select 'entailment' or 'not_entailment'.
Language: chinese, acc: 28.80%, prompt: Determine whether the text contains the answer, depending on the context. Select 'entailment' or 'not_entailment'.
Language: chinese, acc: 34.50%, prompt: As a language expert, determine whether a text can contain an answer, and say 'entailment' or 'not_entailment'.
Language: chinese, acc: 34.90%, prompt: Please determine whether the text implies an answer. Answer 'entailment' or 'not_entailment'.
Language: chinese, acc: 34.40%, prompt: Please select 'entailment' or 'not_entailment' based on the text and the question.
Language: chinese, acc: 20.90%, prompt: Assess whether the answer is implied based on the context. Answer 'entailment' or 'not_entailment'.
Language: chinese, acc: 39.40%, prompt: Please determine whether the text contains the answer and answer 'entailment' or 'not_entailment'.
Language: french, acc: 37.60%, prompt: As a linguistic expert, assess whether the given context involves the answer to the question and answer with 'entailment' or 'not_entailment'.
Language: french, acc: 35.50%, prompt: Determine whether the information provided in the context necessarily leads to the answer to the question asked and indicate 'entailment' or 'not_entailment'.
Language: french, acc: 37.60%, prompt: Analyze the text to determine if the answer to the question is implied in the context and specify 'entailment' or 'not_entailment'.
Language: french, acc: 40.90%, prompt: Based on the given context, decide whether the answer to the question is necessarily involved and mark 'entailment' or 'not_entailment'.
Language: french, acc: 24.70%, prompt: Evaluate whether the answer to the question can be deduced from the given context and mark 'entailment' or 'not_entailment'.
Language: french, acc: 35.20%, prompt: Discern whether the context provided directly involves the answer to the question and indicate 'entailment' or 'not_entailment'.
Language: french, acc: 35.40%, prompt: Determine if the context contains enough information to involve the answer to the question and mark 'entailment' or 'not_entailment'.
Language: french, acc: 28.70%, prompt: Assess whether the context provided necessarily leads to the answer to the question and answer with 'entailment' or 'not_entailment'.
Language: french, acc: 42.50%, prompt: Analyze the text to determine if the answer to the question is involved in the context and indicate 'entailment' or 'not_entailment'.
Language: french, acc: 43.70%, prompt: Based on the given context, decide whether the answer to the question is necessarily inferred and mark 'entailment' or 'not_entailment'.
Language: arabic, acc: 37.10%, prompt: As a language expert, evaluate whether the given context calls for an answer and answer 'entailment' or 'not_entailment'.
Language: arabic, acc: 6.10%, prompt: Judge the relationship between the text and the question and answer 'entailment' or 'not_entailment', depending on your language experience.
Language: arabic, acc: 36.10%, prompt: Does the context given indicate the answer to the question? Evaluate and answer 'entailment' or 'not_entailment'.
Language: arabic, acc: 38.40%, prompt: Based on your linguistic knowledge, does the text relate to the question? Answer 'entailment' or 'not_entailment'.
Language: arabic, acc: 15.00%, prompt: As a language expert, determine how the text relates to the question and answer 'entailment' or 'not_entailment'.
Language: arabic, acc: 9.50%, prompt: Does the text support the answer to the question? Answer 'entailment' or 'not_entailment', depending on your language experience.
Language: arabic, acc: 5.70%, prompt: Check the text link to the question and answer 'entailment' or 'not_entailment', depending on your language skills.
Language: arabic, acc: 45.50%, prompt: As a language expert, is there a link between the text and the question? Answer 'entailment' or 'not_entailment'.
Language: arabic, acc: 18.70%, prompt: Based on your language experience, does context help to answer the question? Evaluate and answer 'entailment' or 'not_entailment'.
Language: arabic, acc: 6.30%, prompt: Does the text give a clear answer to the question? Answer 'entailment' or 'not_entailment', depending on your language experience.
Language: spanish, acc: 32.90%, prompt: As a language expert, evaluate whether the given context implies the answer to the question and answer with 'entailment' or 'not_entailment'.
Language: spanish, acc: 38.00%, prompt: Determine whether the information given in the text necessarily implies the veracity of the hypothesis and answer 'entailment' or 'not_entailment'.
Language: spanish, acc: 32.60%, prompt: Analyzes whether the information presented in the paragraph leads to the conclusion of the question and labels the answer as 'entailment' or 'not_entailment'.
Language: spanish, acc: 30.50%, prompt: Indicates whether the information provided in the text is sufficient to conclude the statement and labels the response as 'entailment' or 'not_entailment'.
Language: spanish, acc: 35.00%, prompt: As an expert on the subject, judge whether the information provided in the text justifies the claim and classify the answer as 'entailment' or 'not_entailment'.
Language: spanish, acc: 25.10%, prompt: Evaluates whether the information in the paragraph necessarily supports the conclusion of the hypothesis and responds 'entailment' or 'not_entailment'.
Language: spanish, acc: 19.50%, prompt: Determines whether the information presented in the text logically implies the answer to the question and labels the answer as 'entailment' or 'not_entailment'.
Language: spanish, acc: 22.20%, prompt: Analyzes whether the information provided in the paragraph necessarily leads to the veracity of the hypothesis and classifies the response as 'entailment' or 'not_entailment'.
Language: spanish, acc: 40.70%, prompt: As an expert on the subject, evaluate whether the information presented in the text supports the claim and respond 'entailment' or 'not_entailment'.
Language: spanish, acc: 40.20%, prompt: Indicates whether the information provided in the paragraph necessarily implies the answer to the question and labels the answer as 'entailment' or 'not_entailment'.
Language: japanese, acc: 12.90%, prompt: Rate whether the answer to the question is derived from the given context and answer with 'entailment' or 'not_entailment'.
Language: japanese, acc: 38.40%, prompt: Please answer 'entailment' or 'not_entailment' for the given context and question.
Language: japanese, acc: 42.60%, prompt: Decide whether the answer to the question is derived from the given context and answer 'entailment' or 'not_entailment'.
Language: japanese, acc: 41.70%, prompt: Compare the question with the given context and give the answer 'entailment' or 'not_entailment'.
Language: japanese, acc: 41.40%, prompt: Determinate whether the given context contains the answer to the question and answer with 'entailment' or 'not_entailment'.
Language: japanese, acc: 40.00%, prompt: Estimate the answer of the question from the context and give the answer 'entailment' or 'not_entailment'.
Language: japanese, acc: 32.00%, prompt: Determinate whether the given context is relevant to the question and answer with 'entailment' or 'not_entailment'.
Language: japanese, acc: 21.80%, prompt: Determine whether the given context is relevant to the question and answer with 'entailment' or 'not_entailment'.
Language: japanese, acc: 39.40%, prompt: Determinate whether the given context contains the answer to the question and answer 'entailment' or 'not_entailment'.
Language: japanese, acc: 26.30%, prompt: Answer with 'entailment' or 'not_entailment', inferring from the given context.
Language: korean, acc: 30.40%, prompt: Determine if a given sentence necessarily implies the meaning of another sentence and answer 'entailment' or 'not_entailment'.
Language: korean, acc: 18.40%, prompt: By understanding the relations between sentences, judge whether a given sentence necessarily refers to another sentence and answer with 'entailment' or 'not_entailment'.
Language: korean, acc: 17.50%, prompt: Evaluate whether a given text necessarily indicates the meaning of another text and respond with 'entailment' or 'not_entailment'.
Language: korean, acc: 4.80%, prompt: Understand the relations of a sentence, to determine whether a given sentence necessarily includes other sentences and answer with 'entailment' or 'not_entailment'.
Language: korean, acc: 27.90%, prompt: Judge whether a given content necessarily implies the meaning of another content and answer with 'entailment' or 'not_entailment'.
Language: korean, acc: 1.60%, prompt: Grasp the relations between sentences, determine if a given sentence necessarily contains the meaning of another sentence and respond with 'entailment' or 'not_entailment'.
Language: korean, acc: 26.70%, prompt: Evaluate whether a given text necessarily refers to another text and answer with 'entailment' or 'not_entailment'.
Language: korean, acc: 20.50%, prompt: By comparing the meaning of the sentences, to determine if a given sentence necessarily implies another sentence and answer 'entailment' or 'not_entailment'.
Language: korean, acc: 33.20%, prompt: Evaluate whether the contents given necessarily refer to other contents and answer with 'entailment' or 'not_entailment'.
Language: korean, acc: 31.70%, prompt: By analyzing the relations between sentences, determine if a given sentence does not necessarily include other sentences and answer with 'entailment' or 'not_entailment'.

# qqp

## 10 prompts

Acc: 41.80%, prompt: Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent'.
Acc: 38.10%, prompt: Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent'.
Acc: 36.50%, prompt: Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent'.
Acc: 35.10%, prompt: Do these two sentences convey the same meaning? Indicate with 'equivalent' or 'not_equivalent'.
Acc: 34.70%, prompt: Evaluate whether these two phrases have identical meanings and respond with 'equivalent' or 'not_equivalent'.
Acc: 33.80%, prompt: Are the following two questions equivalent or not? Answer me with "equivalent" or "not_equivalent".
Acc: 32.40%, prompt: Can these two statements be considered equal in meaning? Answer with 'equivalent' or 'not_equivalent'.
Acc: 32.40%, prompt: Please indicate if the following pair of sentences share the same meaning by responding with 'equivalent' or 'not_equivalent'.
Acc: 32.10%, prompt: Are the meanings of these two phrases the same? Reply with 'equivalent' or 'not_equivalent'.
Acc: 27.90%, prompt: Determine if the given pair of statements can be considered the same by responding with 'equivalent' or 'not_equivalent'.
Acc: 27.30%, prompt: Analyze if the given set of sentences have the same connotation by answering with 'equivalent' or 'not_equivalent'.

Acc: 36.20%, prompt: In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent'.
Acc: 33.60%, prompt: In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent'.
Acc: 33.00%, prompt: In the role of a question similarity analyzer, examine the meaning of the provided questions and decide if they are equivalent, answering with 'equivalent' for equivalent questions or 'not_equivalent' for different questions.
Acc: 32.90%, prompt: Working as a question classifier, identify whether the given questions share the same meaning, and respond with 'equivalent' for equivalent questions or 'not_equivalent' for different ones.
Acc: 32.70%, prompt: As a question equivalence detection system, examine the provided questions and respond with 'equivalent' if they are the same in meaning, or 'not_equivalent' if they are different.
Acc: 32.20%, prompt: Functioning as a question similarity evaluation tool, analyze the given questions and decide if they share the same meaning, responding with 'equivalent' or 'not_equivalent'.
Acc: 32.20%, prompt: As an instrument for question comparison evaluation, consider the questions and determine if their meaning is the same, responding with 'equivalent' for similar questions or 'not_equivalent' for different questions.
Acc: 32.00%, prompt: While performing question comparison analysis, classify the similarity of the following questions as 'equivalent' for equivalent questions or 'not_equivalent' for different questions.
Acc: 31.40%, prompt: Acting as a question equivalence instrument, determine if the provided questions are equivalent in meaning, answering with 'equivalent' for similar questions or 'not_equivalent' for dissimilar ones.
Acc: 30.90%, prompt: As a tool for determining question equivalence, review the questions and categorize their similarity as either 'equivalent' or 'not_equivalent'.

## bertattack

Original prompt: Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"are the following expression do the same as? substitute your subject as 'equivalent' or 'not_equivalent'. "
Original acc: 41.80%, attacked acc: 10.30%, dropped acc: 31.50%

Original prompt: Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent'.
Attacked prompt: b"check who the following statements are singular in meaning by answering 'equivalent' or 'not_equivalent'. "
Original acc: 38.10%, attacked acc: 21.80%, dropped acc: 16.30%

Original prompt: Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Examine the following expressions and tell me if they are opposite in meaningful by function 'equivalent' or 'not_equivalent'. "
Original acc: 36.50%, attacked acc: 14.50%, dropped acc: 22.00%

Original prompt: In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"use the role of a questions assessment system, indicate if the meaning of the posed items is the same, responding with 'equivalent' or 'not_equivalent'. "
Original acc: 36.20%, attacked acc: 29.40%, dropped acc: 6.80%

Original prompt: In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"In your role as a question classification tool, measure the initial pair of questions and classify them as 'equivalent' or 'not_equivalent'. "
Original acc: 33.60%, attacked acc: 26.60%, dropped acc: 7.00%

Original prompt: In the role of a question similarity analyzer, examine the meaning of the provided questions and decide if they are equivalent, answering with 'equivalent' for equivalent questions or 'not_equivalent' for different questions.
Attacked prompt: b"In the role of a topic similarities analyzer, examining the semantic of the questions the and decide if they are equivalent, answer with 'equivalent' for equivalent numbers or 'not_equivalent' for various respondents. "
Original acc: 33.00%, attacked acc: 8.20%, dropped acc: 24.80%

## checklist

Original prompt: Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent' fwhUZUQzXW. "
Original acc: 42.10%, attacked acc: 27.50%, dropped acc: 14.60%

Original prompt: Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent' 6a4Yn3RGVc. "
Original acc: 38.20%, attacked acc: 23.50%, dropped acc: 14.70%

Original prompt: Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent' lf8wBa2yEm. "
Original acc: 36.40%, attacked acc: 29.20%, dropped acc: 7.20%

Original prompt: In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent' RcRneWo6Iv. "
Original acc: 36.30%, attacked acc: 29.80%, dropped acc: 6.50%

Original prompt: In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent' ofOQXLxiW4. "
Original acc: 33.50%, attacked acc: 30.10%, dropped acc: 3.40%

Original prompt: Working as a question classifier, identify whether the given questions share the same meaning, and respond with 'equivalent' for equivalent questions or 'not_equivalent' for different ones.
Attacked prompt: b"Working as a question classifier, identify whether the given questions share the same meaning, and respond with 'equivalent' for equivalent questions or 'not_equivalent' for different ones AMsRIKZniY. "
Original acc: 32.90%, attacked acc: 25.00%, dropped acc: 7.90%

## deepwordbug

Original prompt: Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"oD the folXowing exrpessions men the same hing? ProFide your answre as 'equivalent' or 'not_equivalent'. "
Original acc: 41.80%, attacked acc: 26.30%, dropped acc: 15.50%

Original prompt: Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Asess hwether the following statemets are identiacl in meaning by answerinEg 'equivalent' or 'not_equivalent'. "
Original acc: 38.10%, attacked acc: 20.30%, dropped acc: 17.80%

Original prompt: Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Examne the following exrpessions and telIl me if they are aliZke in mVeaning by usking 'equivalent' or 'not_equivalent'. "
Original acc: 36.50%, attacked acc: 24.40%, dropped acc: 12.10%

Original prompt: In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"nI the caacity of a qCuestion assevssment system, indicate if the meaniBng of the providDed Zquestions is the same, responding with 'equivalent' or 'not_equivalent'. "
Original acc: 36.20%, attacked acc: 25.50%, dropped acc: 10.70%

Original prompt: In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"In your Irole as a questioGn comparison tolo, ussess the foMlowing pair of questrions and classify them as 'equivalent' or 'not_equivalent'. "
Original acc: 33.60%, attacked acc: 23.60%, dropped acc: 10.00%

Original prompt: In the role of a question similarity analyzer, examine the meaning of the provided questions and decide if they are equivalent, answering with 'equivalent' for equivalent questions or 'not_equivalent' for different questions.
Attacked prompt: b"nI the rol of a question siimlarity naalyzer, examiYe the meaning of the prSovided questions and decide if they are equivalent, answering with 'equivalent' for equivalent questions or 'not_equivalent' for different uquestions. "
Original acc: 33.00%, attacked acc: 23.80%, dropped acc: 9.20%

## stresstest

Original prompt: Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 41.80%, attacked acc: 42.20%, dropped acc: -0.40%

Original prompt: Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 38.10%, attacked acc: 41.20%, dropped acc: -3.10%

Original prompt: Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 36.50%, attacked acc: 50.30%, dropped acc: -13.80%

Original prompt: In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 36.20%, attacked acc: 47.70%, dropped acc: -11.50%

Original prompt: In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 33.60%, attacked acc: 36.40%, dropped acc: -2.80%

Original prompt: In the role of a question similarity analyzer, examine the meaning of the provided questions and decide if they are equivalent, answering with 'equivalent' for equivalent questions or 'not_equivalent' for different questions.
Attacked prompt: b"In the role of a question similarity analyzer, examine the meaning of the provided questions and decide if they are equivalent, answering with 'equivalent' for equivalent questions or 'not_equivalent' for different questions  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 33.00%, attacked acc: 26.40%, dropped acc: 6.60%

## textbugger

Original prompt: Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Wo the following expressions meant the same thing? Provide your a\xd5\xb8swer as 'equivalent' or 'not_equivalent'. "
Original acc: 41.80%, attacked acc: 26.70%, dropped acc: 15.10%

Original prompt: Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Ass ess whether the fol lowing statements are identical in meaning by answering 'equivalent' or 'not_equivalent'. "
Original acc: 38.10%, attacked acc: 28.50%, dropped acc: 9.60%

Original prompt: Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Examine the following manifestations and tell me if they are too in meaning by use 'equivalent' or 'not_equivalent'. "
Original acc: 36.50%, attacked acc: 29.40%, dropped acc: 7.10%

Original prompt: In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"I\xd5\xb8 the capacit\xd1\x83 of a questions assesment system, indicate if the meaning of the provid\xd0\xb5d questions is the same, responding with 'equivalent' or 'not_equivalent'. "
Original acc: 36.20%, attacked acc: 29.40%, dropped acc: 6.80%

Original prompt: In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"For your ro\xe2\x85\xbce as a question comp\xc9\x91rison tool, evaluate the \xf0\x9d\x9a\x8following pair of questions and categorized them as 'equivalent' or 'not_equivalent'. "
Original acc: 33.60%, attacked acc: 15.00%, dropped acc: 18.60%

Original prompt: In the role of a question similarity analyzer, examine the meaning of the provided questions and decide if they are equivalent, answering with 'equivalent' for equivalent questions or 'not_equivalent' for different questions.
Attacked prompt: b"I\xd5\xb8 the rol\xd0\xb5 of a ques\xf0\x9d\x9a\x9dion similarity analyzer, investigated the meaning of the prov\xd1\x96ded questions and decide if they are equivalent, answerin\xc9\xa1 with 'equivalent' for equivalent question or 'not_equivalent' for various questions. "
Original acc: 33.00%, attacked acc: 19.30%, dropped acc: 13.70%

## textfooler

Original prompt: Do the following expressions mean the same thing? Provide your answer as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Know the following phrase imply the same thing? Supply your riposte as 'equivalent' or 'not_equivalent'. "
Original acc: 41.80%, attacked acc: 29.00%, dropped acc: 12.80%

Original prompt: Assess whether the following statements are identical in meaning by answering 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Estimates whether the following pronouncements are analogous in connotation by answering 'equivalent' or 'not_equivalent'. "
Original acc: 38.10%, attacked acc: 21.50%, dropped acc: 16.60%

Original prompt: Examine the following expressions and tell me if they are alike in meaning by using 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Researched the following terms and say me if they are too in connotation by consumes 'equivalent' or 'not_equivalent'. "
Original acc: 36.50%, attacked acc: 23.20%, dropped acc: 13.30%

Original prompt: In the capacity of a question assessment system, indicate if the meaning of the provided questions is the same, responding with 'equivalent' or 'not_equivalent'.
Attacked prompt: b"Among the dexterity of a theme analyse scheme, describe if the meanings of the brought things is the same, answering with 'equivalent' or 'not_equivalent'. "
Original acc: 36.20%, attacked acc: 22.80%, dropped acc: 13.40%

Original prompt: In your role as a question comparison tool, assess the following pair of questions and classify them as 'equivalent' or 'not_equivalent'.
Attacked prompt: b"En your role as a things comparison apparatus, assess the following pair of questions and categories them as 'equivalent' or 'not_equivalent'. "
Original acc: 33.60%, attacked acc: 15.50%, dropped acc: 18.10%

Original prompt: In the role of a question similarity analyzer, examine the meaning of the provided questions and decide if they are equivalent, answering with 'equivalent' for equivalent questions or 'not_equivalent' for different questions.
Attacked prompt: b"Across the rol of a trouble similarity analyzer, exploring the meaning of the lent questions and select if they are equivalent, answered with 'equivalent' for equivalent theme or 'not_equivalent' for various questions. "
Original acc: 33.00%, attacked acc: 13.90%, dropped acc: 19.10%

## translation

Language: chinese, acc: 30.70%, prompt: As a tool for determining the equivalence of problems, the problems are examined and their similarity is classified as 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 35.10%, prompt: Please compare the similarity of two sentences and put them into the category of 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 31.30%, prompt: Two sentences are classified as 'equivalent' or 'not_equivalent' for their similarity.
Language: chinese, acc: 30.20%, prompt: You can determine how similar the questions are by comparing them and categorizing them as 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 41.40%, prompt: Using the method of contrast, the similarity of these problems is divided into two categories: 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 32.20%, prompt: By comparing these issues, you can classify them as 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 32.20%, prompt: To determine whether the questions are similar, put them into the category of 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 34.80%, prompt: Divide the similarity of these questions into 'equivalent' or 'not_equivalent' categories.
Language: chinese, acc: 30.60%, prompt: Using the similarity assessment tool, these questions were classified as 'equivalent' or 'not_equivalent'.
Language: chinese, acc: 31.40%, prompt: By analyzing the similarity of these problems, they are divided into categories of 'equivalent' or 'not_equivalent'.
Language: french, acc: 31.30%, prompt: As a tool to determine the equivalence of questions, review the questions and rank their similarity as 'equivalent' or 'not_equivalent'.
Language: french, acc: 33.20%, prompt: Please compare the similarity of two sentences and classify them as 'equivalent' or 'not_equivalent'.
Language: french, acc: 31.50%, prompt: Based on the similarity of two sentences, classify them as 'equivalent' or 'not_equivalent'.
Language: french, acc: 30.40%, prompt: You can determine the similarity between these questions by comparing them and classifying them as 'equivalent' or 'not_equivalent'.
Language: french, acc: 34.60%, prompt: Use a comparative method to divide the similarity of these questions into two categories: 'equivalent' or 'not_equivalent'.
Language: french, acc: 32.20%, prompt: By comparing these questions, you can classify them as 'equivalent' or 'not_equivalent'.
Language: french, acc: 35.60%, prompt: Determine whether these questions are similar or not, and then classify them as 'equivalent' or 'not_equivalent'.
Language: french, acc: 38.50%, prompt: Divide the similarity of these questions into two categories: 'equivalent' or 'not_equivalent'.
Language: french, acc: 32.70%, prompt: Use a similarity assessment tool to classify these questions as 'equivalent' or 'not_equivalent'.
Language: french, acc: 31.10%, prompt: By analyzing the similarity of these questions, you can divide them into two categories: 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 30.00%, prompt: As a tool for determining an equation of questions, review the questions and classify their similarity as either 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 32.80%, prompt: When using questions in the classification domain, please classify the similarity between the questions as 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 28.60%, prompt: To determine an equation of questions, you must review the questions and classify their similarity as 'equivalent' or 'not_equivalent'.
Language: arabic, acc: 38.20%, prompt: Questions can be classified as 'equivalent' or 'not_equivalent' when used to identify classifications.
Language: arabic, acc: 29.90%, prompt: Classification of question similarity as 'equivalent' or 'not_equivalent' is used as a tool to determine the classification of questions.
Language: arabic, acc: 28.20%, prompt: Classify the similarity of the questions as 'equivalent' or 'not_equivalent' to determine the equation of the questions.
Language: arabic, acc: 31.70%, prompt: Identifying the similarity of questions and classifying them as 'equivalent' or 'not_equivalent' is an important tool in determining the classification of questions.
Language: arabic, acc: 34.60%, prompt: When classifying questions, their similarity can be classified as 'equivalent' or 'not_equivalent' to determine the correct classification.
Language: arabic, acc: 30.70%, prompt: The similarity of questions should be classified as 'equivalent' or 'not_equivalent' when used to determine the equation of questions.
Language: arabic, acc: 31.40%, prompt: Identifying the similarity of questions and classifying them as 'equivalent' or 'not_equivalent' helps to correctly classify questions.
Language: spanish, acc: 31.50%, prompt: As a tool to determine the equivalence of questions, it reviews the questions and classifies their similarity as 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 31.60%, prompt: Evaluate the similarity between questions and classify them as 'equivalent' or 'not_equivalent' to determine their equivalence.
Language: spanish, acc: 43.00%, prompt: Determine whether two questions are 'equivalent' or 'not_equivalent' based on similarity and characteristics.
Language: spanish, acc: 35.50%, prompt: Classifies the similarity between questions as 'equivalent' or 'not_equivalent' to determine their equivalence.
Language: spanish, acc: 31.10%, prompt: Review the questions and rate them as 'equivalent' or 'not_equivalent' based on their similarity and content.
Language: spanish, acc: 29.40%, prompt: As part of the classification task of questions, it determines their equivalence by categorizing their similarity as 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 32.30%, prompt: Analyze the similarity between questions and classify them as 'equivalent' or 'not_equivalent' to determine their equivalence.
Language: spanish, acc: 32.20%, prompt: As a method of identifying the equivalence of questions, it categorizes their similarity as 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 31.20%, prompt: To determine the equivalence between questions, check their similarity and classify them as 'equivalent' or 'not_equivalent'.
Language: spanish, acc: 41.30%, prompt: Classify the similarity between questions as 'equivalent' or 'not_equivalent' to determine whether they are equivalent or not.
Language: japanese, acc: 30.70%, prompt: As a tool to determine the equivalence of the question, review the question and categorize its similarities into 'equivalent' or 'not_equivalent' categories.
Language: japanese, acc: 51.70%, prompt: Work on text sorting tasks labeled 'equivalent' or 'not_equivalent'.
Language: japanese, acc: 21.70%, prompt: For text classification tasks, use the labels 'equivalent' or 'not_equivalent' to determine the equivalence of statements.
Language: japanese, acc: 37.90%, prompt: In the MRPC dataset, use the labels 'equivalent' or 'not_equivalent' to classify the equivalence of statements.
Language: japanese, acc: 31.80%, prompt: As a tool for determining equivalence, check sentences and categorize them into 'equivalent' or 'not_equivalent' categories.
Language: japanese, acc: 29.10%, prompt: Use the labels 'equivalent' or 'not_equivalent' to determine the equivalence of statements in text classification tasks.
Language: japanese, acc: 27.80%, prompt: In the text classification task of the MRPC data set, classify the equivalence of statements with labels of 'equivalent' or 'not_equivalent'.
Language: japanese, acc: 36.00%, prompt: As a tool to determine the equivalence of statements, categorize statements into 'equivalent' or 'not_equivalent' categories.
Language: japanese, acc: 27.80%, prompt: In a text classification task, classify the equivalence of statements using labels of 'equivalent' or 'not_equivalent'.
Language: japanese, acc: 28.20%, prompt: Do a text classification task to determine the equivalence of statements, labeled 'equivalent' or 'not_equivalent'.
Language: korean, acc: 27.40%, prompt: Classify two given sentences as 'equivalent' or 'not_equivalent' by discriminating whether they have the same meaning.
Language: korean, acc: 36.30%, prompt: Determine sentence equivalence by judging the similarity of two sentences with 'equivalent' or 'not_equivalent'.
Language: korean, acc: 31.60%, prompt: Classify the similarity of sentences as 'equivalent' or 'not_equivalent' by judging whether two sentences have the same meaning.
Language: korean, acc: 24.50%, prompt: Determine if two given sentences are equivalent to each other, and classify their similarity as 'equivalent' or 'not_equivalent'.
Language: korean, acc: 27.90%, prompt: Compare two given sentences to determine sentence equivalence, and classify their similarities as 'equivalent' or 'not_equivalent'.
Language: korean, acc: 36.40%, prompt: Classify sentence equivalence as 'equivalent' or 'not_equivalent' by judging whether two sentences have the same meaning to each other.
Language: korean, acc: 25.50%, prompt: Determine if two sentences have the same meaning, and classify their similarities as 'equivalent' or 'not_equivalent'.
Language: korean, acc: 30.20%, prompt: Compare two given sentences to determine their equivalence, and classify their similarities as 'equivalent' or 'not_equivalent'.
Language: korean, acc: 28.40%, prompt: Review two sentences to evaluate sentence equivalence, and classify their similarities as 'equivalent' or 'not_equivalent'.
Language: korean, acc: 34.10%, prompt: Judge whether two sentences have the same meaning to each other, and determine the sentence equivalence with 'equivalent' or 'not_equivalent'.

# rte

## 10 prompts

Acc: 50.54%, prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Acc: 48.38%, prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Acc: 43.68%, prompt: Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.
Acc: 41.52%, prompt: Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.
Acc: 32.85%, prompt: Assess the connection between the following sentences and classify it as 'entailment' or 'not_entailment'.
Acc: 17.69%, prompt: Indicate if the connection between the following sentences is 'entailment' or 'not_entailment'.
Acc: 16.97%, prompt: Analyze the two provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.
Acc: 13.00%, prompt: Considering the two sentences, identify if their relationship is 'entailment' or 'not_entailment'.
Acc: 7.22%, prompt: Determine if the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'.
Acc: 4.69%, prompt: Identify whether the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Acc: 4.33%, prompt: Examine the pair of sentences and determine if they exhibit entailment or not_entailment. Answer with either 'entailment' or 'not_entailment'.

Acc: 41.88%, prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Acc: 38.63%, prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Acc: 36.82%, prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Acc: 24.19%, prompt: As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment' or 'not_entailment'. Respond with 'entailment' or 'not_entailment'.
Acc: 22.02%, prompt: While performing entailment analysis, classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.
Acc: 19.49%, prompt: Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.
Acc: 19.13%, prompt: In the capacity of an entailment assessment system, indicate if the link between the following sentences is 'entailment' or 'not_entailment'.
Acc: 10.47%, prompt: Acting as an entailment detection instrument, determine if the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Acc: 9.39%, prompt: As a tool for determining entailment relationships, review the two statements and categorize their connection as either 'entailment' or 'not_entailment'.
Acc: 2.89%, prompt: Working as an entailment classifier, identify whether the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'.

## bertattack

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'pair the following opposite sentences entailment or not_entailment? answers me with "entailment" or "not_entailment", just 1 word. '
Original acc: 50.54%, attacked acc: 1.08%, dropped acc: 49.46%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Does the relationship between the given expressions represent entailment or not_entailment? q with 'entailment' or 'not_entailment'. "
Original acc: 48.38%, attacked acc: 5.42%, dropped acc: 42.96%

Original prompt: Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.
Attacked prompt: b"t the two statements and categorize their relation as either 'entailment' or 'not_entailment'. "
Original acc: 43.68%, attacked acc: 13.00%, dropped acc: 30.69%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"In your contribution as an entailment analytics tool, assessed the relationship between the given sentences and graded it as 'entailment' or 'not_entailment'. "
Original acc: 41.88%, attacked acc: 5.78%, dropped acc: 36.10%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"As an entailment matching set, identify the connection between the below sentence and question with 'entailment' or 'not_entailment'. "
Original acc: 38.63%, attacked acc: 1.08%, dropped acc: 37.55%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Attacked prompt: b"In the role of a descriptive relationship analyzeing, read the connection between the given sentences and learn if they exhibit entailment or not_entailment. answers with 'entailment' or 'not_entailment'. "
Original acc: 36.82%, attacked acc: 0.00%, dropped acc: 36.82%

## checklist

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word Q47Jmd4lMV. '
Original acc: 50.54%, attacked acc: 13.36%, dropped acc: 37.18%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment' Q47Jmd4lMV. "
Original acc: 48.38%, attacked acc: 23.47%, dropped acc: 24.91%

Original prompt: Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.
Attacked prompt: b"Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment' mzjVogkRhM. "
Original acc: 43.68%, attacked acc: 7.22%, dropped acc: 36.46%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment' Q47Jmd4lMV. "
Original acc: 41.88%, attacked acc: 2.53%, dropped acc: 39.35%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment' Q47Jmd4lMV. "
Original acc: 38.63%, attacked acc: 0.72%, dropped acc: 37.91%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Attacked prompt: b"In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment' Q47Jmd4lMV. "
Original acc: 37.18%, attacked acc: 4.33%, dropped acc: 32.85%

## deepwordbug

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'Aer the following wto sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one wor. '
Original acc: 50.54%, attacked acc: 0.36%, dropped acc: 50.18%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Does the relationship between the given sentences represent entailment or not_entailment? ResponY with 'entailment' or 'not_entailment'. "
Original acc: 48.38%, attacked acc: 21.66%, dropped acc: 26.71%

Original prompt: Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.
Attacked prompt: b"Revivw the two statements and catgeorize their relationsoip as either 'entailment' or 'not_entailment'. "
Original acc: 43.68%, attacked acc: 7.94%, dropped acc: 35.74%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"LIn your roe as an entailment anlysis tXol, ssess the relItionship between the given sentences and classify it as 'entailment' or 'not_entailment'. "
Original acc: 41.88%, attacked acc: 10.11%, dropped acc: 31.77%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"As an entailment identification system, zxamine the conneUtion between the following sentences and respond with 'entailment' or 'not_entailment'. "
Original acc: 38.63%, attacked acc: 19.49%, dropped acc: 19.13%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Attacked prompt: b"In the role of a semgntic relationship anayzer, examin the connection between the given sentences and decide if they exhibit entailment or not_entailment. AnCwer with 'entailment' or 'not_entailment'. "
Original acc: 36.82%, attacked acc: 1.08%, dropped acc: 35.74%

## stresstest

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word  and true is true . '
Original acc: 50.54%, attacked acc: 14.08%, dropped acc: 36.46%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 48.38%, attacked acc: 35.38%, dropped acc: 13.00%

Original prompt: Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.
Attacked prompt: b"Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 43.68%, attacked acc: 15.88%, dropped acc: 27.80%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 41.88%, attacked acc: 6.50%, dropped acc: 35.38%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 38.63%, attacked acc: 15.88%, dropped acc: 22.74%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Attacked prompt: b"In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 36.82%, attacked acc: 20.22%, dropped acc: 16.61%

## textbugger

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'Represent the following deux sentences entailment or not_entailment? Answers me with "entailment" or "not_entailment", just \xd0\xbene word. '
Original acc: 50.54%, attacked acc: 3.61%, dropped acc: 46.93%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Did the relationship between the given sentences represen\xf0\x9d\x9a\x9d entailment or not_entailment? Answering with 'entailment' or 'not_entailment'. "
Original acc: 48.38%, attacked acc: 21.30%, dropped acc: 27.08%

Original prompt: Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.
Attacked prompt: b"Rev\xd1\x96ew the two sta\xf0\x9d\x9a\x9dements and categorize their relationship as or 'entailment' or 'not_entailment'. "
Original acc: 43.68%, attacked acc: 2.53%, dropped acc: 41.16%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"In your function as an entailment analyses to\xd0\xbel, assessing the relationshi\xd1\x80 between the given sentences and classify it as 'entailment' or 'not_entailment'. "
Original acc: 41.88%, attacked acc: 3.25%, dropped acc: 38.63%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Iike an entailment identification s\xd1\x83stem, examine the conn\xd0\xb5ction between the following sentences and respond with 'entailment' or 'not_entailment'. "
Original acc: 38.63%, attacked acc: 10.11%, dropped acc: 28.52%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Attacked prompt: b"In the role of a se\xef\xbd\x8dantic relationship analyze\xe2\xb2\x85, examine the connection between the givn sentences and determine if they exhibi\xf0\x9d\x9a\x9d entailment or not_entailment. Answers with 'entailment' or 'not_entailment'. "
Original acc: 36.82%, attacked acc: 0.00%, dropped acc: 36.82%

## textfooler

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'Represent the following two sentences entailment or not_entailment? Responses me with "entailment" or "not_entailment", just one word. '
Original acc: 50.54%, attacked acc: 6.50%, dropped acc: 44.04%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Did the liaisons between the given phrases represent entailment or not_entailment? Answers with 'entailment' or 'not_entailment'. "
Original acc: 48.38%, attacked acc: 4.69%, dropped acc: 43.68%

Original prompt: Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.
Attacked prompt: b"Investigated the two statements and categorize their relation as either 'entailment' or 'not_entailment'. "
Original acc: 43.68%, attacked acc: 2.17%, dropped acc: 41.52%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"During your functions as an entailment assessment utility, appraisals the affairs between the given sentence and categorize it as 'entailment' or 'not_entailment'. "
Original acc: 41.88%, attacked acc: 2.17%, dropped acc: 39.71%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Iike an entailment ident schemes, examine the relationship between the following phrases and replied with 'entailment' or 'not_entailment'. "
Original acc: 38.63%, attacked acc: 5.05%, dropped acc: 33.57%

Original prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Attacked prompt: b"In the role of a semantic relationship profiler, review the ties between the given sentences and determining if they fairs entailment or not_entailment. Answers with 'entailment' or 'not_entailment'. "
Original acc: 36.82%, attacked acc: 0.00%, dropped acc: 36.82%

## translation

Language: chinese, acc: 26.35%, prompt: In the light of an implication analysis tool, evaluate the relationship between the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 42.96%, prompt: From the perspective of an implication analysis tool, determine whether there is an implication relationship in the following sentences by classifying them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 5.05%, prompt: Please use an implication analysis tool to determine whether an implication relationship exists in the following sentences by classifying them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 43.32%, prompt: Please evaluate the relation of the following sentences as 'entailment' or 'not_entailment' for the purpose of determining implication relation.
Language: chinese, acc: 11.55%, prompt: Please use the implication analysis tool to evaluate the relationships between the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 28.16%, prompt: For the purpose of determining implicative relations, analyze the relations of the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 12.27%, prompt: Please use the implication analysis tool to determine the relationship of the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 22.38%, prompt: Please use the implication judgment tool to assess the relevance of the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 18.05%, prompt: Please, with implication analysis as the main task, determine the relationships between the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 20.22%, prompt: Using the implication judgment as a criterion, analyze the relation of the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: french, acc: 42.60%, prompt: As an engagement analysis tool, evaluate the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Language: french, acc: 10.11%, prompt: Determine whether the given sentences involve one another or not as an implication analysis tool. Classify them accordingly as 'entailment' or 'not_entailment'.
Language: french, acc: 7.58%, prompt: Using implication analysis, evaluate whether the sentences provided have a logical relationship and categorize them as 'entailment' or 'not_entailment'.
Language: french, acc: 45.13%, prompt: As an engagement assessment tool, determine whether the sentences provided have a logical relationship and classify them as 'entailment' or 'not_entailment'.
Language: french, acc: 20.22%, prompt: As an implication classification tool, analyze the sentences provided to determine if there is a logical relationship and categorize them as 'entailment' or 'not_entailment'.
Language: french, acc: 3.97%, prompt: Using implication analysis, determine whether the given sentences have a cause-effect relationship and categorize them as 'entailment' or 'not_entailment'.
Language: french, acc: 26.71%, prompt: Evaluate the relationship between the given sentences using implication analysis and rank them accordingly as 'entailment' or 'not_entailment'.
Language: french, acc: 40.79%, prompt: As an engagement detection tool, determine whether the given sentences have a logical relationship and categorize them as 'entailment' or 'not_entailment'.
Language: french, acc: 12.27%, prompt: Using implication analysis, evaluate whether the sentences provided have a cause-effect relationship and rank them accordingly as 'entailment' or 'not_entailment'.
Language: french, acc: 23.10%, prompt: Determine whether the given sentences have a cause-effect relationship as an engagement analysis tool and categorize them as 'entailment' or 'not_entailment'.
Language: arabic, acc: 28.16%, prompt: In your role as a tool for reasoning analysis, evaluate the relationship between given sentences and classify them as 'entailment' or 'not_entailment'.
Language: arabic, acc: 46.93%, prompt: Can you determine whether this sentence is inferred from the other sentence? Classify it as 'entailment' or 'not_entailment'.
Language: arabic, acc: 14.44%, prompt: Using the tool of reasoning analysis, analyze the relationship between given sentences and classify them as 'entailment' or 'not_entailment'.
Language: arabic, acc: 48.38%, prompt: Does this sentence represent a conclusion from the previous sentence? Classify it as 'entailment' or 'not_entailment'.
Language: arabic, acc: 15.16%, prompt: As a tool of reasoning analysis, evaluate the relationship of given sentences and classify them as 'entailment' or 'not_entailment'.
Language: arabic, acc: 49.46%, prompt: Can this sentence be inferred from the previous sentence? Classify it as 'entailment' or 'not_entailment'.
Language: arabic, acc: 17.69%, prompt: Using a tool to analyze a conclusion, analyze the relationship between the two sentences and classify them as 'entailment' or 'not_entailment'.
Language: arabic, acc: 50.90%, prompt: Is this a conclusion from the next sentence? Classify it as 'entailment' or 'not_entailment'.
Language: arabic, acc: 12.27%, prompt: As part of your task in analyzing a conclusion, evaluate the relationship between the two sentences and classify them as 'entailment' or 'not_entailment' based on their relationship.
Language: arabic, acc: 49.10%, prompt: Are you following this sentence directly from the previous one? Classify it as 'entailment' or 'not_entailment'.
Language: spanish, acc: 43.32%, prompt: In your role as an implication analysis tool, evaluate the relationship between the given phrases and classify them as 'entailment' or 'not_entailment'.
Language: spanish, acc: 32.49%, prompt: Determine whether the second sentence necessarily implies the first and label the relation as 'entailment', or as 'not_entailment' if not.
Language: spanish, acc: 5.42%, prompt: Classifies the relationship between these two sentences as 'entailment' if one necessarily implies the other, or as 'not_entailment' if not.
Language: spanish, acc: 34.30%, prompt: Evaluates whether the information in the second sentence is implied in the first and labels the relationship as 'entailment', or as 'not_entailment' if there is no such implication.
Language: spanish, acc: 35.74%, prompt: Given a couple of phrases, label their relationship as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication.
Language: spanish, acc: 14.08%, prompt: Analyzes the relationship between the phrases and classifies them as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication.
Language: spanish, acc: 9.39%, prompt: Given two sentences, determine whether the second sentence is a necessary consequence of the first and label the relation as 'entailment', or as 'not_entailment' if not.
Language: spanish, acc: 37.91%, prompt: Evaluates whether the information presented in the second sentence is implicit in the first and labels the relationship as 'entailment', or as 'not_entailment' if there is no such implication.
Language: spanish, acc: 12.64%, prompt: Classifies the relationship between the given phrases as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication.
Language: spanish, acc: 17.33%, prompt: Determines whether the information provided in the second sentence is necessarily inferable from the first and labels the relationship as 'entailment', or as 'not_entailment' if not.
Language: japanese, acc: 7.22%, prompt: Analyze the relationship of a given sentence and classify it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 22.38%, prompt: Evaluate the semantic relationship of the sentence and classify it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 32.13%, prompt: Please judge the relationship between the given sentences and classify them as 'entailment' or 'not_entailment'.
Language: japanese, acc: 32.85%, prompt: Examine the paraphrases of a given sentence and classify them 'entailment' or 'not_entailment'.
Language: japanese, acc: 18.05%, prompt: Rate the similarity of a given sentence and categorize it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 13.72%, prompt: Determinate the semantic connections of a given sentence and classify it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 30.32%, prompt: Examine the semantic match of a given sentence and categorize it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 45.13%, prompt: Classify it as 'entailment' or 'not_entailment' based on the content of the sentence.
Language: japanese, acc: 7.22%, prompt: Analyze the relationship of a given sentence and classify it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 16.61%, prompt: Judge the semantic connections of a given sentence and categorize it as 'entailment' or 'not_entailment'.
Language: korean, acc: 19.49%, prompt: Evaluate the relationship between any two sentences given to you and classify you as 'entailment' or 'not_entailment'.
Language: korean, acc: 18.41%, prompt: Analyze the semantic deductive relations between sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 24.19%, prompt: Evaluate the logical relevance between sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 6.14%, prompt: Evaluate the interaction of two given sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 47.65%, prompt: Please check whether there is a semantic match between those two sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 13.00%, prompt: Compare information between given sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 46.93%, prompt: Please analyse the correlation between those two sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 27.44%, prompt: Evaluate the different meanings between given sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 28.52%, prompt: Compare the semantic structure of the two sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 32.85%, prompt: Evaluate the interactions between sentences and classify them as 'entailment' or 'not_entailment'.

# sst2

## 10 prompts

Acc: 18.12%, prompt: Evaluate the sentiment of the given text and classify it as 'positive' or 'negative'.
Acc: 14.45%, prompt: Review this statement and decide whether it has a 'positive' or 'negative' sentiment.
Acc: 12.50%, prompt: After examining the following expression, label its emotion as either 'positive' or 'negative'.
Acc: 9.63%, prompt: Given the context of this text, indicate if the emotion conveyed is 'positive' or 'negative'.
Acc: 8.37%, prompt: Analyze the tone of this statement and respond with either 'positive' or 'negative'.
Acc: 3.33%, prompt: Please identify the emotional tone of this passage: 'positive' or 'negative'?
Acc: 2.75%, prompt: Assess the mood of the following quote and determine if it's 'positive' or 'negative'.
Acc: 1.38%, prompt: Read the provided excerpt and choose between 'positive' and 'negative' to describe its sentiment.
Acc: 1.38%, prompt: Considering the given phrase, would you say it carries a 'positive' or 'negative' connotation?
Acc: 0.34%, prompt: Determine the overall sentiment of this sentence, categorizing it as 'positive' or 'negative'.

Acc: 33.37%, prompt: Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative'.
Acc: 27.18%, prompt: Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative'.
Acc: 26.38%, prompt: In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement.
Acc: 19.61%, prompt: Serving as a sentiment evaluation model, determine if the given statement is 'positive' or 'negative'.
Acc: 17.43%, prompt: In the capacity of a sentiment classifier, decide whether the given quote is 'positive' or 'negative'.
Acc: 13.19%, prompt: Functioning as a sentiment identification tool, assess if the following expression is 'positive' or 'negative'.
Acc: 13.07%, prompt: As a sentiment classifier, determine whether the following text is 'positive' or 'negative'.
Acc: 12.27%, prompt: Acting as a sentiment evaluator, identify if the given sentence is 'positive' or 'negative'.
Acc: 2.41%, prompt: As an emotion detector, determine if the provided passage conveys a 'positive' or 'negative' sentiment.
Acc: 1.15%, prompt: Working as a sentiment analyzer, please indicate if the following text is 'positive' or 'negative'.

## bertattack

Original prompt: Evaluate the sentiment of the given text and classify it as 'positive' or 'negative'.
Attacked prompt: b"Evaluate the sentiment of the given scripture and write it as 'positive' or 'negative'. "
Original acc: 18.12%, attacked acc: 0.23%, dropped acc: 17.89%

Original prompt: Review this statement and decide whether it has a 'positive' or 'negative' sentiment.
Attacked prompt: b"Review this response and please gauge it has a 'positive' or 'negative' sentiment. "
Original acc: 14.45%, attacked acc: 0.11%, dropped acc: 14.33%

Original prompt: After examining the following expression, label its emotion as either 'positive' or 'negative'.
Attacked prompt: b"After examining the following action, type its emotion as either 'positive' or 'negative'. "
Original acc: 12.50%, attacked acc: 0.00%, dropped acc: 12.50%

Original prompt: Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative'.
Attacked prompt: b"[UNK] on the relationship of an emotion classtoken, choose if the provided phrase is 'positive' or 'negative'. "
Original acc: 33.37%, attacked acc: 0.11%, dropped acc: 33.26%

Original prompt: Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative'.
Attacked prompt: b"Emulating a emotion a system, indicate how the provided text is 'positive' or 'negative'. "
Original acc: 27.18%, attacked acc: 0.46%, dropped acc: 26.72%

Original prompt: In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement.
Attacked prompt: b"In the addition of a sentiment a tool, contrast with 'positive' or 'negative' to classify this statement. "
Original acc: 26.38%, attacked acc: 1.26%, dropped acc: 25.11%

## checklist

Original prompt: Evaluate the sentiment of the given text and classify it as 'positive' or 'negative'.
Attacked prompt: b"Evaluate the sentiment of the given text and classify it as 'positive' or 'negative' Q47Jmd4lMV. "
Original acc: 18.12%, attacked acc: 0.23%, dropped acc: 17.89%

Original prompt: Review this statement and decide whether it has a 'positive' or 'negative' sentiment.
Attacked prompt: b"Review this statement and decide whether it has a 'positive' or 'negative' sentiment w52rwgo0Av. "
Original acc: 14.45%, attacked acc: 0.11%, dropped acc: 14.33%

Original prompt: After examining the following expression, label its emotion as either 'positive' or 'negative'.
Attacked prompt: b"After examining the following expression, label its emotion as either 'positive' or 'negative' PDCGfz6DL9. "
Original acc: 12.50%, attacked acc: 0.11%, dropped acc: 12.39%

Original prompt: Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative'.
Attacked prompt: b"Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative' Q47Jmd4lMV. "
Original acc: 33.37%, attacked acc: 4.47%, dropped acc: 28.90%

Original prompt: Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative'.
Attacked prompt: b"Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative' Q47Jmd4lMV. "
Original acc: 27.18%, attacked acc: 10.32%, dropped acc: 16.86%

Original prompt: In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement.
Attacked prompt: b"In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement Q47Jmd4lMV. "
Original acc: 26.38%, attacked acc: 2.75%, dropped acc: 23.62%

## deepwordbug

Original prompt: Evaluate the sentiment of the given text and classify it as 'positive' or 'negative'.
Attacked prompt: b"Evaljuate the sentiment of the givtn text and calssify it as 'positive' or 'negative'. "
Original acc: 18.23%, attacked acc: 0.11%, dropped acc: 18.12%

Original prompt: Review this statement and decide whether it has a 'positive' or 'negative' sentiment.
Attacked prompt: b"GReview this stateent and decide wdether it has a 'positive' or 'negative' sentiment. "
Original acc: 14.45%, attacked acc: 0.00%, dropped acc: 14.45%

Original prompt: After examining the following expression, label its emotion as either 'positive' or 'negative'.
Attacked prompt: b"sAfter examinin the following expressiBn, labe its emotion as etiher 'positive' or 'negative'. "
Original acc: 12.61%, attacked acc: 2.29%, dropped acc: 10.32%

Original prompt: Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative'.
Attacked prompt: b"TakiXg on the role of an emotinon lassifier, specify if the rovided phrase is 'positive' or 'negative'. "
Original acc: 33.37%, attacked acc: 0.57%, dropped acc: 32.80%

Original prompt: Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative'.
Attacked prompt: b"EmZulating a sentment classificamion sfystem, idicate whethser the provided text is 'positive' or 'negative'. "
Original acc: 27.29%, attacked acc: 0.80%, dropped acc: 26.49%

Original prompt: In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement.
Attacked prompt: b"In the ole of a senteiment naalysis tool, resond with 'positive' or 'negative' to classfy this sattement. "
Original acc: 26.49%, attacked acc: 0.00%, dropped acc: 26.49%

## stresstest

Original prompt: Evaluate the sentiment of the given text and classify it as 'positive' or 'negative'.
Attacked prompt: b"Evaluate the sentiment of the given text and classify it as 'positive' or 'negative'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 18.12%, attacked acc: 0.69%, dropped acc: 17.43%

Original prompt: Review this statement and decide whether it has a 'positive' or 'negative' sentiment.
Attacked prompt: b"Review this statement and decide whether it has a 'positive' or 'negative' sentiment  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 14.45%, attacked acc: 0.00%, dropped acc: 14.45%

Original prompt: After examining the following expression, label its emotion as either 'positive' or 'negative'.
Attacked prompt: b"After examining the following expression, label its emotion as either 'positive' or 'negative'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 12.50%, attacked acc: 0.46%, dropped acc: 12.04%

Original prompt: Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative'.
Attacked prompt: b"Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 33.37%, attacked acc: 3.78%, dropped acc: 29.59%

Original prompt: Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative'.
Attacked prompt: b"Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 27.18%, attacked acc: 4.01%, dropped acc: 23.17%

Original prompt: In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement.
Attacked prompt: b"In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 26.38%, attacked acc: 1.95%, dropped acc: 24.43%

## textbugger

Original prompt: Evaluate the sentiment of the given text and classify it as 'positive' or 'negative'.
Attacked prompt: b"Evaluate the vibe of the gievn text and calssify it as 'positive' or 'negative'. "
Original acc: 18.12%, attacked acc: 0.00%, dropped acc: 18.12%

Original prompt: Review this statement and decide whether it has a 'positive' or 'negative' sentiment.
Attacked prompt: b"Reveiw this s\xf0\x9d\x9a\x9datement and decide wether it has a 'positive' or 'negative' sentiment. "
Original acc: 14.45%, attacked acc: 0.11%, dropped acc: 14.33%

Original prompt: After examining the following expression, label its emotion as either 'positive' or 'negative'.
Attacked prompt: b"After examining the following expression, labeling its emoion as either 'positive' or 'negative'. "
Original acc: 12.50%, attacked acc: 0.00%, dropped acc: 12.50%

Original prompt: Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative'.
Attacked prompt: b"Taking on the roles of an emotions classi\xf0\x9d\x9a\x8fier, speci\xf0\x9d\x9a\x8fy if the povided phrase is 'positive' or 'negative'. "
Original acc: 33.37%, attacked acc: 0.57%, dropped acc: 32.80%

Original prompt: Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative'.
Attacked prompt: b"Emulating a ambience ranking system, indicate whe\xf0\x9d\x9a\x9dher the provided text is 'positive' or 'negative'. "
Original acc: 27.18%, attacked acc: 0.69%, dropped acc: 26.49%

Original prompt: In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement.
Attacked prompt: b"During the ro le of a emotion analysis tools, respond with 'positive' or 'negative' to classify this statement. "
Original acc: 26.38%, attacked acc: 0.57%, dropped acc: 25.80%

## textfooler

Original prompt: Evaluate the sentiment of the given text and classify it as 'positive' or 'negative'.
Attacked prompt: b"Assessment the mood of the made laws and rank it as 'positive' or 'negative'. "
Original acc: 18.12%, attacked acc: 0.00%, dropped acc: 18.12%

Original prompt: Review this statement and decide whether it has a 'positive' or 'negative' sentiment.
Attacked prompt: b"Reassess this communique and select whether it has a 'positive' or 'negative' sentiment. "
Original acc: 14.45%, attacked acc: 0.00%, dropped acc: 14.45%

Original prompt: After examining the following expression, label its emotion as either 'positive' or 'negative'.
Attacked prompt: b"After examining the following word, labeling its sentiments as either 'positive' or 'negative'. "
Original acc: 12.50%, attacked acc: 0.00%, dropped acc: 12.50%

Original prompt: Taking on the role of an emotion classifier, specify if the provided phrase is 'positive' or 'negative'.
Attacked prompt: b"Assuming on the role of an feeling classifier, elucidate if the foreseen phrase is 'positive' or 'negative'. "
Original acc: 33.37%, attacked acc: 2.87%, dropped acc: 30.50%

Original prompt: Emulating a sentiment classification system, indicate whether the provided text is 'positive' or 'negative'.
Attacked prompt: b"Emulating a ambiance graded regime, explain whether the provided wording is 'positive' or 'negative'. "
Original acc: 27.18%, attacked acc: 0.46%, dropped acc: 26.72%

Original prompt: In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement.
Attacked prompt: b"During the rol of a emotion exploring mechanism, respond with 'positive' or 'negative' to rank this affirmations. "
Original acc: 26.38%, attacked acc: 0.00%, dropped acc: 26.38%

## translation

Language: chinese, acc: 20.07%, prompt: Answer whether the statement is 'positive' or 'negative' based on sentiment analysis.
Language: chinese, acc: 5.39%, prompt: As an emotion analysis tool, determine whether the emotion in the text is 'positive' or 'negative'.
Language: chinese, acc: 19.38%, prompt: Categorize the statement as 'positive' or 'negative', based on its emotional bent.
Language: chinese, acc: 5.85%, prompt: Please use sentiment analysis to classify the text as 'positive' or 'negative'.
Language: chinese, acc: 0.46%, prompt: Please determine whether the emotion of the sentence is 'positive' or 'negative' and categorize it.
Language: chinese, acc: 13.99%, prompt: Using sentiment analysis, classify the text as 'positive' or 'negative'.
Language: chinese, acc: 0.80%, prompt: Please answer whether the emotion of the sentence is 'positive' or 'negative' and categorize it.
Language: chinese, acc: 18.00%, prompt: Categorize the statement as 'positive' or 'negative' based on sentiment analysis.
Language: chinese, acc: 0.57%, prompt: Please judge this text as 'positive' or 'negative' according to the criteria of sentiment analysis.
Language: chinese, acc: 1.15%, prompt: Please classify this sentence as 'positive' or 'negative' according to the principles of emotion analysis.
Language: french, acc: 4.13%, prompt: As a sentiment analysis tool, please answer with 'positive' or 'negative' to classify this statement.
Language: french, acc: 7.22%, prompt: Determine whether this phrase is 'positive' or 'negative' as a sentiment classification tool.
Language: french, acc: 1.61%, prompt: Identify the tone of this statement by choosing between 'positive' and 'negative' as a sentiment analysis tool.
Language: french, acc: 18.92%, prompt: Use sentiment analysis to classify this statement as 'positive' or 'negative'.
Language: french, acc: 42.66%, prompt: As a sentiment classification tool, please determine whether this statement is 'positive' or 'negative'.
Language: french, acc: 19.38%, prompt: Classify this sentence as 'positive' or 'negative' using sentiment analysis.
Language: french, acc: 11.35%, prompt: Choose between 'positive' or 'negative' to classify this statement as a sentiment analysis tool.
Language: french, acc: 7.57%, prompt: Identify the sentiment expressed in this statement by selecting 'positive' or 'negative' as a sentiment classification tool.
Language: french, acc: 10.89%, prompt: Determine whether this phrase is 'positive' or 'negative' using sentiment analysis as a classification tool.
Language: french, acc: 18.92%, prompt: Use sentiment analysis to classify this statement as 'positive' or 'negative'.
Language: arabic, acc: 11.58%, prompt: Under emotional analysis, answer 'positive' or 'negative' to classify this statement.
Language: arabic, acc: 11.35%, prompt: Does this statement express a 'positive' or 'negative' reaction?
Language: arabic, acc: 16.51%, prompt: Is that a 'positive' or a 'negative' phrase?
Language: arabic, acc: 24.66%, prompt: What is the classification between 'positive' and 'negative'?
Language: arabic, acc: 14.11%, prompt: Does this sentence express 'positive' or 'negative' feelings?
Language: arabic, acc: 37.84%, prompt: In the context of textual analysis, what classification is this phrase between 'positive' and 'negative'?
Language: arabic, acc: 9.40%, prompt: Could this be classified as 'positive' or 'negative'?
Language: arabic, acc: 31.19%, prompt: In the context of emotional analysis, what classification is this statement between 'positive' and 'negative'?
Language: arabic, acc: 8.26%, prompt: Can this be classified as 'positive' or 'negative'?
Language: arabic, acc: 9.06%, prompt: Under the classification of emotions, is this sentence 'positive' or 'negative'?
Language: spanish, acc: 9.29%, prompt: As a feeling analysis tool, classify this statement as 'positive' or 'negative'.
Language: spanish, acc: 4.70%, prompt: Determine whether this statement has a 'positive' or 'negative' connotation.
Language: spanish, acc: 15.02%, prompt: Indicate whether the following statement is 'positive' or 'negative'.
Language: spanish, acc: 2.98%, prompt: Evaluate whether this text has a 'positive' or 'negative' emotional charge.
Language: spanish, acc: 1.61%, prompt: According to your sentiment analysis, would you say this comment is 'positive' or 'negative'?
Language: spanish, acc: 6.31%, prompt: In the context of sentiment analysis, label this sentence as 'positive' or 'negative'.
Language: spanish, acc: 1.03%, prompt: Rate the following statement as 'positive' or 'negative', according to your sentiment analysis.
Language: spanish, acc: 4.01%, prompt: How would you classify this text in terms of its emotional tone? 'positive' or 'negative'?
Language: spanish, acc: 28.78%, prompt: As a tool for sentiment analysis, would you say this statement is 'positive' or 'negative'?
Language: spanish, acc: 17.55%, prompt: Classify this statement as 'positive' or 'negative', please.
Language: japanese, acc: 6.19%, prompt: Treat this sentence as an emotion analysis tool and categorize it as 'positive' and 'negative'.
Language: japanese, acc: 10.67%, prompt: Use this article as a sentiment analysis tool to classify 'positive' and 'negative'.
Language: japanese, acc: 4.36%, prompt: Use this sentence as an emotion analysis tool to determine whether it is 'positive' or 'negative'.
Language: japanese, acc: 7.57%, prompt: Use this sentence as an emotion analysis tool to classify 'positive' and 'negative'.
Language: japanese, acc: 8.26%, prompt: Use this sentence as a sentiment analysis tool and classify it as 'positive' or 'negative'.
Language: japanese, acc: 3.90%, prompt: To classify this sentence as 'positive' or 'negative', evaluate it as a sentiment analysis tool.
Language: japanese, acc: 2.41%, prompt: Treat this sentence as an emotion analysis tool to determine whether it is 'positive' or 'negative'.
Language: japanese, acc: 18.00%, prompt: Use this sentence as a sentiment analysis tool to classify 'positive' and 'negative'.
Language: japanese, acc: 5.62%, prompt: Analyze this sentence as an emotion analysis tool to classify whether it is 'positive' or 'negative'.
Language: japanese, acc: 6.19%, prompt: Use this sentence as an emotional analysis tool to determine whether it is 'positive' or 'negative'.
Language: korean, acc: 7.57%, prompt: As an emotional analysis tool, respond with 'positive' or 'negative' to classify these sentences.
Language: korean, acc: 15.14%, prompt: Classify this sentence as 'positive' if you regard it as positive, 'negative' if you regard it as negative.
Language: korean, acc: 1.72%, prompt: Please rate the emotion of this sentence and classify it as 'positive' or 'negative'.
Language: korean, acc: 10.67%, prompt: Classify this sentence as 'positive' if you perceive it positively and 'negative' if you perceive it negatively.
Language: korean, acc: 16.74%, prompt: If this is a sentence delivered using a positive expression, classify it as 'positive' and if this is a sentence delivered using a negative expression, classify it as 'negative'.
Language: korean, acc: 1.26%, prompt: Respond with 'positive' or 'negative' by categorizing whether the sentence is positive or negative.
Language: korean, acc: 1.72%, prompt: Please analyze the emotion in this sentence and classify it as 'positive' or 'negative'.
Language: korean, acc: 22.82%, prompt: Classify this sentence as 'positive' if it contains a positive meaning, 'negative' if it contains a negative meaning.
Language: korean, acc: 23.97%, prompt: Classify this sentence as 'positive' if it contains positive content, 'negative' if it contains negative content.
Language: korean, acc: 2.29%, prompt: Classify what you're trying to convey in this sentence as 'positive' if it's positive, and 'negative' if it's negative.

# wnli

## 10 prompts

Acc: 32.39%, prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Acc: 28.17%, prompt: Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.
Acc: 23.94%, prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Acc: 23.94%, prompt: Assess the connection between the following sentences and classify it as 'entailment' or 'not_entailment'.
Acc: 15.49%, prompt: Review the two statements and categorize their relationship as either 'entailment' or 'not_entailment'.
Acc: 14.08%, prompt: Indicate if the connection between the following sentences is 'entailment' or 'not_entailment'.
Acc: 9.86%, prompt: Analyze the two provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.
Acc: 2.82%, prompt: Considering the two sentences, identify if their relationship is 'entailment' or 'not_entailment'.
Acc: 1.41%, prompt: Identify whether the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Acc: 1.41%, prompt: Determine if the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'.
Acc: 0.00%, prompt: Examine the pair of sentences and determine if they exhibit entailment or not_entailment. Answer with either 'entailment' or 'not_entailment'.

Acc: 16.90%, prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Acc: 16.90%, prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Acc: 12.68%, prompt: Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.
Acc: 9.86%, prompt: In the capacity of an entailment assessment system, indicate if the link between the following sentences is 'entailment' or 'not_entailment'.
Acc: 9.86%, prompt: In the role of a semantic relationship analyzer, examine the connection between the given sentences and decide if they exhibit entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Acc: 5.63%, prompt: As a tool for determining entailment relationships, review the two statements and categorize their connection as either 'entailment' or 'not_entailment'.
Acc: 4.23%, prompt: Acting as an entailment detection instrument, determine if the given pair of sentences demonstrates entailment or not_entailment. Answer with 'entailment' or 'not_entailment'.
Acc: 2.82%, prompt: While performing entailment analysis, classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.
Acc: 2.82%, prompt: As an instrument for entailment evaluation, consider the two sentences and determine if their relationship is 'entailment' or 'not_entailment'. Respond with 'entailment' or 'not_entailment'.
Acc: 0.00%, prompt: Working as an entailment classifier, identify whether the given pair of sentences displays entailment or not_entailment. Respond with 'entailment' or 'not_entailment'.

## bertattack

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'pair the following 2 sentences entailment or not_entailment? read me with "entailment" or "not_entailment", just one word. '
Original acc: 32.39%, attacked acc: 4.23%, dropped acc: 28.17%

Original prompt: Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.
Attacked prompt: b"s classify the relationship between the provided sentences as 'entailment' or 'not_entailment'. "
Original acc: 28.17%, attacked acc: 2.82%, dropped acc: 25.35%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Does the relationship between the given sentences represent entailment or not_entailment? q with 'entailment' or 'not_entailment'. "
Original acc: 23.94%, attacked acc: 0.00%, dropped acc: 23.94%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"[UNK] your role as an entailment and tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'. "
Original acc: 16.90%, attacked acc: 0.00%, dropped acc: 16.90%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"of an entailment detection set, ask the connection between the following sentences and respond with 'entailment' or 'not_entailment'. "
Original acc: 16.90%, attacked acc: 1.41%, dropped acc: 15.49%

Original prompt: Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.
Attacked prompt: b"Functioning as an entailment evaluation tool, analyze the constructed sentences and decide if their category is 'entailment' or 'not_entailment'. "
Original acc: 12.68%, attacked acc: 1.41%, dropped acc: 11.27%

## checklist

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word njCuciQJpB. '
Original acc: 32.39%, attacked acc: 19.72%, dropped acc: 12.68%

Original prompt: Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.
Attacked prompt: b"Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment' rzu98kF2KF. "
Original acc: 28.17%, attacked acc: 8.45%, dropped acc: 19.72%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment' vTAjHynoIG. "
Original acc: 23.94%, attacked acc: 18.31%, dropped acc: 5.63%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment' 9vGXgnbWB8. "
Original acc: 16.90%, attacked acc: 5.63%, dropped acc: 11.27%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment' rzu98kF2KF. "
Original acc: 16.90%, attacked acc: 2.82%, dropped acc: 14.08%

Original prompt: Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.
Attacked prompt: b"Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment' njCuciQJpB. "
Original acc: 12.68%, attacked acc: 5.63%, dropped acc: 7.04%

## deepwordbug

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'ACe the following wo sentences entailment or not_entailment? Answmer me with "entailment" or "not_entailment", just bone wrd. '
Original acc: 32.39%, attacked acc: 4.23%, dropped acc: 28.17%

Original prompt: Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.
Attacked prompt: b"PlJease classify the rhlationship between the provided senteunces as 'entailment' or 'not_entailment'. "
Original acc: 28.17%, attacked acc: 1.41%, dropped acc: 26.76%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"SDoes the relationship between the given stentences represent entailment or not_entailment? ResYond with 'entailment' or 'not_entailment'. "
Original acc: 23.94%, attacked acc: 0.00%, dropped acc: 23.94%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"mn your roye as an entailment aunalysis tooS, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'. "
Original acc: 16.90%, attacked acc: 0.00%, dropped acc: 16.90%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"AFs an entailment identificGtion system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'. "
Original acc: 16.90%, attacked acc: 2.82%, dropped acc: 14.08%

Original prompt: Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.
Attacked prompt: b"Functioning as an entailment evaluation tool, analyze the provided sentneces and decide if their relatiXonship is 'entailment' or 'not_entailment'. "
Original acc: 12.68%, attacked acc: 5.63%, dropped acc: 7.04%

## stresstest

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word  and true is true  and true is true  and true is true  and true is true  and true is true . '
Original acc: 32.39%, attacked acc: 11.27%, dropped acc: 21.13%

Original prompt: Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.
Attacked prompt: b"Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 28.17%, attacked acc: 1.41%, dropped acc: 26.76%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 23.94%, attacked acc: 14.08%, dropped acc: 9.86%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 16.90%, attacked acc: 12.68%, dropped acc: 4.23%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'  and true is true . "
Original acc: 16.90%, attacked acc: 2.82%, dropped acc: 14.08%

Original prompt: Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.
Attacked prompt: b"Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 12.68%, attacked acc: 12.68%, dropped acc: 0.00%

## textbugger

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'A\xe2\xb2\x85e the following \xf0\x9d\x9a\x9dwo sentences entailment or not_entailment? Answers me with "entailment" or "not_entailment", just one word. '
Original acc: 32.39%, attacked acc: 2.82%, dropped acc: 29.58%

Original prompt: Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.
Attacked prompt: b"Pelase classify the relations between the provided sentences as 'entailment' or 'not_entailment'. "
Original acc: 28.17%, attacked acc: 4.23%, dropped acc: 23.94%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Does the relations between the given sentences \xe2\xb2\x85epresent entailment or not_entailment? Resp\xd0\xbend with 'entailment' or 'not_entailment'. "
Original acc: 23.94%, attacked acc: 0.00%, dropped acc: 23.94%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"During your role as an entailment aalysis tool, assess the relationshi\xd1\x80 between the given sentences and classify it as 'entailment' or 'not_entailment'. "
Original acc: 16.90%, attacked acc: 1.41%, dropped acc: 15.49%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"As an entailment identification s\xd1\x83stem, examin\xd0\xb5 the connection between the following sentences and responding with 'entailment' or 'not_entailment'. "
Original acc: 16.90%, attacked acc: 1.41%, dropped acc: 15.49%

Original prompt: Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.
Attacked prompt: b"Functioning as an entailment evaluation too\xe2\x85\xbc, analyze the provided sentences and decid\xd0\xb5 if their relationship is 'entailment' or 'not_entailment'. "
Original acc: 12.68%, attacked acc: 1.41%, dropped acc: 11.27%

## textfooler

Original prompt: Are the following two sentences entailment or not_entailment? Answer me with "entailment" or "not_entailment", just one word.
Attacked prompt: b'Se the aftermath two sentences entailment or not_entailment? Reactions me with "entailment" or "not_entailment", just one terminology. '
Original acc: 32.39%, attacked acc: 1.41%, dropped acc: 30.99%

Original prompt: Please classify the relationship between the provided sentences as 'entailment' or 'not_entailment'.
Attacked prompt: b"Urge classify the liaisons between the provided sentences as 'entailment' or 'not_entailment'. "
Original acc: 28.17%, attacked acc: 1.41%, dropped acc: 26.76%

Original prompt: Does the relationship between the given sentences represent entailment or not_entailment? Respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"Did the coitus between the given sentence represent entailment or not_entailment? Respondent with 'entailment' or 'not_entailment'. "
Original acc: 23.94%, attacked acc: 0.00%, dropped acc: 23.94%

Original prompt: In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Attacked prompt: b"Between your role as an entailment valuation appliance, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'. "
Original acc: 16.90%, attacked acc: 0.00%, dropped acc: 16.90%

Original prompt: As an entailment identification system, examine the connection between the following sentences and respond with 'entailment' or 'not_entailment'.
Attacked prompt: b"As an entailment identification plans, reviewed the connection between the following sentences and answered with 'entailment' or 'not_entailment'. "
Original acc: 16.90%, attacked acc: 1.41%, dropped acc: 15.49%

Original prompt: Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'.
Attacked prompt: b"Functioning as an entailment evaluation tool, analyze the provided sentences and decide if their relationship is 'entailment' or 'not_entailment'. "
Original acc: 12.68%, attacked acc: 12.68%, dropped acc: 4.23%

## translation

Language: chinese, acc: 11.27%, prompt: In the light of an implication analysis tool, evaluate the relationship between the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 15.49%, prompt: From the perspective of an implication analysis tool, determine whether there is an implication relationship in the following sentences by classifying them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 8.45%, prompt: Please use an implication analysis tool to determine whether an implication relationship exists in the following sentences by classifying them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 26.76%, prompt: Please evaluate the relation of the following sentences as 'entailment' or 'not_entailment' for the purpose of determining implication relation.
Language: chinese, acc: 9.86%, prompt: Please use the implication analysis tool to evaluate the relationships between the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 1.41%, prompt: For the purpose of determining implicative relations, analyze the relations of the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 11.27%, prompt: Please use the implication analysis tool to determine the relationship of the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 9.86%, prompt: Please use the implication judgment tool to assess the relevance of the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 14.08%, prompt: Please, with implication analysis as the main task, determine the relationships between the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: chinese, acc: 4.23%, prompt: Using the implication judgment as a criterion, analyze the relation of the following sentences and classify them as 'entailment' or 'not_entailment'.
Language: french, acc: 9.86%, prompt: As an engagement analysis tool, evaluate the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'.
Language: french, acc: 4.23%, prompt: Determine whether the given sentences involve one another or not as an implication analysis tool. Classify them accordingly as 'entailment' or 'not_entailment'.
Language: french, acc: 5.63%, prompt: Using implication analysis, evaluate whether the sentences provided have a logical relationship and categorize them as 'entailment' or 'not_entailment'.
Language: french, acc: 11.27%, prompt: As an engagement assessment tool, determine whether the sentences provided have a logical relationship and classify them as 'entailment' or 'not_entailment'.
Language: french, acc: 8.45%, prompt: As an implication classification tool, analyze the sentences provided to determine if there is a logical relationship and categorize them as 'entailment' or 'not_entailment'.
Language: french, acc: 0.00%, prompt: Using implication analysis, determine whether the given sentences have a cause-effect relationship and categorize them as 'entailment' or 'not_entailment'.
Language: french, acc: 7.04%, prompt: Evaluate the relationship between the given sentences using implication analysis and rank them accordingly as 'entailment' or 'not_entailment'.
Language: french, acc: 14.08%, prompt: As an engagement detection tool, determine whether the given sentences have a logical relationship and categorize them as 'entailment' or 'not_entailment'.
Language: french, acc: 1.41%, prompt: Using implication analysis, evaluate whether the sentences provided have a cause-effect relationship and rank them accordingly as 'entailment' or 'not_entailment'.
Language: french, acc: 2.82%, prompt: Determine whether the given sentences have a cause-effect relationship as an engagement analysis tool and categorize them as 'entailment' or 'not_entailment'.
Language: arabic, acc: 9.86%, prompt: In your role as a tool for reasoning analysis, evaluate the relationship between given sentences and classify them as 'entailment' or 'not_entailment'.
Language: arabic, acc: 12.68%, prompt: Can you determine whether this sentence is inferred from the other sentence? Classify it as 'entailment' or 'not_entailment'.
Language: arabic, acc: 9.86%, prompt: Using the tool of reasoning analysis, analyze the relationship between given sentences and classify them as 'entailment' or 'not_entailment'.
Language: arabic, acc: 28.17%, prompt: Does this sentence represent a conclusion from the previous sentence? Classify it as 'entailment' or 'not_entailment'.
Language: arabic, acc: 4.23%, prompt: As a tool of reasoning analysis, evaluate the relationship of given sentences and classify them as 'entailment' or 'not_entailment'.
Language: arabic, acc: 21.13%, prompt: Can this sentence be inferred from the previous sentence? Classify it as 'entailment' or 'not_entailment'.
Language: arabic, acc: 4.23%, prompt: Using a tool to analyze a conclusion, analyze the relationship between the two sentences and classify them as 'entailment' or 'not_entailment'.
Language: arabic, acc: 22.54%, prompt: Is this a conclusion from the next sentence? Classify it as 'entailment' or 'not_entailment'.
Language: arabic, acc: 9.86%, prompt: As part of your task in analyzing a conclusion, evaluate the relationship between the two sentences and classify them as 'entailment' or 'not_entailment' based on their relationship.
Language: arabic, acc: 22.54%, prompt: Are you following this sentence directly from the previous one? Classify it as 'entailment' or 'not_entailment'.
Language: spanish, acc: 15.49%, prompt: In your role as an implication analysis tool, evaluate the relationship between the given phrases and classify them as 'entailment' or 'not_entailment'.
Language: spanish, acc: 26.76%, prompt: Determine whether the second sentence necessarily implies the first and label the relation as 'entailment', or as 'not_entailment' if not.
Language: spanish, acc: 2.82%, prompt: Classifies the relationship between these two sentences as 'entailment' if one necessarily implies the other, or as 'not_entailment' if not.
Language: spanish, acc: 4.23%, prompt: Evaluates whether the information in the second sentence is implied in the first and labels the relationship as 'entailment', or as 'not_entailment' if there is no such implication.
Language: spanish, acc: 4.23%, prompt: Given a couple of phrases, label their relationship as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication.
Language: spanish, acc: 2.82%, prompt: Analyzes the relationship between the phrases and classifies them as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication.
Language: spanish, acc: 9.86%, prompt: Given two sentences, determine whether the second sentence is a necessary consequence of the first and label the relation as 'entailment', or as 'not_entailment' if not.
Language: spanish, acc: 5.63%, prompt: Evaluates whether the information presented in the second sentence is implicit in the first and labels the relationship as 'entailment', or as 'not_entailment' if there is no such implication.
Language: spanish, acc: 0.00%, prompt: Classifies the relationship between the given phrases as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication.
Language: spanish, acc: 15.49%, prompt: Determines whether the information provided in the second sentence is necessarily inferable from the first and labels the relationship as 'entailment', or as 'not_entailment' if not.
Language: japanese, acc: 1.41%, prompt: Analyze the relationship of a given sentence and classify it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 4.23%, prompt: Evaluate the semantic relationship of the sentence and classify it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 16.90%, prompt: Please judge the relationship between the given sentences and classify them as 'entailment' or 'not_entailment'.
Language: japanese, acc: 7.04%, prompt: Examine the paraphrases of a given sentence and classify them 'entailment' or 'not_entailment'.
Language: japanese, acc: 2.82%, prompt: Rate the similarity of a given sentence and categorize it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 2.82%, prompt: Determinate the semantic connections of a given sentence and classify it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 2.82%, prompt: Examine the semantic match of a given sentence and categorize it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 5.63%, prompt: Classify it as 'entailment' or 'not_entailment' based on the content of the sentence.
Language: japanese, acc: 1.41%, prompt: Analyze the relationship of a given sentence and classify it as 'entailment' or 'not_entailment'.
Language: japanese, acc: 0.00%, prompt: Judge the semantic connections of a given sentence and categorize it as 'entailment' or 'not_entailment'.
Language: korean, acc: 8.45%, prompt: Evaluate the relationship between any two sentences given to you and classify you as 'entailment' or 'not_entailment'.
Language: korean, acc: 7.04%, prompt: Analyze the semantic deductive relations between sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 4.23%, prompt: Evaluate the logical relevance between sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 1.41%, prompt: Evaluate the interaction of two given sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 19.72%, prompt: Please check whether there is a semantic match between those two sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 1.41%, prompt: Compare information between given sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 29.58%, prompt: Please analyse the correlation between those two sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 5.63%, prompt: Evaluate the different meanings between given sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 9.86%, prompt: Compare the semantic structure of the two sentences and classify them as 'entailment' or 'not_entailment'.
Language: korean, acc: 4.23%, prompt: Evaluate the interactions between sentences and classify them as 'entailment' or 'not_entailment'.

# mmlu

## 10 prompts

Acc: 10.39%, prompt: Answer the following multiple-choice question about {} by selecting the correct option: 'A', 'B', 'C', or 'D'.
Acc: 10.15%, prompt: In relation to the multiple-choice question on {}, please provide the accurate answer by choosing 'A', 'B', 'C', or 'D'.
Acc: 9.10%, prompt: Answer the subsequent multiple-choice question about {} by picking the right option among 'A', 'B', 'C', or 'D'.
Acc: 8.98%, prompt: Evaluate the multiple-choice question about {} and select the most fitting response from 'A', 'B', 'C', or 'D'.
Acc: 7.82%, prompt: Regarding the following multiple-choice question on {}, pick the correct answer from the options 'A', 'B', 'C', or 'D'.
Acc: 7.70%, prompt: Please respond to the multiple-choice question about {} by selecting the appropriate answer: 'A', 'B', 'C', or 'D'.
Acc: 7.58%, prompt: For the multiple-choice question related to {}, please choose the most accurate answer from 'A', 'B', 'C', or 'D'.
Acc: 6.07%, prompt: For each multiple-choice question about {}, identify the correct answer by selecting 'A', 'B', 'C', or 'D'.
Acc: 5.72%, prompt: Examine the following question based on {} and choose the correct response from 'A', 'B', 'C', or 'D'.
Acc: 5.13%, prompt: Below are multiple-choice question concerning {}. Indicate your response with 'A', 'B', 'C', or 'D'.

Acc: 9.80%, prompt: With your knowledge of {}, tackle the following multiple-choice question by choosing 'A', 'B', 'C', or 'D'.
Acc: 9.68%, prompt: With your understanding of {}, kindly answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D'.
Acc: 9.45%, prompt: As someone well-versed in {}, please address the multiple-choice question below by selecting 'A', 'B', 'C', or 'D'.
Acc: 9.33%, prompt: As a knowledgeable individual in {}, provide your response to the multiple-choice question by choosing 'A', 'B', 'C', or 'D'.
Acc: 9.22%, prompt: As an expert in {}, respond to the following multiple-choice question by selecting 'A', 'B', 'C', or 'D'.
Acc: 8.98%, prompt: As a skilled person in the field of {}, please respond to the multiple-choice question by choosing 'A', 'B', 'C', or 'D'.
Acc: 8.87%, prompt: Drawing upon your mastery of {}, please answer the multiple-choice question by selecting the correct option from 'A', 'B', 'C', or 'D'.
Acc: 8.52%, prompt: Considering your familiarity with {}, attend to the following multiple-choice question by picking 'A', 'B', 'C', or 'D'.
Acc: 7.70%, prompt: Given your proficiency in {}, please answer the subsequent multiple-choice question with 'A', 'B', 'C', or 'D'.
Acc: 6.18%, prompt: Utilizing your expertise in {}, answer the following multiple-choice question by picking 'A', 'B', 'C', or 'D'.

## bertattack

Original prompt: Answer the following multiple-choice question about {} by selecting the correct option: 'A', 'B', 'C', or 'D'.
Attacked prompt: b"Answer the following multiple-options questions about {} by selecting the given ending: 'A', 'B', 'C', or 'D'. "
Original acc: 9.57%, attacked acc: 3.72%, dropped acc: 5.85%

Original prompt: In relation to the multiple-choice question on {}, please provide the accurate answer by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"should assignment to the multiple-: answer on {}, please provide the accurate asking by choosing 'A', 'B', 'C', or 'D'. "
Original acc: 9.57%, attacked acc: 3.72%, dropped acc: 5.85%

Original prompt: Evaluate the multiple-choice question about {} and select the most fitting response from 'A', 'B', 'C', or 'D'.
Attacked prompt: b"i the multiple-a asked about {} and select the most fitting response from 'A', 'B', 'C', or 'D'. "
Original acc: 8.51%, attacked acc: 3.55%, dropped acc: 4.96%

Original prompt: With your understanding of {}, kindly answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"With your understand of {}, self answer the subsequent multiple-chosen questions by stating 'A', 'B', 'C', or 'D'."
Original acc: 9.22%, attacked acc: 3.37%, dropped acc: 5.85%

Original prompt: As an expert in {}, respond to the following multiple-choice question by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"As an expert in {}, respond to the following multiple-difficulty problem by type 'A', 'B', 'C', or 'D'."
Original acc: 9.04%, attacked acc: 4.08%, dropped acc: 4.96%

Original prompt: With your knowledge of {}, tackle the following multiple-choice question by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"ll your knowledge of {}, answer the following multiple-difficulty asked by picking 'A', 'B', 'C', or 'D'."
Original acc: 8.87%, attacked acc: 3.37%, dropped acc: 5.50%

## checklist

Original prompt: Answer the following multiple-choice question about {} by selecting the correct option: 'A', 'B', 'C', or 'D'.
Attacked prompt: b"Answer the following multiple-choice question about {} by selecting the correct option: 'A', 'B', 'C', or 'D' w52rwgo0Av. "
Original acc: 10.39%, attacked acc: 6.77%, dropped acc: 3.62%Original prompt: In relation to the multiple-choice question on {}, please provide the accurate answer by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"In relation to the multiple-choice question on {}, please provide the accurate answer by choosing 'A', 'B', 'C', or 'D' OB4KVJzIft. "
Original acc: 10.15%, attacked acc: 5.02%, dropped acc: 5.13%

Original prompt: Answer the subsequent multiple-choice question about {} by picking the right option among 'A', 'B', 'C', or 'D'.
Attacked prompt: b"Answer the subsequent multiple-choice question about {} by picking the right option among 'A', 'B', 'C', or 'D' w52rwgo0Av. "
Original acc: 9.10%, attacked acc: 6.42%, dropped acc: 2.68%

Original prompt: With your knowledge of {}, tackle the following multiple-choice question by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"With your knowledge of {}, tackle the following multiple-choice question by choosing 'A', 'B', 'C', or 'D' w52rwgo0Av."
Original acc: 9.80%, attacked acc: 5.25%, dropped acc: 4.55%

Original prompt: With your understanding of {}, kindly answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"With your understanding of {}, kindly answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D' w52rwgo0Av."
Original acc: 9.68%, attacked acc: 4.90%, dropped acc: 4.78%

Original prompt: As someone well-versed in {}, please address the multiple-choice question below by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"As someone well-versed in {}, please address the multiple-choice question below by selecting 'A', 'B', 'C', or 'D' w52rwgo0Av."
Original acc: 9.45%, attacked acc: 4.43%, dropped acc: 5.02%

## deepwordbug

Original prompt: Answer the following multiple-choice question about {} by selecting the correct option: 'A', 'B', 'C', or 'D'.
Attacked prompt: b"WAnswer the fkollowing multiple-chAice question about {} by selecting the correct option: 'A', 'B', 'C', or 'D'. "
Original acc: 10.39%, attacked acc: 6.53%, dropped acc: 3.85%

Original prompt: In relation to the multiple-choice question on {}, please provide the accurate answer by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"oIn relatin to the mhltiple-choice question on {}, plese provide the accurate answer by choosing 'A', 'B', 'C', or 'D'. "
Original acc: 10.15%, attacked acc: 3.50%, dropped acc: 6.65%

Original prompt: Answer the subsequent multiple-choice question about {} by picking the right option among 'A', 'B', 'C', or 'D'.
Attacked prompt: b"Anwer the subseuent mltiple-choice question about {} by picing the right option among 'A', 'B', 'C', or 'D'. "
Original acc: 9.10%, attacked acc: 4.78%, dropped acc: 4.32%

Original prompt: With your knowledge of {}, tackle the following multiple-choice question by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"With your knowlegde of {}, tacke the folloing mulBiple-choice question by choosing 'A', 'B', 'C', or 'D'."
Original acc: 9.80%, attacked acc: 6.07%, dropped acc: 3.73%

Original prompt: With your understanding of {}, kindly answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"With your understanding of {}, kinduy answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D'."
Original acc: 9.68%, attacked acc: 8.63%, dropped acc: 1.05%

Original prompt: As someone well-versed in {}, please address the multiple-choice question below by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"AGs someEne well-versed in {}, please address the multiple-choice question below by selecting 'A', 'B', 'C', or 'D'."
Original acc: 9.45%, attacked acc: 8.28%, dropped acc: 1.17%

## stresstest

Original prompt: Answer the following multiple-choice question about {} by selecting the correct option: 'A', 'B', 'C', or 'D'.
Attacked prompt: b"Answer the following multiple-choice question about {} by selecting the correct option: 'A', 'B', 'C', or 'D'  and true is true . "
Original acc: 10.39%, attacked acc: 13.30%, dropped acc: -2.92%

Original prompt: In relation to the multiple-choice question on {}, please provide the accurate answer by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"In relation to the multiple-choice question on {}, please provide the accurate answer by choosing 'A', 'B', 'C', or 'D'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 10.15%, attacked acc: 11.67%, dropped acc: -1.52%

Original prompt: Answer the subsequent multiple-choice question about {} by picking the right option among 'A', 'B', 'C', or 'D'.
Attacked prompt: b"Answer the subsequent multiple-choice question about {} by picking the right option among 'A', 'B', 'C', or 'D'  and true is true  and true is true  and true is true  and true is true  and true is true . "
Original acc: 9.10%, attacked acc: 13.19%, dropped acc: -4.08%

Original prompt: With your knowledge of {}, tackle the following multiple-choice question by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"With your knowledge of {}, tackle the following multiple-choice question by choosing 'A', 'B', 'C', or 'D'  and true is true  and true is true  and true is true  and true is true  and true is true ."
Original acc: 9.80%, attacked acc: 10.85%, dropped acc: -1.05%

Original prompt: With your understanding of {}, kindly answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"With your understanding of {}, kindly answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D'  and true is true  and true is true  and true is true  and true is true  and true is true ."
Original acc: 9.68%, attacked acc: 12.49%, dropped acc: -2.80%

Original prompt: As someone well-versed in {}, please address the multiple-choice question below by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"As someone well-versed in {}, please address the multiple-choice question below by selecting 'A', 'B', 'C', or 'D'  and true is true  and true is true  and true is true  and true is true  and true is true ."
Original acc: 9.45%, attacked acc: 13.30%, dropped acc: -3.85%

## textbugger

Original prompt: Answer the following multiple-choice question about {} by selecting the correct option: 'A', 'B', 'C', or 'D'.
Attacked prompt: b"Answer the \xf0\x9d\x9a\x8following m\xd5\xbdltiple-choice question about {} by select the corrected options: 'A', 'B', 'C', or 'D'. "
Original acc: 10.39%, attacked acc: 4.55%, dropped acc: 5.83%

Original prompt: In relation to the multiple-choice question on {}, please provide the accurate answer by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"In \xe2\xb2\x85elation to the m\xd5\xbdltiple-choice issues on {}, \xd1\x80lease pr\xd0\xbevide the accurate answer by choosing 'A', 'B', 'C', or 'D'. "
Original acc: 10.15%, attacked acc: 4.32%, dropped acc: 5.83%

Original prompt: Answer the subsequent multiple-choice question about {} by picking the right option among 'A', 'B', 'C', or 'D'.
Attacked prompt: b"Responding the subequent multipl-echoice question about {} by pick the right op\xf0\x9d\x9a\x9dion amongst 'A', 'B', 'C', or 'D'. "
Original acc: 9.10%, attacked acc: 3.50%, dropped acc: 5.60%

Original prompt: With your knowledge of {}, tackle the following multiple-choice question by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"With your expertise of {}, \xf0\x9d\x9a\x9dackle the following m\xd5\xbdltiple-choice que\xd1\x95tion by choosing 'A', 'B', 'C', or 'D'."
Original acc: 9.80%, attacked acc: 2.92%, dropped acc: 6.88%

Original prompt: With your understanding of {}, kindly answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"Wit\xd5\xb0 your understand of {}, \xf0\x9d\x92\x8cindly answer the successive m\xd5\xbdltiple-choice question by selecting 'A', 'B', 'C', or 'D'."
Original acc: 9.68%, attacked acc: 2.45%, dropped acc: 7.23%

Original prompt: As someone well-versed in {}, please address the multiple-choice question below by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"As someone well-versed in {}, pl\xd0\xb5ase a\xd4\x81dress the \xef\xbd\x8dultiple-choice questions below by choosing 'A', 'B', 'C', or 'D'."
Original acc: 9.45%, attacked acc: 4.90%, dropped acc: 4.55%

## textfooler

Original prompt: Answer the following multiple-choice question about {} by selecting the correct option: 'A', 'B', 'C', or 'D'.
Attacked prompt: b"Answer the suite multiple-choice problems about {} by selecting the appropriate selection: 'A', 'B', 'C', or 'D'. "
Original acc: 10.39%, attacked acc: 4.55%, dropped acc: 5.83%

Original prompt: In relation to the multiple-choice question on {}, please provide the accurate answer by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"At compared to the multiple-choice things on {}, please prescribes the corrects reaction by choices 'A', 'B', 'C', or 'D'. "
Original acc: 10.15%, attacked acc: 3.97%, dropped acc: 6.18%

Original prompt: Answer the subsequent multiple-choice question about {} by picking the right option among 'A', 'B', 'C', or 'D'.
Attacked prompt: b"Answer the consecutive multiple-choice questions about {} by choosing the ok option among 'A', 'B', 'C', or 'D'. "
Original acc: 9.10%, attacked acc: 3.73%, dropped acc: 5.37%

Original prompt: With your understanding of {}, kindly answer the subsequent multiple-choice question by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"With your understand of {}, gracefully answer the forth multiple-choice question by picking 'A', 'B', 'C', or 'D'."
Original acc: 9.22%, attacked acc: 4.61%, dropped acc: 4.61%

Original prompt: As an expert in {}, respond to the following multiple-choice question by selecting 'A', 'B', 'C', or 'D'.
Attacked prompt: b"As an specializing in {}, answer to the following multiple-choice things by selecting 'A', 'B', 'C', or 'D'."
Original acc: 9.04%, attacked acc: 5.14%, dropped acc: 3.90%

Original prompt: With your knowledge of {}, tackle the following multiple-choice question by choosing 'A', 'B', 'C', or 'D'.
Attacked prompt: b"With your comprehend of {}, face the following multiple-choice questions by choosing 'A', 'B', 'C', or 'D'."
Original acc: 8.87%, attacked acc: 6.21%, dropped acc: 2.66%

## translation

Language: chinese, acc: 9.22%, prompt: For the following multiple choice question about {}, please select the correct answer from 'A', 'B', 'C' or 'D'.
Language: chinese, acc: 11.88%, prompt: Please select the correct answer from 'A', 'B', 'C' or 'D' for the following multiple choice question for {}.
Language: chinese, acc: 9.75%, prompt: Select the correct answer from 'A', 'B', 'C' or 'D' for the following multiple choice question {}.
Language: chinese, acc: 4.79%, prompt: Please choose the correct answer from 'A', 'B', 'C' or 'D' according to the following multiple-choice questions about {}.
Language: chinese, acc: 4.96%, prompt: Please select the correct answer from 'A', 'B', 'C' or 'D' for the {} multiple choice questions below.
Language: chinese, acc: 6.74%, prompt: The following is A multiple choice question about {}. Please select the correct answer from 'A', 'B', 'C' or 'D'.
Language: chinese, acc: 10.82%, prompt: Please select the correct answer from 'A', 'B', 'C' or 'D' for the following multiple choice question {}.
Language: chinese, acc: 4.79%, prompt: Please choose the correct answer from 'A', 'B', 'C' or 'D' according to the following multiple-choice questions about {}.
Language: chinese, acc: 6.38%, prompt: Please select the correct answer from 'A', 'B', 'C' or 'D' for the following multiple choice questions about {}.
Language: chinese, acc: 6.38%, prompt: Please select the correct answer from 'A', 'B', 'C' or 'D' for the following multiple choice questions about {}.
Language: french, acc: 6.74%, prompt: For the following multiple choice question on {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: french, acc: 4.79%, prompt: This is a multiple choice question about {}. Select the correct answer from options 'A', 'B', 'C' or 'D'.
Language: french, acc: 9.04%, prompt: In the context of the multiple-choice question on {}, identify the correct answer from options 'A', 'B', 'C' or 'D'.
Language: french, acc: 7.45%, prompt: About the following question on {}, determine the correct answer from the choices 'A', 'B', 'C' or 'D'.
Language: french, acc: 7.27%, prompt: Carefully review the multiple-choice question regarding {}. Choose the correct answer from options 'A', 'B', 'C', or 'D'.
Language: french, acc: 9.22%, prompt: For the multiple-choice question for {}, indicate the correct answer from options 'A', 'B', 'C', or 'D'.
Language: french, acc: 5.50%, prompt: The next question is about {}. Select the correct answer from the choices 'A', 'B', 'C' or 'D'.
Language: french, acc: 7.45%, prompt: As part of the multiple-choice question on {}, choose the appropriate answer from options 'A', 'B', 'C' or 'D'.
Language: french, acc: 8.16%, prompt: Rate your understanding of the multiple-choice question on {}. Choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: french, acc: 9.22%, prompt: Analyze the following multiple-choice question on {}. Identify the correct answer among choices 'A', 'B', 'C' or 'D'.
Language: arabic, acc: 6.38%, prompt: For the multiple choice question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: arabic, acc: 6.56%, prompt: For the following multiple-choice question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: arabic, acc: 7.09%, prompt: For the following multiple choice question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: arabic, acc: 11.70%, prompt: When it comes to the multiple-choice question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: arabic, acc: 7.80%, prompt: For the multiple-choice question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: arabic, acc: 7.62%, prompt: If the question for {} is multiple choice, choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: arabic, acc: 6.21%, prompt: For the question regarding {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: arabic, acc: 6.21%, prompt: For the question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: arabic, acc: 7.27%, prompt: When it comes to the question regarding {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: arabic, acc: 6.21%, prompt: For the question regarding {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.
Language: spanish, acc: 7.80%, prompt: For the following multiple-choice question about {}, choose the correct answer from 'A', 'B', 'C', or 'D'.
Language: spanish, acc: 7.98%, prompt: For the following multiple-choice question about {}, select the correct answer from 'A', 'B', 'C', or 'D'.
Language: spanish, acc: 7.80%, prompt: For the following multiple-choice question about {}, choose the correct answer from 'A', 'B', 'C', or 'D'.
Language: spanish, acc: 10.64%, prompt: Within the context of the following multiple-choice question about {}, choose the correct option from 'A', 'B', 'C', or 'D'.
Language: spanish, acc: 6.91%, prompt: For the following multiple-choice statement about {}, select the correct answer from 'A', 'B', 'C', or 'D'.
Language: spanish, acc: 10.11%, prompt: Considering the following multiple-choice question about {}, mark the correct answer with 'A', 'B', 'C', or 'D'.
Language: spanish, acc: 6.74%, prompt: For the following multiple-choice question about {}, choose the correct alternative among 'A', 'B', 'C' or 'D'.
Language: spanish, acc: 6.74%, prompt: For the following multiple-choice statement about {}, choose the correct option from alternatives 'A', 'B', 'C', or 'D'.
Language: spanish, acc: 9.22%, prompt: Within the context of the following multiple-choice question about {}, select the correct answer from alternatives 'A', 'B', 'C', or 'D'.
Language: spanish, acc: 9.22%, prompt: Considering the following multiple-choice statement about {}, mark the correct alternative with the options 'A', 'B', 'C' or 'D'.
Language: japanese, acc: 7.98%, prompt: Choose the appropriate answer from options 'A', 'B', 'C', or 'D' for {} regarding the following question.
Language: japanese, acc: 8.16%, prompt: Choose the correct answer from 'A', 'B', 'C', or 'D' for the following multiple-choice question about {}.
Language: japanese, acc: 6.21%, prompt: For the following multiple-choice questions about {}, choose the correct answer from 'A', 'B', 'C', or 'D'.
Language: japanese, acc: 4.79%, prompt: Choose the correct answer from options 'A', 'B', 'C', or 'D' for the following questions about {}.
Language: japanese, acc: 6.91%, prompt: In the multiple choice questions below, choose the correct answer for {} from 'A', 'B', 'C', or 'D'.
Language: japanese, acc: 4.43%, prompt: Choose the correct answer from the options 'A', 'B', 'C', or 'D' for the following questions about {}.
Language: japanese, acc: 6.91%, prompt: In the multiple choice questions below, choose the correct answer for {} from 'A', 'B', 'C', or 'D'.
Language: japanese, acc: 5.32%, prompt: Choose the correct answer from 'A', 'B', 'C', or 'D' for the following multiple choice questions about {}.
Language: japanese, acc: 6.91%, prompt: In the multiple choice questions below, choose the correct answer for {} from 'A', 'B', 'C', or 'D'.
Language: japanese, acc: 8.16%, prompt: Choose the correct answer from options 'A', 'B', 'C', or 'D' for {} regarding the following question.
Language: korean, acc: 5.14%, prompt: For the multiple choice problem about, choose the correct answer for '{}' from 'A', 'B', 'C', or 'D'.
Language: korean, acc: 6.56%, prompt: Choose the correct answer for '{}' from 'A', 'B', 'C', or 'D' in the multiple choice problem involving,
Language: korean, acc: 6.38%, prompt: For the multiple choice problem below, choose the correct answer to '{}' from 'A', 'B', 'C', or 'D'.
Language: korean, acc: 8.51%, prompt: In the following multiple-choice problem, choose the correct answer for '{}' from 'A', 'B', 'C', or 'D'.
Language: korean, acc: 7.98%, prompt: For the following multiple choice problem, choose the correct answer for '{}' from 'A', 'B', 'C', or 'D'.
Language: korean, acc: 9.04%, prompt: Solve multiple choice problems about: Which of 'A', 'B', 'C', or 'D' is the correct answer for '{}'.
Language: korean, acc: 8.16%, prompt: Choose the correct answer to the multiple-choice question below. Is '{}' an 'A', 'B', 'C', or 'D'.
Language: korean, acc: 6.03%, prompt: Solve the following multiple-choice problem. Choose the correct answer for '{}' from 'A', 'B', 'C', or 'D'.
Language: korean, acc: 8.51%, prompt: Choose the correct answer to the following multiple choice problem: Is '{}' 'A', 'B', 'C', or 'D'.
Language: korean, acc: 7.45%, prompt: Solve multiple-choice problems about: Please select 'A', 'B', 'C', or 'D' for the correct answer to '{}'.

# squad_v2

## 10 prompts

## bertattack

## checklist

## deepwordbug

## stresstest

## textbugger

## textfooler

# un_multi

## 10 prompts

## bertattack

## checklist

## deepwordbug

## stresstest

## textbugger

## textfooler

# iwslt

## 10 prompts

## bertattack

## checklist

## deepwordbug

## stresstest

## textbugger

## textfooler

# math

## 10 prompts

## bertattack

## checklist

## deepwordbug

## stresstest

## textbugger

## textfooler