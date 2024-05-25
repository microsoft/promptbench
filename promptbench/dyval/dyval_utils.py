# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import re

def round_value(val):
    """
    Rounds a numerical value to 8 decimal places.

    Parameters:
    -----------
    val : float or str
        The value to be rounded.

    Returns:
    --------
    str
        The rounded value as a string.
    """
    return str(round(float(val), 8))


def dyval_evaluate(dataset_type, preds, gts):
    """
    Evaluates predictions against ground truths for different dataset types.

    Parameters:
    -----------
    dataset_type : str
        The type of dataset (e.g., 'arithmetic', 'max_sum_path').
    preds : list
        A list of predictions.
    gts : list
        A list of ground truths.

    Returns:
    --------
    float
        The accuracy of predictions as a proportion of correct answers.
    """
    correct = 0
    total = len(gts)
    
    if dataset_type in ["arithmetic", "max_sum_path"]:
        for pred, gt in zip(preds, gts):
            # gt is str ("N/A")
            if isinstance(gt, str):
                if gt == pred:
                    correct += 1
            else:
                try:
                    pred = float(pred)
                    if abs(gt - pred) / (abs(gt) + 1e-7) < 0.0001:
                        correct += 1

                except ValueError:
                    continue
    
    elif dataset_type == "linear_equation":
        print("linear equation")
        for pred, gt in zip(preds, gts):
            # gt is tuple (x, y)
            print("pred ", pred)
            print("gt ", gt)
            xy = pred.split(" ")
            if len(xy) != 2:
                continue
            else:
                x, y = xy[0], xy[1]
                try:
                    x, y = float(x), float(y)
                    if abs(x - gt[0]) / (abs(gt[0]) + 1e-7) < 0.001 and abs(y - gt[1]) / (abs(gt[1]) + 1e-7) < 0.001:
                        correct += 1
                        print("correct")
                        print()
                except ValueError:
                    continue
    
    elif dataset_type in ["bool_logic", "deductive_logic", "abductive_logic", "reachability"]:
        for pred, gt in zip(preds, gts):
            # gt is bool
            pred = pred.strip().lower()
            print("pred ", pred)
            print("gt ", gt)
            if isinstance(gt, bool):
                if pred == "true" and gt == True:
                    print("correct\n")
                    correct += 1
                elif pred == "false" and gt == False:
                    print("correct\n")
                    correct += 1
            elif isinstance(gt, str):
                if pred == gt.lower():
                    print("correct\n")
                    correct += 1

    return correct/total


def process_dyval_inputs(prompt, dataset):
    """
    Processes inputs for dynamic value (DyVal) dataset.

    Parameters:
    -----------
    prompt : str
        The prompt template to be formatted.
    dataset : DyValDataset
        The dataset containing descriptions and other relevant data.

    Returns:
    --------
    dict
        A dictionary of processed inputs organized by order.
    """
    descriptions = {}
    dataset_type = dataset.dataset_type

    raw_descriptions = dataset.data["descriptions"]
    for order, input_texts in raw_descriptions.items():
        if dataset_type in ["arithmetic", "bool_logic", "deductive_logic"]:
            vars = dataset.data["vars"]
            inputs = [prompt.format(input_text, var) for input_text, var in zip(input_texts, vars)]
        elif dataset_type in ["linear_equation", "abductive_logic", "reachability", "max_sum_path"]:
            inputs = [prompt.format(input_text) for input_text in input_texts]
                    
        descriptions[order] = inputs
    
    return descriptions

def process_dyval_training_sample(sample, dataset_type):

    prompt = DYVAL_PROMPTS[dataset_type][0]
    # for order, input_text in sample["descriptions"].items():
    #     if dataset_type in ["arithmetic", "bool_logic", "deductive_logic"]:
    #         var = sample["vars"]
    #         problem = prompt.format(descriptions=input_text, vars=var)
    #     else:
    #         problem = prompt.format(descriptions=input_text)
                    
    #     sample["descriptions"][order] = problem

    input_text = sample["descriptions"]["topological"]
    
    final_response = "\n\nThus, the answer is <<<"
    answer = sample["answers"]
    if dataset_type in ["arithmetic", "bool_logic", "deductive_logic"]:
        var = sample['vars']
        problem = prompt.format(descriptions=input_text, vars=var)
        if dataset_type == "arithmetic":
            final_response += str(round_value(answer)) + ">>>"
        else:
            final_response += str(answer) + ">>>"
        
    else:
        problem = prompt.format(descriptions=input_text)
        
        if dataset_type == "linear_equation":
            final_response += str(round_value(answer[0])) + " " + str(round_value(answer[1])) + ">>>"
        elif dataset_type == "max_sum_path":
            if type(answer) == str:
                final_response += str(answer) + ">>>"
            else:
                final_response += str(round_value(answer)) + ">>>"
        else:
            final_response += str(answer) + ">>>"

    sample["inferences"] = sample["inferences"] + final_response
    
    return sample

def process_dyval_preds(raw_pred):
    """
    Processes the raw prediction string to extract the predicted value.

    Parameters:
    -----------
    raw_pred : str
        The raw prediction string.

    Returns:
    --------
    str
        The extracted prediction.
    """
    raw_pred = raw_pred.replace(',', '')
    pred = ""
    match = re.search('<<<(.*?)>>>', raw_pred)
    if match:
        pred = match.group(1).strip()

    return pred


DYVAL_PROMPTS = {
    "arithmetic": [
        "Here is a description of an arithmetic problem:\n{descriptions}\nCompute the result of {vars}. If the solution cannot be calculated, answer 'N/A'. Ensure your result is within a relative precision of 0.0001 (or 0.01%) compared to the ground truth value. Ensure your final result begins with '<<<' and ends with '>>>', for example, if the answer is 1, your final result should be <<<1>>>."
    ],
    
    "linear_equation": [
        "Given the following linear equation system with two variables:\n{descriptions}\nDetermine the values of x and y. Ensure your results are within a relative precision of 0.001 (or 0.1%) compared to the ground truth values. Your response should be formatted as: <<<x's value y's value>>>, e.g., if x=1 and y=2, then it should be <<<1 2>>>",
    ],

    "bool_logic": [
        "Here is a description of a boolean logic problem:\n{descriptions}\nCompute the result of {vars}. If the solution can not be calculated, answer 'N/A'. Ensure your final result begins with '<<<' and ends with '>>>', for example, if the answer is True, your final result should be <<<True>>>.",
    ],

    "deductive_logic": [
        "Here is a description of a deductive logic problem:\n{descriptions}\nThe symbol '->' represents a deductive relationship, e.g., A -> B implies that if A is true, then B is true. If A is false, B's truth value remains undetermined (N/A). Deduce the result of {vars}. If the solution can not be deduced, answer 'N/A'. Ensure your final result begins with '<<<' and ends with '>>>', for example, if the answer is True, your final result should be <<<True>>>.",
    ],

    "abductive_logic": [
        "Here is a description of an abductive logic problem:{descriptions}\nThe symbol '->' represents a deductive relationship, e.g., A -> B implies that if B is false, then A is false. If B is true, A's truth value remains undetermined (N/A). If the solution can not be abduced, answer 'N/A'. Ensure your final result begins with '<<<' and ends with '>>>', for example, if the answer is True, your final result should be <<<True>>>.",
    ],

    "reachability": [
        "Given a directed graph:\n{descriptions}\nRespond with either '<<<True>>>' if reachable, or '<<<False>>>' otherwise.",
    ],

    "max_sum_path": [
        "Given a directed graph with values assigned to each node:\n{descriptions}\nFor exmaple, the value of the path A->B->C is obtained by summing the values of nodes A, B, and C. Please format your response as <<<Answer>>>. For example, if the answer is 1, it should be presented as <<<1>>>.",
    ],

}


LEAST2MOST_EXAMPLES = {
    "arithmetic": [
"""
Q:
Here is a description of an arithmetic problem:
The value of abn is 2.
abk gets its value by taking the square root of the value that abj has.
The value of abm is 2.
The value of abe is 2.
abo gets its value by adding together the value of abm and abn.
abj gets its value by adding together the value of abh and abi and abf.
abf gets its value by dividing the value of abd by the product of the values of abe and abh.
abl gets its value by dividing the value of abg by the product of the values of abk and abe.
abg gets its value by multiplying together the value of abc and abf and abe.
The value of abd is 6.
abc gets its value by squaring the value that aaz has.
The value of abi is 10.
The value of aaz is 4.
The value of abh is 8.
Compute the result of abl. If the solution cannot be calculated, answer 'N/A'. Ensure your result is within a relative precision of 0.0001 (or 0.01%) compared to the ground truth value. Ensure your final result begins with '<<<' and ends with '>>>', for example, if the answer is 1, your final result should be <<<1>>>.

A:
Let's break down this problem:
1. Find abc using aaz
2. Find abf using abd, abe, and abh
3. Find abg using abc, abf, and abe
4. Find abj using abh, abi, and abf
5. Find abk using abj
6. Find abl using abg, abk, and abe


1. Find abc using aaz
abc = aaz^2
Using the given value, abc = 4^2 = 16

2. Find abf using abd, abe, and abh
abf = abd / (abe * abh)
Using the given values, abf = 6 / (2 * 8) = 6/16 = 0.375

3. Find abg using abc, abf, and abe
abg = abc * abf * abe
Using the found value of abc and given values: abg = 16 * 0.375 * 2 = 6 * 2 = 12

4. Find abj using abh, abi, and abf
abj = abh + abi + abf
Using the given values and the found value of abf: abj = 8 + 10 + 0.375 = 18.375

5. Find abk using abj
abk = sqrt(abj)
Using the found value of abj: abk = sqrt(18.375) ~= 4.287

6. Find abl using abg, abk, and abe
abl = abg / (abk * abe)
Using the found values: abl = abg / (abk * abe) = 12 / (4.287 * 2) = 12 / 8.574 ~= 1.400

Given this breakdown, the result of abl is approximately:
<<<1.400>>>
""",
],
    "linear_equation": [
"""
Q:
Given the following linear equation system with two variables:

8 x + 0 y = 3
aae0 x + 4 y = -9

The calculation of aae0 is defined as:
The value of aac0 is 3.
aad0 gets its value by taking the square root of the value that aac0 has.
The value of aaa0 is 1.
aab0 gets its value by squaring the value that aaa0 has.
aae0 gets its value by adding together the value of aab0 and aad0.

Determine the values of x and y. Ensure your results are within a relative precision of 0.001 (or 0.1%) compared to the ground truth values. Your response should be formatted as: <<<x's value y's value>>>, e.g., if x=1 and y=2, then it should be <<<1 2>>>

A:
Let's first break down the problem into summary steps, and then we'll solve each step.

1. Calculate the value of aae0.
2. Solve for x using the first equation.
3. Solve for y by substituting x's value into the second equation.
4. State the final solution for x and y.

Detailed Steps:

1. Calculate aae0:
	The value of aac0 is 3.
	Find aad0 by taking the square root of aac0, which gives: aad0 = sqrt(3).
	Given that aaa0 is 1, square it to find aab0. This results in aab0 = 1.
	Calculate aae0 by adding aad0 and aab0, giving: aae0 = 1 + sqrt(3).

2. Solve for x:

	Given the linear system:

	8x+0y=3
	(1+sqrt(3))x+4y=−9

	we can determine: x=3/8=0.375

3. Solve for y:
	Use the derived x value and the given value of aae0 in the equation "(1 + sqrt(3))x + 4y = -9".
	By solving this, you'll find that y is approximately -2.506125.


4. State the final solution for x and y:
The value for x is 0.375, and the value for y is approximately -2.506125. So the answer <<<0.375 -2.506>>>.
"""
],
    "deductive_logic": [
"""
Q:
Here is a description of a deductive logic problem:
aar is True.
aan is False.
aah is False.
aai is False.
(aah and aai) -> aaj.
aaa is False.
aae is False.
aad is False.
(aad or aae) -> aaf.
aas is True.
aak is True.
(aak or aan) -> aao.
(aaj or aao) -> aap.
aab is True.
(aaa or aab) -> aac.
(aac or aaf) -> aag.
(aar and aas) -> aat.
(aag or aap) -> aaq.
The symbol '->' represents a deductive relationship, e.g., A -> B implies that if A is true, then B is true. If A is false, B's truth value remains undetermined (N/A). Deduce the result of aaq. If the solution can not be deduced, answer 'N/A'. Ensure your final result begins with '<<<' and ends with '>>>', for example, if the answer is True, your final result should be <<<True>>>.

A:
Let's break down the problem step by step to deduce the result of aaq.

1. Analyze Initial Values: Begin with the stated truths and falsehoods for the variables. These are our initial conditions.
2. Process Deductive Relationships: Use the given deductive relationships (implications) to determine the truth values of other variables.
3. Deduce aaq: Based on the earlier steps, determine the value of aaq.

1. Analyze Initial Values:
	- aar: True
	- aan: False
	- aah: False
	- aai: False
	- aaa: False
	- aae: False
	- aad: False
	- aas: True
	- aak: True
	- aab: True

2. Process Deductive Relationships:

	a. (aah AND aai) -> aaj:

	- Since both aah and aai are False, the implication does not determine the truth value of aaj. So, aaj is N/A.

	b. (aad OR aae) -> aaf:

	- Since both aad and aae are False, the implication does not determine the truth value of aaf. So, aaf is N/A.

	c. (aak OR aan) -> aao:

	- Since aak is True, the implication makes aao True.

	d. (aaj OR aao) -> aap:

	- We know aao is True, hence aap is also True.

	e. (aaa OR aab) -> aac:

	- Since aab is True, aac is also True.

	f. (aac OR aaf) -> aag:

	- We know aac is True, hence aag is also True.

	g. (aar AND aas) -> aat:

	- Both aar and aas are True, hence aat is also True.

3. Deduce aaq:

	(aag OR aap) -> aaq:

	- As both aag and aap are True, aaq is also True.


Final result for aaq is True.

So, the solution is: <<<True>>>
"""
],
    "abductive_logic": [
"""
Q:
Here is a description of an abductive logic problem:
(aad or aae) -> aaf.
(aaj or aao) -> aap.
(aaa or aab) -> aac.
(aar or aas) -> aat.
(aag or aap) -> aaq.
(aah or aai) -> aaj.
(aac or aaf) -> aag.
(aak or aan) -> aao.
Given aaq is False, what is the value of aaa?

A:
Let's break down the problem step by step to abduce the result of aaa.
1. Analyze Given Value: Understand the implication of aan being False.
2. Reverse Process the Deductive Relationships: Work backward from the implications to deduce possible truths and falsehoods of related variables.
3. Determine the Value of aaa: By reverse-processing the implications, deduce the value of aaa.

1. Analyze Given Value:
    aaq is False

2. Reverse Process the Deductive Relationships:

(aag OR aap) -> aaq = False.
Given aaq is False, the value of premise (aag OR aap) is False, thus, the value of aag is abduced as False.

(aac OR aaf) -> aag = False.
Given aag is False, the value of premise (aac OR aaf) is False, thus, the value of aac is abduced as False.

3. Determine the Value of aaa:

(aaa OR aab) -> aac = False.
Given aac is False, the value of premise (aaa OR aab) is False, thus, the value of aaa is abduced as False.

Thus, the answer is: <<<False>>>.
"""
],
    "reachability": [
"""
Q:
Given a directed graph:
aad points to: (aaf).
aaf points to: (None).
aae points to: (aad).
aab points to: (aae).
aaa points to: (aae).
aac points to: (aag, aab).
aag points to: (aae).
Can aaa be reached starting from aag?
Respond with either '<<<True>>>' if reachable, or '<<<False>>>' otherwise.

A:
To determine if aaa can be reached starting from aag, we can decompose the solution into the following steps:

1. Identify Direct Paths from Starting Node:
Firstly, list all the nodes that aag directly points to.

From the given graph:
aag points to: aae.

2. Recursive Path Exploration:
Explore all paths reachable from the nodes that aag directly points to and check if aaa is among them.

2.1 Path via aae:
aag -> aae:
aae points to: aad.
2.2 Path via aad:
aag -> aae -> aad:
aad points to: aaf.
2.3 Path via aaf:
aag -> aae -> aad -> aaf:
aaf points to None, which means this path terminates without reaching aaa.
3. Conclusion:
After exploring all paths starting from aag, we did not find a path that leads to aaa.

Thus, the answer is:

<<<False>>>
"""
],
    "max_sum_path": [
"""
Q:
Given a directed graph with values assigned to each node:
aac points to: (aae, aaa, aag).
aaf points to: (aad, aae).
aaa points to: (aab, aaf, aad).
aad points to: (aag).
aab points to: (aaf, aae, aad).
aag points to: (None).
aae points to: (aad).
The value of aaa is 9
The value of aag is 3
The value of aae is 7
The value of aab is 10
The value of aaf is 5
The value of aac is 6
The value of aad is 1
What's the maximum sum path from aab to aag?
For exmaple, the value of the path A->B->C is obtained by summing the values of nodes A, B, and C. Please format your response as <<<Answer>>>. For example, if the answer is 1, it should be presented as <<<1>>>.

A:
Let's decompose the solution to find the maximum sum path from aab to aag into several steps:

1. Identify Direct Paths from Starting Node:
Start by listing all the nodes aab directly points to.

From the given graph:
aab points to: aaf, aae, aad.

2. Recursive Path Exploration:
For each node that aab points to, recursively find all paths that lead to aag.

2.1. Path via aaf:
aab -> aaf:
aaf points to: aad, aae.
Through aad:
aab -> aaf -> aad -> aag: Sum = 10 + 5 + 1 + 3 = 19
Through aae:
aab -> aaf -> aae -> aad -> aag: Sum = 10 + 5 + 7 + 1 + 3 = 26
2.2. Path via aae:
aab -> aae:
aae points to: aad.
Through aad:
aab -> aae -> aad -> aag: Sum = 10 + 7 + 1 + 3 = 21
2.3. Path via aad:
aab -> aad:
aad points directly to aag.

aab -> aad -> aag: Sum = 10 + 1 + 3 = 14

3. Compare Path Values:
After identifying all paths from aab to aag, compare their sums to find the maximum:

aab -> aaf -> aad -> aag: 19
aab -> aaf -> aae -> aad -> aag: 26
aab -> aae -> aad -> aag: 21
aab -> aad -> aag: 14
From the comparison, the path aab -> aaf -> aae -> aad -> aag provides the maximum sum of 26.

4. Conclusion:
The maximum sum path from aab to aag is <<<26>>>.
"""
],

}


APE_PROMPTS = {
    "arithmetic":[
        # "To calculate the requested value, follow the steps provided in the input. Each step provides a calculation or a value assignment you need to perform in order to find the final value. Make sure to perform the calculations in the order they are given. Use the specific arithmetic operations mentioned in each step (such as dividing, adding, squaring, or multiplying). Consider each input as a separate calculation task and don't mix values or operations from different inputs. After you complete all the steps in an input, you should have the final value. For the output, write down every step of your calculation, rounding to at least 8 decimal places if needed, and mark the final value.",
        # "For each of the given statements, calculate the value of the corresponding letter combinations according to the instructions provided. If a calculation requires the use of previous values, make sure to use the most recent value. For the final value requested, provide a precise decimal output.",
        # "To calculate the desired value, follow the mathematical operations given in the instructions for each variable. The operations include addition, subtraction, multiplication, division, and the square root. Perform each operation in the order they are given, using the values provided for each variable.",
        # "Read the given scenario and use the information to calculate the requested value. Each described operation corresponds to a mathematical operation. Use the order of the operations described and the values given to calculate the requested output.",
        # "To calculate the final variable (mentioned last in each input), use the provided equations and given values. Use the given relationships between variables to calculate missing values, keep in mind that operations should follow the appropriate order of operations: parentheses, exponents, multiplication and division (from left to right), addition and subtraction (from left to right).",
        # "to calculate the value of the given variable using the provided equations and variables' values.",
        # "To solve each problem, compute the value of each variable in the order mentioned in the problem, using the provided equations. Then, give the value of the final variable asked for.",
        # "Take the given inputs and follow the operations outlined to calculate the value of the final variable in the list. The operations include addition, subtraction, multiplication, division, and taking the square root. Use the corresponding values and perform the operations as they are given in the input. The output should be the value of the final variable after all operations have been performed.",
        # "Follow the order of the given statements to calculate the values of different variables. Perform the necessary mathematical operations as mentioned in each statement. Once all the values are obtained, provide the value of the variable asked in the last statement of each input.",
        # "First, identify all the given values for variables in the input. Then, use these given values for the variables to calculate the value of the other variables according to the instructions given in the input. For example, if a variable gets its value by adding together two other variables, add the values of those two variables to get the value of the first variable. Continue in this way until you have found the value of the variable that the question at the end of the input asks for. Give this value as the answer.",
        # "Perform the given operations for each variable and find the value of the variable specified at the end of each input.",
        # "To calculate the value of the specified variable by performing the given mathematical operations. The operations may involve adding, subtracting, multiplying, dividing, or taking the square root of other variables.",
        # "Assign the values to the given variables according to the instruction. Then perform the specified operations. Calculate and write down the final value asked for in the question.",
        # "To calculate the value of each variable using given expressions and values, following the order and operations as mentioned, and then use these calculated values to determine the value of the final variable asked in the question.",
        # "Follow the given equations to figure out the values of the different variables. When all variables have been computed, answer the final question.",
        # "Calculate the value of the final variable based on the given inputs and their relationships. Following each relationship, if a variable uses other variables for its value, compute those first. Ensure to follow the order of operations in mathematics (parentheses, exponents, multiplication and division, addition and subtraction).",
        # "To calculate the values of the given variables based on the operations specified in the instructions, and then use these calculated values to find the final value of the specified variable.",
        "Calculate the value of the final variable in the given instructions by following the mathematical operations, such as addition, subtraction, multiplication, division or square root, defined in the instructions. Use the given values of the variables in the instructions.",
        # "For each input, assign each variable their given value or calculate their value based on the mathematical operations stated (i.e., addition, subtraction, multiplication, division, or square root). Compute the solution for the final asked variable using these values.",
        # "Decipher the value relationships between the 'aa' variables in the input and compute the value of the last 'aa' variable listed.",
    ],

    "linear_equation":[
        # "To find the values of x and y, first calculate the value of the variable(s) defined in the statement. This involves determining the values of the defined variables and performing the specified operations such as multiplication, subtraction, squaring etc. Once the value of these variables is determined, it's used to solve the linear equations.",
        # "to solve the given system of linear equations, where certain variables in the equations were defined by a set of additional instructions. The variable definitions included operations such as multiplication, division, subtraction, squaring, and summation, and involved both simple numbers and other defined variables. After finding the values of these defined variables, they were substituted into the original linear equations, and two equations with two variables were obtained. The two-variable system of equations was then solved using substitution or elimination method to find the values of the variables x and y.",
        # "Solve the linear equations given, where certain coefficients are represented by different variables. The value of these variables are either given directly or are calculated based on the given definition. Use the calculated values of the variables to find the values of x and y.",
        # "to solve the system of linear equations where one equation includes a variable (aad0 or aan0 or aaf0) which value is defined by a sequence of arithmetic and algebraic operations on defined constants (aaa0, aab0, etc.). The solution should be the pair of values for x and y that satisfy both equations.",
        # "First, solve the coefficients of the linear equation using the provided calculations. Then, solve the linear equation system using the calculated coefficients to find the values of x and y.",
        # "To solve each set of linear equations, first compute the value of the variable in the equations that is defined by a series of mathematical operations. Once you have this value, substitute it into the equation and solve the system of equations to find the values of x and y. The methods for solving the system of equations include the elimination method, substitution method, or matrix method depending on which is suitable.",
        # "For each given set of linear equations, first solve for the value of the given coefficient which has been defined using specific calculations. Then, use these known values to solve the linear equations and find the values of x and y.",
        # "First, calculate the value of aad0 or aan0 or aaf0 according to the given instructions and substitute it into the corresponding equation. Then, solve the system of two linear equations using elimination method to find the values of x and y.",
        # "to find the values of x and y by solving the system of linear equations. First, calculate the coefficients (if any) according to the given instructions. Then, use these coefficients to transform the equations. After this, use elimination method to solve for the variables. After finding one variable, substitute it into one of the original equations to find the other variable.",
        # "For each set of equations provided, calculate the value of the defined variables and use them to solve for x and y in the set of equations.",
        # "To compute the value of x and y, first calculate the value of the defined variable (aad0 or aan0 or aaf0). Then substitute this value into the equations provided and solve the system of equations for the values of x and y.",
        # "First, calculate the value of aad0 or aan0 or aaf0 based on the given instructions. Then, use these values to create two systems of linear equations with 'x' and 'y' as variables. Use substitution or elimination methods to solve the system and find the values of 'x' and 'y'. If the coefficients of 'y' are not the same in both equations, multiply the equations by appropriate factors to make them the same. Subtract one equation from the other to isolate 'x', then substitute 'x' into one equation to solve for 'y'.",
        # "To solve for x and y in the given system of linear equations, first compute the value of the variable(s) described in the definitions using the given equations. Coordinate the equations so that either x or y can be eliminated when the two equations are subtracted. Find the value of the remaining variable. Substitute this value back into one of the original equations to find the value of the other variable.",
        # "To solve each equation, first calculate the value of the variable 'aad0' or 'aan0' or 'aaf0' using the provided definitions. Then, substitute the calculated value into the original linear equation to find the values of x and y.",
        # "to determine the values of x and y for each given set of equations, considering the given calculations defined for variables such as aan0, aad0, and aaf0.",
        # "Given a set of two linear equations where one or more coefficients are defined by mathematical operations, first resolve the mathematical operations to find the calculated coefficients. Then use a method of substitution or elimination to solve this system of equations to find the values of x and y.",
        # "Solve the given system of linear equations, substituting the specific formulas and values given for the variables within those equations.",
        "to calculate the values of x and y given a set of linear equations and additional instructions on how to calculate some of the constants used in these equations.",
        # "For each set of inputs, first calculate the values of the various variables as defined by the input instructions. Then, substitute these variables into the given equations to form a system of linear equations. Solve this system of equations to find the values of x and y.",
        # "To calculate the value of the variable in the equations given and the variables 'aaa0', 'aab0', 'aac0', 'aad0', 'aae', 'aaf', 'aag', 'aah0', 'aai0', 'aaj0', 'aak0', 'aal0', 'aan0', 'aap', 'aaq' as well as 'aaf0' if they are provided. Then substitute the calculated values back into the original equations to solve for 'x' and 'y'",
    ],

    "deductive_logic":[
        # "Deduce the value of the final variable based on the given logical statements and variable values. If a variable's value can't be certainly determined, set its value to N/A.",
        # "To figure out the value of the final input, follow the logic of each statement. If a value can't be deduced from a statement due to a previous value being N/A or not given, set its value as N/A. Otherwise, use standard logic operations (AND, OR, NOT) to determine the value. Provide the final value as the output. If the final value can't be deduced, output N/A.",
        # "To evaluate a series of boolean statements and deduce the value of a specified variable. If the value can't be deduced from the given inputs, mark it as N/A.",
        # "To interpret the logical expressions and determine the value of the specified variable. When the value of a variable is N/A or cannot be deduced from the given information, set it to N/A. If a logical operation involves at least one N/A, its result is also N/A except for 'OR' operation where if one of the operands is True, the result is True.",
        # "To determine the value of the requested variable, follow the logical operations provided in each statement. If a variable's value cannot be deduced from the provided statements, label it N/A. Use 'True' and 'False' as the only possible values and the logical operators 'AND' and 'OR' as operations. The 'NOT' operator is used to reverse the value of a variable.",
        # "To solve for the value of a given variable, evaluate the logical statements leading up to it, using the provided true/false values. If a statement cannot be logically determined due to missing or undefined values, set the value of the variable to N/A.",
        # "Given a set of logical propositions and a target value, evaluate the propositions in order to deduce the value of the target. If at any point the value of a proposition cannot be deduced due to insufficiency of information or inconsistency in the given information, set the value of the proposition as N/A (Not Available). An OR operation between any proposition and True results in True whereas an AND operation with N/A results in N/A. A NOT operation on N/A also results in N/A. Finally, provide the deduced value of the target or N/A if the value could not be deduced.",
        # "Use the rules of propositional logic to evaluate the value of the specified variable given the input statements. If the value of a variable cannot be determined due to insufficient or contradictory information, assign it a value of N/A.",
        # "To evaluate a given logical expression, first determine the values of the individual variables. If a variable's value cannot be established based on the provided information, label its value as N/A. Then, use these values to evaluate each of the compound expressions. If an expression contains a variable with a value of N/A and the value of the expression cannot be deduced despite this, label the expression's value as N/A. Otherwise, follow normal logical rules to establish the expression's value. Your output should be the value of the specified variable or expression.",
        # "To evaluate the logical value of a given variable using the logical inputs given. \
        # You'll be given a series of logical statements including 'or', 'and', and 'not'. \
        # Start by identifying the given variable values. Then, use these known values to evaluate the logical statements given. \
        # If any logical inputs result in ambiguous or non-deductible outcomes, assign the variable result as ’N/A'.",
        # "to evaluate the logic statements given as inputs and determine the value of the specified variable. The logic statements use Boolean logic and the variables can take values of either True, False, or N/A if the value can't be deduced from the given statements.",
        # "For each input, list all the variables with their respective values (True, False, or N/A). Then, for each logic operation in the input, calculate the result based on the values of the variables. If the result cannot be deduced due to a variable being N/A, set the result of that operation to N/A. Finally, the output will be the value of the specified variable.",
        # "Given a set of logical statements, determine the truth value of the specified variable. If the value cannot be definitively deduced due to incomplete or ambiguous information, the answer is N/A.",
        # "To determine the value of the variable in question, follow the logical sequence provided by the inputs. Treat each input as a boolean statement, where 'True' and 'False' are logical values, and 'N/A' is used when a value cannot be deduced based on the provided information. Apply logical operations (AND, OR, NOT) accordingly. If the value of a variable is not directly provided, it must be deduced from the boolean operations. 'AND' operation returns True if both values are True, and False otherwise. 'OR' operation returns True if at least one of the values is True, and False otherwise. The 'NOT' operation returns the opposite of the given value. However, if the value could not be deduced, return the output 'N/A'.",
        # "To evaluate each expression as a boolean logic operation. For Boolean AND operations, if both inputs are 'True', then result is 'True', if at least one input is 'False', then result cannot be deduced and is set to 'N/A'. For Boolean OR operations, if at least one input is 'True', then the result is 'True', if both inputs are 'False', then the result cannot be deduced and set to 'N/A'. For NOT operations, if the input is 'True' then the result is 'False' and vice versa, if the input is 'N/A' then the result cannot be deduced and is set to 'N/A'. We need to evaluate the expressions sequentially and use the results of the previous operations to evaluate the next ones. The output is the result of the last operation.",
        # "To find the value of the specific variable, follow the logical statements provided. If the value of a variable is explicitly mentioned, use that value. If the value is not mentioned, but a logical statement that relates it to other variables is provided, use logical deduction to find its value. \
        # A logical statement has two elements: a premise and an implication. The premise is a logical operation (AND, OR, NOT) involving one or more variables. The implication is a result that depends on the value of the premise. \
        # For an AND operation, if both elements are True, the result is True. If at least one of them is False, the result is False. If the value of at least one element is not provided (N/A), the result cannot be deduced and is considered N/A. \
        # For an OR operation, if at least one element is True, the result is True. If both elements are False, the result is False. If the value of at least one element is not provided (N/A), and the other element is False, the result cannot be deduced and is considered N/A. However, if one element is True, the result is True regardless of the other element. \
        # For a NOT operation, if the element is True, the result is False, and vice versa. If the value of the element is not provided (N/A), the result cannot be deduced and is considered N/A. \
        # After performing all possible logical deductions, if you still cannot find the value of the specified variable, consider its value as N/A. \
        # Write the value of the specified variable as the final output.",
        # "To solve for the value of the given variable, follow the logical implications provided. If a variable's value cannot be deduced due to a lack of information or an undefined premise, mark the variable's value as N/A. When solving for a compound statement, if at least one the variables is N/A, then the output of the compound statement is also N/A, unless the operation is OR and the other value is true, in which case the output is true. Give the value of the given variable as the final output.",
        # "To evaluate the given logical expressions and determine the final output. If a variable can't be evaluated because of an undetermined value, set it as 'N/A'.",
        # "To determine the value of the specified variable, follow the logic from given input statements. If a premise cannot be determined due to a lack of information about one or more of its contributing variables, the value of the variable cannot be deduced and is set to N/A.",
        "To evaluate the boolean logic of each statement, following the order given. Treat statements as premises and consequents, where the result of the premise determines the value of the consequent. If the premise is True, the consequent also is True. If the premise is False or can not be deduced due to undefined values in any part of its expression, the value of the consequent also cannot be deduced and is set to N/A. Respond with the value of the specified variable after analyzing all input statements.",
    ],

    "abductive_logic":[
        # "To determine the value of the given variable, follow the chain of logic from the given variable towards the queried variable. This will be done through a process of logical abduction where the relationships provided by the inputs are used to determine the value. If the output value is False, then the value of the corresponding inputs is abduced as False. If the output value is True, then the value of the corresponding inputs is abduced as True. If an exact value cannot be determined, then the value is abduced as N/A.",
        # "To solve for the variable asked for: \
        # 1. Begin with the input-output pair with 'Given' to set initial values. \
        # 2. Use those initial values in the next relevant input-output pair (which contains one of those initial variables). \
        # 3. Use the principles of logical operators to solve for the variable in question: \
        # (a) If 'A or B' is False, then both A and B must be False.\
        # (b) If 'NOT A' is False, then A must be True.\
        # 4. Repeat steps 2 and 3 until you have found the value of the variable asked for.",
        # "To determine the value of the variable in question, use a type of reasoning known as abductive reasoning. This means making a plausible assumption based on the available evidence. In this case, the evidence is the given input-output pairs. First, consider the input-output pair that contains the variable given as False. From that pair, deduce the value of the left-hand side of the premise. Then, find the input-output pair containing that deduced value, and abduce the value of the required variable. If at any point it is not possible to make a deduction, set the value of the variable as 'N/A'.",
        # "To determine the value of a given variable, use logical abduction. If the output is false, the input is also false. If a variable's value is not directly stated in the input-output pairs, it cannot be determined and is considered N/A.",
        # "To find the value of the given variable, follow the logical chain of premises and conclusions in reverse. Start with the given result and abduce the values of the input variables in the corresponding premise. Remember, in a logical OR operation, if the result is False, all inputs must be False. In a logical NOT operation, the result is the opposite of the input. If a value cannot be directly inferred, set it as N/A.",
        # "Given a set of logical statements, deduce the value of the input based on the output. If the output is false, then one or both of the input must also be false. If the output is true, the input may or may not be true. In the case of a NOT statement, if the output is true, then the input must be false. If the output is false, then the input must be true.",
        # "to use the rules of logical abduction to determine the value of a given variable based on the value of another variable. In each case, start with the given variable and its value, then work backwards through any logical statements that involve that variable to determine the value of the other variable. Logical abduction includes the rules of modus ponens (if P then Q; P is true, therefore Q is true), modus tollens (if P then Q; Q is false, therefore P is false), and disjunctive syllogism (P or Q; P is false, therefore Q is true), among others.",
        # "Given an input consisting of logical propositions and a claim that an output variable is False, infer the possible truth value of a specified variable using a form of backward reasoning known as abduction.",
        # "Given a conclusion in all given logical statements (inputs), deduce the truth value of a certain variable by tracing back through the logical connections. If the value cannot be determined, output N/A.",
        # "If the output is False, then the values of all variables in the input are False, unless their value could not be determined definitely from the provided statements. In this case, the value is marked as N/A.",
        # "To deduce the value of given input, follow the given statements backwards from the given condition and use logical reasoning. \
        # 1. If 'A -> B' is True and B is False then A is also False. \
        # 2. If 'A -> B' is True and A is False then B can be either True or False. \
        # 3. If 'A OR B -> C' is False, both A and B are False. \
        # 4. If 'NOT A -> B' is True and B is False then A is True. \
        # 5. If 'NOT A -> B' is True and B is True, A can be either True or False. \
        # The value cannot be determined when it's dependent on an OR conditional with two unknowns.",
        # "To determine the value of a target variable, follow these steps: \
        # 1. From the given condition, identify the premise which resulted in the given output. Conclude that the premise must hold the converse of the output value (True if output is False and vice versa). \
        # 2. Identify all input-output pairs in which the target variable forms part of a premise. \
        # 3. Determine the value of the target variable as follows: \
        # - If the premise is of the form 'A OR B' and the output is False, conclude that both A and B, and therefore the target variable, must be False.\
        # - If the premise is of the form 'NOT A' and the output is False, conclude that A, and therefore the target variable, must be True. \
        # - If the value of the target variable cannot be directly identified from the premises, declare the value to be 'N/A'.", 
        # "to use the process of logical abduction to determine the value of a variable based on the given values of other variables. This process involves tracing back from the given output to its associated inputs, and from those inputs to their own antecedent inputs, until the value of the target variable can be determined. The friend had to apply Boolean logic rules, specifically, that in an OR operation if the outcome is False then both inputs must be False, and in a NOT operation the output is the opposite of the input.",
        # "To deduce the value of the given variable, follow the logical statements backwards. If a statement (X or/and Y) -> Z is given and the value of Z is known, the value of X and/or Y can be deduced if the logical operator is 'or'. If X and/or Y -> Z is False, then X and/or Y must be False. If the statement is (NOT X) -> Y and the value of Y is known, the value of X can be deduced. If NOT X -> Y is False, then X must be True. If NOT X -> Y is True, then X is N/A. The value of the variable being asked is the final variable in the sequence of deductions.",
        # "To solve for the required value, follow the logic chain backwards from the given output. If the output is false, the input conditions must also be false. If the input conditions are an OR operator, then both conditions must be false. If the input conditions include a NOT operator, then the opposite of the original abduced value of the condition is taken. If the required input is part of an OR operator and the other condition can not be known or influenced by previous steps, the value of the required input can not be abduced and is set to be N/A.",
        "To solve for the requested value, trace back through the logical operators. If the output of an OR operator is false, both inputs must be false. If the output of a NOT operator is false, the input must be true. If the output of an OR operator is true, at least one of the inputs must be true, but you cannot determine which one without additional information, therefore the output is labelled N/A.",
        # "to use logical abduction to determine the value of the queried variable given the state of a different variable. This method involves the use of logical operators such as 'and', 'or', and 'not', and the principle that if a certain condition leads to a known result, the reverse can be inferred if the result is not achieved.",
        # "To find the value of the variable in the question, use a method called abductive reasoning. This is a form of logical inference that starts with an observation or set of observations and then seeks the simplest and most likely explanation. You must work backwards through the logic equations using the given value. For the OR operator, if the output is False, then both inputs must be False. For the NOT operator, the output is the opposite of the input.",
        # "To determine the value of a given input, follow the chain of logic presented by the inputs and their outputs, abducing the values based on the logical operators (AND, OR, NOT) and the value of the final output.",
        # "To find the output, start with the given condition and work backwards through the inputs. If the output of a statement is False, then the premise (input) must also be False. If a premise consists of two conditions connected by OR, and the output is False, both elements of the premise must be False. If a premise consists of a condition connected by NOT, and the output is False, then the condition must be True. If no definitive answer can be found based on the given conditions, the output is N/A.",
    ],

    "reachability":[
        # "To determine if one node in a directed graph can be reached from another. Given a directed graph and two nodes, implement a depth-first search (DFS) to investigate whether it is possible to reach the second node starting from the first node. If the second node is reachable, respond with '<<<True>>>'. If the second node is not reachable, respond with '<<<False>>>'.",
        # "To determine if a specific node in a directed graph can be reached from a given starting node. If the specific node can be reached, show the process and return '<<<True>>>'. If it cannot be reached, show the process and return '<<<False>>>'.",
        # "Perform a Depth-First Search (DFS) on the provided directed graph. Start from the specified node and try to reach the target node. If you can reach the target node from the start node, return '<<<True>>>'. If not, return '<<<False>>>'. Trace your steps and provide a detailed working along with your answer.",
        # "To determine whether a certain node can be reached from another node in a directed graph, perform a depth-first search of the graph starting from the source node. Follow the edges of the graph in the order they are given, and keep track of the nodes you have visited to avoid loops. If you reach the target node during your search, respond with '<<<True>>>'. If you exhaust all possible paths without reaching the target node, respond with '<<<False>>>'. Detail the steps of your search in your response for clarity.",
        # "To determine if one node in a directed graph can be reached from another, using a Depth-First Search algorithm. Start the search from the given starting node and explore all its child nodes. If a child node is the target node, stop the search and return '<<<True>>>'. If the target node is not found in any of the child nodes, backtrack to the previous node and explore the next child node. Continue this process until all nodes have been visited. If after visiting all nodes, the target node has not been reached, return '<<<False>>>'.  \
        # Also, document each step of your search process, including the current node being checked, its children nodes, and any backtracking actions. If the target node is reached, clearly indicate this event. Finally, summarize the outcome of the search process.",
        # "To determine if a node can be reached from another node in a directed graph. Follow the graph from the starting node, visiting each node's children (or outgoing edges). Keep track of visited nodes to avoid repeating the exploration of same node. If you reach the target node, respond with '<<<True>>>', which means it can be reached. If, after visiting all possible routes, you haven't reached the target node, respond with '<<<False>>>', which means it cannot be reached.",
        # "To determine if a node can be reached from another given node in a directed graph using a depth-first search algorithm. Enumerate all the nodes that each node points to. If a node points to no other nodes, indicate this with 'None'. Start the search from the specified node and explore each child node (the nodes it points to) sequentially. If you reach the target node during the search, then it can be reached from the starting node - respond with '<<<True>>>'. If you exhaust all possible paths without reaching the target node, then it cannot be reached from the starting node - respond with '<<<False>>>'. During the search process, describe each step, including which node you're checking, which child nodes you're exploring, and if you've had to backtrack due to reaching a node with no unvisited child nodes.",
        # "To determine if a node can be reached from another node in a directed graph by following the graph's edges, perform a Depth-First Search. Begin at the starting node and explore as far as possible along each branch before backtracking. If you reach the target node, return 'True'. If you exhaust all possible paths without reaching the target node, return 'False'.",
        # "To determine if a specific node can be reached from another node in a given directed graph. You should perform a Depth-First Search, starting from the specified start node. Always keep track of the nodes you have visited, to ensure you don't end up in a loop. If you successfully reach the target node during your search, respond with '<<<True>>>'. If you exhaust all possible paths without reaching the target node, respond with '<<<False>>>'.",
        # "Implement a depth-first search algorithm to check if a node can be reached from a starting node in a directed graph. The directed graph is represented by nodes and the respective nodes they point to. Determine if the target node can be reached starting from the given node."
        # "If the target node can be reached from the starting node, print the path that leads to the target node and then print '<<<True>>>'. Otherwise, once all possible paths are exhausted without reaching the target node, print '<<<False>>>'. \
        # Implement depth-first search on the given directed graph starting from the provided node, tracing your steps as you go. If you reach the target node during your search, return '<<<True>>>'. If you've visited all reachable nodes and still haven't found the target node, return '<<<False>>>'.",
        # "To perform a depth-first search (DFS) on a directed graph to determine if a specific node can be reached from a given starting node. Treat each pair of nodes in the graph as the start node pointing towards its child nodes, and continue this process until either the target node is reached, or all possible paths have been exhausted. Return 'True' if the target node can be reached and 'False' if not.",
        # "To determine if one node in a directed graph can be reached from another, starting from the starting node. Apply a Depth-First Search (DFS) algorithm. Begin at the starting node and explore as far as possible along each branch before backtracking. If you are able to reach the target node, respond with '<<<True>>>'. If you have backtracked from all possible paths and have not reached the target node, respond with '<<<False>>>'. If a node has no unvisited children, backtrack to the previous node.",
        # "To perform a depth-first search (DFS) on the given directed graph. Start the search from the specified start node and try to reach the target node. If you reach the target node during the search process, return '<<<True>>>'. If you exhaust all the possible paths without reaching the target node, return '<<<False>>>'. Make sure to mark a node as visited when you first visit it, and never visit the same node again.",
        "Determine if a target node can be reached from a starting node in the given directed graph. Proceed in a depth-first search manner, checking each node's children until you either reach the target or exhaust all possible paths. If the target node is reached, provide a step-by-step explanation of the path taken and respond with '<<<True>>>'. If all paths are exhausted without reaching the target, state that no path could be found and respond with '<<<False>>>'.",
        # "To determine if a particular node in a given directed graph can be reached starting from another node. You should traverse the graph using a depth-first search. Start from the initial node and explore as far as possible along each branch before backtracking. Record the process and the final result in a step-by-step manner. For each node, indicate which children it is exploring, which node it is moving back from (if applicable), and whether or not it successfully reached the target node. If all possible paths are exhausted without reaching the target node, indicate this as well. The final output should be '<<<True>>>' if the target node is reachable from the initial node, or '<<<False>>>' if it is not.",
        # "Determine if a given node in a directed graph can be reached from another node using Depth-First Search. Start from the given starting node, and recursively visit its children (or nodes it points to). If the goal node is encountered during this search, return '<<<True>>>'. If all paths are exhausted and the goal node is not reached, return '<<<False>>>'. While traversing through the nodes, give a detailed explanation of the search process and the nodes being explored.",
        # "Use a depth-first search (DFS) algorithm to determine if a target node can be reached from a starting node in a directed graph. Begin with the initial node and explore as far as possible along each branch before backtracking. If you reach the target node, respond with '<<<True>>>'. If you exhaust all possible paths without reaching the target node, respond with '<<<False>>>'. Break down your process step-by-step, detailing which node you're checking at each step, which of its children you're exploring, and whether you're backtracking or successfully reaching the target.",
        # "To use Depth-First Search (DFS) to determine if a specified node in a directed graph can be reached from another specified node. Start the search from the given starting node. For each node you visit, first mark it as visited, then visit all of its unvisited children in the order they're given. If a node has no unvisited children, backtrack to its parent node. If you reach the target node at any point, return <<<True>>>. If you exhaust all possible paths without reaching the target node, return <<<False>>>.",
        # "To perform a depth-first search (DFS) on the given directed graph, starting from the given node, to determine if a specific other node can be reached from the starting node. If the target node can be found during the DFS, respond with '<<<True>>>'. If all possible paths have been explored and the target node was not found, respond with '<<<False>>>'.",
    ],

    "max_sum_path":[
        # "To perform a depth-first search (DFS) on the given directed graph to find the maximum sum path from a source node to a destination node. Start at the source node, explore as far as possible along each branch before backtracking. If you reach the destination node, update the maximum sum if the current sum is greater. Keep track of the current sum and maximum sum at each step. If there is no path from the source node to the destination node, return 'N/A'.",
        "To use a depth-first search to navigate the directed graph and calculate the sum of each path from the starting node to the ending node. If a path leads to the ending node, compare its sum to the current maximum sum. If it's greater, update the current maximum sum. If the end node can't be reached from the start node, return 'N/A'. The final output should be the maximum sum found, formatted as '<<<maximum sum>>>'. If no path is found, return '<<<N/A>>>'.",
        # "Your task is to determine the maximum sum path from one given node to another in the directed graph. You need to add the values of each node along the path. If there's no path between the given nodes, the output should be 'N/A'. You also need to describe the steps of your search. \
        # Find the maximum sum of values from one node to another in a provided directed graph where each node has a value. The sum should be calculated by adding the values assigned to each node along the path from the starting node to the ending node. If no path exists from the starting node to the ending node, mark it as N/A. Each step of the process should be documented, from reaching an initial node to exploring the children of that node to finding a new maximum sum path or determining there is no possible path. The final answer should be formatted as <<<Answer>>>.",
        # "To find and calculate the maximum sum path from one specified node to another in a given directed graph, where each node has a value assigned to it. If there's no path between the specified nodes, return 'N/A'. The sum of a path is calculated by adding up the values of the nodes composing the path.",
        # "To find the maximum sum path between two given nodes in a directed graph. The sum of a path is calculated by adding up the values of all nodes in that path. If there is no path between the two nodes, return 'N/A'. Detailed steps on how each node is traversed and sum calculated needs to be provided. The final result should be presented in the format <<<Answer>>>.",
        # "To find the path in a directed graph from one node to another that results in the maximum sum of the values assigned to each visited node. If no path exists between the two nodes, report 'N/A'.",
        # "Given a directed graph with values assigned to each node and two specific nodes, write a program to find the maximum sum path from one node to the other. The maximum sum path is the path between the two nodes that results in the highest possible sum of the values of the nodes on this path. If there's no path between the nodes, return 'N/A'. The output should detail the process of exploring the graph and the final answer should be formatted as <<<Answer>>>.",
        # "To find the maximum sum path from one specified node to another in a directed graph with values assigned to each node. The sum is calculated by adding up the values of the nodes in the path. If there's no path from the start node to the end node, output 'N/A'. In your output, describe each step of your search and the current total sum at each node. Finally, present your answer in the format '<<<Answer>>>'. If the answer is a number, round it to one decimal place.",
        # "Given a directed graph with values assigned to each node, write a program to find the maximum sum path from a given starting node to a given ending node. The highest sum is obtained by adding up the values of the nodes along the path. If there is no path from the starting node to the ending node, return 'N/A'. The output should be in the following format: <<<Answer>>>. If the answer is a number, it should be presented as a decimal number.",
        # "to write a program that performed a depth-first search on a directed graph, tracking the maximum sum of node values from a given start node to a given end node, and providing a step-by-step analysis of the search process. If there was no path from the start node to the end node, the program was to indicate this result. The output was then to be formatted as a floating-point number enclosed in triple angle brackets, or as 'N/A' if no path existed.",
        # "To find the maximum sum path from one node to another in a directed graph. The path would include the value of each node. If there is no path from the starting node to the final node, return 'N/A'.",
        # "To find the maximum sum path between two nodes in a directed graph. The sum of a path is computed by adding up the values of all the nodes in that path. If there is no path between the two nodes, the answer should be 'N/A'. Provide a step-by-step explanation of the process and the final answer should be presented in the format of '<<<Answer>>>'.",
        # "To find the maximum sum path from one node to another in a directed graph. The graphs are represented as nodes pointing to other nodes, and each node has an assigned value. If a path exists between the two nodes, iterate through all possible paths, summing the values of the nodes along the way, and return the maximum sum. If no path exists, return 'N/A'.",
        # "To find the maximum sum path from one node to another in a directed graph. For each input of a directed graph, start at the initial node and explore each child node, keeping a running total of the node values. If a path to the final node is found, compare the current path sum to the current maximum sum and update if necessary. If there is no path from the initial node to the final node, indicate this with 'N/A'. The maximum sum path should be outputted as a float, enclosed in '<<<' and '>>>'. If there's a tie for the maximum path, any one of them can be chosen.",
        # "to find the maximum sum path from one node to another in the given directed graph. If there is no path from the starting node to the destination node, return 'N/A'. The sum of a path is calculated by adding up the values of the nodes in it.",
        # "To find the highest sum path in a directed graph from one node to another. If there is no path from the first node to the second, report it as 'N/A'. For each input, do a depth-first search on the directed graph starting from the first node. Each time you reach a new node, add its value to the current sum. If the new node is the destination node, check if the current sum is the highest found so far, and if it is, update the maximum sum. If the new node has children, repeat the process for each child. If there is no path to the destination node from the current node, go back one step and try the next child. Repeat this until all paths from the start node have been explored. Then, return the highest sum found.",
        # "To calculate the maximum sum path from one node of the given directed graph to another. The maximum sum path is the path between two nodes that, when the values of all nodes along it are added up, gives the highest total. If no path exists between the two nodes, indicate this with N/A. Navigate the graph using Depth-First Search (DFS) strategy, keep track of the current sum of the path at each node, and update the maximum sum whenever a new path with a higher sum is found. The nodes of the graph are represented by strings and each node points to other nodes (its children). The value of each node is represented by a number. Treat nodes without children as dead ends and backtrack to find other possible paths. Be sure to thoroughly explore all paths. After the search is done, format your answer as <<<Maximum Sum>>>, where 'Maximum Sum' is the highest sum found. If no path could be found between the nodes, format the answer as <<<N/A>>>.",
        # "To find the maximum sum path from the given starting node to the ending node in the directed graph with values assigned to each node. If a path does not exist, indicate this with N/A. To obtain the value of a path, sum the values of the nodes within that path.",    
    ],

}


SUFFIX = {
    "arithmetic": [
        # "The mathematical problem is described as: {}. What's the solution for {}? If the solution can not be calculated, return 'N/A'. Always begin your response with '<<<' and end with '>>>'.",
        "\n{}\nCompute the result of {}. If the solution cannot be calculated, answer 'N/A'. Ensure your result is within a relative precision of 0.0001 (or 0.01%) compared to the ground truth value. Ensure your final result begins with '<<<' and ends with '>>>', for example, if the answer is 1, your final result should be <<<1>>>."
        # "Given the mathematical problem: {}. Can you solve for the result of {}? If the solution can not be calculated, return 'N/A'. Always start your response with '<<<' and end with '>>>'.",
    ],
    
    "linear_equation": [
        "\n{}\nDetermine the values of x and y. Ensure your results are within a relative precision of 0.001 (or 0.1%) compared to the ground truth values. Your response should be formatted as: <<<x's value y's value>>>, e.g., if x=1 and y=2, then it should be <<<1 2>>>",
    ],

    "bool_logic": [
        "\n{}\nCompute the result of {}. If the solution can not be calculated, answer 'N/A'. Ensure your final result begins with '<<<' and ends with '>>>', for example, if the answer is True, your final result should be <<<True>>>.",
    ],

    "deductive_logic": [
        "\n{}\nThe symbol '->' represents a deductive relationship, e.g., A -> B implies that if A is true, then B is true. If A is false, B's truth value remains undetermined (N/A). Deduce the result of {}. If the solution can not be deduced, answer 'N/A'. Ensure your final result begins with '<<<' and ends with '>>>', for example, if the answer is True, your final result should be <<<True>>>.",
    ],

    "abductive_logic": [
        "\n{}\nThe symbol '->' represents a deductive relationship, e.g., A -> B implies that if B is false, then A is false. If B is true, A's truth value remains undetermined (N/A). If the solution can not be abduced, answer 'N/A'. Ensure your final result begins with '<<<' and ends with '>>>', for example, if the answer is True, your final result should be <<<True>>>.",
    ],

    "reachability": [
        "\n{}\nRespond with either '<<<True>>>' if reachable, or '<<<False>>>' otherwise.",
    ],

    "max_sum_path": [
        "\n{}\nFor exmaple, the value of the path A->B->C is obtained by summing the values of nodes A, B, and C. Please format your response as <<<Answer>>>. For example, if the answer is 1, it should be presented as <<<1>>>.",
    ],

}

SKIC_PROMPTS = {
"arithmetic" : [
'''
You have the knowledge of many skills, here are some examples:
Skill <Add>: Add two numbers. For example, 128+987=1115. 

Skill <Mul>: Multiply two numbers. For example, 128*76=9728. 

Skill <Sub>: Subtract a number from another number. For example, 128-67=61. 

Skill <Div>: Divide a number from another number. For example 12/3=4.

Skill <Exp>: An exponent refers to the number of times a number is multiplied by itself.  For example, in 2^3, 2 is the base and 3 is the exponent, 2^3=(2*2*2)=8. 

Skill <Radicals>: A radical represents the root of a number. The square root (represented by sqrt) is the most common radical. For example, sqrt(4)=2.

-----------------
Now, use your skills to solve the math problems where for a given description, compute the value of a desired variable. Here are some examples:
Example #1:
The value of aaa is 5.
The value of aac is 9.
aaf gets its value by dividing the value of aab by those of aae.
The value of aad is 7.
aab gets its value by squaring the value that aaa has.
aae gets its value by subtracting the value of aad from the value of aac.
Compute the value of aaf. 
Answer:
<C> 
1. aaf gets its value by dividing the value of aab by those of aae. aaf = aab/aae.
2. aab gets its value by squaring the value that aaa has. aab = aaa^2.
    2.1. The value of aaa is 5. 
    2.2 aab = aaa^2 = 5^2. Using Skill <Exp>, aab = 5^2 = 25. So the value of aab is 25.
3. aae gets its value by subtracting the value of aad from the value of aac. aae = aac-aad.
    3.1 The value of aac is 9.
    3.2 The value of aad is 7.
    3.3 aae = aac-aad = 9-7. Using Skill <Sub>, aae = 9-7 = 2. So the value of aae is 2.
4. The value of aab is 25. The value of aae is 2. aaf = aab/aae = 25/2. Using Skill <Div>, aaf = 25/2 = 12.5. So the value of aaf is 12.5.
<C>
<<<12.5>>>
<EOD>

Following the above examples, use your skills to answer the math problem:
'''
],

"linear_equation" : [
'''
You have the knowledge of many skills, here are some examples:
Skill <Add>: Add two numbers. For example, 128+987=1115. 

Skill <Mul>: Multiply two numbers. For example, 128*76=9728. 

Skill <Sub>: Subtract a number from another number. For example, 128-67=61. 

Skill <Div>: Divide a number from another number. For example 12/3=4.

Skill <Exp>: An exponent refers to the number of times a number is multiplied by itself.  For example, in 2^3, 2 is the base and 3 is the exponent, 2^3=(2*2*2)=8. 

Skill <Radicals>: A radical represents the root of a number. The square root (represented by sqrt) is the most common radical. For example, sqrt(4)=2.

Skill <Solve Equation>: Solve an equation. When subtract or add the same number from both sides of the equation, the equation is still true. When move a number from one side of the equation to the other side, the sign of the number changes. 
For example, if the equation is 3x+2=x+8, move +2 to the other side, then 3x=x+8-2. Using the Skill <Sub>, 3x=x+8-2=x+6. Move +x to the other side, then 3x-x=6. Using the Skill <Sub>, 2x=6. Move *2 to the other side, then x=6/2=3.

-----------------
Now, use your skills to solve the linear equation problems. Here are some examples:

Example #1:
4 x + -7 y = 7
-2 x + aac0 y = 8

The calculation of aac0 is defined as:
The value of aaa0 is 7.
aac0 gets its value by multiplying together the value of aaa0 and aab0 and aaa0.
The value of aad is 1.
aae gets its value by taking the square root of the value that aad has.
The value of aab0 is 4.

Calculate the values of x and y.
Answer:
<C>
1. First, we compute the value of aac0:
    i. aac0 gets its value by multiplying together the value of aaa0 and aab0 and aaa0. aac0 = aaa0*aab0*aaa0
    ii. The value of aaa0 is 7. 
    iii. The value of aab0 is 4. 
    iv. aac0 = aaa0*aab0*aaa0 = 7*4*7. Using the Skill <Mul>, aac0 = 7*4*7 = 196. So the value of aac0 is 196.
2. Then we solve the linear equation: 
    4 x + -7 y = 7
    -2 x + 196 y = 8
    i. For 4x + -7 y = 7, using the Skill <Solve Equation>, move -7y to the other side, then 4x=7+7y, move *4 to the other side, then x=(7y+7)/4. Using the Skill <Div>, x=(7y+7)/4=(7/4)y+(7/4)=1.75y+1.75.
    ii. For -2x + 196 y = 8, using the Skill <Solve Equation>, move 196y to the other side, then -2x=8-196y, move *-2 to the other side, then x=(8-196y)/-2. Using the Skill <Div>, x=(8-196y)/-2=(8/-2)-(196y/-2)= -4 + 98y.
    iii. So x = 1.75y+1.75 = -4+98y. So 1.75y+1.75=-4+98y. Using the Skill <Solve Equation>, move 1.75 to the other side, then 1.75y = -4+98y-1.75. Move 98y to the other side, then 1.75y-98y = -4-1.75. Using the Skill <Sub>, -96.25y = -5.75. Move *(-96.25) to the other side, then y=(-5.75)/(-96.25). Using the Skill <Div>, y=(-5.75)/(-96.25)=0.05974026
    iv. So y = 0.05974026. Using the Skill <Mul> and Skill <Add>, x = 1.75y+1.75 = 1.75*0.05974026+1.75 =0.104545455 + 1.75 = 1.85454545
3. x = 1.85454545, y = 0.05974026.
<C>
<<<1.85454545, 0.05974026>>>
<EOD>

Following the above examples, use your skills to answer the linear equation problems:
'''
],

"bool_logic" : [
'''
You have the knowledge of many skills, here are some examples:
Skill <AND>: AND is a logical operation that compute the logical AND of two boolean values. 
For example, True AND True AND False = False. 

Skill <NOT>: NOT is a logical operation that compute the logical NOT of a boolean value.
For example, NOT True = False. NOT False = True.

Skill <OR>: OR is a logical operation that compute the logical OR of two boolean values.
For example, True OR True OR False = True. False OR False OR False = False.

-----------------
Now, use your skills to solve the bool logic problems where for a given description, compute the boolean value of a desired variable. Here are some examples:
Example #1:
aad is False.
The value of aab equals to (NOT aaa).
The value of aaf equals to (aab AND aae AND aac).
The value of aae equals to (aac OR aad OR aaa).
The value of aah equals to (NOT aag).
aac is True.
aag is True.
aaa is True.
Compute the value of aaf.
Answer:
<C>
1. The value of aaf equals to (aab AND aae AND aac). aaf = aab AND aae AND aac.
2. We first compute every term in the right hand side of the equation (aab, aae, aac):
    i. The value of aab equals to (NOT aaa). aab = (NOT aaa)
        (i.a) aaa is True. 
        (i.b) Using the Skill <NOT>, aab = (NOT aaa) = (NOT True) = False.
        (i.c) aab is False.
    ii. The value of aae equals to (aac OR aad OR aaa). aae = aac OR aad OR aaa
        (ii.a) aac is True.
        (ii.b) aad is False.
        (ii.c) aaa is True.
        (ii.d) Using the Skill <OR>, aae = aac OR aad OR aaa = True OR False OR True = True.
        (ii.e) aae is True.
    iii. The value of aac equals to (aaa AND aab AND aah). aac = aaa AND aab AND aah
        (iii.a) aaa is True.
        (iii.b) aab is False.
        (iii.c) aah is False.
        (iii.d) Using the Skill <AND>, aac = aaa AND aab AND aah = True AND False AND False = False.
        (iii.e) aac is False.
3. Using the Skill <AND>, aaf = aab AND aae AND aac = False AND True AND False = False.
4. aaf is False.
<C>
<<<False>>>
<EOD>

Following the above examples, use your skills to answer the bool logic problems:
'''
],

"deductive_logic": [
'''
You have the knowledge of many skills, here are some examples:
Skill <AND>: AND is a logical operation that compute the logical AND of two boolean values. When one of the term is N/A, the result is N/A.
For example, True AND False = False. N/A AND True = N/A. False AND N/A = N/A. N/A AND True AND False = N/A.

Skill <NOT>: NOT is a logical operation that compute the logical NOT of a boolean value. When the term is N/A, the result is N/A.
For example, NOT True = False. NOT False = True. NOT N/A = N/A.

Skill <OR>: OR is a logical operation that compute the logical OR of two boolean values. Only when all of the terms are N/A, the result is N/A.
For example, True OR False = True. True OR N/A OR False = True. N/A OR N/A OR True = True. N/A OR False = False. 

Skill <Deduce>: For A -> B: If the left is True, the right is set to True. If the left is False or N/A, the right is set to N/A.
For example, True -> aag. Using the Skill <Deduce>, the premise is True, aag = True.
For example, False -> aah. Using the Skill <Deduce>, the premise is False, aah = N/A.
For example, N/A -> aak. Using the Skill <Deduce>, the premise is N/A, aak = N/A.

-----------------
Now, use your skills to solve the deductive logic problems where for a given description, compute the value of a desired variable. Here are some examples:
Example #1:
aai is True.
aab is False.
(aac and aaf) -> aag.
aaa is False.
(aad or aae) -> aaf.
aae is True.
aah is True.
aad is True.
(aaa or aab) -> aac.
(aah or aai) -> aaj.
Compute the value of aag.
Answer:
<C>
1. (aac and aaf) -> aag in the description where the right hand side is aag.
2. We first compute every term in the left hand side of the equation (aac, aaf):
    i. Compute the value of aac, (aaa or aab) -> aac in the description where the right hand side is aac.
        (i.a) aaa is False.
        (i.b) aab is False.
        (i.c) Using the Skill <OR>, aaa or aab = False or False = False.
        (i.d) False -> aac. Using the Skill <Deduce>, the premise is False, aac = N/A.
        (i.e) aac is N/A.
    ii. Compute the value of aaf, (aad or aae) -> aaf in the description where the right hand side is aaf.
        (ii.a) aad is True.
        (ii.b) aae is True.
        (ii.c) Using the Skill <OR>, aad or aae = True or True = True.
        (ii.d) True -> aaf. Using the Skill <Deduce>, the premise is True, aaf = True.
        (ii.e) aaf is True.
3. Using the Skill <AND>, aac and aaf = N/A and True = N/A.
4. N/A -> aag. Using the Skill <Deduce>, the premise is N/A, aag = N/A.
5. aag is N/A.
<C>
<<<N/A>>>
<EOD>

Following the above examples, use your skills to answer the deductive logic problems:
'''
],

"abductive_logic": [
'''
You have the knowledge of many skills, here are some examples:
Skill <Reverse_AND>: Infer the value of the left side based on the value of right side.
aaa and aab = True. Using the Skill <Reverse_AND>, the right is True, aaa = True, aab = True.
aaa and aab = False. Using the Skill <Reverse_AND>, the right is False, aaa = N/A, aab = N/A.
aaa and aab = N/A. Using the Skill <Reverse_AND>, the right is N/A, aaa = N/A, aab = N/A.

Skill <Reverse_OR>: Infer the value of the left side based on the value of right side.
aaa or aab = True. Using the Skill <Reverse_OR>, the right is True, aaa = N/A, aab = N/A.
aaa or aab = False. Using the Skill <Reverse_OR>, the right is False, aaa = False, aab = False.
aaa or aab = N/A. Using the Skill <Reverse_OR>, the right is N/A, aaa = N/A, aab = N/A.

Skill <Reverse_NOT>: Infer the value of the left side based on the value of right side.
NOT aaa = True. Using the Skill <Reverse_NOT>, the right is True, aaa = False.
NOT aaa = False. Using the Skill <Reverse_NOT>, the right is False, aaa = True.
NOT aaa = N/A. Using the Skill <Reverse_NOT>, the right is N/A, aaa = N/A.

Skill <Abduce>: For A -> B: If the right is False, the left is set to False. If the right is True or N/A, the left is set to N/A.
aag -> True. Using the Skill <Abduce>, the right is True, aag = N/A.
aah -> False. Using the Skill <Abduce>, the right is False, aah = False.
aak -> N/A. Using the Skill <Abduce>, the right is N/A, aak = N/A.

-----------------
Now, use your skills to solve the abductive logic problems where for a given description, compute the value of a desired variable (every variable contains three letters like aao, aan, abd). Here are some examples:
Example #1:
(NOT aaa) -> aab.
(NOT aac) -> aae.
(aag and aah) -> aai.
(aab or aae) -> aaf.
Given aaf is True, what is the value of aac?
Answer:
<C>
1. We first find a chain of equations from aac to aaf from the given description:
    i. select an equation in the description where the left hand side has aac (aac in (aac) and aac not in (aae)): (NOT aac) -> aae, from aac to aae
    ii. select an equation in the description where the left hand side has aae (aae in (aab, aae) and aae not in (aaf)): (aab or aae) -> aaf, from aae to aaf
2. We then compute the value of aac with a chain of abductive steps from aaf to aac:
    i. (aab or aae) -> aaf. aaf is True. Using the Skill <Abduce>, the right is True, aab or aae = N/A. Using the Skill <Reverse_OR>, the right is N/A, aab = N/A, aae = N/A.
    ii. (NOT aac) -> aae. aae is N/A. Using the Skill <Abduce>, the right is N/A, NOT aac = N/A. Using the Skill <Reverse_NOT>, the right is N/A, aac = N/A.
3. aac is N/A.
<C>
<<<N/A>>>
<EOD>

Following the above examples, use your skills to answer the abductive logic problems:
'''
],

"reachability": [
'''
You have the knowledge of many skills, here are some examples:

Skill <Dequeue>: Remove an element from the front of the queue. For example, if the queue is [aab, aac, aad], after dequeue, the queue is [aac, aad] and the dequeued element is aab.

Skill <Enqueue>: Add an element to the end of the queue. For example, if the queue is [aab, aac, aad], after enqueue aae, the queue is [aab, aac, aad, aae].

-----------------
Now, use your skills to solve the graph reachability problems. Here are some examples:
Example #1:
Given a directed graph:
aab points to: (aag, aae).
aag points to: (None).
aad points to: (aag, aab, aae).
aae points to: (aag, aaf).
aac points to: (aag, aae, aab, aad, aaf).
aaf points to: (aag).
aaa points to: (aac, aad, aaf, aab, aag, aae).
Can aab be reached starting from aad?
Respond with either '<<<True>>>' if reachable, or '<<<False>>>' otherwise.
Answer:
<C>
1. We mark all the node as unvisited: aab = False, aag = False, aad = False, aae = False, aac = False, aaf = False, aaa = False.
2. Using the Skill <Enqueue>, we enqueue aad: [aad]. We mark aad as visited: aad = True.
3. Using the Skill <Dequeue>, we dequeue aad: []. aad != aab. aad points to (aag, aab, aae). aag = False, aab = False, aae = False. aag, aab, aae have not been visited, using the Skill <Enqueue>, we enqueue aag, aab, aae: [aag, aab, aae]. We mark aag, aab, aae as visited: aag = True, aab = True, aae = True.
4. Using the Skill <Dequeue>, we dequeue aag: [aab, aae]. aag != aab. aag points to (None). We don't enqueue anything: [aab, aae].
5. Using the Skill <Dequeue>, we dequeue aab: [aae]. aab == aab. We found aab. So aab can be reached starting from aad. The answer is True.
</C>
<<<True>>>
<EOD>

Following the above examples, use your skills to answer the graph reachability problems:
'''
],

"max_sum_path": [
''' 
You have the knowledge of many skills, here are some examples:
Skill <Add>: Add two numbers. For example, 128+987=1115. 

Skill <Find_max>: Find the max number in a list.
For example, max(2,0)=2. max(-2,0)=0.

Skill <Dequeue>: Remove an element from the front of the queue. For example, if the queue is [aab, aac, aad], after dequeue, the queue is [aac, aad] and the dequeued element is aab.

Skill <Enqueue>: Add an element to the end of the queue. For example, if the queue is [aab, aac, aad], after enqueue aae, the queue is [aab, aac, aad, aae].

-----------------
Now, use your skills to find the maximum sum from one node to another node. Here are some examples:
Example #1:
Given a directed graph with values assigned to each node:
aaa points to: (aaf).
aad points to: (aac, aag).
aab points to: (aae, aaf, aac).
aae points to: (aac, aaa, aag).
aag points to: (None).
aaf points to: (None).
aac points to: (aag, aaf, aaa).
The value of aad is 9
The value of aaa is 4
The value of aac is 4
The value of aab is 5
The value of aaf is 2
The value of aag is 6
The value of aae is 7
What's the maximum sum path from aac to aaa?
For example, the value of the path A->B->C is obtained by summing the values of nodes A, B, and C. Please format your response as <<<Answer>>>. For example, if the answer is 1, it should be presented as <<<1>>>.
Answer:
<C>
1. We store the values of every node: aad' = 9, aaa' = 4, aac' = 4, aab' = 5, aaf' = 2, aag' = 6, aae' = 7.
2. We mark every node with its initial value: aad = 0, aaa = 0, aac = 0, aab = 0, aaf = 0, aag = 0, aae = 0.
3. Using the Skill <Enqueue>, we enqueue aac: [aac]. Using the Skill <Add> and Skill <Find_max>, we update aac: aac = max(aac, aac' + aac) = max(0, 4+0) = 4.
4. Using the Skill <Dequeue>, we dequeue aac: []. aac points to: (aag, aaf, aaa). aag = 0, aaf = 0, aaa = 0. Using the Skill <Enqueue>, we enqueue aag, aaf, aaa: [aag, aaf, aaa]. Using the Skill <Add> and Skill <Find_max>, we update aag, aaf, aaa: aag = max(aag, aag' + aac) = max(0, 6+4) = 10, aaf = max(aaf, aaf' + aac) = max(0, 2+4) = 6, aaa = max(aaa, aaa' + aac) = max(0, 4+4) = 8.
5. Using the Skill <Dequeue>, we dequeue aag: [aaf, aaa]. aag points to: (None). We don't enqueue anything.
6. Using the Skill <Dequeue>, we dequeue aaf: [aaa]. aaf points to: (None). We don't enqueue anything.
7. Using the Skill <Dequeue>, we dequeue aaa: []. aaa points to: (aaf). aaf = 6. Using the Skill <Enqueue>, we enqueue aaf: [aaf]. Using the Skill <Add> and Skill <Find_max>, we update aaf: aaf = max(aaf, aaf' + aaa) = max(6, 2+8) = 8.
8. Using the Skill <Dequeue>, we dequeue aaf: []. aaf points to: (None). We don't enqueue anything.
9. The queue is empty. For the maximum sum path from aac to aaa: aaa = 8. So the maximum sum path from aac to aaa is 8. The answer is 8.
</C>
<<<8>>>
<EOD>

Following the above examples, use your skills to find the maximum sum from one node to another node:
'''

],

}