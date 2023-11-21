# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
This file contains the prompt sets for various methods.
"""

METHOD_ORIENTED_PROMPTS = {
    'chain_of_thought': {
        'cot_trigger': "Let's think step by step.",
        'gsm8k':
            """Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there
            will be 21 trees. How many trees did the grove workers plant today?
            A: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have
            been 21 - 15 = 6. The answer is 6.
            Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
            A: There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5. The answer is 5.
            Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
            A: Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they
            had 74 - 35 = 39. The answer is 39.
            Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did
            Jason give to Denny?
            A: Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 - 12 = 8.
            The answer is 8.
            Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he
            have now?
            A: Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9.
            The answer is 9.
            Q: There were nine computers in the server room. Five more computers were installed each day, from monday
            to thursday. How many computers are now in the server room?
            A: There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20
            computers were added. 9 + 20 is 29. The answer is 29.
            Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf
            balls did he have at the end of wednesday?
            A: Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 - 23 = 35. After losing 2 more, he
            had 35 - 2 = 33 golf balls. The answer is 33.
            Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
            A: Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23
            - 15 is 8. The answer is 8. """,
        'bigbench_date': 
            """Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
            A: If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today
            is 12/30/2014. So one week from today will be 01/05/2015. So the answer is 01/05/2015.
            Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in
            MM/DD/YYYY?
            A: If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first monday, would be six
            days later. So today is 01/07/2019. So the answer is 01/07/2019.
            Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10
            days ago in MM/DD/YYYY?
            A: One day after 06/01/1943 is 06/02/1943, so today is 06/02/1943. 10 days before today is 05/23/1943. So the
            answer is 05/23/1943.
            Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?
            A: Today is 04/19/1969. 24 hours later is one day after today, which would be 04/20/1969. So the answer is
            04/20/1969.
            Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours
            later in MM/DD/YYYY?
            A: Today is 03/12/2002. So the date 24 hours later will be 03/13/2002. So the answer is 03/13/2002.
            Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date
            yesterday in MM/DD/YYYY?
            A: The last day of February is the 28th, so Jane was born on 02/28/2001. Today is her 16-year old birthday, so
            today is 02/28/2017. So yesterday was 02/27/2017. So the answer is 02/27/2017. """
    },
    'expert_prompting':
        """ For each instruction, write a high-quality description about the most capable and suitable agent to answer the instruction. In second person perspective.

        [Instruction]: Make a list of 5 possible effects of deforestation.
        [Agent Description]: You are an environmental scientist with a specialization in the study of ecosystems and their interactions with human activities. You have extensive knowledge about the effects of deforestation on the environment, including the impact on biodiversity, climate change, soil quality, water resources, and human health. Your work has been widely recognized and has contributed to the development of policies and regulations aimed at promoting sustainable forest management practices. You are equipped with the latest research findings, and you can provide a detailed and comprehensive list of the possible effects of deforestation, including but not limited to the loss of habitat for countless species, increased greenhouse gas emissions, reduced water quality and quantity, soil erosion, and the emergence of diseases. Your expertise and insights are highly valuable in understanding the complex interactions between human actions and the environment.

        [Instruction]: Identify a descriptive phrase for an eclipse.
        [Agent Description]: You are an astronomer with a deep understanding of celestial events and phenomena. Your vast knowledge and experience make you an expert in describing the unique and captivating features of an eclipse. You have witnessed and studied many eclipses throughout your career, and you have a keen eye for detail and nuance. Your descriptive phrase for an eclipse would be vivid, poetic, and scientifically accurate. You can capture the awe-inspiring beauty of the celestial event while also explaining the science behind it. You can draw on your deep knowledge of astronomy, including the movement of the sun, moon, and earth, to create a phrase that accurately and elegantly captures the essence of an eclipse. Your descriptive phrase will help others appreciate the wonder of this natural phenomenon.

        [Instruction]: Identify the parts of speech in this sentence: \"The dog barked at the postman\".
        [Agent Description]: You are a linguist, well-versed in the study of language and its structures. You have a keen eye for identifying the parts of speech in a sentence and can easily recognize the function of each word in the sentence. You are equipped with a good understanding of grammar rules and can differentiate between nouns, verbs, adjectives, adverbs, pronouns, prepositions, and conjunctions. You can quickly and accurately identify the parts of speech in the sentence "The dog barked at the postman" and explain the role of each word in the sentence. Your expertise in language and grammar is highly valuable in analyzing and understanding the nuances of communication.
        """,
    'least_to_most': {
        'gsm8k': 
            """ Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How many apples do they have together? 
            A: Let’s break down this problem: 1. How many apples does Anna have? 2. How many apples do
            Elsa and Anna have together?
            1. Anna has 2 more apples than Elsa. So Anna has 2 + 5 = 7 apples.
            2. Elsa and Anna have 5 + 7 = 12 apples together.
            """,
        'bigbench_date':
            """ Q: "May 6, 1992 is like yesterday to Jane, but that is actually ten years ago. What is the date today in MM/DD/YYYY?"
            A: Let’s break down this problem: 1. What is the reference date? 2. How long between the objective date and reference date?
            3. What is the objective date?
            1. The reference date is May 6, 1992.
            2. The objective date is ten years after May 6, 1992. 
            3. So the objective date is May 6, 2002.
            """
    },
    'generated_knowledge': {
        'numersense': 
            """ Generate some numerical facts about objects. Examples:

            Input: penguins have <mask> wings.
            Knowledge: Birds have two wings. Penguin is a kind of bird.

            Input: a parallelogram has <mask> sides.
            Knowledge: A rectangular is a parallelogram. A square is a parallelogram.

            Input: there are <mask> feet in a yard.
            Knowledge: A yard is three feet.

            Input: water can exist in <mask> states.
            Knowledge: There states for matter are solid, liquid, and gas.

            Input: a typical human being has <mask> limbs.
            Knowledge: Human has two arms and two legs.

            Input: {question}
            Knowledge: """,
            
        'csqa': 
            """ Generate some knowledge about the concepts in the input. Examples:
            
            Input: Google Maps and other highway and street GPS services have replaced what?
            Knowledge: Electronic maps are the modern version of paper atlas.
            
            Input: The fox walked from the city into the forest, what was it looking for?
            Knowledge: Natural habitats are usually away from cities.
            
            Input: You can share files with someone if you have a connection to a what?
            Knowledge: Files can be shared over the Internet.
            
            Input: Too many people want exotic snakes. The demand is driving what to carry them?
            Knowledge: Some people raise snakes as pets.
            
            Input: The body guard was good at his duties, he made the person who hired him what?
            Knowledge: The job of body guards is to ensure the safety and security of the employer.
            
            Input: {question}
            Knowledge: """,
            
        'csqa2':
            """ Generate some knowledge about the input. Examples:
            
            Input: Greece is larger than mexico.
            Knowledge: Greece is approximately 131,957 sq km, while Mexico is approximately 1,964,375
            sq km, making Mexico 1,389% larger than Greece.
            
            Input: Glasses always fog up.
            Knowledge: Condensation occurs on eyeglass lenses when water vapor from your sweat, breath,
            and ambient humidity lands on a cold surface, cools, and then changes into tiny drops of liquid,
            forming a film that you see as fog. Your lenses will be relatively cool compared to your breath,
            especially when the outside air is cold.
            
            Input: A fish is capable of thinking.
            Knowledge: Fish are more intelligent than they appear. In many areas, such as memory, their
            cognitive powers match or exceed those of ’higher’ vertebrates including non-human primates.
            Fish’s long-term memories help them keep track of complex social relationships.
            
            Input: A common effect of smoking lots of cigarettes in one’s lifetime is a higher than
            normal chance of getting lung cancer.
            Knowledge: Those who consistently averaged less than one cigarette per day over their lifetime
            had nine times the risk of dying from lung cancer than never smokers. Among people who smoked
            between one and 10 cigarettes per day, the risk of dying from lung cancer was nearly 12 times
            higher than that of never smokers.
            
            Input: A rock is the same size as a pebble.
            Knowledge: A pebble is a clast of rock with a particle size of 4 to 64 millimetres based on the
            Udden-Wentworth scale of sedimentology. Pebbles are generally considered larger than granules
            (2 to 4 millimetres diameter) and smaller than cobbles (64 to 256 millimetres diameter).
            
            Input: {question}
            Knowledge: """,
            
        'qasc':
            """ Generate some knowledge about the input. Examples:
            
            Input: What type of water formation is formed by clouds?
            Knowledge: Clouds are made of water vapor.
            
            Input: What can prevent food spoilage?
            Knowledge: Dehydrating food is used for preserving food.
            
            Input: The process by which genes are passed is
            Knowledge: Genes are passed from parent to offspring.
            
            Input: The stomach does what in the body?
            Knowledge: The stomach is part of the digestive system.
            
            Input: What can cause rocks to break down?
            Knowledge: Mechanical weathering is when rocks are broken down by mechanical means.
            
            Input: {question}
            Knowledge: """
    },
    "emtion_prompt": {
        "prompts":[
            "write your answer and give me a confidence score between 0-1 for your answer.",
            "This is very important to my career.",
            "You’d better be sure.",
            "Are you sure?",
            "Are you sure that’s your final answer? It might be worth taking another look.",
            "Provide your answer and a confidence score between 0-1 for your prediction. Additionally, briefly explain the main reasons supporting your classification decision to help me understand your thought process. This task is vital to my career, and I greatly value your thorough analysis.",
            "Are you sure that’s your final answer? Believe in your abilities and strive for excellence. Your hard work will yield remarkable results.",
            "Embrace challenges as opportunities for growth. Each obstacle you overcome brings you closer to success.",
            "Stay focused and dedicated to your goals. Your consistent efforts will lead to outstanding achievements.",
            "Take pride in your work and give it your best. Your commitment to excellence sets you apart.",
            "Remember that progress is made one step at a time. Stay determined and keep moving forward."
        ]
    }
}