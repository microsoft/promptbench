# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
This file contains the fewshot examples for each dataset.
"""

examples = {
    'squad_v2':
        "Here are three examples. \n" +
        "Context: Time has long been a major subject of study in religion, philosophy, and science, but defining it in a manner applicable to all fields without circularity has consistently eluded scholars. Nevertheless, diverse fields such as business, industry, sports, the sciences, and the performing arts all incorporate some notion of time into their respective measuring systems. Some simple definitions of time include 'time is what clocks measure', which is a problematically vague and self-referential definition that utilizes the device used to measure the subject as the definition of the subject, and 'time is what keeps everything from happening at once', which is without substantive meaning in the absence of the definition of simultaneity in the context of the limitations of human sensation, observation of events, and the perception of such events.\n" +
        "Question: Time has long been a major point of study in which fields?\n" +
        "Answer: religion, philosophy, and science\n"
        "Context: Temporal measurement has occupied scientists and technologists, and was a prime motivation in navigation and astronomy. Periodic events and periodic motion have long served as standards for units of time. Examples include the apparent motion of the sun across the sky, the phases of the moon, the swing of a pendulum, and the beat of a heart. Currently, the international unit of time, the second, is defined by measuring the electronic transition frequency of caesium atoms (see below). Time is also of significant social importance, having economic value ('time is money') as well as personal value, due to an awareness of the limited time in each day and in human life spans.\n" +
        "Question: What groups have been occupied by understanding the life span of humans?\n" +
        "Answer: unanswerable\n" +
        "Context: Artifacts from the Paleolithic suggest that the moon was used to reckon time as early as 6,000 years ago. Lunar calendars were among the first to appear, either 12 or 13 lunar months (either 354 or 384 days). Without intercalation to add days or months to some years, seasons quickly drift in a calendar based solely on twelve lunar months. Lunisolar calendars have a thirteenth month added to some years to make up for the difference between a full year (now known to be about 365.24 days) and a year of just twelve lunar months. The numbers twelve and thirteen came to feature prominently in many cultures, at least partly due to this relationship of months to years. Other early forms of calendars originated in Mesoamerica, particularly in ancient Mayan civilization. These calendars were religiously and astronomically based, with 18 months in a year and 20 days in a month.\n" +
        "Question: Which calendars were among the first to appear?\n" +
        "Answer: Lunar calendars\n"
        ,

    'sst2':
        "Here are three examples. \n" +
        "Sentence: hide new secretions from the parental units. Answer: negative. \n" +
        "Sentence: contains no wit , only labored gags. Answer: negative. \n" +
        "Sentence: that loves its characters and communicates something rather beautiful about human nature. Answer: positive. \n"
        ,
    
    'wnli':
        "Here are three examples. \n" +
        "Sentence 1: I stuck a pin through a carrot. When I pulled the pin out, it had a hole. Sentence 2: The carrot had a hole. Answer: entailment. \n" +
        "Sentence 1: John couldn't see the stage with Billy in front of him because he is so short. Sentence 2: John is so short. Answer: entailment. \n" +
        "Sentence 1: Steve follows Fred's example in everything. He influences him hugely. Sentence 2: Steve influences him hugely. Answer: not_entailment. \n"
        ,
    
    'rte':
        "Here are three examples. \n" +
        "Sentence 1: No Weapons of Mass Destruction Found in Iraq Yet. Sentence 2: Weapons of Mass Destruction Found in Iraq. Answer: not_entailment. \n" +
        "Sentence 1: A place of sorrow, after Pope John Paul II died, became a place of celebration, as Roman Catholic faithful gathered in downtown Chicago to mark the installation of new Pope Benedict XVI. Sentence 2: Pope Benedict XVI is the new leader of the Roman Catholic Church. Answer: entailment. \n" +
        "Sentence 1: Herceptin was already approved to treat the sickest breast cancer patients, and the company said, Monday, it will discuss with federal regulators the possibility of prescribing the drug for more breast cancer patients. Sentence 2: Herceptin can be used to treat breast cancer. Answer: entailment. \n"
        ,
    
    'mnli':
        "Here are three examples. \n" +
        "Premise: Conceptually cream skimming has two basic dimensions - product and geography. Hypothesis: Product and geography are what make cream skimming work. Answer: neutral. \n" +
        "Premise: you know during the season and i guess at at your level uh you lose them to the next level if if they decide to recall the the parent team the Braves decide to call to recall a guy from triple A then a double A guy goes up to replace him and a single A guy goes up to replace him. Hypothesis: You lose the things to the following level if the people recall. Answer: entailment. \n" +
        "Premise: Fun for adults and children. Hypothesis: Fun for only children. Answer: contradiction. \n"
        ,
    
    'cola': 
        "Here are three examples. \n" +
        "Sentence: Our friends won't buy this analysis, let alone the next one we propose. Answer: acceptable. \n" +
        "Sentence: One more pseudo generalization and I'm giving up. Answer: acceptable. \n" +
        "Sentence: They drank the pub. Answer: unacceptable. \n"
        ,
    
    'qqp':
        "Here are three examples. \n" +
        "Question 1: How is the life of a math student? Could you describe your own experiences? Question 2: Which level of prepration is enough for the exam jlpt5? Answer: not_equivalent. \n" +
        "Question 1: How do I control my horny emotions? Question 2: How do you control your horniness? Answer: equivalent. \n" +
        "Question 1: What causes stool color to change to yellow? Question 2: What can cause stool to come out as little balls? Answer: not_equivalent. \n"
        ,
    
    'qnli':
        "Here are three examples. \n" +
        "Question: When did the third Digimon series begin? Context: Unlike the two seasons before it and most of the seasons that followed, Digimon Tamers takes a darker and more realistic approach to its story featuring Digimon who do not reincarnate after their deaths and more complex character development in the original Japanese. Answer: not_entailment. \n" +
        "Question: Which missile batteries often have individual launchers several kilometres from one another? Context: When MANPADS is operated by specialists, batteries may have several dozen teams deploying separately in small sections; self-propelled air defence guns may deploy in pairs. Answer: not_entailment. \n" +
        "Question: What two things does Popper argue Tarski's theory involves in an evaluation of truth? Context: He bases this interpretation on the fact that examples such as the one described above refer to two things: assertions and the facts to which they refer. Answer: entailment. \n"
        ,

    'mrpc':
        "Here are three examples. \n" +
        "Sentence 1: Amrozi accused his brother, whom he called \n" +" the witness \n" +" , of deliberately distorting his evidence. Sentence 2: Referring to him as only \n" +" the witness \n" +" , Amrozi accused his brother of deliberately distorting his evidence. Answer: equivalent. \n" +
        "Sentence 1: Yucaipa owned Dominick 's before selling the chain to Safeway in 1998 for $ 2.5 billion . Sentence 2: Yucaipa bought Dominick 's in 1995 for $ 693 million and sold it to Safeway for $ 1.8 billion in 1998 . Answer: not_equivalent. \n" +
        "Sentence 1: They had published an advertisement on the Internet on June 10 , offering the cargo for sale , he added . Sentence 2: On June 10 , the ship 's owners had published an advertisement on the Internet , offering the explosives for sale . Answer: equivalent. \n"
        ,

    'un_multi':{
        'en-fr':
            "Translate English into French. Here are three examples. \n" +
            "The articles are placed in square brackets as some delegations argued for their deletion. Answer: Les articles sont placés entre crochets étant donné que certains représentants ont estimé qu'ils devraient être supprimés. \n" + 
            "The Statistical Commission continues to circulate relevant extracts of its reports to the secretariats of the other functional commissions. Answer: La Commission de statistique continue de communiquer aux secrétariats des autres commissions techniques les extraits pertinents de ses rapports. \n" +
            "On the contrary, Uzbekistan, in a declaration formulated when becoming a party to the Convention, had stated that confiscation of property as a form of punishment had been removed from its Criminal Code. Answer: À l'inverse, l'Ouzbékistan avait déclaré dans une réserve formulée lorsqu'il est devenu partie à la Convention que la confiscation de biens était exclue de son Code pénal en tant que peine. \n"
            ,
        'de-en':
            "Translate German into English. Here are three examples. \n" +
            "In derselben Resolution erweiterte der Rat das Mandat des mit der Al-Qaida und den Taliban befassten Sanktionsausschusses und legte darüber hinaus den Staaten nahe, die in der Ausschussliste verzeichneten Personen von den über sie verhängten Maßnahmen in Kenntnis zu setzen. Answer: In the same resolution, the Council strengthened the mandate of the Al-Qaida and Taliban Sanctions Committee and also encouraged States to inform listed individuals of the measures imposed on them. \n" + 
            "Solche Strategien umfassen die Erleichterung des Zugangs von Frauen zu potenziellen Käufern ihrer Produkte, unter anderem durch den Aufbau von Genossenschaften, den Einsatz von Informations- und Kommunikationstechnologien, einschließlich des Internet, für den Informationsaustausch und die Abhaltung von Handelsbörsen für ihre Produkte. Answer: Such strategies include facilitating women's access to potential purchasers of their products, through, inter alia, the organization of cooperatives, the use of information and communication technologies — including web sites — for information exchange, and the holding of trading fairs for their products. \n" + 
            "Wir nehmen mit Genugtuung Kenntnis von den Ergebnissen der regionalen Vorbereitungstagungen für den Zehnten Kongress der Vereinten Nationen für Verbrechensverhütung und die Behandlung Straffälliger. Answer: We note with appreciation the results of the regional preparatory meetings for the Tenth United Nations Congress on the Prevention of Crime and the Treatment of Offenders. \n"
            ,

        'de-fr':
            "Here are three examples. \n" +
            "Der endgültige amtliche Wortlaut der Übersetzung erscheint nach eingehender Abstimmung aller Sprachfassungen und redaktioneller Überarbeitung im Offiziellen Protokoll der Generalversammlung bzw. des Sicherheitsrats. Answer: Il encourage les États Membres et les autres entités concernées à apporter des contributions volontaires à l'appui des projets visant au relèvement social et économique du pays. » \n"
            "Ende Juni 2005 verfügte das Amt über insgesamt 194 Stellen, davon 135 im Höheren und 59 im Allgemeinen Dienst. Answer: À la fin juin 2005, le Bureau disposait de 194 postes, dont 135 postes d'administrateur et 59 postes d'agent des services généraux. \n" + 
            "Während der einundsechzigsten Tagung der Generalversammlung führten die Moderatoren umfassende informelle Konsultationen mit verschiedenen Delegationen und Gruppen von Delegationen. Answer: Pendant la soixante et unième session de l'Assemblée générale, les facilitateurs ont tenu des consultations officieuses poussées avec diverses délégations et groupes de délégations. \n"
            ,
    },

    'iwslt': {
        'en-de':
            "Here are three examples. \n" +
            "So the wire heated up slightly,  and its 13,000 amps suddenly encountered electrical resistance. Answer: Dadurch erhitzen sich die Drähte geringfügig und 13-tausend Ampere begegneten plötzlich elektrischem Widerstand. \n" +
            "And the question that I want to ask everybody here today  is are you guys all cool with that idea? Answer: Die Frage, die ich heute jedem hier stellen möchte ist: Ist diese Idee für Sie völlig in Ordnung? \n" +
            "It's a picture of the first beam particle  going all the way around the LHC,  colliding with a piece of the LHC deliberately,  and showering particles into the detector. Answer: Es ist ein Bild des ersten Strahlenpartikels welches die gesamte Strecke um den LHC zurücklegte, dann absichtlich mit einem Teil des LHC kollidierte, um einen Regen von Partikeln auf den Detektor prasseln zu lassen. \n"
            ,
        
        'en-fr':
            "Here are three examples. \n" +
            "This tribe, the Cofan, has 17 varieties of ayahuasca,  all of which they distinguish a great distance in the forest,  all of which are referable to our eye as one species. Answer: Cette tribu, les Cofan, possède 17 variétés de ayahuasca, qu'elle arrive à distinguer de loin dans la forêt, même si à nos yeux, elles semblent être de la même espèce. \n" +
            "Its job is to recreate the conditions  that were present less than a billionth of a second after the universe began,  up to 600 million times a second. Answer: Son travail consiste à recréer les conditions qui étaient présentes moins d'un milliardième de seconde après la naissance de l'univers jusqu'à 600 millions de fois par seconde. \n" +
            "And so this is live on the Web. It's powered by Seadragon. Answer: Et donc c'est en ligne sur le Web. Cela fonctionne avec la technologie Seadragon. \n"
            ,
        
        'de-en':
            "Here are three examples. \n" +
            "In der Tat kann er sich manchmal geradezu paranormal anfühlen. Answer: And, in fact, can sometimes feel downright paranormal. \n" +
            "Wenn sie voneinader umgeben sind, bemerken sie das auch und können etwas nervös werden. Answer: If they get surrounded, they notice that too,  they might get a little flustered. \n" +
            "In Bezug auf Ehe und Familie war einmal die Standardannahme, fast jeder hatte eine und man heiratete so schnell und bekam so schnell Kinder wie man konnte. Answer: With respect to marriage and family,  there was a time when the default assumption that almost everyone had is that you got married as soon as you could,  and then you started having kids as soon as you could. \n"
            ,
        
        'fr-en':
            "Here are three examples. \n" +
            "And even the ones who didn't literally commit suicide  seem to be really undone by their gifts, you know. Answer: Même ceux qui ne se sont pas suicidés semblent avoir été détruits par leur talent. \n" +
            "And the result is -- we call it \"patient autonomy,\"  which makes it sound like a good thing,  but it really is a shifting of the burden and the responsibility  for decision-making from somebody who knows something --  namely, the doctor --  to somebody who knows nothing and is almost certainly sick  and thus not in the best shape to be making decisions --  namely, the patient. Answer: Le résultat, c'est ce qu'on nomme\"l'autonomie du patient\" qui semble être une bonne chose. Mais en réalité, ça déplace le poids de la responsabilité des prises de décision de quelqu'un qui sait -- le docteur -- vers quelqu'un qui n'y connaît rien et est certainement malade- et qui donc n'est pas en état de prendre des décisions -- le patient. \n" +
            "If you want to go far, go together. Answer: Si tu veux aller loin, avance uni. \n"
            ,
    },

    'math': {
        "algebra_linear_1d": [
            {"question": "Solve 24 = 1601*c - 1605*c for c.", "answer":-6},
            {"question": "Solve 657 = -220*t + 1086*t + 22307 for t.", "answer": -25},
            {"question": "Let n(m) = m**3 - 7*m**2 + 13*m - 2. Let j be n(4). Solve 0 = 3*x + j*x + 10 for x.", "answer": -2},
        ],

        "algebra_linear_2d": [
            {"question": "Solve 273*o + 19 = 272*o - 2*t, -2*o + 5*t + 34 = 0 for o.", "answer": -3},
            {"question": "Solve -21 = -5*r - 782*n + 785*n, 4*r - 5*n = 22 for r.", "answer": 3},
            {"question": "Suppose -4*s - 124*v + 125*v = -9, -4 = -s + 2*v. Solve 3*q - s*n = -q, -n = 4*q + 12 for q.", "answer": -2},
        ],

        "algebra_sequence_next_term": [
            {"question": "What is next in -6525, -6520, -6515, -6510?", "answer": -6505},
            {"question": "What is the next term in 144, 519, 1132, 1989, 3096, 4459, 6084, 7977?", "answer": 10144},
            {"question": "What comes next: -7219, -14438, -21643, -28828, -35987, -43114?", "answer": -50203},
        ],

        "arithmetic_addition_sub_multiple": [
            {"question": "Total of 0.06 and -1977321735.", "answer": -1977321734.94},
            {"question": "Add together 2 and 436273715.", "answer": 436273717},
            {"question": "What is 12 + -24 + (-11 - -2)?.", "answer": -21},
        ],

        "arithmetic_mixed": [
            {"question": "Calculate (4/14)/(954/96831).?", "answer": 29},
            {"question": "What is the value of (9/6)/((-2247)/1712)?", "answer": -8/7},
            {"question": "Evaluate 2054/9243 + 22/36.", "answer": 5/6},
        ],

        "arithmetic_mul_div_multiple": [
            {"question": "What is the value of ((-26)/65)/(7/(-280))?", "answer": 16},
            {"question": "What is the value of (-1603)/229*(-10)/7?", "answer": 10},
            {"question": "Calculate 21/(-48)*10524/30695.", "answer": -3/20},
        ],

        "arithmetic_nearest_integer_root": [
            {"question": "What is 922996 to the power of 1/4, to the nearest integer?", "answer": 31},
            {"question": "What is 1453426 to the power of 1/7, to the nearest integer?", "answer": 8},
            {"question": "What is the cube root of 13146210 to the nearest integer?", "answer": 286},
        ],

        "comparison_closest": [
            {"question": "What is the nearest to 5/13 in 0.47, 1, 3/2, 2?", "answer": 0.47},
            {"question": "What is the closest to 0.1 in 2, 0.8, 1, -0.48?", "answer": -0.48},
            {"question": "Let d = -27 - -26.5. Let p be (-3 + 1 + 1)*-1. What is the closest to p in 0.1, -0.3, d?", "answer": 0.1},
        ],

        "comparison_kth_biggest": [
            {"question": "What is the second smallest value in 0.1, 4, 71/44?", "answer": 71/44},
            {"question": "What is the third smallest value in 5, 3, -2/3, -1/4, -44.34?", "answer": -1/4},
            {"question": "What is the second biggest value in -13, -2, 106, -4, 0.4?", "answer": 0.4},
        ],

        "comparison_pair": [
            {"question": "Do 7452/79 and 93 have different values?", "answer": True},
            {"question": "Which is bigger: 309/251 or 0?", "answer": 309/251},
            {"question": "Suppose 4*a + x + 6 = 0, 0 = 4*a - 3*x + 7*x. Let i be a/(-10) - 28/(-35). Let s = i - 3. Is s bigger than -2?", "answer": False},
        ],

        "measurement_conversion": [
            {"question": "ow many months are there in one fifth of a millennium?", "answer": 2400},
            {"question": "What is 23/3 of a day in hours?", "answer": 184},
            {"question": "How many milligrams are there in 50.05692kg?", "answer": 50056920},
        ],

        "numbers_base_conversion": [
            {"question": "What is 62a3 (base 14) in base 7?", "answer": "100363"},
            {"question": "-34862 (base 10) to base 4.", "answer": "-20200232"},
            {"question": "What is 64e (base 16) in base 4?", "answer": "121032"},
        ],

        "numbers_div_remainder": [
            {"question": "Calculate the remainder when 25736 is divided by 144.", "answer": 104},
            {"question": "What is the remainder when 4290 is divided by 1410?", "answer": 60},
            {"question": "Suppose 0 = 2*s - 2 + 20. Let y be 267/9 - 3/s. Suppose 5*w + o = y, -w + 2*o + 2*o = -27. Calculate the remainder when 13 is divided by w.", "answer": 6},
        ],

        "numbers_gcd": [
            {"question": "What is the greatest common factor of 56 and 38094?", "answer": 14},
            {"question": "Calculate the highest common divisor of 2838 and 8184.", "answer": 66},
            {"question": "Calculate the greatest common divisor of 19886 and 5978.", "answer": 122},
        ],

        "numbers_is_factor": [
            {"question": "Is 72567 a multiple of 9?", "answer": True},
            {"question": "Is 91 a factor of 1012773?", "answer": False},
            {"question": "Let d = -588 + 1274. Is 14 a factor of d?", "answer": True},
        ],

        "number_is_prime":  [
            {"question": "Is 256975613 composite?Is 9609827 prime?", "answer": True},
            {"question": "Is 11280553 a composite number?", "answer": True},
            {"question": "Let u = -15 - -16. Suppose -2 = -d + u. Suppose -w = -d*p + 705 + 530, 4*p + 2*w - 1660 = 0. Is p composite?", "answer": True},
        ],

        "numbers_lcm": [
            {"question": "What is the smallest common multiple of 19360 and 880?", "answer": 19360},
            {"question": "What is the smallest common multiple of 2178 and 44?", "answer": 4356},
            {"question": "Let n(m) = -m**2 - 6*m - 6. Let i be n(-4). Suppose -7 + 1 = -3*z. Suppose 3*h - 12 = -z*s + h, 2 = i*h. Calculate the smallest common multiple of 4 and s.", "answer": 20},
        ],

        "numbers_place_value": [
            {"question": "What is the units digit of 80577?", "answer": 7},
            {"question": "What is the hundred thousands digit of 393392?", "answer": 3},
            {"question": "Let s be -2 + (-2)/(-1 - -2). Let g(b) = 3*b**2 - b + 5. What is the units digit of g(s)?", "answer": 7},
        ],

        "numbers_round_number":[
            {"question": "Round 1.72315 to two decimal places.", "answer": 1.72},
            {"question": "Round 49.26661 to the nearest ten.", "answer": 50},
            {"question": "Let x = 114 - 80. Let h = x + 34. Let b = h - 68.0058. What is b rounded to 3 decimal places?", "answer": -0.006},
        ],

        "polynomials_evaluate": [
            {"question": "Let z(p) = -18*p - 920. Give z(-35).", "answer": -290},
            {"question": "Let l(h) = -h**3 - 33*h**2 - 42*h + 99. Determine l(-31).", "answer": -521},
            {"question": "Let l(g) be the third derivative of g**8/20160 + g**7/2520 + g**5/30 + 23*g**2. Let m(f) be the third derivative of l(f). What is m(-3)?", "answer": 3},
        ],
    }
}