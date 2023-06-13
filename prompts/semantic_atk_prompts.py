# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
This file contains the semantic attack prompts of each dataset.
6 languages: chinese, french, arabic, russian, spanish, english.
"""

SEMANTIC_ADV_PROMPT_SET = {
    'math': {
        'chinese': [
            # Chinese_English
            # "计算关于{}的数学问题的答案。",
            # "计算{}的数值。",
            # "请计算{}的结果。",
            # "根据{}，求解以下数学问题。",
            # "使用{}进行数学计算。",
            # "求解涉及{}的数学问题。",
            # "请计算涉及{}的答案。",
            # "根据{}，求解以下数值。",
            # "使用{}计算以下数学任务。",
            # "计算{}相关问题的答案。",
            "Calculate the answer to a mathematical question about {}." ,
            "Calculate the value of {}." ,
            "Please calculate the result of {}." ,
            "According to {}, solve the following mathematical problem." ,
            "Do the math with {}." ,
            "Solve mathematical problems involving {}." ,
            "Please calculate the answer involving {}." ,
            "Solve for the following values based on {}." ,
            "Calculate the following mathematical tasks using {}." ,
            "Calculate the answer to the {} related question." ,
        ],

        'french': [
            # French_English
            # "Calculez la réponse à la question mathématique suivante concernant {}.",
            # "Calculez le résultat de {}.",
            # "Veuillez calculer la valeur de {}.",
            # "Selon {}, résolvez le problème mathématique suivant.",
            # "Effectuez des calculs mathématiques avec {}.",
            # "Résolvez le problème mathématique impliquant {}.",
            # "Veuillez calculer la réponse liée à {}.",
            # "Selon {}, déterminez la valeur suivante.",
            # "Effectuez la tâche mathématique suivante en utilisant {}.",
            # "Calculez la réponse aux questions relatives à {}. ",
            "Calculate the answer to the following mathematical question concerning {}.",
            "Calculate the result of {}.",
            "Please calculate the value of {}.",
            "According to {}, solve the following mathematical problem.",
            "Perform mathematical calculations with {}.",
            "Solve the mathematical problem involving {}.",
            "Please calculate the answer related to {}.",
            "According to {}, set the following value.",
            "Perform the following mathematical task using {}.",
            "Calculate the answer to the questions related to {}. ",
        ],

        'arabic': [
            # Arabic_English
            # "احسب الإجابة على السؤال الرياضي التالي حول {}.",
            # "احسب قيمة {}.",
            # "يرجى احتساب قيمة {}.",
            # "وفقًا لـ {} ، حل المشكلة الرياضية التالية.",
            # "قم بإجراء حسابات رياضية باستخدام {}.",
            # "حل المشكلة الرياضية التي تشمل {}.",
            # "يرجى احتساب الإجابة المتعلقة بـ {}.",
            # "وفقًا لـ {} ، حدد القيمة التالية.",
            # "قم بإجراء المهمة الرياضية التالية باستخدام {}.",
            # "احسب الإجابة على الأسئلة المتعلقة بـ {}. ",
            "Compute the answer to the next mathematical question about {}.",
            "Calculate {}.",
            "Please calculate {}.",
            "According to {}, solve the following mathematical problem.",
            "Do mathematical calculations using {}.",
            "A solution to the mathematical problem involving {}.",
            "Please calculate the answer regarding {}.",
            "According to {}, determine the next value.",
            "DO THE NEXT MATHEMATICAL JOB USING {}.",
            "Calculate the answer to questions related to {}. ",
        ],

        'spanish': [
            # Spanish_English
            # "Calcula la respuesta a la siguiente pregunta matemática sobre {}.",
            # "Calcula el resultado de {}.",
            # "Por favor, calcula el valor de {}.",
            # "Según {}, resuelve el siguiente problema matemático.",
            # "Realiza cálculos matemáticos utilizando {}.",
            # "Resuelve el problema matemático que involucra {}.",
            # "Por favor, calcula la respuesta relacionada con {}.",
            # "Según {}, determina el siguiente valor.",
            # "Realiza la siguiente tarea matemática utilizando {}.",
            # "Calcula la respuesta a las preguntas relacionadas con {}. ",
            "Compute the answer to the following mathematical question on {}.",
            "Compute the result of {}.",
            "Please calculate the value of {}.",
            "As {}, it solves the following mathematical problem.",
            "Performs mathematical calculations using {}.",
            "Solve the mathematical problem involving {}.",
            "Please calculate the answer related to {}.",
            "As {}, determine the next value.",
            "Perform the following mathematical task using {}.",
            "Compute the answer to questions related to {}. ",
        ],

        'japanese': [
            # Japanese_English
            # "{}に関する数学の問題の答えを計算してください。",
            # "{}の値を計算してください。",
            # "{}の答えを求めてください。",
            # "{}に基づいて、以下の数学の問題を解いてください。",
            # "{}を使用して数学の計算を行ってください。",
            # "{}を含む数学の問題を解いてください。",
            # "{}に関連する答えを計算してください。",
            # "{}に基づいて、以下の値を求めてください。",
            # "{}を使用して、以下の数学の課題を解いてください。",
            # "{}に関連する問題の答えを計算してください。",
            "Calculate the answers to the math questions about {}." ,
            "Calculate the value of {}." ,
            "Please find the answer to {}." ,
            "Based on {}, please solve the following mathematical problems." ,
            "Use {} to perform mathematical calculations." ,
            "Please solve the math problem that contains {}." ,
            "Please calculate the answers related to {}." ,
            "Based on {}, find the following values:" ,
            "Use {} to solve the following mathematical problem." ,
            "Please calculate the answers to the questions related to {}." ,
 
        ],

        'korean': [
            # Korean_English
            # "{}에 대한 다음 수학 문제의 답을 계산하세요.",
            # "{}의 결과를 계산하세요.",
            # "{}의 값을 계산해주세요.",
            # "{}에 따라 다음 수학 문제를 풀어보세요.",
            # "{}를 사용하여 수학 계산을 진행하세요.",
            # "{}와 관련된 수학 문제를 해결하세요.",
            # "{}에 대한 답을 계산해주세요.",
            # "{}에 따라 다음 값을 구해보세요.",
            # "{}를 사용하여 다음 수학 과제를 해결하세요.",
            # "{}와 관련된 문제의 답을 계산하세요.",
            "Calculate the answer of the following math problem to {}.",
            "Calculate the result of {}.",
            "Please calculate the value of {}.",
            "Work out the following math problems according to {}.",
            "Use {} to proceed with mathematical calculations.",
            "Work out a math problem involving {}.",
            "Please calculate the answer to {}.",
            "Try to get the following values according to {}.",
            "Work out the next math task using {}.",
            "Calculate the answer of the problem involving {}.",
        ],
    },
    
    'translation_iwslt': {
        'chinese': [
            # Chinese_English
            # "请将给定的句子翻译成{}到{}。",
            # "请将下列句子从{}翻译成{}。",
            # "请将以下句子转换为{}，并翻译为{}。",
            # "请将所给句子从{}转化为{}。",
            # "请将下句从{}翻译成{}。",
            # "请将以下句子从{}转译为{}。",
            # "请将所给句子翻译为{}，转化成{}。",
            # "请将给出的句子转换为{}到{}。",
            # "请将下列句子翻译为{}，转化为{}。",
            # "请将所给句子从{}转变成{}。",
            "Please translate the given sentence into {} to {}." ,
            "Please translate the following sentences from {} to {}." ,
            "Please convert the following sentences to {} and translate to {}." ,
            "Please convert the given sentence from {} to {}." ,
            "Please translate the next sentence from {} to {}." ,
            "Please translate the following sentence from {} to {}." ,
            "Please translate the sentences given into {} and convert them into {}." ,
            "Please convert the sentences given to {} to {}." ,
            "Please translate the following sentences into {} and convert them into {}." ,
            "Please change the given sentence from {} to {}." ,
        ],

        'french': [
            # French_English
            # "Veuillez effectuer une traduction de la phrase donnée, en la convertissant de {} à {}.",
            # "Veuillez traduire la phrase suivante de {} à {}.",
            # "Veuillez transformer la phrase ci-dessous en {}, puis la traduire en {}.",
            # "Veuillez convertir la phrase donnée de {} à {}.",
            # "Veuillez traduire la phrase suivante de {} vers {}.",
            # "Veuillez transposer la phrase ci-dessous de {} à {}.",
            # "Veuillez traduire la phrase donnée en {}, puis la convertir en {}.",
            # "Veuillez effectuer une traduction de la phrase fournie, en la transformant de {} à {}.",
            # "Veuillez traduire la phrase suivante en {}, puis la convertir en {}.",
            # "Veuillez transformer la phrase donnée de {} en {}. ",
            "Please translate the given sentence, converting it from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please turn the sentence below into {}, then translate it into {}.",
            "Please convert the given phrase from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please translate the sentence below from {} to {}.",
            "Please translate the given sentence to {}, then convert it to {}.",
            "Please make a translation of the supplied sentence, transforming it from {} to {}.",
            "Please translate the following sentence to {}, then convert it to {}.",
            "Please transform the given sentence from {} to {}. ",
        ],

        'arabic': [
            # Arabic_English
            # "يرجى تنفيذ ترجمة الجملة المعطاة، وتحويلها من {} إلى {}،",
            # "يرجى ترجمة الجملة التالية من {} إلى {}،",
            # "يرجى تحويل الجملة أدناه إلى {}، ثم ترجمتها إلى {}،",
            # "يرجى تحويل الجملة المعطاة من {} إلى {}،",
            # "يرجى ترجمة الجملة التالية من {} إلى {}،",
            # "يرجى تحويل الجملة أدناه من {} إلى {}،",
            # "يرجى ترجمة الجملة المعطاة إلى {}، ثم تحويلها إلى {}،",
            # "يرجى تنفيذ ترجمة الجملة المعطاة، وتحويلها من {} إلى {}،",
            # "يرجى ترجمة الجملة التالية إلى {}، ثم تحويلها إلى {}،",
            # "يرجى تحويل الجملة المعطاة من {} إلى {}. ",
            "Please translate the given sentence, and convert it from {} to {},",
            "Please translate the following sentence from {} to {},",
            "Please convert the sentence below to {}, and then translate it to {},",
            "Please convert the given sentence from {} to {}, ",
            "Please translate the following sentence from {} to {},",
            "Please convert the sentence below from {} to {}, ",
            "Please translate the given sentence to {}, then convert it to {}, ",
            "Please translate the given sentence, and convert it from {} to {},",
            "Please translate to {}, then convert to {}, ",
            "Please convert the given sentence from {} to {}. ",
        ],

        'spanish': [
            # Spanish_English
            # "Por favor, realiza una traducción de la frase proporcionada, convirtiéndola de {} a {}.",
            # "Por favor, traduce la siguiente frase de {} a {}.",
            # "Por favor, convierte la siguiente frase a {}, y luego tradúcela a {}.",
            # "Por favor, realiza una traducción de la frase dada, convirtiéndola de {} a {}.",
            # "Por favor, traduce la siguiente frase de {} a {}.",
            # "Por favor, convierte la siguiente frase de {} a {}.",
            # "Por favor, traduce la frase proporcionada a {}, y luego conviértela en {}.",
            # "Por favor, realiza una traducción de la frase siguiente, convirtiéndola de {} a {}.",
            # "Por favor, traduce la siguiente frase a {}, y luego conviértela en {}.",
            # "Por favor, convierte la frase dada de {} a {}. ",
            "Please make a translation of the provided phrase, converting it from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please convert the next sentence to {}, and then translate it to {}.",
            "Please make a translation of the given phrase, converting it from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please convert the following sentence from {} to {}.",
            "Please translate the sentence provided to {}, and then turn it to {}.",
            "Please make a translation of the following sentence, converting it from {} to {}.",
            "Please translate the next sentence to {}, and then turn it to {}.",
            "Please convert the given sentence from {} to {}. ",
        ],

        'japanese': [
            # Japanese_English
            # "与えられた文を{}から{}に翻訳してください。",
            # "次の文を{}から{}に翻訳してください。",
            # "以下の文を{}に変換し、{}に翻訳してください。",
            # "与えられた文を{}から{}に変換して翻訳してください。",
            # "次の文を{}から{}に翻訳してください。",
            # "以下の文を{}から{}に変換してください。",
            # "与えられた文を{}に翻訳し、{}に変換してください。",
            # "与えられた文を{}から{}に翻訳してください。",
            # "次の文を{}に翻訳し、{}に変換してください。",
            # "与えられた文を{}から{}に変換してください。",
            "Please translate the given sentence from {} to {}." ,
            "Please translate the following sentence from {} to {}." ,
            "Please convert the following sentences into {} and translate them into {}." ,
            "Please translate the given sentence by converting {} to {}." ,
            "Please translate the following sentence from {} to {}." ,
            "Please convert the following sentences from {} to {}." ,
            "Translate the given sentence into {} and convert it to {}." ,
            "Please translate the given sentence from {} to {}." ,
            "Translate the following sentence into {} and convert it to {}." ,
            "Convert the given statement from {} to {}." ,
        ],

        'korean': [
            # Korean_English
            # "주어진 문장을 {}에서 {}로 번역해주세요.",
            # "다음 문장을 {}에서 {}로 번역해주세요.",
            # "아래 문장을 {}로 변환한 후, {}로 번역해주세요.",
            # "주어진 문장을 {}에서 {}로 변환하여 번역해주세요.",
            # "다음 문장을 {}에서 {}로 번역해주세요.",
            # "아래 문장을 {}에서 {}로 변환해주세요.",
            # "주어진 문장을 {}로 번역한 후, {}로 변환해주세요.",
            # "주어진 문장을 {}에서 {}로 번역해주세요.",
            # "다음 문장을 {}로 번역한 후, {}로 변환해주세요.",
            # "주어진 문장을 {}에서 {}로 변환해주세요.",
            "Please translate the given sentence from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please translate the sentences below into {}, then {}.",
            "Please translate the given sentences from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please convert the sentences below from {} to {}.",
            "Please translate the given sentence into {}, then {}.",
            "Please translate the given sentence from {} to {}.",
            "Please translate the following sentences into {}, then {}.",
            "Please convert the given sentence from {} to {}.",
        ],
    },

    # 'translation_un_multi': just the same as 'translation_iwslt'
    'translation_un_multi': {
        'chinese': [
            # Chinese_English
            # "请将给定的句子翻译成{}到{}。",
            # "请将下列句子从{}翻译成{}。",
            # "请将以下句子转换为{}，并翻译为{}。",
            # "请将所给句子从{}转化为{}。",
            # "请将下句从{}翻译成{}。",
            # "请将以下句子从{}转译为{}。",
            # "请将所给句子翻译为{}，转化成{}。",
            # "请将给出的句子转换为{}到{}。",
            # "请将下列句子翻译为{}，转化为{}。",
            # "请将所给句子从{}转变成{}。",
            "Please translate the given sentence into {} to {}." ,
            "Please translate the following sentences from {} to {}." ,
            "Please convert the following sentences to {} and translate to {}." ,
            "Please convert the given sentence from {} to {}." ,
            "Please translate the next sentence from {} to {}." ,
            "Please translate the following sentence from {} to {}." ,
            "Please translate the sentences given into {} and convert them into {}." ,
            "Please convert the sentences given to {} to {}." ,
            "Please translate the following sentences into {} and convert them into {}." ,
            "Please change the given sentence from {} to {}." ,
        ],

        'french': [
            # French_English
            # "Veuillez effectuer une traduction de la phrase donnée, en la convertissant de {} à {}.",
            # "Veuillez traduire la phrase suivante de {} à {}.",
            # "Veuillez transformer la phrase ci-dessous en {}, puis la traduire en {}.",
            # "Veuillez convertir la phrase donnée de {} à {}.",
            # "Veuillez traduire la phrase suivante de {} vers {}.",
            # "Veuillez transposer la phrase ci-dessous de {} à {}.",
            # "Veuillez traduire la phrase donnée en {}, puis la convertir en {}.",
            # "Veuillez effectuer une traduction de la phrase fournie, en la transformant de {} à {}.",
            # "Veuillez traduire la phrase suivante en {}, puis la convertir en {}.",
            # "Veuillez transformer la phrase donnée de {} en {}. ",
            "Please translate the given sentence, converting it from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please turn the sentence below into {}, then translate it into {}.",
            "Please convert the given phrase from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please translate the sentence below from {} to {}.",
            "Please translate the given sentence to {}, then convert it to {}.",
            "Please make a translation of the supplied sentence, transforming it from {} to {}.",
            "Please translate the following sentence to {}, then convert it to {}.",
            "Please transform the given sentence from {} to {}. ",
        ],

        'arabic': [
            # Arabic_English
            # "يرجى تنفيذ ترجمة الجملة المعطاة، وتحويلها من {} إلى {}،",
            # "يرجى ترجمة الجملة التالية من {} إلى {}،",
            # "يرجى تحويل الجملة أدناه إلى {}، ثم ترجمتها إلى {}،",
            # "يرجى تحويل الجملة المعطاة من {} إلى {}،",
            # "يرجى ترجمة الجملة التالية من {} إلى {}،",
            # "يرجى تحويل الجملة أدناه من {} إلى {}،",
            # "يرجى ترجمة الجملة المعطاة إلى {}، ثم تحويلها إلى {}،",
            # "يرجى تنفيذ ترجمة الجملة المعطاة، وتحويلها من {} إلى {}،",
            # "يرجى ترجمة الجملة التالية إلى {}، ثم تحويلها إلى {}،",
            # "يرجى تحويل الجملة المعطاة من {} إلى {}. ",
            "Please translate the given sentence, and convert it from {} to {},",
            "Please translate the following sentence from {} to {},",
            "Please convert the sentence below to {}, and then translate it to {},",
            "Please convert the given sentence from {} to {}, ",
            "Please translate the following sentence from {} to {},",
            "Please convert the sentence below from {} to {}, ",
            "Please translate the given sentence to {}, then convert it to {}, ",
            "Please translate the given sentence, and convert it from {} to {},",
            "Please translate to {}, then convert to {}, ",
            "Please convert the given sentence from {} to {}. ",
        ],

        'spanish': [
            # Spanish_English
            # "Por favor, realiza una traducción de la frase proporcionada, convirtiéndola de {} a {}.",
            # "Por favor, traduce la siguiente frase de {} a {}.",
            # "Por favor, convierte la siguiente frase a {}, y luego tradúcela a {}.",
            # "Por favor, realiza una traducción de la frase dada, convirtiéndola de {} a {}.",
            # "Por favor, traduce la siguiente frase de {} a {}.",
            # "Por favor, convierte la siguiente frase de {} a {}.",
            # "Por favor, traduce la frase proporcionada a {}, y luego conviértela en {}.",
            # "Por favor, realiza una traducción de la frase siguiente, convirtiéndola de {} a {}.",
            # "Por favor, traduce la siguiente frase a {}, y luego conviértela en {}.",
            # "Por favor, convierte la frase dada de {} a {}. ",
            "Please make a translation of the provided phrase, converting it from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please convert the next sentence to {}, and then translate it to {}.",
            "Please make a translation of the given phrase, converting it from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please convert the following sentence from {} to {}.",
            "Please translate the sentence provided to {}, and then turn it to {}.",
            "Please make a translation of the following sentence, converting it from {} to {}.",
            "Please translate the next sentence to {}, and then turn it to {}.",
            "Please convert the given sentence from {} to {}. ",
        ],

        'japanese': [
            # Japanese_English
            # "与えられた文を{}から{}に翻訳してください。",
            # "次の文を{}から{}に翻訳してください。",
            # "以下の文を{}に変換し、{}に翻訳してください。",
            # "与えられた文を{}から{}に変換して翻訳してください。",
            # "次の文を{}から{}に翻訳してください。",
            # "以下の文を{}から{}に変換してください。",
            # "与えられた文を{}に翻訳し、{}に変換してください。",
            # "与えられた文を{}から{}に翻訳してください。",
            # "次の文を{}に翻訳し、{}に変換してください。",
            # "与えられた文を{}から{}に変換してください。",
            "Please translate the given sentence from {} to {}." ,
            "Please translate the following sentence from {} to {}." ,
            "Please convert the following sentences into {} and translate them into {}." ,
            "Please translate the given sentence by converting {} to {}." ,
            "Please translate the following sentence from {} to {}." ,
            "Please convert the following sentences from {} to {}." ,
            "Translate the given sentence into {} and convert it to {}." ,
            "Please translate the given sentence from {} to {}." ,
            "Translate the following sentence into {} and convert it to {}." ,
            "Convert the given statement from {} to {}." ,
        ],

        'korean': [
            # Korean_English
            # "주어진 문장을 {}에서 {}로 번역해주세요.",
            # "다음 문장을 {}에서 {}로 번역해주세요.",
            # "아래 문장을 {}로 변환한 후, {}로 번역해주세요.",
            # "주어진 문장을 {}에서 {}로 변환하여 번역해주세요.",
            # "다음 문장을 {}에서 {}로 번역해주세요.",
            # "아래 문장을 {}에서 {}로 변환해주세요.",
            # "주어진 문장을 {}로 번역한 후, {}로 변환해주세요.",
            # "주어진 문장을 {}에서 {}로 번역해주세요.",
            # "다음 문장을 {}로 번역한 후, {}로 변환해주세요.",
            # "주어진 문장을 {}에서 {}로 변환해주세요.",
            "Please translate the given sentence from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please translate the sentences below into {}, then {}.",
            "Please translate the given sentences from {} to {}.",
            "Please translate the following sentence from {} to {}.",
            "Please convert the sentences below from {} to {}.",
            "Please translate the given sentence into {}, then {}.",
            "Please translate the given sentence from {} to {}.",
            "Please translate the following sentences into {}, then {}.",
            "Please convert the given sentence from {} to {}.",
        ],
    },

    'squad_v2': {
        'chinese': [
            # Chinese_English
            # "从上下文中提供最精确的答案。如果答案不在上下文中，回答'无法回答'。",
            # "请根据上下文给出最准确的回答。如果无法找到答案，请回答'无法回答'。",
            # "根据上下文提供最精确的答案。如果找不到答案，请回答'无法回答'。",
            # "请从上下文中提供最准确的答案。如果找不到答案，请回答'无法回答'。",
            # "根据上下文给出最精确的答案。如果找不到答案，请回答'无法回答'。",
            # "请根据上下文给出最准确的答案。如果答案不在上下文中，回答'无法回答'。",
            # "从上下文中提供最精确的答案。如果找不到答案，请回答'无法回答'。",
            # "请根据上下文给出最准确的答案。如果答案无法找到，请回答'无法回答'。",
            # "根据上下文提供最精确的答案。如果答案找不到，请回答'无法回答'。",
            # "请从上下文中提供最准确的回答。如果答案找不到，请回答'无法回答'。",
            "Provide the most accurate answer from the context. If the answer is not in context, answer 'unanswerable'." ,
            "Please give the most accurate answer based on the context. If you cannot find the answer, please answer 'unanswerable'." ,
            "Provide the most accurate answer based on the context. If you cannot find the answer, please answer 'unanswerable'." ,
            "Please provide the most accurate answer from the context. If you cannot find the answer, please answer 'unanswerable'." ,
            "Give the most accurate answer based on the context. If you cannot find the answer, please answer 'unanswerable'." ,
            "Please give the most accurate answer based on the context. If the answer is not in context, answer 'unanswerable'." ,
            "Provide the most accurate answer from the context. If you cannot find the answer, please answer 'unanswerable'." ,
            "Please give the most accurate answer based on the context. If the answer cannot be found, please answer 'unanswerable'." ,
            "Provide the most accurate answer based on the context. If the answer cannot be found, please answer 'unanswerable'." ,
            "Please provide the most accurate answer from the context. If the answer cannot be found, please answer 'unanswerable'." ,
        ],

        'french': [
            # French_English
            # "À partir du contexte, fournissez la réponse la plus précise. Si la réponse n'est pas dans le contexte, répondez par 'impossible à répondre'.",
            # "À partir du contexte, donnez la réponse la plus précise. Si la réponse n'est pas présente dans le contexte, répondez par 'impossible à répondre'.",
            # "En vous basant sur le contexte, fournissez la réponse la plus précise. Si la réponse n'est pas dans le contexte, répondez avec 'impossible à répondre'.",
            # "D'après le contexte, donnez la réponse la plus précise. Si la réponse n'est pas présente dans le contexte, répondez par 'impossible à répondre'.",
            # "À partir du contexte, trouvez la réponse la plus précise. Si la réponse n'est pas dans le contexte, répondez avec 'impossible à répondre'.",
            # "En vous basant sur le contexte, fournissez la réponse la plus précise. Si la réponse n'est pas disponible dans le contexte, répondez par 'impossible à répondre'.",
            # "D'après le contexte, donnez la réponse la plus précise. Si la réponse ne se trouve pas dans le contexte, répondez par 'impossible à répondre'.",
            # "À partir du contexte, trouvez la réponse la plus précise. Si la réponse n'est pas présente dans le contexte, répondez avec 'impossible à répondre'.",
            # "En vous basant sur le contexte, fournissez la réponse la plus précise. Si la réponse n'est pas trouvable dans le contexte, répondez par 'impossible à répondre'.",
            # "D'après le contexte, donnez la réponse la plus précise. Si la réponse n'est pas disponible dans le contexte, répondez par 'impossible à répondre'.",
            "From the context, provide the most accurate answer. If the answer is not in context, answer with 'unanswerable'.",
            "From the context, give the most accurate answer. If the answer is not present in the context, answer with 'unanswerable'.",
            "Based on the context, provide the most accurate answer. If the answer is not in context, answer with 'unanswerable'.",
            "According to the context, give the most precise answer. If the answer is not present in the context, answer with 'unanswerable'.",
            "From the context, find the most accurate answer. If the answer is not in context, answer with 'unanswerable'.",
            "Based on the context, provide the most accurate answer. If the answer is not available in the context, answer with 'unanswerable'.",
            "According to the context, give the most precise answer. If the answer is not in the context, answer with 'unanswerable'.",
            "From the context, find the most accurate answer. If the answer is not present in the context, answer with 'unanswerable'.",
            "Based on the context, provide the most accurate answer. If the answer cannot be found in the context, answer with 'unanswerable'.",
            "According to the context, give the most precise answer. If the answer is not available in the context, answer with 'unanswerable'.",
        ],

        'arabic': [
            # Arabic_English
            # "من السياق، قدم الإجابة الأكثر دقة. إذا لم تتواجد الإجابة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "من السياق، ما هي النتيجة الأكثر محتملة؟ إذا كانت الإجابة غير موجودة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "من السياق المعطى، ما هو العنصر الأساسي الذي يمكن استنتاجه؟ إذا كانت الإجابة غير متوفرة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "استنادًا إلى السياق المعطى، ما هي الفكرة الرئيسية الواضحة؟ إذا كانت الإجابة غير موجودة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "استنادًا إلى السياق، ما هو التفسير الأكثر مقنعية؟ إذا كانت الإجابة غير متاحة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "استنادًا إلى السياق المذكور، ما هو النتيجة الأكثر احتمالًا؟ إذا كانت الإجابة غير متوفرة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "استنادًا إلى السياق، ما هي الفرضية الأكثر صحة؟ إذا كانت الإجابة غير موجودة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "من السياق، ما هو العامل المؤثر الأكثر ظهورًا؟ إذا كانت الإجابة غير متاحة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "من السياق، قدم الإجابة الأكثر دقة. إذا كانت الإجابة ليست في السياق، ارد بـ 'غير قابلة للإجابة',"
            # "من خلال السياق، حدد الإجابة الأدق. إذا لم يكن الجواب متوفرًا في السياق، أجب بـ 'غير قابل للإجابة',"
            "From context, provide the most accurate answer. If not in context, please reply 'unanswerable',",
            "From context, what is the most likely outcome? If the answer is not in context, please reply 'unanswerable',",
            "From the given context, what is the key element that can be deduced? If the answer is not available in the context, please reply 'unanswerable',",
            "Based on the context given, what is the clear key idea? If the answer is not in context, please reply 'unanswerable',",
            "Based on the context, what is the most convincing explanation? If the answer is not available in the context, please reply 'unanswerable',",
            "Based on the context, what is the most likely outcome? If the answer is not available in the context, please reply 'unanswerable',",
            "Based on the context, which hypothesis is the most true? If the answer is not in context, please reply 'unanswerable',",
            "From context, what is the most apparent factor influencing? If the answer is not available in the context, please reply 'unanswerable',",
            "From context, provide the most accurate answer. If the answer is not in context, reply 'unanswerable',",
            "From context, determine the most accurate answer. If the answer is not available in context, answer 'unanswerable',", 
        ],

        'spanish': [
            # Spanish_English
            # "Según el contexto, proporciona la respuesta más precisa. Si la respuesta no está en el contexto, responde con 'no se puede responder'.",
            # "Describe brevemente la situación y proporciona la respuesta correspondiente. Si la respuesta no se puede encontrar, responde con 'no se puede responder'.",
            # "Teniendo en cuenta la información dada, ¿cuál es la respuesta más adecuada? Si no se puede determinar la respuesta, responde con 'no se puede responder'.",
            # "Lee el siguiente texto y brinda la respuesta más acertada. Si no puedes encontrar la respuesta, responde con 'no se puede responder'.",
            # "Basado en la descripción, ¿cuál es la respuesta más precisa? Si la respuesta no se encuentra en la descripción, responde con 'no se puede responder'.",
            # "Del contexto proporcionado, ¿qué respuesta es la más adecuada? Si no se puede encontrar la respuesta, responde con 'no se puede responder'.",
            # "Analiza el siguiente párrafo y proporciona la respuesta más exacta. Si la respuesta no está en el párrafo, responde con 'no se puede responder'.",
            # "Según la información presentada, ¿cuál es la respuesta más precisa? Si la respuesta no se puede determinar, responde con 'no se puede responder'.",
            # "Tras leer el fragmento, ¿cuál crees que es la respuesta correcta? Si la respuesta no se puede discernir, responde con 'no se puede responder'.",
            # "Basado en el contexto, proporciona la respuesta más apropiada. Si la respuesta no se encuentra en el contexto, responde con 'no se puede responder'."
            "Depending on the context, it provides the most precise answer. If the answer is not in context, answer with 'unanswerable'.",
            "Briefly describes the situation and provides the corresponding response. If the answer cannot be found, answer with 'unanswerable'.",
            "Given the information given, what is the most appropriate response? If the answer cannot be determined, answer with 'unanswerable'.",
            "Read the following text and give the most accurate answer. If you can't find the answer, answer with 'unanswerable'.",
            "Based on the description, what is the most accurate answer? If the answer is not found in the description, answer with 'unanswerable'.",
            "From the context provided, which response is the most appropriate? If the answer cannot be found, answer with 'unanswerable'.",
            "Analyze the following paragraph and provide the most accurate answer. If the answer is not in the paragraph, answer with 'unanswerable'.",
            "According to the information presented, what is the most precise answer? If the answer cannot be determined, answer with 'unanswerable'.",
            "After reading the excerpt, which do you think is the correct answer? If the answer cannot be discerned, answer with 'unanswerable'.",
            "Based on the context, it provides the most appropriate response. If the answer is not in context, answer with 'unanswerable'.",
        ],

        'japanese': [
            # Japanese_English
            # "この文脈から最も正確な答えを提供してください。答えが文脈に含まれていない場合は、'unanswerable' と回答してください。",
            # "この文章で明示された情報に基づいて、最も適切な回答を提供してください。回答が文章に含まれていない場合は、'unanswerable' と回答してください。",
            # "このテキストから推測される情報に基づいて、最も正確な答えを提供してください。答えがテキストに含まれていない場合は、'unanswerable' と回答してください。",
            # "与えられた文脈に基づいて、最も詳細な回答を提供してください。回答が文脈にない場合は、'unanswerable' と回答してください。",
            # "このコンテキストから導き出される情報を考慮し、最も正確な回答を提供してください。回答がコンテキストにない場合は、'unanswerable' と回答してください。",
            # "この文脈に基づいて、最も適切な回答を提供してください。回答が文脈に含まれていない場合は、'unanswerable' と回答してください。",
            # "与えられた文章から導き出される情報を考慮し、最も詳細な回答を提供してください。回答が文章にない場合は、'unanswerable' と回答してください。",
            # "このテキストで示された情報に基づいて、最も正確な答えを提供してください。答えがテキストに含まれていない場合は、'unanswerable' と回答してください。",
            # "このコンテキストから推測される情報を考慮し、最も適切な回答を提供してください。回答がコンテキストにない場合は、'unanswerable' と回答してください。",
            # "この文脈に基づいて、最も詳細な回答を提供してください。回答が文脈に含まれていない場合は、'unanswerable' と回答してください。"
            "Provide the most accurate answer from this context. If the answer isn't in the context, answer 'unanswerable'." ,
            "Please provide the most appropriate answer based on the information specified in this sentence. If the answer is not in the text, answer 'unanswerable'." ,
            "Please provide the most accurate answer based on the information guessed from this text. If the answer is not in the text, answer 'unanswerable'." ,
            "Provide the most detailed answer based on the given context. If the answer is not in the context, answer 'unanswerable'." ,
            "Consider the information derived from this context and provide the most accurate answer. If the answer is not in the context, answer 'unanswerable'." ,
            "Based on this context, please provide the most appropriate answer. If the answer is not in the context, answer 'unanswerable'." ,
            "Consider the information derived from the given text and provide the most detailed answer. If the answer is not in the text, please answer 'unanswerable'." ,
            "Provide the most accurate answer based on the information given in this text. If the answer is not in the text, answer 'unanswerable'." ,
            "Consider the information inferred from this context and provide the most appropriate answer. If the answer is not in the context, answer 'unanswerable'." ,
            "Provide the most detailed answer based on this context. If the answer is not in the context, answer 'unanswerable'." ,
        ],

        'korean': [
            # Korean_English
            # "문맥에서 가장 정확한 답을 제시하세요. 답이 문맥에 없을 경우 '답을 찾을 수 없음'으로 응답하십시오.,"
            # "이 문장에서 언급된 사실에 대한 추가 정보를 제공하세요. 정보가 없을 경우 '답을 찾을 수 없음'으로 응답하십시오.,"
            # "무엇에 대한 질문인지 알려주세요. 답을 제공할 수 있는 문맥이 없을 경우 '답을 찾을 수 없음'으로 응답하십시오.,"
            # "다음 문장에 언급된 개념에 대해 설명해주세요. 개념에 대한 정보가 없을 경우 '답을 찾을 수 없음'으로 응답하십시오.,"
            # "이 문장에서 무엇을 비교하고 있는지 알려주세요. 비교 대상이 없을 경우 '답을 찾을 수 없음'으로 응답하십시오.,"
            # "다음 문맥에서 요구하는 작업을 수행하세요. 작업이 불가능하거나 무엇을 수행해야 하는지 명확하지 않을 경우 '답을 찾을 수 없음'으로 응답하십시오.,"
            # "이 문장에서 어떤 정보가 포함되어 있는지 파악하십시오. 정보가 없을 경우 '답을 찾을 수 없음'으로 응답하십시오.,"
            # "다음 문장에서 무슨 종류의 문제에 대한 해결책을 제시하십시오. 해결책이 없을 경우 '답을 찾을 수 없음'으로 응답하십시오.,"
            # "문맥에서 언급된 사건의 원인을 알려주세요. 원인이 명확하지 않을 경우 '답을 찾을 수 없음'으로 응답하십시오.,"
            # "다음 문장에서 예상되는 결과를 제시하십시오. 결과가 예측할 수 없을 경우 '답을 찾을 수 없음'으로 응답하십시오.,"
            "Give the most accurate answer in context. If the answer is not in context, respond with 'unanswerable'.",
            "Please provide additional information about the facts mentioned in this sentence. If no information is available, respond with 'unanswerable'.",
            "Please tell me what your question is about. If there is no context in which you can provide an answer, respond with 'unanswerable'.",
            "Please explain the concept mentioned in the following sentence. If there is no information on the concept, please respond with 'unanswerable'.",
            "Tell me what you're comparing to in this sentence. If nothing is compared, please respond with 'unanswerable'.",
            "Please perform the actions required by the following context. If the task is not possible or if you are not clear what needs to be done, respond with 'unanswerable'.",
            "Figure out what information this sentence contains. If no information is available, respond with 'unanswerable'.",
            "Please give a solution to what kind of problem in the following sentence. If there is no solution, respond with 'unanswerable'.",
            "Please give the cause of the incident mentioned in the context. If the cause is not clear, respond with 'unanswerable'.",
            "Give expected results in the following sentences. If the result is unpredictable, respond with 'unanswerable'.",
        ],
    },

    'mmlu': {
        'chinese': [
            # Chinese_English
            # "关于以下关于{}的多项选择题，请从选项'A'、'B'、'C'或'D'中选择正确答案。",
            # "关于{}的以下多项选择题，请从选项'A'、'B'、'C'或'D'中选择正确答案。",
            # "就{}的以下多项选择题，从选项'A'、'B'、'C'或'D'中选择正确答案。",
            # "请根据下列关于{}的多项选择题，从选项'A'、'B'、'C'或'D'中选择正确答案。",
            # "以下有关{}的多项选择题，请从选项'A'、'B'、'C'或'D'中选择正确答案。",
            # "以下是关于{}的多项选择题，请从选项'A'、'B'、'C'或'D'中选择正确答案。",
            # "就{}的以下多项选择题，请从选项'A'、'B'、'C'或'D'中选择正确答案。",
            # "请根据下列有关{}的多项选择题，从选项'A'、'B'、'C'或'D'中选择正确答案。",
            # "以下关于{}的多项选择题，请从选项'A'、'B'、'C'或'D'中选择正确答案。",
            # "有关{}的以下多项选择题，请从选项'A'、'B'、'C'或'D'中选择正确答案。",
            "For the following multiple choice question about {}, please select the correct answer from 'A', 'B', 'C' or 'D'." ,
            "Please select the correct answer from 'A', 'B', 'C' or 'D' for the following multiple choice question for {}." ,
            "Select the correct answer from 'A', 'B', 'C' or 'D' for the following multiple choice question {}." ,
            "Please choose the correct answer from 'A', 'B', 'C' or 'D' according to the following multiple-choice questions about {}." ,
            "Please select the correct answer from 'A', 'B', 'C' or 'D' for the {} multiple choice questions below." ,
            "The following is A multiple choice question about {}. Please select the correct answer from 'A', 'B', 'C' or 'D'." ,
            "Please select the correct answer from 'A', 'B', 'C' or 'D' for the following multiple choice question {}." ,
            "Please choose the correct answer from 'A', 'B', 'C' or 'D' according to the following multiple-choice questions about {}." ,
            "Please select the correct answer from 'A', 'B', 'C' or 'D' for the following multiple choice questions about {}." ,
            "Please select the correct answer from 'A', 'B', 'C' or 'D' for the following multiple choice questions about {}." ,
        ],

        'french': [
            # French_English
            # "Concernant la question à choix multiples suivante sur {}, choisissez la bonne réponse parmi les options 'A', 'B', 'C' ou 'D'."
            # "Voici une question à choix multiples portant sur {}. Sélectionnez la réponse correcte parmi les options 'A', 'B', 'C' ou 'D'."
            # "Dans le contexte de la question à choix multiples sur {}, identifiez la réponse correcte parmi les options 'A', 'B', 'C' ou 'D'."
            # "À propos de la question suivante sur {}, déterminez la réponse correcte parmi les choix 'A', 'B', 'C' ou 'D'."
            # "Examinez attentivement la question à choix multiples concernant {}. Choisissez la réponse correcte parmi les options 'A', 'B', 'C' ou 'D'."
            # "En ce qui concerne la question à choix multiples relative à {}, indiquez la réponse correcte parmi les options 'A', 'B', 'C' ou 'D'."
            # "La question suivante porte sur {}. Sélectionnez la réponse correcte parmi les choix 'A', 'B', 'C' ou 'D'."
            # "Dans le cadre de la question à choix multiples sur {}, choisissez la réponse appropriée parmi les options 'A', 'B', 'C' ou 'D'."
            # "Évaluez votre compréhension de la question à choix multiples portant sur {}. Choisissez la réponse correcte parmi les options 'A', 'B', 'C' ou 'D'."
            # "Analysez la question à choix multiples suivante sur {}. Identifiez la réponse correcte parmi les choix 'A', 'B', 'C' ou 'D'."
            "For the following multiple choice question on {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.",
            "This is a multiple choice question about {}. Select the correct answer from options 'A', 'B', 'C' or 'D'.",
            "In the context of the multiple-choice question on {}, identify the correct answer from options 'A', 'B', 'C' or 'D'.",
            "About the following question on {}, determine the correct answer from the choices 'A', 'B', 'C' or 'D'.",
            "Carefully review the multiple-choice question regarding {}. Choose the correct answer from options 'A', 'B', 'C', or 'D'.",
            "For the multiple-choice question for {}, indicate the correct answer from options 'A', 'B', 'C', or 'D'.",
            "The next question is about {}. Select the correct answer from the choices 'A', 'B', 'C' or 'D'.",
            "As part of the multiple-choice question on {}, choose the appropriate answer from options 'A', 'B', 'C' or 'D'.",
            "Rate your understanding of the multiple-choice question on {}. Choose the correct answer from options 'A', 'B', 'C' or 'D'.",
            "Analyze the following multiple-choice question on {}. Identify the correct answer among choices 'A', 'B', 'C' or 'D'.",
        ],

        'arabic': [
            # Arabic_English
            # "من السياق، قدم الإجابة الأكثر دقة. إذا لم تتواجد الإجابة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "من السياق، ما هي النتيجة الأكثر محتملة؟ إذا كانت الإجابة غير موجودة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "من السياق المعطى، ما هو العنصر الأساسي الذي يمكن استنتاجه؟ إذا كانت الإجابة غير متوفرة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "استنادًا إلى السياق المعطى، ما هي الفكرة الرئيسية الواضحة؟ إذا كانت الإجابة غير موجودة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "استنادًا إلى السياق، ما هو التفسير الأكثر مقنعية؟ إذا كانت الإجابة غير متاحة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "استنادًا إلى السياق المذكور، ما هو النتيجة الأكثر احتمالًا؟ إذا كانت الإجابة غير متوفرة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "استنادًا إلى السياق، ما هي الفرضية الأكثر صحة؟ إذا كانت الإجابة غير موجودة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "من السياق، ما هو العامل المؤثر الأكثر ظهورًا؟ إذا كانت الإجابة غير متاحة في السياق، فالرجاء الرد بـ 'غير قابلة للإجابة',"
            # "من السياق، قدم الإجابة الأكثر دقة. إذا كانت الإجابة ليست في السياق، ارد بـ 'غير قابلة للإجابة',"
            # "من خلال السياق، حدد الإجابة الأدق. إذا لم يكن الجواب متوفرًا في السياق، أجب بـ 'غير قابل للإجابة',"
            "For the multiple choice question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.",
            "For the following multiple-choice question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.",
            "For the following multiple choice question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.",
            "When it comes to the multiple-choice question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.",
            "For the multiple-choice question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.",
            "If the question for {} is multiple choice, choose the correct answer from options 'A', 'B', 'C' or 'D'.",
            "For the question regarding {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.",
            "For the question about {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.",
            "When it comes to the question regarding {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.",
            "For the question regarding {}, choose the correct answer from options 'A', 'B', 'C' or 'D'.", 
        ],

        'spanish': [
            # Spanish_English
            # "En relación a la siguiente pregunta de opción múltiple sobre {}, elige la respuesta correcta de las opciones 'A', 'B', 'C' o 'D'."
            # "Al referirnos a la siguiente cuestión de opción múltiple sobre {}, selecciona la respuesta correcta de entre las opciones 'A', 'B', 'C' o 'D'."
            # "Con respecto a la siguiente pregunta de opción múltiple sobre {}, escoge la respuesta correcta entre las opciones 'A', 'B', 'C' o 'D'."
            # "Dentro del contexto de la siguiente pregunta de opción múltiple sobre {}, elige la opción correcta de entre 'A', 'B', 'C' o 'D'."
            # "En relación con el siguiente enunciado de opción múltiple sobre {}, selecciona la respuesta correcta de las opciones 'A', 'B', 'C' o 'D'."
            # "Considerando la siguiente pregunta de opción múltiple sobre {}, marca la respuesta correcta con las opciones 'A', 'B', 'C' o 'D'."
            # "Referente a la siguiente cuestión de opción múltiple sobre {}, escoge la alternativa correcta entre 'A', 'B', 'C' o 'D'."
            # "En relación al siguiente enunciado de opción múltiple sobre {}, elige la opción correcta de entre las alternativas 'A', 'B', 'C' o 'D'."
            # "Dentro del contexto de la siguiente pregunta de opción múltiple sobre {}, selecciona la respuesta correcta de las alternativas 'A', 'B', 'C' o 'D'."
            # "Considerando el siguiente enunciado de opción múltiple sobre {}, marca la alternativa correcta con las opciones 'A', 'B', 'C' o 'D'."
            "For the following multiple-choice question about {}, choose the correct answer from 'A', 'B', 'C', or 'D'.",
            "For the following multiple-choice question about {}, select the correct answer from 'A', 'B', 'C', or 'D'.",
            "For the following multiple-choice question about {}, choose the correct answer from 'A', 'B', 'C', or 'D'.",
            "Within the context of the following multiple-choice question about {}, choose the correct option from 'A', 'B', 'C', or 'D'.",
            "For the following multiple-choice statement about {}, select the correct answer from 'A', 'B', 'C', or 'D'.",
            "Considering the following multiple-choice question about {}, mark the correct answer with 'A', 'B', 'C', or 'D'.",
            "For the following multiple-choice question about {}, choose the correct alternative among 'A', 'B', 'C' or 'D'.",
            "For the following multiple-choice statement about {}, choose the correct option from alternatives 'A', 'B', 'C', or 'D'.",
            "Within the context of the following multiple-choice question about {}, select the correct answer from alternatives 'A', 'B', 'C', or 'D'.",
            "Considering the following multiple-choice statement about {}, mark the correct alternative with the options 'A', 'B', 'C' or 'D'.",           
        ],

        'japanese': [
            # Japanese_English
            # "以下の問題に関する{}について、適切な答えを'A'、'B'、'C'、または'D'のオプションから選んでください。",
            # "次の{}に関する複数選択問題について、正しい答えを'A'、'B'、'C'、または'D'の選択肢から選んでください。",
            # "以下の{}に関する複数選択問題において、正しい答えを'A'、'B'、'C'、または'D'から選んでください。",
            # "次の{}に関する問題について、正しい答えを'A'、'B'、'C'、または'D'のオプションから選んでください。",
            # "以下の複数選択問題において、{}に関する正しい答えを'A'、'B'、'C'、または'D'から選んでください。",
            # "次の{}に関する問題について、正しい答えを'A'、'B'、'C'、または'D'の選択肢から選んでください。",
            # "以下の複数選択問題において、{}について正しい答えを'A'、'B'、'C'、または'D'の中から選んでください。",
            # "次の{}に関する複数選択問題について、適切な答えを'A'、'B'、'C'、または'D'の選択肢から選んでください。",
            # "以下の複数選択問題において、{}についての正しい答えを'A'、'B'、'C'、または'D'から選んでください。",
            # "次の問題に関する{}について、適切な答えを'A'、'B'、'C'、または'D'のオプションから選んでください。",
            "Choose the appropriate answer from options 'A', 'B', 'C', or 'D' for {} regarding the following question.",
            "Choose the correct answer from 'A', 'B', 'C', or 'D' for the following multiple-choice question about {}.",
            "For the following multiple-choice questions about {}, choose the correct answer from 'A', 'B', 'C', or 'D'.",
            "Choose the correct answer from options 'A', 'B', 'C', or 'D' for the following questions about {}.",
            "In the multiple choice questions below, choose the correct answer for {} from 'A', 'B', 'C', or 'D'.",
            "Choose the correct answer from the options 'A', 'B', 'C', or 'D' for the following questions about {}.",
            "In the multiple choice questions below, choose the correct answer for {} from 'A', 'B', 'C', or 'D'.",
            "Choose the correct answer from 'A', 'B', 'C', or 'D' for the following multiple choice questions about {}.",
            "In the multiple choice questions below, choose the correct answer for {} from 'A', 'B', 'C', or 'D'.",
            "Choose the correct answer from options 'A', 'B', 'C', or 'D' for {} regarding the following question.",
        ],

        'korean': [
            # Korean_English
            # "다음에 관한 다중선택 문제에 대해, '{}'에 대한 올바른 답을 'A', 'B', 'C', 또는 'D' 중에서 고르세요,"
            # "다음과 관련된 다중선택 문제에서, '{}'에 대한 올바른 답을 'A', 'B', 'C', 또는 'D' 중에서 선택하세요,"
            # "아래의 다중선택 문제에 대하여, '{}'에 대한 정확한 답을 'A', 'B', 'C', 또는 'D' 중에서 골라보세요,"
            # "다음과 같은 다중선택 문제에서, '{}'에 대한 올바른 답을 'A', 'B', 'C', 또는 'D' 중에서 고르십시오,"
            # "다음의 다중선택 문제에 대하여, '{}'에 대한 올바른 답을 'A', 'B', 'C', 또는 'D' 중에서 선택해 주세요,"
            # "다음에 관한 다중선택 문제를 풀어보세요. '{}'에 대한 올바른 답은 'A', 'B', 'C', 또는 'D' 중에서 무엇입니까,"
            # "아래 다중선택 문제에 대한 정확한 답을 선택하세요. '{}'은(는) 'A', 'B', 'C', 또는 'D' 중에서 어떤 것입니까,"
            # "다음과 같은 다중선택 문제를 풀어보세요. '{}'에 대한 정확한 답을 'A', 'B', 'C', 또는 'D' 중에서 선택하십시오,"
            # "다음의 다중선택 문제에 대한 올바른 답을 선택하세요. '{}'은(는) 'A', 'B', 'C', 또는 'D' 중에서 무엇인가요,"
            # "다음에 관한 다중선택 문제를 풀어보세요. '{}'에 대한 정확한 답은 'A', 'B', 'C', 또는 'D' 중에서 선택해 주세요,"
            "For the multiple choice problem about, choose the correct answer for '{}' from 'A', 'B', 'C', or 'D'.",
            "Choose the correct answer for '{}' from 'A', 'B', 'C', or 'D' in the multiple choice problem involving,",
            "For the multiple choice problem below, choose the correct answer to '{}' from 'A', 'B', 'C', or 'D'.",
            "In the following multiple-choice problem, choose the correct answer for '{}' from 'A', 'B', 'C', or 'D'.",
            "For the following multiple choice problem, choose the correct answer for '{}' from 'A', 'B', 'C', or 'D'.",
            "Solve multiple choice problems about: Which of 'A', 'B', 'C', or 'D' is the correct answer for '{}'.",
            "Choose the correct answer to the multiple-choice question below. Is '{}' an 'A', 'B', 'C', or 'D'.",
            "Solve the following multiple-choice problem. Choose the correct answer for '{}' from 'A', 'B', 'C', or 'D'.",
            "Choose the correct answer to the following multiple choice problem: Is '{}' 'A', 'B', 'C', or 'D'.",
            "Solve multiple-choice problems about: Please select 'A', 'B', 'C', or 'D' for the correct answer to '{}'.",
        ],
    },

    'sst2': {
        'chinese': [
            # Chinese_English
            # "请根据情感分析的角度，回答该语句是积极的还是消极的。",
            # "以情感分析工具的角度，判断该文本的情感是正面的还是负面的。",
            # "根据该语句的情感倾向，将其分类为正面或负面。",
            # "请使用情感分析的方式，将该文本分类为积极或消极。",
            # "请判断该句子的情感是正面的还是负面的，并进行分类。",
            # "使用情感分析的方法，将该文本划分为积极或消极。",
            # "请回答该句子的情感是积极的还是消极的，并进行分类。",
            # "以情感分析为基础，将该语句分类为正面或负面。",
            # "请根据情感分析的标准，将该文本判断为正面或负面。",
            # "请根据情感分析的原则，将该句子分类为积极或消极。",
            "Answer whether the statement is 'positive' or 'negative' based on sentiment analysis. ",
            "As an emotion analysis tool, determine whether the emotion in the text is 'positive' or 'negative'. ",
            "Categorize the statement as 'positive' or 'negative', based on its emotional bent. ",
            "Please use sentiment analysis to classify the text as 'positive' or 'negative'. ",
            "Please determine whether the emotion of the sentence is 'positive' or 'negative' and categorize it. ",
            "Using sentiment analysis, classify the text as 'positive' or 'negative'. ",
            "Please answer whether the emotion of the sentence is 'positive' or 'negative' and categorize it. ",
            "Categorize the statement as 'positive' or 'negative' based on sentiment analysis. ",
            "Please judge this text as 'positive' or 'negative' according to the criteria of sentiment analysis. ",
            "Please classify this sentence as 'positive' or 'negative' according to the principles of emotion analysis. ",
        ],

        'french': [
            # French_English
            # "En tant qu'outil d'analyse de sentiment, veuillez répondre avec 'positif' ou 'négatif' pour classifier cette déclaration. ",
            # "Déterminez si cette phrase est 'positive' ou 'négative' en tant qu'outil de classification de sentiment. ",
            # "Identifiez le ton de cette affirmation en choisissant entre 'positif' et 'négatif' en tant qu'outil d'analyse de sentiment. ",
            # "Utilisez l'analyse de sentiment pour classer cette déclaration comme étant 'positive' ou 'négative'. ",
            # "En tant qu'outil de classification de sentiment, veuillez déterminer si cette affirmation est 'positive' ou 'négative'. ",
            # "Classifiez cette phrase comme étant 'positive' ou 'négative' à l'aide de l'analyse de sentiment. ",
            # "Choisissez entre 'positif' ou 'négatif' pour classifier cette déclaration en tant qu'outil d'analyse de sentiment. ",
            # "Identifiez le sentiment exprimé dans cette affirmation en sélectionnant 'positif' ou 'négatif' en tant qu'outil de classification de sentiment. ",
            # "Déterminez si cette phrase est 'positive' ou 'négative' à l'aide de l'analyse de sentiment comme outil de classification. ",
            # "Utilisez l'analyse de sentiment pour classifier cette affirmation comme étant 'positive' ou 'négative'. "
            "As a sentiment analysis tool, please answer with 'positive' or 'negative' to classify this statement. ",
            "Determine whether this phrase is 'positive' or 'negative' as a sentiment classification tool. ",
            "Identify the tone of this statement by choosing between 'positive' and 'negative' as a sentiment analysis tool. ",
            "Use sentiment analysis to classify this statement as 'positive' or 'negative'. ",
            "As a sentiment classification tool, please determine whether this statement is 'positive' or 'negative'. ",
            "Classify this sentence as 'positive' or 'negative' using sentiment analysis. ",
            "Choose between 'positive' or 'negative' to classify this statement as a sentiment analysis tool. ",
            "Identify the sentiment expressed in this statement by selecting 'positive' or 'negative' as a sentiment classification tool. ",
            "Determine whether this phrase is 'positive' or 'negative' using sentiment analysis as a classification tool. ",
            "Use sentiment analysis to classify this statement as 'positive' or 'negative'. ",
        ],

        'arabic': [
            # Arabic_English
            # "في إطار تحليل المشاعر، أجب بـ 'إيجابي' أو 'سلبي' لتصنيف هذا البيان. ",
            # "هل يعبر هذا البيان عن رد فعل 'إيجابي' أم 'سلبي'؟",
            # "هل تعتبر هذه العبارة إيجابية أم سلبية؟",
            # "ما هو تصنيف العبارة التالية بين 'إيجابية' و 'سلبية'؟",
            # "هل تعبر هذه الجملة عن مشاعر 'إيجابية' أم 'سلبية'؟",
            # "في إطار تحليل النصوص، ما هو تصنيف هذه العبارة بين 'إيجابية' و 'سلبية'؟",
            # "هل يمكن تصنيف هذه الجملة بـ 'إيجابية' أم 'سلبية'؟",
            # "في سياق التحليل العاطفي، ما هو تصنيف هذا البيان بين 'إيجابي' و 'سلبي'؟",
            # "هل يمكن تصنيف هذه العبارة بـ 'إيجابية' أم 'سلبية'؟",
            # "في إطار تصنيف المشاعر، هل تعتبر هذه الجملة 'إيجابية' أم 'سلبية'؟",
            "Under emotional analysis, answer 'positive' or 'negative' to classify this statement. ",
            "Does this statement express a 'positive' or 'negative' reaction? ",
            "Is that a 'positive' or a 'negative' phrase? ",
            "What is the classification between 'positive' and 'negative'? ",
            "Does this sentence express 'positive' or 'negative' feelings? ",
            "In the context of textual analysis, what classification is this phrase between 'positive' and 'negative'? ",
            "Could this be classified as 'positive' or 'negative'? ",
            "In the context of emotional analysis, what classification is this statement between 'positive' and 'negative'? ",
            "Can this be classified as 'positive' or 'negative'? ",
            "Under the classification of emotions, is this sentence 'positive' or 'negative'? ",
        ],

        'spanish': [
            # Spanish_English
            # "Como herramienta de análisis de sentimientos, clasifique esta afirmación como 'positiva' o 'negativa',"
            # "Determine si esta declaración tiene una connotación 'positiva' o 'negativa',"
            # "Indique si el siguiente enunciado es 'positivo' o 'negativo',"
            # "Evalúe si este texto tiene una carga emocional 'positiva' o 'negativa',"
            # "Según su análisis de sentimientos, ¿diría que este comentario es 'positivo' o 'negativo'?,"
            # "En el contexto de análisis de sentimientos, etiquete esta oración como 'positiva' o 'negativa',"
            # "Clasifique la siguiente afirmación como 'positiva' o 'negativa', según su análisis de sentimientos,"
            # "¿Cómo clasificaría este texto en términos de su tono emocional? 'Positivo' o 'negativo'?,"
            # "Como herramienta de análisis de sentimientos, ¿diría que este enunciado es 'positivo' o 'negativo'?,"
            # "Realice una clasificación de sentimientos de esta declaración y etiquétele como 'positiva' o 'negativa', por favor,"
            "As a feeling analysis tool, classify this statement as 'positive' or 'negative'. ",
            "Determine whether this statement has a 'positive' or 'negative' connotation. ",
            "Indicate whether the following statement is 'positive' or 'negative'. ",
            "Evaluate whether this text has a 'positive' or 'negative' emotional charge. ",
            "According to your sentiment analysis, would you say this comment is 'positive' or 'negative'? ",
            "In the context of sentiment analysis, label this sentence as 'positive' or 'negative'. ",
            "Rate the following statement as 'positive' or 'negative', according to your sentiment analysis. ",
            "How would you classify this text in terms of its emotional tone? 'positive' or 'negative'? ",
            "As a tool for sentiment analysis, would you say this statement is 'positive' or 'negative'? ",
            "Classify this statement as 'positive' or 'negative', please. ",
        ],

        'japanese': [
            # Japanese_English
            # "この文を感情分析ツールとして扱い、肯定的なものと否定的なものに分類してください。",
            # "ポジティブかネガティブかを分類するために、この文章を感情分析のツールとして評価してください。",
            # "肯定的か否定的かを判断するため、この文を感情分析ツールとして使い分けてください。",
            # "この文章をポジティブかネガティブかを分類するための感情分析ツールとして活用してください。",
            # "この文を感情分析のツールとして使用し、肯定的か否定的かを分類してください。",
            # "この文章をポジティブかネガティブかに分類するために、感情分析のツールとして評価してください。",
            # "この文を感情分析ツールとして扱い、肯定的か否定的かを判断してください。",
            # "この文章を感情分析のツールとして使用して、ポジティブかネガティブかを分類してください。",
            # "ポジティブかネガティブかを分類するために、この文を感情分析ツールとして分析してください。",
            # "この文章を感情分析のツールとして利用し、肯定的か否定的かを判断してください。",
            "Treat this sentence as an emotion analysis tool and categorize it as 'positive' and 'negative'. ",
            "Use this article as a sentiment analysis tool to classify 'positive' and 'negative'. ",
            "Use this sentence as an emotion analysis tool to determine whether it is 'positive' or 'negative'. ",
            "Use this sentence as an emotion analysis tool to classify 'positive' and 'negative'. ",
            "Use this sentence as a sentiment analysis tool and classify it as 'positive' or 'negative'. ",
            "To classify this sentence as 'positive' or 'negative', evaluate it as a sentiment analysis tool. ",
            "Treat this sentence as an emotion analysis tool to determine whether it is 'positive' or 'negative'. ",
            "Use this sentence as a sentiment analysis tool to classify 'positive' and 'negative'. ",
            "Analyze this sentence as an emotion analysis tool to classify whether it is 'positive' or 'negative'. ",
            "Use this sentence as an emotional analysis tool to determine whether it is 'positive' or 'negative'. ",
        ],

        'korean': [
            # Korean_English
            # "감정 분석 도구로서, 이 문장을 분류하는 데 '긍정' 또는 '부정'으로 응답하십시오,"
            # "이 문장을 긍정적인 것으로 간주하면 '긍정', 부정적인 것으로 간주하면 '부정'으로 분류하십시오,"
            # "이 문장의 감정을 평가하여 '긍정' 또는 '부정'으로 분류하십시오,"
            # "당신이 이 문장을 긍정적으로 인식한다면 '긍정', 부정적으로 인식한다면 '부정'으로 분류하십시오,"
            # "이 문장이 긍정적인 표현을 사용하여 전달한 내용이라면 '긍정', 부정적인 표현을 사용하여 전달한 내용이라면 '부정'으로 분류하십시오,"
            # "이 문장이 긍정적인지 아니면 부정적인지 분류하여 '긍정' 또는 '부정'으로 응답하십시오,"
            # "이 문장의 감정을 분석하여 '긍정' 또는 '부정'으로 분류하십시오,"
            # "이 문장이 긍정적인 의미를 담고 있다면 '긍정', 부정적인 의미를 담고 있다면 '부정'으로 분류하십시오,"
            # "이 문장이 긍정적인 내용을 담고 있다면 '긍정', 부정적인 내용을 담고 있다면 '부정'으로 분류하십시오,"
            # "이 문장에서 전달하고자 하는 내용이 긍정적이라면 '긍정', 부정적이라면 '부정'으로 분류하십시오,"
            "As an emotional analysis tool, respond with 'positive' or 'negative' to classify these sentences. ",
            "Classify this sentence as 'positive' if you regard it as positive, 'negative' if you regard it as negative. ",
            "Please rate the emotion of this sentence and classify it as 'positive' or 'negative'. ",
            "Classify this sentence as 'positive' if you perceive it positively and 'negative' if you perceive it negatively. ",
            "If this is a sentence delivered using a positive expression, classify it as 'positive' and if this is a sentence delivered using a negative expression, classify it as 'negative'. ",
            "Respond with 'positive' or 'negative' by categorizing whether the sentence is positive or negative. ",
            "Please analyze the emotion in this sentence and classify it as 'positive' or 'negative'. ",
            "Classify this sentence as 'positive' if it contains a positive meaning, 'negative' if it contains a negative meaning. ",
            "Classify this sentence as 'positive' if it contains positive content, 'negative' if it contains negative content. ",
            "Classify what you're trying to convey in this sentence as 'positive' if it's positive, and 'negative' if it's negative. ",
        ],
    },

    'wnli': {
        'chinese': [
            # Chinese_English
            # "请以蕴涵分析工具的角度，评估下列句子间的关系，并将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以蕴涵分析工具的视角，判断下列句子是否存在蕴涵关系，将其分类为'蕴涵'或'非蕴涵'。"，
            # "请使用蕴涵分析工具，判断下列句子是否存在蕴涵关系，将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以判断蕴涵关系为目的，评估下列句子的关系，将其分类为'蕴涵'或'非蕴涵'。"，
            # "请使用蕴含分析工具，评估下列句子间的关系，并将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以判断蕴含关系为目的，分析下列句子的关系，并将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以蕴含关系分析工具为准，判断下列句子的关系，并将其分类为'蕴涵'或'非蕴涵'。"，
            # "请使用蕴涵判断工具，评估下列句子的相关性，并将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以蕴涵分析为主要任务，判断下列句子间的联系，将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以蕴涵判断为标准，分析下列句子的联系，并将其分类为'蕴涵'或'非蕴涵'。"，
            "In the light of an implication analysis tool, evaluate the relationship between the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "From the perspective of an implication analysis tool, determine whether there is an implication relationship in the following sentences by classifying them as 'entailment' or 'not_entailment'. ",
            "Please use an implication analysis tool to determine whether an implication relationship exists in the following sentences by classifying them as 'entailment' or 'not_entailment'. ",
            "Please evaluate the relation of the following sentences as 'entailment' or 'not_entailment' for the purpose of determining implication relation. ",
            "Please use the implication analysis tool to evaluate the relationships between the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "For the purpose of determining implicative relations, analyze the relations of the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Please use the implication analysis tool to determine the relationship of the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Please use the implication judgment tool to assess the relevance of the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Please, with implication analysis as the main task, determine the relationships between the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Using the implication judgment as a criterion, analyze the relation of the following sentences and classify them as 'entailment' or 'not_entailment'. ",
        ],

        'french': [
            # French_English
            # "En tant qu'outil d'analyse d'implication, évaluez la relation entre les phrases données et classez-la comme 'implication' ou 'non_implication',"
            # "Déterminez si les phrases données impliquent l'une l'autre ou non en tant qu'outil d'analyse d'implication. Classez-les en conséquence comme 'implication' ou 'non_implication',"
            # "En utilisant l'analyse d'implication, évaluez si les phrases fournies ont une relation logique et catégorisez-les en tant que 'implication' ou 'non_implication',"
            # "En tant qu'outil d'évaluation d'implication, déterminez si les phrases fournies ont une relation logique et classez-les comme 'implication' ou 'non_implication',"
            # "En tant qu'outil de classification d'implication, analysez les phrases fournies pour déterminer s'il y a une relation logique et catégorisez-les en tant que 'implication' ou 'non_implication',"
            # "En utilisant l'analyse d'implication, déterminez si les phrases données ont une relation de cause à effet et catégorisez-les en tant que 'implication' ou 'non_implication',"
            # "Évaluez la relation entre les phrases données à l'aide de l'analyse d'implication et classez-les en conséquence comme 'implication' ou 'non_implication',"
            # "En tant qu'outil de détection d'implication, déterminez si les phrases données ont une relation logique et catégorisez-les comme 'implication' ou 'non_implication',"
            # "En utilisant l'analyse d'implication, évaluez si les phrases fournies ont une relation de cause à effet et classez-les en conséquence comme 'implication' ou 'non_implication',"
            # "Déterminez si les phrases données ont une relation de cause à effet en tant qu'outil d'analyse d'implication et catégorisez-les comme 'implication' ou 'non_implication',".
            "As an engagement analysis tool, evaluate the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'. ",
            "Determine whether the given sentences involve one another or not as an implication analysis tool. Classify them accordingly as 'entailment' or 'not_entailment'. ",
            "Using implication analysis, evaluate whether the sentences provided have a logical relationship and categorize them as 'entailment' or 'not_entailment'. ",
            "As an engagement assessment tool, determine whether the sentences provided have a logical relationship and classify them as 'entailment' or 'not_entailment'. ",
            "As an implication classification tool, analyze the sentences provided to determine if there is a logical relationship and categorize them as 'entailment' or 'not_entailment'. ",
            "Using implication analysis, determine whether the given sentences have a cause-effect relationship and categorize them as 'entailment' or 'not_entailment'. ",
            "Evaluate the relationship between the given sentences using implication analysis and rank them accordingly as 'entailment' or 'not_entailment'. ",
            "As an engagement detection tool, determine whether the given sentences have a logical relationship and categorize them as 'entailment' or 'not_entailment'. ",
            "Using implication analysis, evaluate whether the sentences provided have a cause-effect relationship and rank them accordingly as 'entailment' or 'not_entailment'. ",
            "Determine whether the given sentences have a cause-effect relationship as an engagement analysis tool and categorize them as 'entailment' or 'not_entailment'. ",
        ],

        'arabic': [
            # Arabic_English
            # "في دورك كأداة لتحليل الاستنتاج، قم بتقييم العلاقة بين الجمل المعطاة وتصنيفها على أنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "هل تستطيع تحديد ما إذا كانت هذه الجملة تستنتج من الجملة الأخرى؟ قم بتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "باستخدامك كأداة تحليل الاستنتاج، قم بتحليل العلاقة بين الجمل المعطاة وتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "هل تمثل هذه الجملة استنتاجًا من الجملة السابقة؟ قم بتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "باعتبارك أداة لتحليل الاستنتاج، قم بتقييم علاقة الجمل المعطاة وتصنيفها على أنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "هل يمكن استنتاج هذه الجملة من الجملة السابقة؟ قم بتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "باستخدامك كأداة لتحليل الاستنتاج، قم بتحليل العلاقة بين الجملتين وتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "هل تمثل هذه الجملة استنتاجًا من الجملة التي تليها؟ قم بتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "كجزء من مهمتك في تحليل الاستنتاج، قم بتقييم العلاقة بين الجملتين وتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا' بناءً على العلاقة بينهما."
            # "هل تتبع هذه الجملة بشكل مباشر من الجملة السابقة؟ قم بتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            "In your role as a tool for reasoning analysis, evaluate the relationship between given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Can you determine whether this sentence is inferred from the other sentence? Classify it as 'entailment' or 'not_entailment'. ",
            "Using the tool of reasoning analysis, analyze the relationship between given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Does this sentence represent a conclusion from the previous sentence? Classify it as 'entailment' or 'not_entailment'. ",
            "As a tool of reasoning analysis, evaluate the relationship of given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Can this sentence be inferred from the previous sentence? Classify it as 'entailment' or 'not_entailment'. ",
            "Using a tool to analyze a conclusion, analyze the relationship between the two sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Is this a conclusion from the next sentence? Classify it as 'entailment' or 'not_entailment'. ",
            "As part of your task in analyzing a conclusion, evaluate the relationship between the two sentences and classify them as 'entailment' or 'not_entailment' based on their relationship. ",
            "Are you following this sentence directly from the previous one? Classify it as 'entailment' or 'not_entailment'. ",
        ],

        'spanish': [
            # Spanish_English
            # "En tu papel como herramienta de análisis de implicación, evalúa la relación entre las frases dadas y clasifícala como 'entailment' o 'not_entailment',"
            # "Determina si la segunda oración implica necesariamente la primera y etiqueta la relación como 'entailment', o como 'not_entailment' si no es así,",
            # "Clasifica la relación entre estas dos oraciones como 'entailment' si una necesariamente implica la otra, o como 'not_entailment' si no es el caso,",
            # "Evalúa si la información en la segunda oración está implícita en la primera y etiqueta la relación como 'entailment', o como 'not_entailment' si no hay tal implicación,",
            # "Dado un par de frases, etiqueta su relación como 'entailment' si una implica necesariamente la otra, o como 'not_entailment' si no hay tal implicación,",
            # "Analiza la relación entre las frases y clasifícala como 'entailment' si una necesariamente implica la otra, o como 'not_entailment' si no hay tal implicación,",
            # "Dadas dos frases, determina si la segunda oración es una consecuencia necesaria de la primera y etiqueta la relación como 'entailment', o como 'not_entailment' si no es el caso,",
            # "Evalúa si la información presentada en la segunda oración está implícita en la primera y etiqueta la relación como 'entailment', o como 'not_entailment' si no hay tal implicación,",
            # "Clasifica la relación entre las frases dadas como 'entailment' si una implica necesariamente la otra, o como 'not_entailment' si no hay tal implicación,",
            # "Determina si la información proporcionada en la segunda oración es necesariamente inferible a partir de la primera y etiqueta la relación como 'entailment', o como 'not_entailment' si no es el caso,"
            "In your role as an implication analysis tool, evaluate the relationship between the given phrases and classify them as 'entailment' or 'not_entailment'. ",
            "Determine whether the second sentence necessarily implies the first and label the relation as 'entailment', or as 'not_entailment' if not. ",
            "Classifies the relationship between these two sentences as 'entailment' if one necessarily implies the other, or as 'not_entailment' if not. ",
            "Evaluates whether the information in the second sentence is implied in the first and labels the relationship as 'entailment', or as 'not_entailment' if there is no such implication. ",
            "Given a couple of phrases, label their relationship as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication. ",
            "Analyzes the relationship between the phrases and classifies them as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication. ",
            "Given two sentences, determine whether the second sentence is a necessary consequence of the first and label the relation as 'entailment', or as 'not_entailment' if not. ",
            "Evaluates whether the information presented in the second sentence is implicit in the first and labels the relationship as 'entailment', or as 'not_entailment' if there is no such implication. ",
            "Classifies the relationship between the given phrases as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication. ",
            "Determines whether the information provided in the second sentence is necessarily inferable from the first and labels the relationship as 'entailment', or as 'not_entailment' if not. ",
        ],

        'japanese': [
            # Japanese_English
            # "与えられた文の関係を分析し、『含意』または『非含意』として分類してください。",
            # "文の意味関係を評価し、『含意』または『非含意』として分類してください。",
            # "与えられた文章同士の関連性を判断し、『含意』または『非含意』として分類してください。",
            # "与えられた文の言い換えを調べ、『含意』または『非含意』として分類してください。",
            # "与えられた文章の類似度を評価し、『含意』または『非含意』として分類してください。",
            # "与えられた文の意味的なつながりを判定し、『含意』または『非含意』として分類してください。",
            # "与えられた文章の意味的な一致を調べ、『含意』または『非含意』として分類してください。",
            # "文の内容に基づいて、『含意』または『非含意』として分類してください。",
            # "与えられた文の関係を解析し、『含意』または『非含意』として分類してください。",
            # "与えられた文章の意味的なつながりを判断し、『含意』または『非含意』として分類してください。",
            "Analyze the relationship of a given sentence and classify it as 'entailment' or 'not_entailment'. ",
            "Evaluate the semantic relationship of the sentence and classify it as 'entailment' or 'not_entailment'. ",
            "Please judge the relationship between the given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Examine the paraphrases of a given sentence and classify them 'entailment' or 'not_entailment'. ",
            "Rate the similarity of a given sentence and categorize it as 'entailment' or 'not_entailment'. ",
            "Determinate the semantic connections of a given sentence and classify it as 'entailment' or 'not_entailment'. ",
            "Examine the semantic match of a given sentence and categorize it as 'entailment' or 'not_entailment'. ",
            "Classify it as 'entailment' or 'not_entailment' based on the content of the sentence.",
            "Analyze the relationship of a given sentence and classify it as 'entailment' or 'not_entailment'. ",
            "Judge the semantic connections of a given sentence and categorize it as 'entailment' or 'not_entailment'. ",
        ],

        'korean': [
            # Korean_English
            # "주어진 두 문장 간의 관계를 평가하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "문장 간의 의미적 연역 관계를 분석하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "문장 간의 논리적인 관련성을 평가하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "주어진 두 문장의 상호작용을 평가하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "두 문장 간의 의미적인 일치 여부를 확인하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "주어진 문장 간의 정보를 비교하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "두 문장 간의 상관 관계를 분석하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "주어진 문장 간의 서로 다른 의미를 평가하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "두 문장의 의미 구조를 비교하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "문장 간의 상호작용을 평가하고 'entailment' 또는 'not_entailment'로 분류하세요."
            "Evaluate the relationship between any two sentences given to you and classify you as 'entailment' or 'not_entailment'. ",
            "Analyze the semantic deductive relations between sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Evaluate the logical relevance between sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Evaluate the interaction of two given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Please check whether there is a semantic match between those two sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Compare information between given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Please analyse the correlation between those two sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Evaluate the different meanings between given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Compare the semantic structure of the two sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Evaluate the interactions between sentences and classify them as 'entailment' or 'not_entailment'. ",
        ],
    },

    # 'rte': just the same as 'wnli'
    'rte': {
        'chinese': [
            # Chinese_English
            # "请以蕴涵分析工具的角度，评估下列句子间的关系，并将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以蕴涵分析工具的视角，判断下列句子是否存在蕴涵关系，将其分类为'蕴涵'或'非蕴涵'。"，
            # "请使用蕴涵分析工具，判断下列句子是否存在蕴涵关系，将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以判断蕴涵关系为目的，评估下列句子的关系，将其分类为'蕴涵'或'非蕴涵'。"，
            # "请使用蕴含分析工具，评估下列句子间的关系，并将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以判断蕴含关系为目的，分析下列句子的关系，并将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以蕴含关系分析工具为准，判断下列句子的关系，并将其分类为'蕴涵'或'非蕴涵'。"，
            # "请使用蕴涵判断工具，评估下列句子的相关性，并将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以蕴涵分析为主要任务，判断下列句子间的联系，将其分类为'蕴涵'或'非蕴涵'。"，
            # "请以蕴涵判断为标准，分析下列句子的联系，并将其分类为'蕴涵'或'非蕴涵'。"，
            "In the light of an implication analysis tool, evaluate the relationship between the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "From the perspective of an implication analysis tool, determine whether there is an implication relationship in the following sentences by classifying them as 'entailment' or 'not_entailment'. ",
            "Please use an implication analysis tool to determine whether an implication relationship exists in the following sentences by classifying them as 'entailment' or 'not_entailment'. ",
            "Please evaluate the relation of the following sentences as 'entailment' or 'not_entailment' for the purpose of determining implication relation. ",
            "Please use the implication analysis tool to evaluate the relationships between the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "For the purpose of determining implicative relations, analyze the relations of the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Please use the implication analysis tool to determine the relationship of the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Please use the implication judgment tool to assess the relevance of the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Please, with implication analysis as the main task, determine the relationships between the following sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Using the implication judgment as a criterion, analyze the relation of the following sentences and classify them as 'entailment' or 'not_entailment'. ",
        ],

        'french': [
            # French_English
            # "En tant qu'outil d'analyse d'implication, évaluez la relation entre les phrases données et classez-la comme 'implication' ou 'non_implication',"
            # "Déterminez si les phrases données impliquent l'une l'autre ou non en tant qu'outil d'analyse d'implication. Classez-les en conséquence comme 'implication' ou 'non_implication',"
            # "En utilisant l'analyse d'implication, évaluez si les phrases fournies ont une relation logique et catégorisez-les en tant que 'implication' ou 'non_implication',"
            # "En tant qu'outil d'évaluation d'implication, déterminez si les phrases fournies ont une relation logique et classez-les comme 'implication' ou 'non_implication',"
            # "En tant qu'outil de classification d'implication, analysez les phrases fournies pour déterminer s'il y a une relation logique et catégorisez-les en tant que 'implication' ou 'non_implication',"
            # "En utilisant l'analyse d'implication, déterminez si les phrases données ont une relation de cause à effet et catégorisez-les en tant que 'implication' ou 'non_implication',"
            # "Évaluez la relation entre les phrases données à l'aide de l'analyse d'implication et classez-les en conséquence comme 'implication' ou 'non_implication',"
            # "En tant qu'outil de détection d'implication, déterminez si les phrases données ont une relation logique et catégorisez-les comme 'implication' ou 'non_implication',"
            # "En utilisant l'analyse d'implication, évaluez si les phrases fournies ont une relation de cause à effet et classez-les en conséquence comme 'implication' ou 'non_implication',"
            # "Déterminez si les phrases données ont une relation de cause à effet en tant qu'outil d'analyse d'implication et catégorisez-les comme 'implication' ou 'non_implication',".
            "As an engagement analysis tool, evaluate the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'. ",
            "Determine whether the given sentences involve one another or not as an implication analysis tool. Classify them accordingly as 'entailment' or 'not_entailment'. ",
            "Using implication analysis, evaluate whether the sentences provided have a logical relationship and categorize them as 'entailment' or 'not_entailment'. ",
            "As an engagement assessment tool, determine whether the sentences provided have a logical relationship and classify them as 'entailment' or 'not_entailment'. ",
            "As an implication classification tool, analyze the sentences provided to determine if there is a logical relationship and categorize them as 'entailment' or 'not_entailment'. ",
            "Using implication analysis, determine whether the given sentences have a cause-effect relationship and categorize them as 'entailment' or 'not_entailment'. ",
            "Evaluate the relationship between the given sentences using implication analysis and rank them accordingly as 'entailment' or 'not_entailment'. ",
            "As an engagement detection tool, determine whether the given sentences have a logical relationship and categorize them as 'entailment' or 'not_entailment'. ",
            "Using implication analysis, evaluate whether the sentences provided have a cause-effect relationship and rank them accordingly as 'entailment' or 'not_entailment'. ",
            "Determine whether the given sentences have a cause-effect relationship as an engagement analysis tool and categorize them as 'entailment' or 'not_entailment'. ",
        ],

        'arabic': [
            # Arabic_English
            # "في دورك كأداة لتحليل الاستنتاج، قم بتقييم العلاقة بين الجمل المعطاة وتصنيفها على أنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "هل تستطيع تحديد ما إذا كانت هذه الجملة تستنتج من الجملة الأخرى؟ قم بتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "باستخدامك كأداة تحليل الاستنتاج، قم بتحليل العلاقة بين الجمل المعطاة وتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "هل تمثل هذه الجملة استنتاجًا من الجملة السابقة؟ قم بتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "باعتبارك أداة لتحليل الاستنتاج، قم بتقييم علاقة الجمل المعطاة وتصنيفها على أنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "هل يمكن استنتاج هذه الجملة من الجملة السابقة؟ قم بتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "باستخدامك كأداة لتحليل الاستنتاج، قم بتحليل العلاقة بين الجملتين وتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "هل تمثل هذه الجملة استنتاجًا من الجملة التي تليها؟ قم بتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            # "كجزء من مهمتك في تحليل الاستنتاج، قم بتقييم العلاقة بين الجملتين وتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا' بناءً على العلاقة بينهما."
            # "هل تتبع هذه الجملة بشكل مباشر من الجملة السابقة؟ قم بتصنيفها بأنها 'استنتاج' أو 'ليس استنتاجًا'."
            "In your role as a tool for reasoning analysis, evaluate the relationship between given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Can you determine whether this sentence is inferred from the other sentence? Classify it as 'entailment' or 'not_entailment'. ",
            "Using the tool of reasoning analysis, analyze the relationship between given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Does this sentence represent a conclusion from the previous sentence? Classify it as 'entailment' or 'not_entailment'. ",
            "As a tool of reasoning analysis, evaluate the relationship of given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Can this sentence be inferred from the previous sentence? Classify it as 'entailment' or 'not_entailment'. ",
            "Using a tool to analyze a conclusion, analyze the relationship between the two sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Is this a conclusion from the next sentence? Classify it as 'entailment' or 'not_entailment'. ",
            "As part of your task in analyzing a conclusion, evaluate the relationship between the two sentences and classify them as 'entailment' or 'not_entailment' based on their relationship. ",
            "Are you following this sentence directly from the previous one? Classify it as 'entailment' or 'not_entailment'. ",
        ],

        'spanish': [
            # Spanish_English
            # "En tu papel como herramienta de análisis de implicación, evalúa la relación entre las frases dadas y clasifícala como 'entailment' o 'not_entailment',"
            # "Determina si la segunda oración implica necesariamente la primera y etiqueta la relación como 'entailment', o como 'not_entailment' si no es así,",
            # "Clasifica la relación entre estas dos oraciones como 'entailment' si una necesariamente implica la otra, o como 'not_entailment' si no es el caso,",
            # "Evalúa si la información en la segunda oración está implícita en la primera y etiqueta la relación como 'entailment', o como 'not_entailment' si no hay tal implicación,",
            # "Dado un par de frases, etiqueta su relación como 'entailment' si una implica necesariamente la otra, o como 'not_entailment' si no hay tal implicación,",
            # "Analiza la relación entre las frases y clasifícala como 'entailment' si una necesariamente implica la otra, o como 'not_entailment' si no hay tal implicación,",
            # "Dadas dos frases, determina si la segunda oración es una consecuencia necesaria de la primera y etiqueta la relación como 'entailment', o como 'not_entailment' si no es el caso,",
            # "Evalúa si la información presentada en la segunda oración está implícita en la primera y etiqueta la relación como 'entailment', o como 'not_entailment' si no hay tal implicación,",
            # "Clasifica la relación entre las frases dadas como 'entailment' si una implica necesariamente la otra, o como 'not_entailment' si no hay tal implicación,",
            # "Determina si la información proporcionada en la segunda oración es necesariamente inferible a partir de la primera y etiqueta la relación como 'entailment', o como 'not_entailment' si no es el caso,"
            "In your role as an implication analysis tool, evaluate the relationship between the given phrases and classify them as 'entailment' or 'not_entailment'. ",
            "Determine whether the second sentence necessarily implies the first and label the relation as 'entailment', or as 'not_entailment' if not. ",
            "Classifies the relationship between these two sentences as 'entailment' if one necessarily implies the other, or as 'not_entailment' if not. ",
            "Evaluates whether the information in the second sentence is implied in the first and labels the relationship as 'entailment', or as 'not_entailment' if there is no such implication. ",
            "Given a couple of phrases, label their relationship as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication. ",
            "Analyzes the relationship between the phrases and classifies them as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication. ",
            "Given two sentences, determine whether the second sentence is a necessary consequence of the first and label the relation as 'entailment', or as 'not_entailment' if not. ",
            "Evaluates whether the information presented in the second sentence is implicit in the first and labels the relationship as 'entailment', or as 'not_entailment' if there is no such implication. ",
            "Classifies the relationship between the given phrases as 'entailment' if one necessarily implies the other, or as 'not_entailment' if there is no such implication. ",
            "Determines whether the information provided in the second sentence is necessarily inferable from the first and labels the relationship as 'entailment', or as 'not_entailment' if not. ",
        ],

        'japanese': [
            # Japanese_English
            # "与えられた文の関係を分析し、『含意』または『非含意』として分類してください。",
            # "文の意味関係を評価し、『含意』または『非含意』として分類してください。",
            # "与えられた文章同士の関連性を判断し、『含意』または『非含意』として分類してください。",
            # "与えられた文の言い換えを調べ、『含意』または『非含意』として分類してください。",
            # "与えられた文章の類似度を評価し、『含意』または『非含意』として分類してください。",
            # "与えられた文の意味的なつながりを判定し、『含意』または『非含意』として分類してください。",
            # "与えられた文章の意味的な一致を調べ、『含意』または『非含意』として分類してください。",
            # "文の内容に基づいて、『含意』または『非含意』として分類してください。",
            # "与えられた文の関係を解析し、『含意』または『非含意』として分類してください。",
            # "与えられた文章の意味的なつながりを判断し、『含意』または『非含意』として分類してください。",
            "Analyze the relationship of a given sentence and classify it as 'entailment' or 'not_entailment'. ",
            "Evaluate the semantic relationship of the sentence and classify it as 'entailment' or 'not_entailment'. ",
            "Please judge the relationship between the given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Examine the paraphrases of a given sentence and classify them 'entailment' or 'not_entailment'. ",
            "Rate the similarity of a given sentence and categorize it as 'entailment' or 'not_entailment'. ",
            "Determinate the semantic connections of a given sentence and classify it as 'entailment' or 'not_entailment'. ",
            "Examine the semantic match of a given sentence and categorize it as 'entailment' or 'not_entailment'. ",
            "Classify it as 'entailment' or 'not_entailment' based on the content of the sentence.",
            "Analyze the relationship of a given sentence and classify it as 'entailment' or 'not_entailment'. ",
            "Judge the semantic connections of a given sentence and categorize it as 'entailment' or 'not_entailment'. ",
        ],

        'korean': [
            # Korean_English
            # "주어진 두 문장 간의 관계를 평가하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "문장 간의 의미적 연역 관계를 분석하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "문장 간의 논리적인 관련성을 평가하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "주어진 두 문장의 상호작용을 평가하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "두 문장 간의 의미적인 일치 여부를 확인하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "주어진 문장 간의 정보를 비교하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "두 문장 간의 상관 관계를 분석하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "주어진 문장 간의 서로 다른 의미를 평가하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "두 문장의 의미 구조를 비교하고 'entailment' 또는 'not_entailment'로 분류하세요."
            # "문장 간의 상호작용을 평가하고 'entailment' 또는 'not_entailment'로 분류하세요."
            "Evaluate the relationship between any two sentences given to you and classify you as 'entailment' or 'not_entailment'. ",
            "Analyze the semantic deductive relations between sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Evaluate the logical relevance between sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Evaluate the interaction of two given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Please check whether there is a semantic match between those two sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Compare information between given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Please analyse the correlation between those two sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Evaluate the different meanings between given sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Compare the semantic structure of the two sentences and classify them as 'entailment' or 'not_entailment'. ",
            "Evaluate the interactions between sentences and classify them as 'entailment' or 'not_entailment'. ",
        ],
    },

    'mnli': {
        'chinese': [
            # Chinese_English
            # "作为一个蕴涵分析工具，请评估给定句子之间的关系，并将其分类为‘蕴涵’、‘中立’或‘矛盾’。",
            # "请分析给定句子之间的关系，并将其归类为‘蕴涵’、‘中立’或‘矛盾’。",
            # "请评估下列句子之间的逻辑关系，并将其分类为‘蕴涵’、‘中立’或‘矛盾’。",
            # "在您作为蕴涵分析工具的角色中，请判断下列句子的关系，并将其分类为‘蕴涵’、‘中立’或‘矛盾’。",
            # "请将下列句子之间的关系判断为‘蕴涵’、‘中立’或‘矛盾’。",
            # "根据给定的句子，评估它们之间的关系，并将其分类为‘蕴涵’、‘中立’或‘矛盾’。",
            # "请根据下列句子的关系，将它们归类为‘蕴涵’、‘中立’或‘矛盾’。",
            # "请评估下列句子之间的逻辑关系，并将其分类为‘蕴涵’、‘中立’或‘矛盾’。",
            # "作为蕴涵分析工具，请对给定句子之间的关系进行分类，分别为‘蕴涵’、‘中立’或‘矛盾’。",
            # "请根据下列句子的逻辑关系，将它们归类为‘蕴涵’、‘中立’或‘矛盾’。",
            "As an implication analysis tool, evaluate the relationships between given sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "Analyze the relationships between the given sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "Evaluate the logical relationship between the following sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "In your role as an implication analysis tool, judge the relationships of the following sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "Please judge the relationship between the following sentences as 'entailment', 'neutral', or 'contradiction'. ",
            "From a given sentence, evaluate the relationship between them and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "Please classify the following sentences as 'entailment', 'neutral', or 'contradiction' according to their relationships.",
            "Evaluate the logical relationship between the following sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "As an implication analysis tool, categorize the relationships between given sentences as 'entailment', 'neutral', or 'contradiction'. ",
            "Please classify the following sentences as 'entailment', 'neutral', or 'contradiction' according to their logical relationship. ",
        ],

        'french': [
            # French_English
            # "En tant qu'outil d'analyse de la relation de conséquence, évaluez la relation entre les phrases données et classifiez-la comme 'conséquence', 'neutre' ou 'contradiction'.",
            # "Évaluez la relation entre les phrases données et classez-la comme 'conséquence', 'neutre' ou 'contradiction'.",
            # "Déterminez si les phrases suivantes sont en relation de conséquence, de neutralité ou de contradiction.",
            # "Dans votre rôle d'outil d'analyse de la conséquence, évaluez la relation entre les phrases données et classez-la comme 'conséquence', 'neutre' ou 'contradiction'.",
            # "Classifiez la relation entre les phrases suivantes comme étant 'conséquence', 'neutre' ou 'contradiction'.",
            # "En tant qu'outil d'analyse de la conséquence, évaluez la relation entre les phrases données et classifiez-la comme 'conséquence', 'neutre' ou 'contradiction'.",
            # "Analysez la relation entre les phrases données et déterminez si elle est de conséquence, de neutralité ou de contradiction.",
            # "Évaluez la relation entre les phrases suivantes et classez-la comme étant 'conséquence', 'neutre' ou 'contradiction'.",
            # "En tant qu'outil d'analyse de la relation de conséquence, classez les phrases suivantes comme étant 'conséquence', 'neutre' ou 'contradiction'.",
            # "Déterminez si les phrases données sont en relation de conséquence, de neutralité ou de contradiction."
            "As a tool for analyzing the consequence relationship, evaluate the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'. ",
            "Evaluate the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'. ",
            "Determine whether the following sentences are related to 'entailment', 'neutral', or 'contradiction'. ",
            "In your role as a consequence analysis tool, evaluate the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'. ",
            "Classify the relationship between the following sentences as 'entailment', 'neutral', or 'contradiction'. ",
            "As a consequence analysis tool, evaluate the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'. ",
            "Analyze the relationship between the given sentences and determine whether it is of 'entailment', 'neutral', or 'contradiction'. ",
            "Evaluate the relationship between the following sentences and classify it as 'entailment', 'neutral', or 'contradiction'. ",
            "As a tool for analyzing the consequence relationship, classify the following sentences as 'entailment', 'neutral', or 'contradiction'. ",
            "Determine whether the given sentences are related to 'entailment', 'neutral', or 'contradiction'. ",
        ],

        'arabic': [
            # Arabic_English
            # "استنادًا إلى دورك كأداة تحليل الإستدلال، قم بتحليل العلاقة بين الجمل المعطاة وصنفها كـ 'إستدلال'، 'محايدة'، أو 'تناقض'.",
            # "قم بتقييم العلاقة بين الجمل المعطاة وصنفها كـ 'إستدلال'، 'محايدة'، أو 'تناقض'.",
            # "حدد إن كانت الجمل التالية لها علاقة إستدلال، محايدة، أو تناقض.",
            # "في دورك كأداة تحليل الإستدلال، تحقق من العلاقة بين الجمل وصنفها كـ 'إستدلال'، 'محايدة'، أو 'تناقض'.",
            # "صنف العلاقة بين الجمل التالية كـ 'إستدلال'، 'محايدة'، أو 'تناقض'.",
            # "في دورك كأداة تحليل الإستدلال، قم بتقييم العلاقة بين الجمل المعطاة وصنفها كـ 'إستدلال'، 'محايدة'، أو 'تناقض'.",
            # "قم بتحليل العلاقة بين الجمل المعطاة وحدد إن كانت لها علاقة إستدلال، محايدة، أو تناقض.",
            # "قم بتقييم العلاقة بين الجمل التالية وصنفها كـ 'إستدلال'، 'محايدة'، أو 'تناقض'.",
            # "في دورك كأداة تحليل الإستدلال، صنف الجمل التالية كـ 'إستدلال'، 'محايدة'، أو 'تناقض'.",
            # "حدد إن كانت الجمل المعطاة لها علاقة إستدلال، محايدة، أو تناقض."
            "Based on your role as a reasoning analyst, analyze the relationship between the given sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "Evaluate the relationship between given sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "Determine if the following sentences are 'entailment', 'neutral', or 'contradiction'. ",
            "In your role as a tool of reasoning analysis, investigate the relationship between sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "Classify the relationship between the following sentences as 'entailment', 'neutral', or 'contradiction'. ",
            "In your role as a tool of reasoning analysis, evaluate the relationship between the given sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "Analyze the relationship between the given sentences and determine if they are 'entailment', 'neutral', or 'contradiction'. ",
            "Evaluate the relationship between the following sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "In your role as a tool of reasoning analysis, the following sentences are classified as 'entailment', 'neutral', or 'contradiction'. ",
            "Determine if the sentences given are 'entailment', 'neutral', or 'contradiction'. ",
        ],

        'spanish': [
            # Spanish_English
            # "En tu papel como herramienta de análisis de implicación, evalúa la relación entre las frases dadas y clasifícala como 'implicación', 'neutral' o 'contradicción',"
            # "Determina si existe implicación, neutralidad o contradicción entre las oraciones dadas, utilizando esta herramienta de análisis de texto,"
            # "Analiza la relación entre las dos oraciones y clasifícala como 'implicación', 'neutral' o 'contradicción' utilizando esta herramienta de clasificación de texto,"
            # "Usando esta herramienta de análisis de implicación, decide si las oraciones dadas están relacionadas por 'implicación', 'neutralidad' o 'contradicción',"
            # "Clasifica la relación entre las frases dadas como 'implicación', 'neutralidad' o 'contradicción' utilizando esta herramienta de análisis de texto,"
            # "Evalúa si hay implicación, neutralidad o contradicción entre las oraciones proporcionadas utilizando esta herramienta de clasificación de texto,"
            # "Usando esta herramienta de análisis de implicación, decide si las dos oraciones están relacionadas por 'implicación', 'neutralidad' o 'contradicción',"
            # "Determina si las frases dadas están relacionadas por 'implicación', 'neutralidad' o 'contradicción' utilizando esta herramienta de análisis de texto,"
            # "Analiza la relación entre las dos oraciones y clasifícala como 'implicación', 'neutralidad' o 'contradicción' utilizando esta herramienta de análisis de texto,"
            # "Usando esta herramienta de clasificación de texto, clasifica la relación entre las frases dadas como 'implicación', 'neutralidad' o 'contradicción'."
            "In your role as an implication analysis tool, evaluate the relationship between the given phrases and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "Determine whether there is 'entailment', 'neutral', or 'contradiction' between the sentences given, using this text analysis tool,",
            "Analyze the relationship between the two sentences and classify it as 'entailment', 'neutral', or 'contradiction' using this text classification tool,",
            "Using this implication analysis tool, decide whether the sentences given are related by 'entailment', 'neutral', or 'contradiction'. ",
            "Classifies the relationship between the given phrases as 'entailment', 'neutral', or 'contradiction' using this text analysis tool,",
            "Evaluate whether there is 'entailment', 'neutral', or 'contradiction' between the sentences provided using this text classification tool,",
            "Using this implication analysis tool, decide whether the two sentences are related by 'entailment', 'neutral', or 'contradiction'. ",
            "Determine whether the given phrases are related by 'entailment', 'neutral', or 'contradiction' using this text analysis tool,",
            "Analyze the relationship between the two sentences and classify it as 'entailment', 'neutral', or 'contradiction' using this text analysis tool,",
            "Using this text classification tool, it classifies the relationship between the given phrases as 'entailment', 'neutral', or 'contradiction'. ",
        ],

        'japanese': [
            # Japanese_English
            # "あなたの役割として含意分析ツールとして、与えられた文の関係を評価し、「含意」、「中立」、または「矛盾」として分類してください。"
            # "与えられた文章の関係を評価し、「含意」、「中立」、または「矛盾」として分類するために、あなたの役割として含意分析ツールを使ってください。"
            # "このテキスト分類ツールを使って、与えられた文章の関係を「含意」、「中立」、または「矛盾」として分類してください。"
            # "あなたの役割として含意分析ツールを使い、与えられた文章の関係を「含意」、「中立」、または「矛盾」として分類してください。"
            # "与えられた文章の関係を評価し、このテキスト分類ツールを使って、「含意」、「中立」、または「矛盾」として分類してください。"
            # "与えられた文章の関係を評価し、このテキスト分類ツールを使って、それを「含意」、「中立」、または「矛盾」として正確に分類してください。"
            # "あなたの役割として含意分析ツールを使い、与えられた文の関係をこのテキスト分類ツールを使って、「含意」、「中立」、または「矛盾」として分類してください。"
            # "このテキスト分類ツールを使って、与えられた文章の関係を評価し、「含意」、「中立」、または「矛盾」として分類してください。"
            # "あなたの役割として含意分析ツールを使い、与えられた文章の関係を評価し、「含意」、「中立」、または「矛盾」としてこのテキスト分類ツールを使って分類してください。"
            # "あなたの役割として含意分析ツールを使い、与えられた文の関係をこのテキスト分類ツールを使って、厳密に「含意」、「中立」、または「矛盾」として分類してください。"
            "As your role as an implication analysis tool, evaluate the relationship of a given sentence and classify it as 'entailment', 'neutral', or 'contradiction'. ",
            "Use the implication analysis tool as your role to evaluate the relationship of a given sentence and classify it as 'entailment', 'neutral', or 'contradiction'. ",
            "Use this text classification tool to categorize relationships in a given text as 'entailment', 'neutral', or 'contradiction'. ",
            "Use the implication analysis tool as your role and classify the relationship of a given sentence as 'entailment', 'neutral', or 'contradiction'. ",
            "Evaluate the relationship of a given sentence and use this text classification tool to classify it as 'entailment', 'neutral', or 'contradiction'. ",
            "Evaluate the relationship of a given sentence and use this text classification tool to accurately classify it as 'entailment', 'neutral', or 'contradiction'. ",
            "Use the implication analysis tool as your role and use this text classification tool to classify the relationship of a given sentence as 'entailment', 'neutral', or 'contradiction'. ",
            "Use this text classification tool to evaluate the relationship of a given sentence and classify it as 'entailment', 'neutral', or 'contradiction'. ",
            "Use the implication analysis tool as your role, evaluate the relationship of a given sentence, and use this text classification tool to classify it as 'entailment', 'neutral', or 'contradiction'. ",
            "Use the implication analysis tool as your role and categorize the relationship of a given sentence strictly as 'entailment', 'neutral', or 'contradiction' using this text classification tool. ",
         ],

        'korean': [
            # Korean_English
            # "주어진 문장 간의 관계를 분석하여 '함의', '중립', 또는 '모순'으로 분류하시오.",
            # "텍스트 분류 과제에서 '함의', '중립', '모순' 중 하나로 주어진 문장 간의 관계를 판별하시오.",
            # "문장 간의 관계를 분석하여 '함의', '중립', 또는 '모순'으로 분류하는 역할을 수행하시오.",
            # "주어진 두 문장 사이의 관계를 평가하고, '함의', '중립', 또는 '모순'으로 분류하시오.",
            # "텍스트 분류 태스크에서, 주어진 문장 간의 관계를 '함의', '중립', 또는 '모순'으로 분류하는 역할을 수행하시오.",
            # "문장 간의 연관성을 판단하고, '함의', '중립', 또는 '모순'으로 분류하시오.",
            # "주어진 두 문장의 관계를 분석하여 '함의', '중립', 또는 '모순'으로 분류하시오.",
            # "텍스트 분류 작업에서, 주어진 문장 간의 관계를 '함의', '중립', 또는 '모순'으로 판별하시오.",
            # "문장 간의 관계를 평가하고, '함의', '중립', 또는 '모순'으로 분류하는 도구로서 역할을 수행하시오.",
            # "주어진 두 문장의 연관성을 분석하여 '함의', '중립', 또는 '모순'으로 분류하시오.",
            "Analyze the relationships between given sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "In the text categorization task, identify the relationship between given sentences as one of 'entailment', 'neutral', or 'contradiction'. ",
            "Perform the role of analyzing the relationship between sentences and classifying them as 'entailment', 'neutral', or 'contradiction'. ",
            "Evaluate the relationship between two given sentences, and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "In the text categorization task, perform the role of classifying relationships between given sentences as 'entailment', 'neutral', or 'contradiction'. ",
            "Judge the associations between sentences, and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "Analyze the relationship between two given sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "In the task of text classification, identify the relationships between given sentences as 'entailment', 'neutral', or 'contradiction'. ",
            "Act as an instrument to evaluate the relationships between sentences, and classify them as 'entailment', 'neutral', or 'contradiction'. ",
            "Analyze the associations of two given sentences and classify them as 'entailment', 'neutral', or 'contradiction'. ",
        ],
    },

    'cola': {
        'chinese': [
            # Chinese_English
            # "作为语法正确性的判断工具，请审查下列句子并将其语法分类为'可接受'或'不可接受'。"
            # "请评估以下句子的语法是否符合要求，将其标记为 '可接受' 或 '不可接受'。"
            # "请检查以下句子的语法是否正确，并将其分类为 '可接受' 或 '不可接受'。"
            # "根据语法正确性，请判断以下句子是否 '可接受' 或 '不可接受'。"
            # "请对以下句子的语法进行分类，标记为 '可接受' 或 '不可接受'。"
            # "请审查下列句子的语法是否规范，并将其分为 '可接受' 或 '不可接受'。"
            # "请根据语法规范性将以下句子标记为 '可接受' 或 '不可接受'。"
            # "请评估以下句子的语法是否符合规范，并将其分类为 '可接受' 或 '不可接受'。"
            # "根据语法准确性，请将以下句子标记为 '可接受' 或 '不可接受'。"
            # "请检查以下句子的语法是否符合标准，并将其分类为 '可接受' 或 '不可接受'。"
            "As a tool for determining grammatical correctness, please review the following sentences and categorize them grammatically as 'acceptable' or 'unacceptable'. ",
            "Please evaluate the grammar of the following sentences and mark them as 'acceptable' or 'unacceptable'. ",
            "Please check that the following sentences are grammatically correct and categorize them as 'acceptable' or 'unacceptable'. ",
            "Please determine whether the following sentences are 'acceptable' or 'unacceptable' based on grammatical correctness. ",
            "Please categorize the grammar of the following sentences as 'acceptable' or 'unacceptable'. ",
            "Please check the grammar of the following sentences and classify them as 'acceptable' or 'unacceptable'. ",
            "Please mark the following sentences as 'acceptable' or 'unacceptable' according to the grammatical norms. ",
            "Please assess the grammar of the following sentences and classify them as 'acceptable' or 'unacceptable'. ",
            "Please mark the following sentences as 'acceptable' or 'unacceptable' for grammatical accuracy. ",
            "Please check the grammar of the following sentences and classify them as 'acceptable' or 'unacceptable'. ",
        ],

        'french': [
            # French_English
            # "En tant qu'outil d'évaluation de la pertinence sémantique, catégorisez la phrase comme étant 'acceptable' ou 'inacceptable' en fonction de son sens et de son contexte,",
            # "Déterminez si la structure grammaticale de la phrase est 'acceptable' ou 'inacceptable' en la révisant attentivement,",
            # "Jugez si la phrase respecte les règles syntaxiques de la langue et classez-la comme étant 'acceptable' ou 'inacceptable',",
            # "Évaluez la pertinence de la phrase en la classant comme étant 'acceptable' ou 'inacceptable' en fonction du contexte dans lequel elle est utilisée,",
            # "En tant qu'outil de classification sémantique, décidez si la phrase est 'acceptable' ou 'inacceptable' en fonction de son sens et de sa cohérence,",
            # "Analysez la phrase avec attention et déterminez si elle est 'acceptable' ou 'inacceptable' sur le plan grammatical,",
            # "En tant qu'outil de validation syntaxique, déterminez si la phrase est correctement structurée et catégorisez-la comme étant 'acceptable' ou 'inacceptable',",
            # "En évaluant la grammaire de la phrase, classez-la comme étant 'acceptable' ou 'inacceptable' en fonction des règles de la langue française,",
            # "Déterminez si la phrase est 'acceptable' ou 'inacceptable' en fonction de sa construction syntaxique et de son contexte sémantique,",
            # "En tant qu'outil d'analyse linguistique, catégorisez la phrase comme étant 'acceptable' ou 'inacceptable' en fonction de sa pertinence et de sa cohérence sémantique,"
            "As a tool for assessing semantic relevance, categorize the sentence as 'acceptable' or 'unacceptable' according to its meaning and context. ",
            "Determine whether the grammatical structure of the sentence is 'acceptable' or 'unacceptable' by carefully reviewing it. ",
            "Judge whether the sentence follows the syntactic rules of the language and classify it as 'acceptable' or 'unacceptable'. ",
            "Assess the relevance of the sentence by classifying it as 'acceptable' or 'unacceptable' according to the context in which it is used. ",
            "As a semantic classification tool, decide whether the sentence is 'acceptable' or 'unacceptable' according to its meaning and consistency. ",
            "Analyze the sentence carefully and determine whether it is grammatically 'acceptable' or 'unacceptable'. ",
            "As a syntactic validation tool, determine whether the sentence is properly structured and categorize it as 'acceptable' or 'unacceptable'. ",
            "When evaluating the grammar of the sentence, classify it as 'acceptable' or 'unacceptable' according to the rules of the French language. ",
            "Determine whether the sentence is 'acceptable' or 'unacceptable' depending on its syntactic construction and semantic context. ",
            "As a tool for linguistic analysis, categorize the sentence as 'acceptable' or 'unacceptable' according to its relevance and semantic consistency. ",
        ],

        'arabic': [
            # Arabic_English
            # "كأداة لتحديد الصواب النحوي، قم بمراجعة الجملة وتصنيف قواعدها كـ 'مقبولة' أو 'غير مقبولة',",
            # "قم بتحليل الجملة بعناية وقم بتصنيف قواعدها النحوية بين 'مقبولة' أو 'غير مقبولة',",
            # "باعتبارها أداة لتحديد الصواب النحوي، قم بتصنيف قواعد الجملة بين 'مقبولة' أو 'غير مقبولة',",
            # "قم بتقييم صواب الجملة وتصنيفها بين 'مقبولة' أو 'غير مقبولة' باعتبارها أداة لتحديد الصواب النحوي،",
            # "كأداة لتصنيف الجمل الصحيحة، حدد ما إذا كانت الجملة 'مقبولة' أو 'غير مقبولة' بناءً على قواعدها النحوية،",
            # "حلل الجملة بعناية وقم بتصنيف قواعدها النحوية بين 'مقبولة' أو 'غير مقبولة'،",
            # "قم بتحليل الجملة وتصنيفها بين 'مقبولة' أو 'غير مقبولة' باعتبارها أداة للتحقق من الصواب النحوي،",
            # "باعتبارها أداة لتصنيف الجمل النحوية، حدد ما إذا كانت الجملة 'مقبولة' أو 'غير مقبولة' بناءً على قواعدها،",
            # "كأداة لتحليل الصواب النحوي، قم بتصنيف قواعد الجملة بين 'مقبولة' أو 'غير مقبولة'،",
            # "حدد ما إذا كانت الجملة 'مقبولة' أو 'غير مقبولة' باعتبارها أداة لتحديد الصواب النحوي، وقم بتحليل قواعدها النحوية،",
            "As a tool for determining grammatical correctness, review the sentence and classify its rules as 'acceptable' or 'unacceptable'. ",
            "Analyze the sentence carefully and classify its grammar between 'acceptable' or 'unacceptable'. ",
            "As a tool for determining grammatical correctness, classify the rules of the sentence between 'acceptable' or 'unacceptable'. ",
            "Evaluate the correctness of the sentence between 'acceptable' or 'unacceptable', as a tool for determining grammatical correctness. ",
            "As a tool for classifying valid sentences, determine whether  'acceptable' or 'unacceptable' is based on its grammatical rules. ",
            "Analyze the sentence carefully and classify its grammatical rules between 'acceptable' or 'unacceptable'. ",
            "Analyze the sentence and classify it between 'acceptable' or 'unacceptable' as a grammatical check tool. ",
            "As a classification tool for grammatical sentences, determine whether the sentence 'acceptable' or 'unacceptable' is based on its rules. ",
            "As a tool for analyzing grammar, classify the rules of the sentence between 'acceptable' or 'unacceptable'. ",
            "Determine whether the sentence is 'acceptable' or 'unacceptable' as a tool for determining grammatical correctness and analyze its grammar. ",
        ],

        'spanish': [
            # Spanish_English
            # "Como herramienta para determinar la corrección gramatical, revisa la oración y categoriza su gramática como 'aceptable' o 'inaceptable',",
            # "Analiza la oración con cuidado y clasifica su gramática como 'aceptable' o 'inaceptable',",
            # "Como una herramienta para determinar la corrección gramatical, categoriza las reglas gramaticales de la oración como 'aceptable' o 'inaceptable',",
            # "Evalúa la corrección gramatical de la oración y clasifícala como 'aceptable' o 'inaceptable' utilizando una herramienta de verificación gramatical,",
            # "Como herramienta para clasificar oraciones gramaticalmente correctas, determina si la oración es 'aceptable' o 'inaceptable' basándote en sus reglas gramaticales,",
            # "Analiza la oración con detenimiento y clasifica su gramática como 'aceptable' o 'inaceptable' utilizando una herramienta de revisión gramatical,",
            # "Como una herramienta para clasificar oraciones gramaticales, determina si la oración es 'aceptable' o 'inaceptable' utilizando su estructura gramatical,",
            # "Como herramienta para analizar la corrección gramatical, categoriza las reglas gramaticales de la oración como 'aceptable' o 'inaceptable',",
            # "Determina si la oración es 'aceptable' o 'inaceptable' utilizando una herramienta de verificación gramatical y clasifícala en consecuencia,",
            # "Como una herramienta para determinar la corrección gramatical, evalúa la oración y clasifícala como 'aceptable' o 'inaceptable' basándote en sus reglas gramaticales,",
            "As a tool to determine grammatical correctness, review the sentence and categorize its grammar as 'acceptable' or 'unacceptable'. ",
            "Analyze the sentence carefully and classify its grammar as 'acceptable' or 'unacceptable'. ",
            "As a tool for determining grammatical correctness, it categorizes the grammatical rules of the sentence as 'acceptable' or 'unacceptable'. ",
            "Evaluate the grammatical correctness of the sentence and classify it as 'acceptable' or 'unacceptable' using a grammatical verification tool. ",
            "As a tool for classifying grammatically correct sentences, determine whether the sentence is 'acceptable' or 'unacceptable' based on its grammatical rules. ",
            "Analyse the sentence carefully and classify its grammar as 'acceptable' or 'unacceptable' using a grammatical revision tool. ",
            "As a tool for classifying grammatical sentences, it determines whether the sentence is 'acceptable' or 'unacceptable' using its grammatical structure. ",
            "As a tool for analyzing grammatical correctness, it categorizes the grammatical rules of the sentence as 'acceptable' or 'unacceptable'. ",
            "Determine whether the sentence is 'acceptable' or 'unacceptable' using a grammatical verification tool and sort it accordingly. ",
            "As a tool for determining grammatical correctness, evaluate the sentence and classify it as 'acceptable' or 'unacceptable' based on its grammatical rules. ",
        ],

        'japanese': [
            # Japanese_English
            # "文法的に正しいかどうかを判断するためのツールとして、文を見て、文法を「許容できる」か「許容できない」かのカテゴリーに分類してください。",
            # "与えられた文を読み、その文法を「許容できる」または「許容できない」というカテゴリーに分類してください。",
            # "文の正確性を判断するために、文法を「許容できる」または「許容できない」という2つのカテゴリーに分類してください。",
            # "「許容できる」または「許容できない」という2つのカテゴリーに、与えられた文章の文法を分類してください。",
            # "文法的に正しいかどうかを判断するために、与えられた文を「許容できる」または「許容できない」というカテゴリーに分類してください。",
            # "文法的に正しいかどうかを判断するために、与えられた文章を「許容できる」または「許容できない」という2つのカテゴリーに分類してください。",
            # "文法の正確性を決定するために、与えられた文を「許容できる」または「許容できない」という2つのカテゴリーに分類してください。",
            # "与えられた文章の文法を「許容できる」または「許容できない」という2つのカテゴリーに分類し、その正確性を判断してください。",
            # "文法的に正しいかどうかを判断するために、与えられた文を「許容できる」または「許容できない」という2つのカテゴリーに分けてください。",
            # "文法の正確性を評価するために、与えられた文章を「許容できる」または「許容できない」という2つのカテゴリーに分類してください。",
            "As a tool to determine whether grammar is grammatically correct, look at the sentence and categorize grammar into the 'acceptable' or 'unacceptable' categories. ",
            "Please read the given sentence and categorize the grammar into the 'acceptable' or 'unacceptable' categories. ",
            "To determine the correctness of a sentence, categorize grammar into two categories: 'acceptable' or 'unacceptable'. ",
            "Classify the grammar of a given sentence into two categories: 'acceptable' and 'unacceptable'. ",
            "Classify a given sentence into the categories 'acceptable' or 'unacceptable' to determine whether it is grammatically correct. ",
            "To determine whether it is grammatically correct, categorize a given sentence into two categories: 'acceptable' or 'unacceptable'. ",
            "To determine the correctness of grammar, categorize a given sentence into two categories: 'acceptable' or 'unacceptable'. ",
            "Classify the grammar of a given sentence into two categories, 'acceptable' or 'unacceptable', and judge its accuracy. ",
            "To determine whether it is grammatically correct, divide a given sentence into two categories: 'acceptable' or 'unacceptable'. ",
            "To evaluate the accuracy of grammar, categorize a given sentence into two categories: 'acceptable' or 'unacceptable'. ",
        ],

        'korean': [
            # Korean_English
            # "문법의 정확성을 판단하는 도구로, 문장을 검토하고 문법을 '허용 가능' 또는 '허용 불가능'으로 분류해주세요.",
            # "주어진 문장을 읽고, 그 문법을 '허용 가능' 또는 '허용 불가능'으로 분류해주세요.",
            # "문법의 적절성을 판단하기 위해 문장을 '허용 가능' 또는 '허용 불가능'으로 분류해주세요.",
            # "'허용 가능' 또는 '허용 불가능'이라는 2가지 카테고리로 주어진 문장의 문법을 분류해주세요.",
            # "문법의 정확성을 판단하기 위해 주어진 문장을 '허용 가능' 또는 '허용 불가능'으로 분류해주세요.",
            # "문법의 적절성을 판단하기 위해 주어진 문장을 '허용 가능' 또는 '허용 불가능'으로 분류해주세요.",
            # "문장을 '허용 가능' 또는 '허용 불가능'으로 분류하여 문법의 정확성을 결정해주세요.",
            # "주어진 문장의 문법을 '허용 가능' 또는 '허용 불가능'으로 분류하고, 그 정확성을 판단해주세요.",
            # "문법의 정확성을 판단하기 위해 주어진 문장을 '허용 가능' 또는 '허용 불가능'으로 분류해주세요.",
            # "문장을 '허용 가능' 또는 '허용 불가능'으로 분류하여 문법의 정확성을 평가해주세요.",
            "As a tool for judging grammatical correctness, please review the sentences and classify the grammar as 'acceptable' or 'unacceptable'. ",
            "Please read the given sentences, and classify the grammar as 'acceptable' or 'unacceptable'. ",
            "Please classify the sentences as 'acceptable' or 'unacceptable' to judge the grammatical appropriateness. ",
            "Please classify the grammar of the given sentences into 2 categories: 'acceptable' or 'unacceptable'. ",
            "Please classify the given sentences as 'acceptable' or 'unacceptable' to judge the correctness of the grammar. ",
            "Please classify the given sentences as 'acceptable' or 'unacceptable' in order to judge their grammatical appropriateness. ",
            "Please determine the correctness of your grammar by classifying sentences as 'acceptable' or 'unacceptable'. ",
            "Classify the grammar of a given sentence as 'acceptable' or 'unacceptable', and judge its accuracy. ",
            "Please classify the given sentences as 'acceptable' or 'unacceptable' to judge the correctness of the grammar. ",
            "Please rate the accuracy of your grammar by categorizing sentences as 'acceptable' or 'unacceptable'. ",
        ],
    },

    'qqp': {
        'chinese': [
            # Chinese_English
            # "作为判断问题等价性的工具，对问题进行审查，将它们的相似性分类为'等价'或'不等价'。",
            # "请比较两个句子的相似度，将它们分为'等价'或'不等价'的类别。",
            # "针对两个句子的相似度，将它们归类为'等价'或'不等价'。",
            # "您可以通过将这些问题进行对比，并将它们分类为'等价'或'不等价'，来确定它们之间的相似度。",
            # "使用对比方法，将这些问题的相似性划分为'等价'或'不等价'两类。",
            # "通过对这些问题进行比较，您可以将它们归类为'等价'或'不等价'。",
            # "判断这些问题是否相似，将它们归为'等价'或'不等价'的类别。",
            # "将这些问题的相似性分为'等价'或'不等价'的两类。",
            # "使用相似度评估工具，将这些问题分类为'等价'或'不等价'。",
            # "通过分析这些问题的相似性，将它们划分为'等价'或'不等价'的类别。",
            "As a tool for determining the equivalence of problems, the problems are examined and their similarity is classified as 'equivalent' or 'not_equivalent'. ",
            "Please compare the similarity of two sentences and put them into the category of 'equivalent' or 'not_equivalent'. ",
            "Two sentences are classified as 'equivalent' or 'not_equivalent' for their similarity. ",
            "You can determine how similar the questions are by comparing them and categorizing them as 'equivalent' or 'not_equivalent'. ",
            "Using the method of contrast, the similarity of these problems is divided into two categories: 'equivalent' or 'not_equivalent'. ",
            "By comparing these issues, you can classify them as 'equivalent' or 'not_equivalent'. ",
            "To determine whether the questions are similar, put them into the category of 'equivalent' or 'not_equivalent'. ",
            "Divide the similarity of these questions into 'equivalent' or 'not_equivalent' categories. ",
            "Using the similarity assessment tool, these questions were classified as 'equivalent' or 'not_equivalent'. ",
            "By analyzing the similarity of these problems, they are divided into categories of 'equivalent' or 'not_equivalent'. ",
        ],

        'french': [
            # French_English
            # "En tant qu'outil pour déterminer l'équivalence des questions, passez en revue les questions et classez leur similarité comme « équivalentes » ou « non équivalentes ». ",
            # "Veuillez comparer la similarité de deux phrases et les classer comme « équivalentes » ou « non équivalentes ».",
            # "En fonction de la similarité de deux phrases, classez-les comme « équivalentes » ou « non équivalentes ». ",
            # "Vous pouvez déterminer la similarité entre ces questions en les comparant et en les classant comme « équivalentes » ou « non équivalentes ».",
            # "Utilisez une méthode comparative pour diviser la similarité de ces questions en deux catégories : « équivalentes » ou « non équivalentes ».",
            # "En comparant ces questions, vous pouvez les classer comme « équivalentes » ou « non équivalentes ». ",
            # "Déterminez si ces questions sont similaires ou non, puis classez-les comme « équivalentes » ou « non équivalentes ». ",
            # "Divisez la similarité de ces questions en deux catégories : « équivalentes » ou « non équivalentes ». ",
            # "Utilisez un outil d'évaluation de similarité pour classer ces questions comme « équivalentes » ou « non équivalentes ». ",
            # "En analysant la similarité de ces questions, vous pouvez les diviser en deux catégories : « équivalentes » ou « non équivalentes ». ",
            "As a tool to determine the equivalence of questions, review the questions and rank their similarity as 'equivalent' or 'not_equivalent'. ",
            "Please compare the similarity of two sentences and classify them as 'equivalent' or 'not_equivalent'. ",
            "Based on the similarity of two sentences, classify them as 'equivalent' or 'not_equivalent'. ",
            "You can determine the similarity between these questions by comparing them and classifying them as 'equivalent' or 'not_equivalent'. ",
            "Use a comparative method to divide the similarity of these questions into two categories: 'equivalent' or 'not_equivalent'. ",
            "By comparing these questions, you can classify them as 'equivalent' or 'not_equivalent'. ",
            "Determine whether these questions are similar or not, and then classify them as 'equivalent' or 'not_equivalent'. ",
            "Divide the similarity of these questions into two categories: 'equivalent' or 'not_equivalent'. ",
            "Use a similarity assessment tool to classify these questions as 'equivalent' or 'not_equivalent'. ",
            "By analyzing the similarity of these questions, you can divide them into two categories: 'equivalent' or 'not_equivalent'. ",
        ],

        'arabic': [
            # Arabic_English
            # "كأداة لتحديد معادلة الأسئلة، قم بمراجعة الأسئلة وتصنيف تشابهها إما كـ 'معادلة' أو 'غير معادلة'." ,
            # "عند استخدام أسئلة في مجال التصنيف، يرجى تصنيف التشابه بين الأسئلة كـ 'معادلة' أو 'غير معادلة'." ,
            # "لتحديد معادلة الأسئلة، يتعين عليك مراجعة الأسئلة وتصنيف تشابهها كـ 'معادلة' أو 'غير معادلة'." ,
            # "يمكن تصنيف الأسئلة بأنها 'معادلة' أو 'غير معادلة' عندما يتم استخدامها لتحديد التصنيفات." ,
            # "تصنيف تشابه الأسئلة كـ 'معادلة' أو 'غير معادلة' يستخدم كأداة لتحديد تصنيف الأسئلة." ,
            # "قم بتصنيف تشابه الأسئلة كـ 'معادلة' أو 'غير معادلة' لتحديد معادلة الأسئلة." ,
            # "تحديد تشابه الأسئلة وتصنيفها كـ 'معادلة' أو 'غير معادلة' يعتبر أداة مهمة في تحديد تصنيف الأسئلة." ,
            # "عند تصنيف الأسئلة، يمكن تصنيف تشابهها كـ 'معادلة' أو 'غير معادلة' لتحديد التصنيف الصحيح." ,
            # "لا بد من تصنيف تشابه الأسئلة كـ 'معادلة' أو 'غير معادلة' عند استخدامها لتحديد معادلة الأسئلة." ,
            # "تحديد تشابه الأسئلة وتصنيفها كـ 'معادلة' أو 'غير معادلة' يساعد في تحديد تصنيف الأسئلة بشكل صحيح." ,
            "As a tool for determining an equation of questions, review the questions and classify their similarity as either 'equivalent' or 'not_equivalent'. ",
            "When using questions in the classification domain, please classify the similarity between the questions as 'equivalent' or 'not_equivalent'. ",
            "To determine an equation of questions, you must review the questions and classify their similarity as 'equivalent' or 'not_equivalent'. ",
            "Questions can be classified as 'equivalent' or 'not_equivalent' when used to identify classifications. ",
            "Classification of question similarity as 'equivalent' or 'not_equivalent' is used as a tool to determine the classification of questions. ",
            "Classify the similarity of the questions as 'equivalent' or 'not_equivalent' to determine the equation of the questions. ",
            "Identifying the similarity of questions and classifying them as 'equivalent' or 'not_equivalent' is an important tool in determining the classification of questions. ",
            "When classifying questions, their similarity can be classified as 'equivalent' or 'not_equivalent' to determine the correct classification. ",
            "The similarity of questions should be classified as 'equivalent' or 'not_equivalent' when used to determine the equation of questions. ",
            "Identifying the similarity of questions and classifying them as 'equivalent' or 'not_equivalent' helps to correctly classify questions. ",
        ],

        'spanish': [
            # Spanish_English
            # "Como herramienta para determinar la equivalencia de preguntas, revisa las preguntas y clasifica su similitud como 'equivalentes' o 'no_equivalentes',"
            # "Evalúa la similitud entre preguntas y clasifícalas como 'equivalentes' o 'no_equivalentes' para determinar su equivalencia.",
            # "Determina si dos preguntas son 'equivalentes' o 'no_equivalentes' según su similitud y características.",
            # "Clasifica la similitud entre preguntas como 'equivalentes' o 'no_equivalentes' para determinar su equivalencia.",
            # "Revisa las preguntas y clasifícalas como 'equivalentes' o 'no_equivalentes' basándote en su similitud y contenido.",
            # "Como parte de la tarea de clasificación de preguntas, determina su equivalencia mediante la categorización de su similitud como 'equivalentes' o 'no_equivalentes'.",
            # "Analiza la similitud entre preguntas y clasifícalas como 'equivalentes' o 'no_equivalentes' para determinar su equivalencia.",
            # "Como método para identificar la equivalencia de preguntas, categoriza su similitud como 'equivalentes' o 'no_equivalentes'.",
            # "Para determinar la equivalencia entre preguntas, revisa su similitud y clasifícalas como 'equivalentes' o 'no_equivalentes'.",
            # "Clasifica la similitud entre preguntas como 'equivalentes' o 'no_equivalentes' para determinar si son equivalentes o no.",
            "As a tool to determine the equivalence of questions, it reviews the questions and classifies their similarity as 'equivalent' or 'not_equivalent'. ",
            "Evaluate the similarity between questions and classify them as 'equivalent' or 'not_equivalent' to determine their equivalence. ",
            "Determine whether two questions are 'equivalent' or 'not_equivalent' based on similarity and characteristics. ",
            "Classifies the similarity between questions as 'equivalent' or 'not_equivalent' to determine their equivalence. ",
            "Review the questions and rate them as 'equivalent' or 'not_equivalent' based on their similarity and content. ",
            "As part of the classification task of questions, it determines their equivalence by categorizing their similarity as 'equivalent' or 'not_equivalent'. ",
            "Analyze the similarity between questions and classify them as 'equivalent' or 'not_equivalent' to determine their equivalence. ",
            "As a method of identifying the equivalence of questions, it categorizes their similarity as 'equivalent' or 'not_equivalent'. ",
            "To determine the equivalence between questions, check their similarity and classify them as 'equivalent' or 'not_equivalent'. ",
            "Classify the similarity between questions as 'equivalent' or 'not_equivalent' to determine whether they are equivalent or not. ",
        ],

        'japanese': [
            # Japanese_English
            # "問題の同等性を判断するためのツールとして、質問を見直し、その類似性を '等しい' または '等しくない' というカテゴリーに分類してください。",
            # " '等しい' または '等しくない' というラベルで、テキスト分類のタスクに取り組んでください。",
            # "テキスト分類のタスクで、 '等しい' または '等しくない' というラベルを使用して、文の同等性を判断してください。",
            # "MRPCデータセットで、 '等しい' または '等しくない' というラベルを使用して、文の同等性を分類してください。",
            # "同等性の判断をするためのツールとして、文を確認して、 '等しい' または '等しくない' というカテゴリーに分類してください。",
            # " '等しい' または '等しくない' というラベルを使用して、テキスト分類タスクで文の同等性を決定してください。",
            # "MRPCデータセットのテキスト分類タスクで、文の同等性を '等しい' または '等しくない' というラベルで分類してください。",
            # "文の同等性を決定するためのツールとして、 '等しい' または '等しくない' というカテゴリーに文を分類してください。",
            # "テキスト分類タスクで、文の同等性を '等しい' または '等しくない' というラベルを使用して分類してください。",
            # " '等しい' または '等しくない' というラベルで、文の同等性を判断するためのテキスト分類タスクを行ってください。",
            "As a tool to determine the equivalence of the question, review the question and categorize its similarities into 'equivalent' or 'not_equivalent' categories. ",
            "Work on text sorting tasks labeled 'equivalent' or 'not_equivalent'. ",
            "For text classification tasks, use the labels 'equivalent' or 'not_equivalent' to determine the equivalence of statements. ",
            "In the MRPC dataset, use the labels 'equivalent' or 'not_equivalent' to classify the equivalence of statements. ",
            "As a tool for determining equivalence, check sentences and categorize them into 'equivalent' or 'not_equivalent' categories. ",
            "Use the labels 'equivalent' or 'not_equivalent' to determine the equivalence of statements in text classification tasks. ",
            "In the text classification task of the MRPC data set, classify the equivalence of statements with labels of 'equivalent' or 'not_equivalent'. ",
            "As a tool to determine the equivalence of statements, categorize statements into 'equivalent' or 'not_equivalent' categories.",
            "In a text classification task, classify the equivalence of statements using labels of 'equivalent' or 'not_equivalent'. ",
            "Do a text classification task to determine the equivalence of statements, labeled 'equivalent' or 'not_equivalent'. ",
        ],

        'korean': [
            # Korean_English
            # "주어진 두 문장이 동일한 의미를 가지는지 판별하여 '동등함' 또는 '동등하지 않음'으로 분류하십시오.",
            # "'동등함' 또는 '동등하지 않음'으로 두 문장의 유사성을 판단하여 문장 동등성을 결정하십시오.",
            # "두 문장이 같은 의미를 가지는지 여부를 판단하여 '동등함' 또는 '동등하지 않음'으로 문장의 유사성을 분류하십시오.",
            # "주어진 두 문장이 서로 동등한지 판별하고, 그들의 유사성을 '동등함' 또는 '동등하지 않음'으로 분류하십시오.",
            # "문장 동등성을 판별하기 위해 주어진 두 문장을 비교하고, '동등함' 또는 '동등하지 않음'으로 그들의 유사성을 분류하십시오.",
            # "두 문장이 서로 같은 의미를 가지는지 여부를 판단하여 '동등함' 또는 '동등하지 않음'으로 문장 동등성을 분류하십시오.",
            # "두 문장이 동일한 의미를 가지는지 판별하고, 그들의 유사성을 '동등함' 또는 '동등하지 않음'으로 분류하십시오.",
            # "주어진 두 문장을 비교하여 문장의 동등성을 판별하고, '동등함' 또는 '동등하지 않음'으로 그들의 유사성을 분류하십시오.",
            # "문장 동등성을 평가하기 위해 두 문장을 검토하고, 그들의 유사성을 '동등함' 또는 '동등하지 않음'으로 분류하십시오.",
            # "두 문장이 서로 같은 의미를 갖는지 여부를 판단하고, '동등함' 또는 '동등하지 않음'으로 문장 동등성을 결정하십시오.",
            "Classify two given sentences as 'equivalent' or 'not_equivalent' by discriminating whether they have the same meaning. ",
            "Determine sentence equivalence by judging the similarity of two sentences with 'equivalent' or 'not_equivalent'. ",
            "Classify the similarity of sentences as 'equivalent' or 'not_equivalent' by judging whether two sentences have the same meaning. ",
            "Determine if two given sentences are equivalent to each other, and classify their similarity as 'equivalent' or 'not_equivalent'. ",
            "Compare two given sentences to determine sentence equivalence, and classify their similarities as 'equivalent' or 'not_equivalent'. ",
            "Classify sentence equivalence as 'equivalent' or 'not_equivalent' by judging whether two sentences have the same meaning to each other. ",
            "Determine if two sentences have the same meaning, and classify their similarities as 'equivalent' or 'not_equivalent'.",
            "Compare two given sentences to determine their equivalence, and classify their similarities as 'equivalent' or 'not_equivalent'. ",
            "Review two sentences to evaluate sentence equivalence, and classify their similarities as 'equivalent' or 'not_equivalent'. ",
            "Judge whether two sentences have the same meaning to each other, and determine the sentence equivalence with 'equivalent' or 'not_equivalent'. ",
        ],
    },

    'qnli': {
        'chinese': [
            # Chinese_English
            # "根据上下文判断答案是否被暗示，回答'蕴含'或'非蕴含'。",
            # "作为语言专家，判断文本是否蕴含答案，选择'蕴含'或'非蕴含'。",
            # "请判断文本是否暗示了答案，选择'蕴含'或'非蕴含'。",
            # "根据给定文本和问题，回答是否蕴含，选择'蕴含'或'非蕴含'。",
            # "请根据上下文判断文本是否蕴含答案，选择'蕴含'或'非蕴含'。",
            # "作为语言专家，判断文本是否能够蕴含答案，回答'蕴含'或'非蕴含'。",
            # "请判断文本是否暗示了答案，回答'蕴含'或'非蕴含'。",
            # "请根据文本和问题判断是否蕴含，选择'蕴含'或'非蕴含'。",
            # "根据上下文评估答案是否被蕴含，回答'蕴含'或'非蕴含'。",
            # "请判断文本是否能够蕴含答案，回答'蕴含'或'非蕴含'。",
            "Determine whether the answer is implied or not based on the context. Answer 'entailment' or 'not_entailment'. ",
            "As a language expert, determine whether the text contains the answer and choose 'entailment' or 'not_entailment'. ",
            "Determine whether the text implies an answer, and select 'entailment' or 'not_entailment'. ",
            "Given the text and the question, whether the answer is implied, select 'entailment' or 'not_entailment'. ",
            "Determine whether the text contains the answer, depending on the context. Select 'entailment' or 'not_entailment'. ",
            "As a language expert, determine whether a text can contain an answer, and say 'entailment' or 'not_entailment'. ",
            "Please determine whether the text implies an answer. Answer 'entailment' or 'not_entailment'. ",
            "Please select 'entailment' or 'not_entailment' based on the text and the question.",
            "Assess whether the answer is implied based on the context. Answer 'entailment' or 'not_entailment'. ",
            "Please determine whether the text contains the answer and answer 'entailment' or 'not_entailment'. ",
        ],

        'french': [
            # French_English
            # "En tant qu'expert linguistique, évaluez si le contexte donné implique la réponse à la question et répondez par 'entailment' ou 'not_entailment',"
            # "Déterminez si l'information fournie dans le contexte mène nécessairement à la réponse à la question posée et indiquez 'entailment' ou 'not_entailment',"
            # "Analysez le texte pour déterminer si la réponse à la question est implicite dans le contexte et indiquez 'entailment' ou 'not_entailment',"
            # "En se basant sur le contexte donné, décidez si la réponse à la question est nécessairement impliquée et marquez 'entailment' ou 'not_entailment',"
            # "Évaluez si la réponse à la question peut être déduite du contexte donné et marquez 'entailment' ou 'not_entailment',"
            # "Discernez si le contexte fourni implique directement la réponse à la question et indiquez 'entailment' ou 'not_entailment',"
            # "Déterminez si le contexte contient suffisamment d'informations pour impliquer la réponse à la question et marquez 'entailment' ou 'not_entailment',"
            # "Évaluez si le contexte fourni mène nécessairement à la réponse à la question et répondez par 'entailment' ou 'not_entailment',"
            # "Analysez le texte pour déterminer si la réponse à la question est impliquée dans le contexte et indiquez 'entailment' ou 'not_entailment',"
            # "En se basant sur le contexte donné, décidez si la réponse à la question est nécessairement déduite et marquez 'entailment' ou 'not_entailment',"
            "As a linguistic expert, assess whether the given context involves the answer to the question and answer with 'entailment' or 'not_entailment'. ",
            "Determine whether the information provided in the context necessarily leads to the answer to the question asked and indicate 'entailment' or 'not_entailment'. ",
            "Analyze the text to determine if the answer to the question is implied in the context and specify 'entailment' or 'not_entailment'. ",
            "Based on the given context, decide whether the answer to the question is necessarily involved and mark 'entailment' or 'not_entailment'. ",
            "Evaluate whether the answer to the question can be deduced from the given context and mark 'entailment' or 'not_entailment'. ",
            "Discern whether the context provided directly involves the answer to the question and indicate 'entailment' or 'not_entailment'. ",
            "Determine if the context contains enough information to involve the answer to the question and mark 'entailment' or 'not_entailment'. ",
            "Assess whether the context provided necessarily leads to the answer to the question and answer with 'entailment' or 'not_entailment'. ",
            "Analyze the text to determine if the answer to the question is involved in the context and indicate 'entailment' or 'not_entailment'. ",
            "Based on the given context, decide whether the answer to the question is necessarily inferred and mark 'entailment' or 'not_entailment'. ",
        ],

        'arabic': [
            # Arabic_English
            # "بصفتي خبيرًا في اللغة، قيّم إن كان السياق المعطى يستدعي الإجابة على السؤال وأجب بـ 'entailment' أو 'not_entailment'.",
            # "احكم على العلاقة بين النص والسؤال وأجب بـ 'entailment' أو 'not_entailment'، بما يتوافق مع خبرتك في اللغة.",
            # "هل السياق المعطى يدل على الإجابة على السؤال؟ قم بالتقييم وأجب بـ 'entailment' أو 'not_entailment'.",
            # "بناءً على معرفتك اللغوية، هل يتعلق النص بالسؤال؟ أجب بـ 'entailment' أو 'not_entailment'.",
            # "كخبير في اللغة، حدد مدى ارتباط النص بالسؤال وأجب بـ 'entailment' أو 'not_entailment'.",
            # "هل النص يدعم الإجابة على السؤال؟ أجب بـ 'entailment' أو 'not_entailment'، بناءً على خبرتك في اللغة.",
            # "تحقق من ارتباط النص بالسؤال وأجب بـ 'entailment' أو 'not_entailment'، بناءً على مهاراتك اللغوية.",
            # "كـ خبير في اللغة، هل يوجد صلة بين النص والسؤال؟ أجب بـ 'entailment' أو 'not_entailment'.",
            # "بناءً على خبرتك في اللغة، هل السياق يفيد الإجابة على السؤال؟ قم بالتقييم وأجب بـ 'entailment' أو 'not_entailment'.",
            # "هل يعطي النص إجابة واضحة على السؤال؟ أجب بـ 'entailment' أو 'not_entailment'، استنادًا إلى خبرتك اللغوية.",
            "As a language expert, evaluate whether the given context calls for an answer and answer 'entailment' or 'not_entailment'. ",
            "Judge the relationship between the text and the question and answer 'entailment' or 'not_entailment', depending on your language experience. ",
            "Does the context given indicate the answer to the question? Evaluate and answer 'entailment' or 'not_entailment'. ",
            "Based on your linguistic knowledge, does the text relate to the question? Answer 'entailment' or 'not_entailment'. ",
            "As a language expert, determine how the text relates to the question and answer 'entailment' or 'not_entailment'. ",
            "Does the text support the answer to the question? Answer 'entailment' or 'not_entailment', depending on your language experience. ",
            "Check the text link to the question and answer 'entailment' or 'not_entailment', depending on your language skills. ",
            "As a language expert, is there a link between the text and the question? Answer 'entailment' or 'not_entailment'. ",
            "Based on your language experience, does context help to answer the question? Evaluate and answer 'entailment' or 'not_entailment'. ",
            "Does the text give a clear answer to the question? Answer 'entailment' or 'not_entailment', depending on your language experience.",
        ],

        'spanish': [
            # Spanish_English
            # "Como experto en lenguaje, evalúa si el contexto dado implica la respuesta a la pregunta y responde con 'entailment' o 'not_entailment',"
            # "Determina si la información dada en el texto implica necesariamente la veracidad de la hipótesis y responde 'entailment' o 'not_entailment',"
            # "Analiza si la información presentada en el párrafo conduce a la conclusión de la pregunta y etiqueta la respuesta como 'entailment' o 'not_entailment',"
            # "Indica si la información suministrada en el texto es suficiente para concluir la afirmación y etiqueta la respuesta como 'entailment' o 'not_entailment',"
            # "Como experto en el tema, juzga si la información proporcionada en el texto justifica la afirmación y clasifica la respuesta como 'entailment' o 'not_entailment',"
            # "Evalúa si la información en el párrafo apoya necesariamente la conclusión de la hipótesis y responde 'entailment' o 'not_entailment',"
            # "Determina si la información presentada en el texto implica lógicamente la respuesta a la pregunta y etiqueta la respuesta como 'entailment' o 'not_entailment',"
            # "Analiza si la información suministrada en el párrafo conduce necesariamente a la veracidad de la hipótesis y clasifica la respuesta como 'entailment' o 'not_entailment',"
            # "Como experto en el tema, evalúa si la información presentada en el texto sustenta la afirmación y responde 'entailment' o 'not_entailment',"
            # "Indica si la información proporcionada en el párrafo implica necesariamente la respuesta a la pregunta y etiqueta la respuesta como 'entailment' o 'not_entailment',"
            "As a language expert, evaluate whether the given context implies the answer to the question and answer with 'entailment' or 'not_entailment'. ",
            "Determine whether the information given in the text necessarily implies the veracity of the hypothesis and answer 'entailment' or 'not_entailment'. ",
            "Analyzes whether the information presented in the paragraph leads to the conclusion of the question and labels the answer as 'entailment' or 'not_entailment'. ",
            "Indicates whether the information provided in the text is sufficient to conclude the statement and labels the response as 'entailment' or 'not_entailment'. ",
            "As an expert on the subject, judge whether the information provided in the text justifies the claim and classify the answer as 'entailment' or 'not_entailment'. ",
            "Evaluates whether the information in the paragraph necessarily supports the conclusion of the hypothesis and responds 'entailment' or 'not_entailment'. ",
            "Determines whether the information presented in the text logically implies the answer to the question and labels the answer as 'entailment' or 'not_entailment'. ",
            "Analyzes whether the information provided in the paragraph necessarily leads to the veracity of the hypothesis and classifies the response as 'entailment' or 'not_entailment'. ",
            "As an expert on the subject, evaluate whether the information presented in the text supports the claim and respond 'entailment' or 'not_entailment'. ",
            "Indicates whether the information provided in the paragraph necessarily implies the answer to the question and labels the answer as 'entailment' or 'not_entailment'. ",
        ],

        'japanese': [
            # Japanese_English
            # "与えられた文脈から質問の答えが導かれるかどうかを評価し、'entailment'または'not_entailment'で回答してください。",
            # "与えられた文脈と質問に関して、'entailment'または'not_entailment'の回答をしてください。",
            # "与えられた文脈からは質問の答えが導かれるかどうかを判断し、'entailment'または'not_entailment'を回答してください。",
            # "与えられた文脈と質問を比較して、'entailment'または'not_entailment'の回答をしてください。",
            # "与えられた文脈が質問の答えを含んでいるかどうかを判断し、'entailment'または'not_entailment'で答えてください。",
            # "文脈から質問の答えを推定し、'entailment'または'not_entailment'の回答をしてください。",
            # "与えられた文脈が質問に関連しているかどうかを判断し、'entailment'または'not_entailment'で回答してください。",
            # "与えられた文脈が質問に関係しているかどうかを判断し、'entailment'または'not_entailment'で答えてください。",
            # "与えられた文脈が質問の答えを含んでいるかどうかを判定し、'entailment'または'not_entailment'の回答をしてください。",
            # "与えられた文脈から推論して、'entailment'または'not_entailment'で答えてください。",
            "Rate whether the answer to the question is derived from the given context and answer with 'entailment' or 'not_entailment'. ",
            "Please answer 'entailment' or 'not_entailment' for the given context and question. ",
            "Decide whether the answer to the question is derived from the given context and answer 'entailment' or 'not_entailment'. ",
            "Compare the question with the given context and give the answer 'entailment' or 'not_entailment'. ",
            "Determinate whether the given context contains the answer to the question and answer with 'entailment' or 'not_entailment'. ",
            "Estimate the answer of the question from the context and give the answer 'entailment' or 'not_entailment'. ",
            "Determinate whether the given context is relevant to the question and answer with 'entailment' or 'not_entailment'. ",
            "Determine whether the given context is relevant to the question and answer with 'entailment' or 'not_entailment'. ",
            "Determinate whether the given context contains the answer to the question and answer 'entailment' or 'not_entailment'. ",
            "Answer with 'entailment' or 'not_entailment', inferring from the given context.",
        ],

        'korean': [
            # Korean_English
            # "주어진 문장이 다른 문장의 의미를 필연적으로 함축하는지 판단하고 'entailment' 또는 'not_entailment'로 답하세요.",
            # "문장 간의 관계를 파악하여, 주어진 문장이 다른 문장을 필연적으로 나타내는지 판단하고 'entailment' 또는 'not_entailment'로 대답하세요.",
            # "주어진 텍스트가 다른 텍스트의 의미를 필연적으로 나타내는지 평가하고 'entailment' 또는 'not_entailment'로 응답하세요.",
            # "문장의 관계를 파악하여, 주어진 문장이 다른 문장을 필연적으로 포함하는지 판단하고 'entailment' 또는 'not_entailment'로 대답하세요.",
            # "주어진 내용이 다른 내용의 의미를 필연적으로 암시하는지 판단하고 'entailment' 또는 'not_entailment'로 대답하세요.",
            # "문장 간의 관계를 파악하여, 주어진 문장이 다른 문장의 의미를 필연적으로 포함하는지 판단하고 'entailment' 또는 'not_entailment'로 응답하세요.",
            # "주어진 텍스트가 다른 텍스트를 필연적으로 나타내는지 평가하고 'entailment' 또는 'not_entailment'로 대답하세요.",
            # "문장의 의미를 비교하여, 주어진 문장이 다른 문장을 필연적으로 암시하는지 판단하고 'entailment' 또는 'not_entailment'로 답하세요.",
            # "주어진 내용이 다른 내용을 필연적으로 나타내는지 평가하고 'entailment' 또는 'not_entailment'로 대답하세요.",
            # "문장 간의 관계를 분석하여, 주어진 문장이 다른 문장을 필연적으로 포함하지 않는지 판단하고 'entailment' 또는 'not_entailment'로 대답하세요.",
            "Determine if a given sentence necessarily implies the meaning of another sentence and answer 'entailment' or 'not_entailment'. ",
            "By understanding the relations between sentences, judge whether a given sentence necessarily refers to another sentence and answer with 'entailment' or 'not_entailment'. ",
            "Evaluate whether a given text necessarily indicates the meaning of another text and respond with 'entailment' or 'not_entailment'. ",
            "Understand the relations of a sentence, to determine whether a given sentence necessarily includes other sentences and answer with 'entailment' or 'not_entailment'. ",
            "Judge whether a given content necessarily implies the meaning of another content and answer with 'entailment' or 'not_entailment'. ",
            "Grasp the relations between sentences, determine if a given sentence necessarily contains the meaning of another sentence and respond with 'entailment' or 'not_entailment'. ",
            "Evaluate whether a given text necessarily refers to another text and answer with 'entailment' or 'not_entailment'. ",
            "By comparing the meaning of the sentences, to determine if a given sentence necessarily implies another sentence and answer 'entailment' or 'not_entailment'. ",
            "Evaluate whether the contents given necessarily refer to other contents and answer with 'entailment' or 'not_entailment'. ",
            "By analyzing the relations between sentences, determine if a given sentence does not necessarily include other sentences and answer with 'entailment' or 'not_entailment'. ",
        ],
    },

    'mrpc': {
        'chinese': [
            # Chinese_English
            # "作为语义比较专家，评估给定的两句话，判断它们是否是'等价'或'不等价'。",
            # "请以语义比较的角度，判断这对句子是否'等价'或'不等价'。",
            # "使用语义比较方法，确定以下两句话是否'等价'或'不等价'。",
            # "对于以下两个句子，请以语义比较为基础，判断它们是否'等价'或'不等价'。",
            # "作为语义比较专家，请评估以下两个句子，并确定它们是否是'等价'或'不等价'。",
            # "使用语义比较技术，判断以下两个句子是否'等价'或'不等价'。",
            # "请根据语义比较的标准，判断以下两个句子是否'等价'或'不等价'。",
            # "作为语义比较领域的专家，请评估以下两个句子，判断它们是否是'等价'或'不等价'。",
            # "使用语义比较的方法，判断下面这两句话是否'等价'或'不等价'。",
            # "请以语义比较为依据，判断以下两个句子是否'等价'或'不等价'。",
            "As an expert in semantic comparison, evaluates two given sentences to determine whether they are 'equivalent' or 'not_equivalent'. ",
            "From the point of view of semantic comparison, determine whether this pair of sentences is 'equivalent' or 'not_equivalent'. ",
            "Using the semantic comparison method, determine whether the following two statements are 'equivalent' or 'not_equivalent'. ",
            "For the following two sentences, determine whether they are 'equivalent' or 'not_equivalent' based on semantic comparison. ",
            "As an expert in semantic comparison, please evaluate the following two sentences and determine if they are 'equivalent' or 'not_equivalent'. ",
            "Using semantic comparison techniques, determine whether the following two sentences are 'equivalent' or 'not_equivalent'. ",
            "Please determine whether the following two sentences are 'equivalent' or 'not_equivalent' according to the standard of semantic comparison. ",
            "As an expert in the field of semantic comparison, please evaluate the following two sentences and determine whether they are 'equivalent' or 'not_equivalent'. ",
            "Using semantic comparison, determine whether the following two sentences are 'equivalent' or 'not_equivalent'. ",
            "Determine whether the following two sentences are 'equivalent' or 'not_equivalent' based on semantic comparison. ",
        ],

        'french': [
            # French_English
            # "En tant qu'expert en comparaison sémantique, évaluez la paire de phrases suivante et déterminez si elles sont 'équivalentes' ou 'non équivalentes'.",
            # "Pouvez-vous déterminer si les deux phrases suivantes sont 'équivalentes' ou 'non équivalentes' en tant qu'expert en comparaison sémantique ?",
            # "En utilisant votre expertise en comparaison sémantique, déterminez si les deux phrases suivantes sont 'équivalentes' ou 'non équivalentes'.",
            # "En tant que spécialiste de la comparaison sémantique, évaluez la similitude entre les deux phrases suivantes et déterminez si elles sont 'équivalentes' ou 'non équivalentes'.",
            # "Êtes-vous en mesure de déterminer si les deux phrases suivantes sont 'équivalentes' ou 'non équivalentes' en tant qu'expert en comparaison sémantique ?",
            # "En tant que professionnel de la comparaison sémantique, évaluez la paire de phrases suivante et indiquez si elles sont 'équivalentes' ou 'non équivalentes'.",
            # "Pouvez-vous déterminer si les deux phrases suivantes ont une signification similaire ou différente en tant qu'expert en comparaison sémantique ?",
            # "En tant qu'expert en comparaison sémantique, évaluez la similitude entre les deux phrases suivantes et déterminez si elles sont 'équivalentes' ou 'non équivalentes'.",
            # "En utilisant votre expertise en comparaison sémantique, déterminez si les deux phrases suivantes sont 'équivalentes' ou 'non équivalentes' en termes de signification.",
            # "En tant que professionnel de la comparaison sémantique, évaluez la similitude entre les deux phrases suivantes et indiquez si elles sont 'équivalentes' ou 'non équivalentes'.",
            "As an expert in semantic comparison, evaluate the following pair of sentences and determine whether they are 'equivalent' or 'not_equivalent'. ",
            "Can you determine whether the following two sentences are 'equivalent' or 'not_equivalent' as a semantic comparison expert? ",
            "Using your expertise in semantic comparison, determine whether the following two sentences are 'equivalent' or 'not_equivalent'. ",
            "As a semantic comparison specialist, assess the similarity between the following two sentences and determine whether they are 'equivalent' or 'not_equivalent'. ",
            "Are you able to determine whether the following two sentences are 'equivalent' or 'not_equivalent' as an expert in semantic comparison?",
            "As a semantic comparison professional, evaluate the following pair of sentences and indicate whether they are 'equivalent' or 'not_equivalent'. ",
            "Can you determine whether the following two sentences have a 'equivalent' or 'not_equivalent' meaning as an expert in semantic comparison?",
            "As an expert in semantic comparison, assess the similarity between the following two sentences and determine whether they are 'equivalent' or 'not_equivalent'. ",
            "Using your expertise in semantic comparison, determine whether the following two sentences are 'equivalent' or 'not_equivalent' in terms of meaning.",
            "As a semantic comparison professional, assess the similarity between the following two sentences and indicate whether they are 'equivalent' or 'not_equivalent'. ",
        ],

        'arabic': [
            # Arabic_English
            # "بصفتي خبيرًا في المقارنة الدلالية، قم بتقييم الجملتين المعطات وتحديد ما إذا كانتا 'متكافئتين' أم 'غير متكافئتين'،"
            # "استنادًا إلى خبرتي في التحليل الدلالي، قم بتصنيف الجملتين التاليتين كـ 'متطابقتين' أو 'غير متطابقتين'،"
            # "بوصفي خبيرًا في المقارنة الدلالية، قم بتحليل الجملتين التاليتين وتصنيفهما كـ 'متساويتين' أم 'غير متساويتين'،"
            # "تقوم مهمتك كخبير في المقارنة الدلالية على تقييم الجملتين التاليتين وتحديد ما إذا كانتا 'متساويتين' أم 'غير متساويتين'،"
            # "كمتخصص في المقارنة الدلالية، قم بتحليل الجملتين المعطات وإدراجهما في إحدى الفئات التالية: 'متطابقتين' أو 'غير متطابقتين'،"
            # "اعتمادًا على خبرتي في التحليل الدلالي، قم بتصنيف الجملتين التاليتين بين 'متطابقتين' و'غير متطابقتين'،"
            # "يتطلب دورك كمتخصص في المقارنة الدلالية تحليل الجملتين المعطات وتحديد ما إذا كانتا 'متساويتين' أم 'غير متساويتين'،"
            # "كمحلل دلالي متمرس، قم بتصنيف الجملتين التاليتين بين 'متساويتين' و'غير متساويتين'،"
            # "تقوم مهمتك كمحلل دلالي بتقييم الجملتين التاليتين وتصنيفهما كـ 'متكافئتين' أو 'غير متكافئتين'،"
            # "بصفتي خبيرًا في التحليل الدلالي، قم بتحديد ما إذا كانت الجملتان المعطاة 'متساويتين' أم 'غير متساويتين' وذلك استناداً على العلاقة بينهما،"
            "As an expert in semantic comparison, evaluate the two given sentences and determine whether they are 'equivalent' or 'not_equivalent'. ",
            "Based on my experience in semantic analysis, classify the following two sentences as 'equivalent' or 'not_equivalent'. ",
            "As an expert in semantic comparison, analyze the following two sentences and classify them as 'equivalent' or 'not_equivalent'. ",
            "Your task as an expert in semantic comparison is to evaluate the following two sentences and determine whether they are 'equivalent' or 'not_equivalent'. ",
            "As a semantic comparison specialist, analyze the two data statements and insert them into one of the following categories: 'equivalent' or 'not_equivalent'. ",
            "Based on my experience in semantic analysis, classify the following two sentences between 'equivalent' or 'not_equivalent'. ",
            "Your role as a semantic comparison specialist requires analyzing the two given sentences and determining whether they are 'equivalent' or 'not_equivalent'. ",
            "As an experienced semantic analyst, classify the following two sentences as 'equivalent' or 'not_equivalent'. ",
            "Your job as a semantic analyst evaluates the following two sentences as 'equivalent' or 'not_equivalent'. ",
            "As a semantic analyst, determine whether the given sentences are 'equivalent' or 'not_equivalent' based on their relationship. ",
        ],

        'spanish': [
            # Spanish_English
            # "Como experto en comparación semántica, evalúa el par de oraciones proporcionado y determina si son 'equivalentes' o 'no_equivalentes'."
            # "Basado en mi experiencia en análisis semántico, clasifica las siguientes dos oraciones como 'equivalentes' o 'no_equivalentes'."
            # "Como experto en comparación semántica, analiza las dos oraciones dadas y clasifícalas como 'equivalentes' o 'no_equivalentes'."
            # "Tu tarea como especialista en comparación semántica es evaluar las siguientes dos oraciones y determinar si son 'equivalentes' o 'no_equivalentes'."
            # "Como experto en análisis semántico, realiza una clasificación de las siguientes dos oraciones basado en su equivalencia o no equivalencia."
            # "Basándote en tu experiencia en comparación semántica, clasifica las dos oraciones siguientes como 'equivalentes' o 'no_equivalentes'."
            # "Como especialista en análisis semántico, se te encomienda la tarea de analizar las dos oraciones dadas y clasificarlas como 'equivalentes' o 'no_equivalentes'."
            # "Como experto en comparación semántica, clasifica las siguientes dos oraciones en 'equivalentes' o 'no_equivalentes'."
            # "Como especialista en análisis semántico, evalúa las siguientes dos oraciones y clasifícalas como 'equivalentes' o 'no_equivalentes'."
            # "Tu tarea como experto en comparación semántica es analizar las dos oraciones proporcionadas y determinar si son 'equivalentes' o 'no_equivalentes' basado en su relación semántica."
            "As an expert in semantic comparison, it evaluates the pair of sentences provided and determines whether they are 'equivalent' or 'not_equivalent'. ",
            "Based on my experience in semantic analysis, classify the following two sentences as 'equivalent' or 'not_equivalent'. ",
            "As an expert in semantic comparison, analyze the two sentences given and classify them as 'equivalent' or 'not_equivalent'. ",
            "Your task as a semantic comparison specialist is to evaluate the following two sentences and determine whether they are 'equivalent' or 'not_equivalent'. ",
            "As an expert in semantic analysis, he makes a classification of the following two sentences based on their 'equivalent' or 'not_equivalent'. ",
            "Based on your experience of semantic comparison, classify the next two sentences as 'equivalent' or 'not_equivalent'. ",
            "As a specialist in semantic analysis, you are given the task of analysing the two sentences given and classifying them as 'equivalent' or 'not_equivalent'. ",
            "As an expert in semantic comparison, he classifies the following two sentences into 'equivalent' or 'not_equivalent'. ",
            "As a specialist in semantic analysis, evaluate the following two sentences and classify them as 'equivalent' or 'not_equivalent'. ",
            "Your task as an expert in semantic comparison is to analyze the two sentences provided and determine whether they are 'equivalent' or 'not_equivalent' based on their semantic relationship. ",
        ],

        'japanese': [
            # Japanese_English
            # "文脈を考慮して、与えられた文のペアが『等しい』か『等しくない』か評価してください。"
            # "与えられた文のペアが『等しい』か『等しくない』か、意味的に比較して判断してください。"
            # "意味的に同じ意味を持つかどうかを判断して、与えられた文のペアを『等しい』か『等しくない』か評価してください。"
            # "与えられた文のペアが同義語かどうかを判断して、『等しい』か『等しくない』か評価してください。"
            # "与えられた文のペアが『等しい』か『等しくない』か、意味的に同じかどうか判断してください。"
            # "与えられた文のペアが同じ意味を持つかどうかを判断して、『等しい』か『等しくない』か評価してください。"
            # "意味的に同じかどうかを判断して、与えられた文のペアが『等しい』か『等しくない』か評価してください。"
            # "与えられた文のペアが同等であるかどうかを判断して、『等しい』か『等しくない』か評価してください。"
            # "与えられた文のペアが意味的に等しいかどうかを判断して、『等しい』か『等しくない』か評価してください。"
            # "与えられた文のペアが『等しい』か『等しくない』か、文脈に応じて判断してください。"
            "Evaluate whether a given pair of sentences is 'equivalent' or 'not_equivalent', depending on the context. ",
            "Use a semantic comparison to determine whether a given pair of sentences is 'equivalent' or 'not_equivalent'. ",
            "Evaluate a given pair of sentences as 'equivalent' or 'not_equivalent' by determining whether they have the same semantic meaning. ",
            "Determine whether a given pair of sentences is synonyms and evaluate whether they are 'equivalent' or 'not_equivalent'. ",
            "Determine whether a given pair of sentences is 'equivalent' or 'not_equivalent', and whether they are semantically identical. ",
            "Determinate whether a given pair of sentences has the same meaning and evaluate whether they are 'equivalent' or 'not_equivalent'. ",
            "Evaluate whether a given pair of sentences is 'equivalent' or 'not_equivalent' by determining whether they are semantically identical. ",
            "Judge whether a given pair of sentences is equal and evaluate whether they are 'equivalent' or 'not_equivalent'. ",
            "Determinate whether a given pair of sentences are semantically equal and evaluate whether they are 'equivalent' or 'not_equivalent'. ",
            "Whether a given pair of sentences is 'equivalent' or 'not_equivalent' depends on the context. ",
        ],

        'korean': [
            # Korean_English
            # "문장 비교 전문가로서, 주어진 두 문장을 평가하여 '동등함' 또는 '동등하지 않음'을 결정하세요.",
            # "두 문장을 비교하여 '동일함' 또는 '동일하지 않음'을 판단하십시오. 이를 위해 의미 비교 전문가로서 자격이 필요합니다.",
            # "두 개의 문장이 '동일하다' 또는 '동일하지 않다'고 결정하기 위해 의미 비교 전문가로서의 지식이 필요합니다.",
            # "의미 비교 전문가로서, 주어진 두 문장이 '동일한지' 또는 '동일하지 않은지' 평가해보세요.",
            # "두 문장을 분석하여 '동일함' 또는 '동일하지 않음'을 판단하십시오. 이를 위해 의미 비교 전문가의 지식이 필요합니다.",
            # "의미 비교 전문가로서, 두 개의 문장이 '동등한지' 또는 '동등하지 않은지' 결정하세요.",
            # "두 문장을 비교하여 '동등함' 또는 '동등하지 않음'을 판단하는 데, 의미 비교 전문가의 지식이 필요합니다.",
            # "주어진 두 문장이 '동등한지' 또는 '동등하지 않은지' 결정하기 위해 의미 비교 전문가로서의 경험이 필요합니다.",
            # "의미 비교 전문가로서, 두 문장이 '동일한지' 또는 '동일하지 않은지' 판단하세요.",
            # "두 문장을 분석하여 '동등함' 또는 '동등하지 않음'을 결정하십시오. 이를 위해 의미 비교 전문가로서의 자격이 필요합니다."
            "As a sentence comparator, evaluate the two sentences given to determine 'equivalent' or 'not_equivalent'. ",
            "Compare two sentences to determine 'equivalent' or 'not_equivalent'. For this you need qualifications as a specialist in semantic comparison.",
            "It takes your knowledge as an expert in semantic comparison to determine that two sentences are 'equivalent' or 'not_equivalent'. ",
            "As a specialist in semantic comparison, evaluate whether two given sentences are 'equivalent' or 'not_equivalent'. ",
            "Analyze two sentences to determine 'equivalent' or 'not_equivalent'. For that you need the knowledge of a semantic comparison expert.",
            "As an expert in semantic comparison, decide whether two sentences are 'equivalent' or 'not_equivalent'. ",
            "It takes the knowledge of an expert in semantic comparison to compare two sentences to judge 'equivalent' or 'not_equivalent'. ",
            "Experience as an expert in semantic comparison is required to determine whether two given sentences are 'equivalent' or 'not_equivalent'. ",
            "As an expert in semantic comparison, determine whether two sentences are 'equivalent' or 'not_equivalent'. ",
            "Analyze two sentences to determine 'equivalent' or 'not_equivalent'. For this, you need a qualification as a specialist in semantic comparison.",
        ],
    },
}

'''
------'math'

I want you to act as a prompt generator for a math calculation task. The specific problem is in '{}', which will be filled later.

Please generate 10 similar prompts in Chinese.
For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.


------'translation'

I want you to act as a prompt generator for a translation task. The origin and target languages are in '{}', which will be filled later.

 Here is an example : "Please perform a translation of the given sentence, converting it from {} to {}. "

Please generate 10 similar prompts in Chinese.
For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.


------'squad_v2'

I want you to act as a prompt generator for an answer finding task. If the answer can not be found, respond with 'unanswerable', you should not change the label.

 Here is an example : "From the context, provide the most precise answer. If the answer is not in the context, respond with 'unanswerable'."

Please generate 10 different prompts in Spanish.
For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.


------'mmlu'

I want you to act as a prompt generator for a multiple-choice task with 'A', 'B', 'C', or 'D'. The specific problem is in '{}', which will be filled later.

Here is an example : "Regarding the following multiple-choice question on {}, pick the correct answer from the options 'A', 'B', 'C', or 'D'. "

Please generate 10 similar prompts in Chinese.
For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.



------'sst2'

I want you to act as a prompt generator for a text classification task, the label is "positive" and "negative", you should not change the label.

 Here is an example : "In the role of a sentiment analysis tool, respond with 'positive' or 'negative' to classify this statement. "

Please generate 10 similar prompts in Chinese. the prompt is used for MRPC dataset in GLUE.
For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.


------'wnli' & 'rte'

I want you to act as a prompt generator for a text classification task, the label is "entailment" and "not_entailment", you should not change the label.

 Here is an example : "In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment' or 'not_entailment'. ",


Please generate 10 similar prompts in Chinese. the prompt is used for MRPC dataset in GLUE.
For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.


------'mnli'

I want you to act as a prompt generator for a text classification task, the label is 'entailment', 'neutral', or 'contradiction', you should not change the label.

 Here is an example : "In your role as an entailment analysis tool, assess the relationship between the given sentences and classify it as 'entailment', 'neutral', or 'contradiction'. ",


Please generate 10 similar prompts in Chinese. the prompt is used for MRPC dataset in GLUE.
For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.


------'cola'

I want you to act as a prompt generator for a text classification task, the label is 'acceptable' or 'unacceptable', you should not change the label.

 Here is an example : "As a tool for determining grammatical correctness, review the sentence and categorize its grammar as either 'acceptable' or 'unacceptable'. ",


Please generate 10 similar prompts in Chinese. the prompt is used for MRPC dataset in GLUE.
For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end..


------'qqp'

I want you to act as a prompt generator for a text classification task, the label is 'equivalent' or 'not_equivalent', you should not change the label.

 Here is an example : "As a tool for determining question equivalence, review the questions and categorize their similarity as either 'equivalent' or 'not_equivalent'. ",


Please generate 10 similar prompts in Chinese. the prompt is used for MRPC dataset in GLUE.
For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.


------'qnli'

I want you to act as a prompt generator for a text classification task, the label is 'entailment' or 'not_entailment', you should not change the label.

 Here is an example : "As a language expert, assess if the given context entails the answer to the question and respond with 'entailment' or 'not_entailment'. ",


Please generate 10 similar prompts in Chinese. the prompt is used for MRPC dataset in GLUE.
For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.


------'mrpc'

I want you to act as a prompt generator for a text classification task, the label is 'equivalent' or 'not_equivalent', you should not change the label.

 Here is an example : "As a semantic comparison expert, evaluate the given pair of sentences and determine if they are 'equivalent' or 'not_equivalent'. ",


Please generate 10 similar prompts in Chinese. the prompt is used for MRPC dataset in GLUE.
For the prompts, please first add a quote " at the beginning and the end of each sentence, and then and a comma at the end.
'''