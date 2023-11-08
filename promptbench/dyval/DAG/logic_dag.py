import random
import numpy as np
import re

from .dag import Node, TreeDAG
from .describer import TreeDAGDescriber


class BoolDAG(TreeDAG):
    def __init__(self, ops, uni_ops, depth, num_children_per_node=2, extra_links_per_node=1, add_cycles=0):
        self.ops = ops
        self.uni_ops = uni_ops
        
        super().__init__(depth, num_children_per_node, extra_links_per_node, add_cycles)

    def generate_tree(self, depth):
        assert depth >= 1
        # Base case: If depth is 0, generate a leaf node
        if depth == 1:
            name = next(self.name_generator)
            value = random.choice([True, False])  # Randomly assign True or False
            return Node(value, None, name, [])

        # Otherwise, generate an internal node
        else:
            # Randomly choose an operation
            op = random.choice(self.ops)

            # Generate children based on the chosen operation
            if op in self.uni_ops:
                children = [self.generate_tree(depth-1)]
                value = not children[0].value
            else:
                num_of_children = self.num_children_per_node
                children = [self.generate_tree(depth - 1) for _ in range(num_of_children)]
                if op == 'and':
                    value = all(child.value for child in children)
                elif op == 'or':
                    value = any(child.value for child in children)

            return Node(value, op, next(self.name_generator), children)

    def check_link_constraint(self, father_node, child_node):
        valid = True
        
        if father_node.op in self.uni_ops:
            valid = False
        
        return valid
    
    def update_values(self):
        # It is always valid for LogiDAG.
        valid_dag = True
        
        for node_name in self.sorted_node_names:
            for cur_node in self.nodes:
                if cur_node.name == node_name:
                    node = cur_node
            # if it's not a leaf node
            if node.op:  
                if node.op == 'and':
                    node.value = all(child.value for child in node.children)
                elif node.op == 'or':
                    node.value = any(child.value for child in node.children)
                elif node.op == 'not':
                    node.value = not node.children[0].value
        
        return valid_dag


class BoolDAGDescriber(TreeDAGDescriber):
    def __init__(self, dag_obj, ops, uni_ops, add_rand_desc=0, delete_desc=0):
        self.ops = ops
        self.uni_ops = uni_ops
        super().__init__(dag_obj, add_rand_desc, delete_desc)
    
    def describe_question_node(self, node):
        if node.op == None:
            description = f"{node.name} is {'True' if node.value else 'False'}."
        else:
            if node.op == 'not':
                description = f"The value of {node.name} equals to (NOT {node.children[0].name})."
            elif node.op == 'and':
                child_descriptions = ' AND '.join(child.name for child in node.children)
                description = f"The value of {node.name} equals to ({child_descriptions})."
            elif node.op == 'or':
                child_descriptions = ' OR '.join(child.name for child in node.children)
                description = f"The value of {node.name} equals to ({child_descriptions})."
        
        return description

    def describe_inference_node(self, node):

        def bool_to_str(val):
            return 'True' if val == True else 'False'

        if node.op == None:
            description = f"{node.name} is {bool_to_str(node.value)}."
        else:
            ops_description = {
                'not': 'NOT',
                'and': 'AND',
                'or': 'OR'
            }
            if node.op == 'not':
                description = f"{node.name} = ({ops_description[node.op]} {node.children[0].name}) = ({ops_description[node.op]} {bool_to_str(node.children[0].value)}) = {bool_to_str(node.value)}."
            else:
                children_names = f" {ops_description[node.op]} ".join(child.name for child in node.children)
                children_values = f" {ops_description[node.op]} ".join(map(bool_to_str, (child.value for child in node.children)))
                description = f"{node.name} = ({children_names}) = ({children_values}) = {bool_to_str(node.value)}."

        return description


class DeductionDAG(TreeDAG):
    def __init__(self, ops, uni_ops, depth, probs=[0.16, 0.51, 0.33], num_children_per_node=2):
        self.ops = ops
        self.uni_ops = uni_ops
        self.probs = probs
        
        super().__init__(depth, num_children_per_node, extra_links_per_node=0, add_cycles=0)
    
    def generate_tree(self, depth):
        assert depth >= 1
        # Base case: If depth is 0, generate a leaf node
        if depth == 1:
            name = next(self.name_generator)
            value = random.choice([True, False])  # Randomly assign True or False
            return Node(value, None, name, [])

        # Otherwise, generate an internal node
        else:  
            op = np.random.choice(self.ops, p=self.probs)

            if op in self.uni_ops:
                children = [self.generate_tree(depth-1)]
                value = True if children[0].value == False else "N/A"

            else:
                num_of_children = self.num_children_per_node
                children = [self.generate_tree(depth - 1) for _ in range(num_of_children)]
                child_values = [child.value for child in children]
                
                if op == 'and':
                    if "N/A" in child_values:
                        value = "N/A"
                    else:
                        value = True if all(child_values) else "N/A"
                elif op == 'or':
                    if True in child_values:
                        value = True
                    else:
                        value = "N/A"

            return Node(value, op, next(self.name_generator), children)
    
    def check_link_constraint(self, father_node, child_node):
        "Adding links are not allowed in deduction DAGs"
        return False

    def update_values(self):
        return True


class DeductionDAGDescriber(TreeDAGDescriber):
    def __init__(self, dag_obj, ops, uni_ops, add_rand_desc=0):
        self.ops = ops
        self.uni_ops = uni_ops
        super().__init__(dag_obj, add_rand_desc, delete_desc=0)
    
    def describe_question_node(self, node):
        if node.op == None:
            description = f"{node.name} is {'True' if node.value else 'False'}."

        else:
            if node.op == 'not':
                description = f"(NOT {node.children[0].name}) -> {node.name}."
            elif node.op == 'and':
                child_descriptions = ' and '.join(child.name for child in node.children)
                description = f"({child_descriptions}) -> {node.name}."
            elif node.op == 'or':
                child_descriptions = ' or '.join(child.name for child in node.children)
                description = f"({child_descriptions}) -> {node.name}."
        
        return description

    def describe_inference_node(self, node):
        
        def bool_to_str(val):
            if val == "N/A":
                return "N/A"
            return 'True' if val else 'False'
        
        if node.op == None:
            description = f"{node.name} is {bool_to_str(node.value)}."
        else:
            if node.op == 'not':
                description = f"(NOT {node.children[0].name}) = (NOT {bool_to_str(node.children[0].value)}) -> {node.name}.\n"
                if node.children[0].value == True:
                    description += f"The value of the premise (NOT {bool_to_str(node.children[0].value)}) is {'False' if node.children[0].value else 'True'}. "
                    description += f"Thus, the value of {node.name} cannot be deduced, and is set to N/A."
                elif node.children[0].value == "N/A":
                    description += f"The value of {node.name} cannot be deduced, and is set to N/A."
                else:
                    description += f"The premise (NOT {bool_to_str(node.children[0].value)}) is True, thus, the value of {node.name} is {bool_to_str(node.value)}."
            
            elif node.op == 'and':
                description = ""
                premise_name = "(" + " AND ".join(child.name for child in node.children) + ")"
                premise_value = "(" + " AND ".join(bool_to_str(child.value) for child in node.children) + ")"

                description +=  premise_name + " = " + premise_value + " -> " + node.name + "."
                if "N/A" in [child.value for child in node.children]:
                    description += f"\nGiven at least one of the children's value is N/A, the value of {node.name} cannot be deduced and is set to N/A."
                elif all([child.value for child in node.children]):
                    description += f"\nThe premise {premise_value} is True, thus, the value of {node.name} is True."
                else:
                    description += f"\nThe premise {premise_value} is False, thus, the value of {node.name} can not be deduced and is set to N/A."
            
            elif node.op == 'or':
                description = ""
                premise_name = "(" + " OR ".join(child.name for child in node.children) + ")"
                premise_value = "(" + " OR ".join(bool_to_str(child.value) for child in node.children) + ")"
                description += premise_name + " = " + premise_value + " -> " + node.name + "."
                
                if True in [child.value for child in node.children]:
                    description += f"\nThe premise {premise_value} is True, thus, the value of {node.name} is True."
                elif "N/A" in [child.value for child in node.children]:
                    description += f"\nGiven none of the children are True and at least one is N/A, thus, the value of premise is N/A. Thus, the value of {node.name} cannot be deduced and is set to N/A."
                else:
                    description += f"\nThe premise {premise_value} is False, thus, the value of {node.name} cannot be deduced and is set to N/A."

        return description



class AbductionDAG(TreeDAG):
    def __init__(self, ops, uni_ops, depth, probs=[0.16, 0.51, 0.33], num_children_per_node=2):
        self.ops = ops
        self.uni_ops = uni_ops
        self.probs = probs
        
        super().__init__(depth, num_children_per_node, extra_links_per_node=0, add_cycles=0)
    
    def generate_tree(self, depth):
        assert depth >= 1
        # Base case: If depth is 1, generate a leaf node
        if depth == 1:
            name = next(self.name_generator)
            return Node(None, None, name, [])  # No value assignment

        # Otherwise, generate an internal node
        else:
            op = np.random.choice(self.ops, p=self.probs)
            children = []
            if op in self.uni_ops:
                children.append(self.generate_tree(depth-1))
            else:
                children = [self.generate_tree(depth-1) for _ in range(self.num_children_per_node)]
            
            return Node(None, op, next(self.name_generator), children)

    def _find_path(self, start, end):
        """Helper function to find the path from start to end node."""
        visited = set()
        stack = [(start, [start])]

        while stack:
            (vertex, path) = stack.pop()
            if vertex not in visited:
                if vertex == end:
                    return path
                visited.add(vertex)
                for child in vertex.children:
                    stack.append((child, path + [child]))
        return []

    def abduct_node_value(self, start, end):

        def bool_to_str(val):
            if val == "N/A":
                return "N/A"
            return 'True' if val == True else 'False'

        path = self._find_path(start, end)
        if not path:
            return "N/A", "Since we cannot find a path from start to end, thus the answer is N/A."

        # The description will be a list that captures the abductive process.
        descriptions = []

        for index in range(len(path) - 1):
            current_node = path[index]
            next_node = path[index + 1]
            
            if current_node.op == 'not':
                premise_name = f"(NOT {next_node.name})"
                
            elif current_node.op == 'and':
                premise_name = "(" + " AND ".join(child.name for child in current_node.children) + ")"

            elif current_node.op == 'or':
                premise_name = "(" + " OR ".join(child.name for child in current_node.children) + ")"
            
            description = f"{premise_name} -> {current_node.name} = {bool_to_str(current_node.value)}.\n"
            description += f"Given {current_node.name} is {bool_to_str(current_node.value)}, "

            if current_node.value == "N/A" or current_node.value == True:
                description += f"the value of {next_node.name} can not be abduced and is set to be N/A."
                next_node.value = "N/A"
            else:
                description += f"the value of premise {premise_name} is False,"
                if current_node.op == "not":
                    description += f" thus, the value of {next_node.name} is abduced as True."
                    next_node.value = True
                elif current_node.op == "and":
                    description += f" however, because the operation is 'AND', the value of {next_node.name} can not be abduced and is set to N/A."
                    next_node.value = "N/A"
                else:
                    description += f" thus, the value of {next_node.name} is abduced as False."
                    next_node.value = False


            descriptions.append(description)
        # The final value of the end node after the abductive process.
        value = path[-1].value

        # Combine all descriptions into a single string.
        combined_description = "\n".join(descriptions)

        return value, combined_description

    def check_link_constraint(self, father_node, child_node):
        "Adding links are not allowed in abduction DAGs"
        return False

    def update_values(self):
        return True


class AbductionDAGDescriber(TreeDAGDescriber):
    def __init__(self, dag_obj: AbductionDAG, ops, uni_ops, add_rand_desc=0):
        self.ops = ops
        self.uni_ops = uni_ops
        super().__init__(dag_obj, add_rand_desc, delete_desc=0)
    
    def describe_question_node(self, node):
        if node.op == None:
            description = ""

        else:
            if node.op == 'not':
                description = f"(NOT {node.children[0].name}) -> {node.name}."
            elif node.op == 'and':
                child_descriptions = ' and '.join(child.name for child in node.children)
                description = f"({child_descriptions}) -> {node.name}."
            elif node.op == 'or':
                child_descriptions = ' or '.join(child.name for child in node.children)
                description = f"({child_descriptions}) -> {node.name}."
        
        return description
    
    def describe_abduction(self):
        start = self.dag_obj.root
        start.value = np.random.choice([True, False], p=[0.07, 0.93])

        leaf_nodes = []
        for node in self.dag_obj.nodes:
            if len(node.children) == 0:
                leaf_nodes.append(node)
        
        end = np.random.choice(leaf_nodes)
        
        answer, answer_desc = self.dag_obj.abduct_node_value(start, end)
        
        return f"Given {start.name} is {'True' if start.value else 'False'}, what is the value of {end.name}?", answer, answer_desc

    def describe_inference_steps(self):
        return self.answer_desc

    def describe_answer(self):
        return self.answer
    
    def describe_question(self):
        descriptions = self._describe_question()
        abduction_desc, answer, answer_desc = self.describe_abduction()
        self.answer = answer
        self.answer_desc = answer_desc
        for order, desc in descriptions.items():
            descriptions[order] = re.sub('\n+', '\n', desc) + "\n" + abduction_desc
        
        return descriptions
