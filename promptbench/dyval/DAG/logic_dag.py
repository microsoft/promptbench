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
    
    def describe_node(self, node):
        if node.op is None:
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
                value = not children[0].value if children[0].value != "N/A" else "N/A"

            else:
                num_of_children = self.num_children_per_node
                children = [self.generate_tree(depth - 1) for _ in range(num_of_children)]
                child_values = [child.value for child in children]
                
                if "N/A" in child_values:
                    value = "N/A"
                elif op == 'and':
                    value = True if all(child_values) else "N/A"
                elif op == 'or':
                    value = True if any(child_values) else "N/A"

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
    
    def describe_node(self, node):
        if node.op is None:
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
    
    def abduct_node_value(self, start, end):
        if start == end:
            return start.value

        visited = set()
        queue = [(start, start.value)]  # Each element in the queue is a tuple (node, current_value)
        
        while queue:
            node, value = queue.pop(0)

            # If we reach the end node, return the value
            if node == end:
                return value

            if node not in visited:
                visited.add(node)
                if value == "N/A" or node.op == 'or':
                    child_value = "N/A"
                elif node.op == 'not':
                    child_value = not value
                elif node.op == 'and':
                    child_value = value

                for child in node.children:
                    queue.append((child, child_value))

        # If end node is not reached
        return "N/A"

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
    
    def describe_node(self, node):
        if node.op is None:
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
        start.value = np.random.choice([True, False], p=[0.1, 0.9])

        leaf_nodes = []
        for node in self.dag_obj.nodes:
            if len(node.children) == 0:
                leaf_nodes.append(node)
        
        end = np.random.choice(leaf_nodes)
        
        if start.value:
            answer = "N/A"
        else:
            answer = self.dag_obj.abduct_node_value(start, end)
        
        return f"Given {start.name} is {'True' if start.value else 'False'}, what is the value of {end.name}?", answer

    def describe(self):
        descriptions = self._describe()
        abduction_desc, answer = self.describe_abduction()
        for order, desc in descriptions.items():
            descriptions[order] = re.sub('\n+', '\n', desc) + "\n" + abduction_desc
        
        return {'descriptions': descriptions, 'answers': answer}        