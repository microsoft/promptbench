# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import random
from math import sqrt, prod
import numpy as np

from .dag import Node, TreeDAG
from .describer import TreeDAGDescriber
from ..dyval_utils import round_value

class ArithmeticDAG(TreeDAG):
    """
    A specialized TreeDAG for arithmetic operations.

    Extends TreeDAG to represent arithmetic operations with nodes representing numerical values and operations.

    Parameters:
    -----------
    ops : list
        List of arithmetic operations (e.g., '+', '-', '*', '/').
    uni_ops : list
        List of unary operations (e.g., 'sqrt', '**').
    depth : int
        Depth of the tree.
    num_children_per_node : int, optional
        Number of children per node (default is 2).
    extra_links_per_node : int, optional
        Extra links per node (default is 1).
    add_cycles : int, optional
        Number of cycles to add to the tree (default is 0).

    Methods:
    --------
    generate_tree(depth)
        Generates the tree structure with specified depth.
    check_link_constraint(father_node, child_node)
        Checks if a link between two nodes is valid.
    update_values()
        Updates the values of the nodes based on arithmetic operations.
    """
    def __init__(self, ops, uni_ops, depth, num_children_per_node=2, extra_links_per_node=1, add_cycles=0):
        self.ops = ops
        self.uni_ops = uni_ops
        self.num_children_per_node = num_children_per_node
        super().__init__(depth, num_children_per_node, extra_links_per_node, add_cycles)

    def generate_tree(self, depth):
        assert depth >= 1
        # Base case: If depth is 0, generate a leaf node
        if depth == 1:
            name = next(self.name_generator)  # Generate a name
            value = random.randint(1, 10)  # Randomly select a value ranging from 1 to 10.
            return Node(value, None, name, [])

        # Otherwise, generate an internal node
        else:
            # Randomly choose an operation
            op = random.choice(self.ops)

            # Generate children based on the chosen operation
            if op in self.uni_ops:
                # For unary operations, generate one child
                children = [self.generate_tree(depth - 1)]
                
                if op == 'sqrt':
                    while True:
                        try:
                            value = sqrt(children[0].value)
                            break
                        except ValueError:  # Catching sqrt of a negative number
                            children[0] = self.generate_tree(depth - 1)
                
                elif op == '**':
                    while True:
                        try:
                            value = children[0].value**2
                            break
                        except OverflowError:
                            children[0] = self.generate_tree(depth - 1)
            
            else:
                # For binary operations, generate two or more children
                num_of_children = self.num_children_per_node
                children = [self.generate_tree(depth - 1) for _ in range(num_of_children)]
                if op == '+':
                    while True:
                        try:
                            value = sum(child.value for child in children)
                            break
                        except OverflowError:
                            # For simplicity, we'll regenerate all children if an overflow occurs
                            children = [self.generate_tree(depth - 1) for _ in range(num_of_children)]
                            
                elif op == '-':
                    while True:
                        try:
                            value = children[0].value - sum(child.value for child in children[1:])
                            break
                        except OverflowError:
                            # For simplicity, we'll regenerate all children if an overflow occurs
                            children = [self.generate_tree(depth - 1) for _ in range(num_of_children)]

                elif op == '*':
                    while True:
                        try:
                            value = prod(child.value for child in children)
                            break
                        except OverflowError:
                            children = [self.generate_tree(depth - 1) for _ in range(num_of_children)]
                
                elif op == '/':
                    while True:
                        try:
                            value = children[0].value / prod(child.value for child in children[1:])
                            if value == float('inf') or value == float('-inf'):
                                raise ValueError("Infinite value detected.")
                            break
                        except ZeroDivisionError:
                            for i, child in enumerate(children[1:]):
                                while child.value == 0:  # Regenerate the child if its value is 0
                                    child = self.generate_tree(depth - 1)
                                    children[i+1] = child
                        except ValueError:
                            children = [self.generate_tree(depth - 1) for _ in range(num_of_children)]

            return Node(value, op, next(self.name_generator), children)
        
    def check_link_constraint(self, father_node, child_node):
        valid = True
        
        if father_node.op in self.uni_ops:
            valid = False
        if father_node.op == "/" and child_node.value == 0:
            valid = False
        
        return valid

    def update_values(self):
        
        valid_dag = True

        for node_name in self.sorted_node_names:
            # if it's not a leaf node
            for cur_node in self.nodes:
                if cur_node.name == node_name:
                    node = cur_node
            
            if node.op:  
                if node.op == '+':
                    try:
                        node.value = sum(child.value for child in node.children)
                    except OverflowError:
                        valid_dag = False
                        break
                elif node.op == '-':
                    try:
                        node.value = node.children[0].value - sum(child.value for child in node.children[1:])
                    except OverflowError:
                        valid_dag = False
                        break
                elif node.op == '*':
                    try:
                        node.value = prod(child.value for child in node.children)
                    except OverflowError:
                        valid_dag = False
                        break
                elif node.op == '/':
                    try:
                        node.value = node.children[0].value / prod(child.value for child in node.children[1:])
                        if node.value == float('inf') or node.value == float('-inf'):
                            valid_dag = False
                            break
                    except ZeroDivisionError:
                        valid_dag = False
                        break
                elif node.op == 'sqrt':
                    try:
                        node.value = sqrt(node.children[0].value)
                    except ValueError:  # Catching sqrt of a negative number
                        valid_dag = False
                        break
                elif node.op == '**':
                    try:
                        node.value = node.children[0].value**2
                    except OverflowError:
                        valid_dag = False
                        break
        
        if self.root.value < 1e-4:
            valid_dag = False

        return valid_dag

    
class ArithmeticDAGDescriber(TreeDAGDescriber):
    """
    Describer class for ArithmeticDAG.

    Provides methods to describe ArithmeticDAG nodes and their arithmetic operations.

    Parameters:
    -----------
    dag_obj : ArithmeticDAG
        The ArithmeticDAG instance to describe.
    ops : list
        List of binary operations.
    uni_ops : list
        List of unary operations.
    add_rand_desc : int, optional
        Number of random descriptions to add.
    delete_desc : int, optional
        Number of descriptions to delete.

    Methods:
    --------
    describe_question_node(node)
        Describes an ArithmeticDAG node for question formation.
    describe_inference_node(node)
        Describes an ArithmeticDAG node for inference.
    """
    def __init__(self, dag_obj, ops, uni_ops, add_rand_desc=0, delete_desc=0):
        self.ops = ops
        self.uni_ops = uni_ops
        super().__init__(dag_obj, add_rand_desc, delete_desc)

    def describe_question_node(self, node):

        op_descriptions = {
            '+': 'adding together',
            '-': 'subtracting',
            '*': 'multiplying together',
            '/': 'dividing',
            'sqrt': 'taking the square root of',
            '**': 'squaring'
        }

        if node.op is None:
            description = f"The value of {node.name} is {node.value}."
        else:
            description = f"{node.name} gets its value by "
            if node.op in self.uni_ops:
                description += f"{op_descriptions[node.op]} the value that {node.children[0].name} has."
            elif node.op == '-':
                if len(node.children) > 2:
                    description += f"{op_descriptions[node.op]} the sum of the values of {' and '.join(child.name for child in node.children[1:])} from the value of {node.children[0].name}."
                else:
                    description += f"{op_descriptions[node.op]} the value of {node.children[1].name} from the value of {node.children[0].name}."
            elif node.op == '/':
                if len(node.children) > 2:
                    description += f"{op_descriptions[node.op]} the value of {node.children[0].name} by the product of the values of {' and '.join(child.name for child in node.children[1:])}."
                else:
                    description += f"{op_descriptions[node.op]} the value of {node.children[0].name} by those of {node.children[1].name}."
            else:
                description += f"{op_descriptions[node.op]} the value of {' and '.join(child.name for child in node.children)}."
            
        return description

    def describe_inference_node(self, node):

        if node.op is None:
            description = f"{node.name} is {round_value(node.value)}"
        else:
            description = f"{node.name} ="
            if node.op in self.uni_ops:
                if node.op == "**":
                    description += f" {node.children[0].name}^2 = ({round_value(node.children[0].value)})^2 = {round_value(node.value)}"
                else:
                    description += f" {node.op} {node.children[0].name} = {node.op}({round_value(node.children[0].value)}) = {round_value(node.value)}"

            else:
                description += f" {node.children[0].name} {node.op} {f' {node.op} '.join(child.name for child in node.children[1:])} = {round_value(node.children[0].value)} {node.op} {f' {node.op} '.join(map(round_value, (child.value for child in node.children[1:])))} = {round_value(node.value)}"

        return description


class LinearEq:
    """
    Class for generating and describing linear equations using ArithmeticDAGs.

    It creates a set of linear equations and uses ArithmeticDAGs to represent the coefficients.

    Parameters:
    -----------
    ops : list
        List of arithmetic operations.
    uni_ops : list
        List of unary operations.
    depth : int, optional
        Depth of the DAGs (default is 3).
    num_dags : int, optional
        Number of DAGs to generate (default is 1).
    num_children_per_node : int, optional
        Number of children per node in the DAG.
    extra_links_per_node : int, optional
        Extra links per node in the DAG.
    add_rand_desc : int, optional
        Number of random descriptions to add.

    Methods:
    --------
    describe_question()
        Describes the linear equation problem.
    describe_inference_steps()
        Describes the inference steps to solve the linear equation.
    describe_answer()
        Provides the answer to the linear equation.
    _solve_linear_eq()
        Solves the linear equation using numpy's linear algebra solver.
    _has_unique_solution(coeff)
        Checks if the equation has a unique solution.
    _describe_linear_eq_solution()
        Describes the solution of the linear equation.
    """
    def __init__(self, ops, uni_ops, depth=3, num_dags=1, num_children_per_node=2, extra_links_per_node=1, add_rand_desc=0):
        self.ops = ops
        self.uni_ops = uni_ops
        self.depth = depth
        self.num_dags = num_dags
        self.num_children_per_node = num_children_per_node
        self.extra_links_per_node = extra_links_per_node
        self.add_rand_desc = add_rand_desc
        self.coeff = []
        self.coeff_inference_steps = []

    def describe_question(self):
        while True:
            coeff = []
            coeff_inference_steps = []
            coeff_descriptions = []
            
            for _ in range(6 - self.num_dags):
                value = random.randint(-10, 10)
                coeff.append((value, value))  # Format: (name, value)

            for idx in range(self.num_dags):
                dag = ArithmeticDAG(self.ops, self.uni_ops, self.depth, self.num_children_per_node, self.extra_links_per_node)
                for node in dag.nodes:
                    node.name += str(idx)
                describer = ArithmeticDAGDescriber(dag, self.ops, self.uni_ops, self.add_rand_desc)
                coeff_descriptions.append({"descriptions": describer.describe_question(), "vars": dag.root.name})
                coeff.append((dag.root.name, dag.root.value))
                inference_desc = describer.describe_inference_steps()
                inference_desc += f"\nThus, {dag.root.name} = {round_value(dag.root.value)}"
                coeff_inference_steps.append(inference_desc)

            random.shuffle(coeff)

            if self._has_unique_solution(coeff):
                self.coeff = coeff
                self.coeff_inference_steps = coeff_inference_steps
                break
        
        linear_eq_desc = f"\n{coeff[0][0]} x + {coeff[1][0]} y = {coeff[4][0]}\n{coeff[2][0]} x + {coeff[3][0]} y = {coeff[5][0]}\n"

        problem_desc = {}
        for coeff_desc in coeff_descriptions:
            for order, desc in coeff_desc["descriptions"].items():
                if order not in problem_desc:
                    problem_desc[order] = linear_eq_desc
                problem_desc[order] += f"\nThe calculation of {coeff_desc['vars']} is defined as:\n{desc}\n"
       
        return problem_desc

    def describe_inference_steps(self):
        coeff = self.coeff
        desc = "Let's first solve the coefficients of the linear equation."
        for steps in self.coeff_inference_steps:
            desc += f"\n{steps}"
        
        desc += "\n\nNext, solve the linear equation:\n"
        desc += f"\n{round_value(coeff[0][1])} x + {round_value(coeff[1][1])} y = {round_value(coeff[4][1])}\n{round_value(coeff[2][1])} x + {round_value(coeff[3][1])} y = {round_value(coeff[5][1])}\n"
        desc += self._describe_linear_eq_solution()
        return desc


    def describe_answer(self):
        return self._solve_linear_eq()

    def _solve_linear_eq(self):
        coeff = self.coeff

        A = [[coeff[0][1], coeff[1][1]],
            [coeff[2][1], coeff[3][1]]]
        b = [coeff[4][1], coeff[5][1]]

        solutions = np.linalg.solve(A, b)
        return solutions.tolist()

    def _has_unique_solution(self, coeff):
        a, b, c, d = [c[1] for c in coeff[:4]]
        return (a * d - b * c) != 0

    def _describe_linear_eq_solution(self):
        coeff = self.coeff
        # Extracting coefficients for clarity
        a, b, c, d, e, f = coeff[0][1], coeff[1][1], coeff[4][1], coeff[2][1], coeff[3][1], coeff[5][1]

        description = ""

        # Subtract to eliminate y
        new_a = a * e - d * b
        new_c = c * e - f * b

        description += (f"To eliminate 'y', multiply the first equation by {e} and the second equation by {b}. "
                        f"This makes the coefficients of 'y' equal. "
                        f"Subtracting the second equation from the first then gives: {round_value(new_a)}x = {round_value(new_c)}.\n")

        description += f"From the equation {round_value(new_a)}x = {round_value(new_c)}, we can solve for x.\n"

        # Solve for x (theoretically, without actually computing)
        x_value = new_c / new_a
        description += f"Solving for x, we get x = {round_value(x_value)}.\n"

        # Substitute x into the first original equation to solve for y
        if b != 0:
            y_value = (c - a * x_value) / b
        else:
            y_value = (f - d * x_value) / e
            
        description += (f"Substituting x = {round_value(x_value)} into the first original equation, we get: "
                        f"{round_value(b)}y = {round_value(c - a * x_value)}, which gives y = {round_value(y_value)}.\n")

        return description

