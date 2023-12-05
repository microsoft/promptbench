# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import random
import itertools
import nltk
nltk.download('words')
from nltk.corpus import words


class Node:
    """
    Represents a node in a graph or a tree structure.

    Attributes:
    -----------
    value : Any
        The value stored in the node.
    op : Any, optional
        The operation or function associated with the node.
    name : str, optional
        The unique identifier of the node.
    children : list of Node, optional
        The children nodes of this node.
    """
    def __init__(self, value=None, op=None, name=None, children=None):
        self.value = value
        self.op = op
        self.children = children if children is not None else []
        self.name = name


class BaseDAG:
    """
    Base class for Directed Acyclic Graph (DAG) structures.

    This class provides foundational functionality for DAG operations, including node management,
    topological sorting, and cycle detection.

    Attributes:
    -----------
    symbols_set : str
        A string of alphabets used in generating unique node names.
    forbidden_names : set of str
        A set of names that are not allowed for nodes.
    name_generator : generator
        A generator for producing unique node names.
    nodes : list of Node
        The list of nodes in the DAG.
    add_cycles : int
        The number of cycles to add to the DAG.

    Methods:
    --------
    get_node_by_name(name)
        Retrieves a node by its name.
    topological_sort()
        Performs topological sorting on the DAG nodes.
    check_link_constraint(father_node, child_node)
        Checks if a link between two nodes is valid.
    generate_cycles()
        Introduces cycles in the DAG.
    _form_cycle(start, end)
        Checks if adding a link forms a cycle.
    _generate_name()
        Generates a unique name for a node.
    _get_reachable_nodes(start)
        Finds all nodes reachable from a given starting node.
    """
    def __init__(self, add_cycles=0):
        self.symbols_set = 'abcdefghijklmnopqrstuvwxyz'
        self.forbidden_names = {word for word in set(words.words()) if len(word) < 4}
        self.name_generator = self._generate_name()
        self.nodes = []
        self.add_cycles = add_cycles
    
    def get_node_by_name(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def topological_sort(self):
        visited_name = set()
        results = []

        # Recursive DFS function
        def visit(node):
            if node.name not in visited_name:
                visited_name.add(node.name)
                for child in set(node.children):  # Using set to ensure unique children
                    visit(child)
                results.append(node.name)

        # Start DFS from each node to handle potential disconnected subgraphs
        for node in self.nodes:
            if node not in visited_name:
                visit(node)

        return results
    
    def check_link_constraint(self, father_node, child_node):
        return True

    def generate_cycles(self):
        """Introduce cycles in the DAG."""
        random.shuffle(self.nodes)
        for _ in range(self.add_cycles):
            successful_add = False
            for node in self.nodes:
                if successful_add:
                    break
                # Make sure that the node has children and its children are not leaf nodes
                if len(node.children) == 0 or all(len(child.children) == 0 for child in node.children):
                    continue
                
                # print(node.name)
                        
                # Find all reachable nodes from the selected node
                reachable_nodes = self._get_reachable_nodes(node)
                random.shuffle(reachable_nodes)
            
                # Pick one of the reachable nodes and create a link from the node to the selected reachable node
                for target in reachable_nodes:
                    # print("Target ", target.name)
                    # Make sure that we link two non-leaf nodes and the link is valid.
                    if len(target.children) > 0 and self.check_link_constraint(target, node):
                        successful_add = True
                        target.children.append(node)
                        break

    def _form_cycle(self, start, end):
        """Check if adding a link from start to end would form a cycle."""
        visited = set()
        stack = [end]

        while stack:
            node = stack.pop()
            if node.name == start.name:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(child for child in node.children if child not in visited)
        
        return False

    def _generate_name(self):
        for comb in itertools.product(self.symbols_set, repeat=3):
            name = ''.join(comb)
            if name not in self.forbidden_names:
                yield name

    def _get_reachable_nodes(self, start):
        """Find all nodes reachable from a given starting node."""
        visited = set()
        stack = [start]

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(child for child in current.children)
        
        visited.remove(start)  # We don't count the starting node
        return list(visited)


class GeneralDAG(BaseDAG):
    """
    Represents a general Directed Acyclic Graph with customizable parameters.

    Inherits from BaseDAG and allows for specifying the number of nodes and the range of links per node.

    Parameters:
    -----------
    num_nodes : int
        The number of nodes in the DAG.
    min_links_per_node : int
        The minimum number of links each node can have.
    max_links_per_node : int
        The maximum number of links each node can have.
    add_cycles : int, optional
        The number of cycles to be added to the DAG (default is 0).

    Methods:
    --------
    generate_dag(num_nodes)
        Generates the DAG with the specified number of nodes.
    """
    def __init__(self, num_nodes, min_links_per_node=1, max_links_per_node=3, add_cycles=0):
        super().__init__(add_cycles)
        
        self.num_nodes = num_nodes
        self.min_links_per_node = min_links_per_node
        self.max_links_per_node = max_links_per_node
        
        self.nodes = self.generate_dag(self.num_nodes)
        self.sorted_node_names = self.topological_sort()
        # Adding cycles
        self.generate_cycles()

    def generate_dag(self, num_nodes):
        nodes = []
        # Create all nodes first without any links
        for _ in range(num_nodes):
            new_node = Node(value=random.randint(1, 10), name=next(self.name_generator))
            nodes.append(new_node)
        
        # Once all nodes are created, iterate and decide links
        for node in nodes:
            potential_children = [potential_node for potential_node in nodes if potential_node.name != node.name]
            num_links = random.randint(self.min_links_per_node, min(self.max_links_per_node, len(potential_children)))
            for _ in range(num_links):
                child = random.choice(potential_children)
                if not self._form_cycle(node, child):
                    node.children.append(child)
                potential_children.remove(child)

        return nodes


class TreeDAG(BaseDAG):
    """
    Represents a Directed Acyclic Graph built from a tree structure.

    This class extends BaseDAG and allows for the creation of a DAG from a tree, with additional
    properties like depth, number of children per node, and extra links per node.

    Parameters:
    -----------
    depth : int
        The depth of the tree to generate.
    num_children_per_node : int
        The number of children each node can have.
    extra_links_per_node : int
        The number of extra links per node.
    add_cycles : int, optional
        The number of cycles to be added to the DAG (default is 0).

    Methods:
    --------
    generate_tree(depth)
        Generates the tree structure.
    update_values()
        Updates the value of each node after adding links.
    check_link_constraint(father_node, child_node)
        Defines constraints for link addition between nodes.
    check_uni_ops()
        Checks if all nodes' operations are unary.
    generate_dag()
        Generates the DAG based on the tree.
    collect_nodes(node)
        Collects all nodes from a given starting node.
    """
    def __init__(self, depth, num_children_per_node=2, extra_links_per_node=1, add_cycles=0):
        super().__init__(add_cycles)
        self.num_children_per_node = num_children_per_node
        self.extra_links_per_node = extra_links_per_node
        
        # The DAG may not valid after adding links.
        while True:
            self.root = self.generate_tree(depth)
            self.nodes = self.collect_nodes(self.root)
            valid = self.generate_dag()
            # if we need add cycles, we should check if all nodes's ops are uni ops.
            if self.add_cycles > 0 and self.check_uni_ops():
              valid = False  
            if valid:
                # Adding cycles
                self.generate_cycles()
                break             
    
    """
    Function that generate a tree first.
    """
    def generate_tree(self, depth):
        raise NotImplementedError
    
    """
    After adding links, we should update the value of each node.
    """
    def update_values(self):
        raise NotImplementedError
        # Update the value of nodes in DAG.
        # Return True or False

    """
    Define the constraints to nodes which can not be added with links.
    E.g., for math problem, a unary operation node can not have links.
    """
    def check_link_constraint(self, father_node, child_node):
        raise NotImplementedError
        # return True or False

    """
    Check if all nodes' ops are uni ops.
    When we add cycles, we need to make sure that at least one node's ops is not unary ops.
    """
    def check_uni_ops(self):
        all_uni_ops = True
        for node in self.nodes:
            if node.op not in self.uni_ops:
                all_uni_ops = False
                break

        return all_uni_ops

    """
    Generate a DAG based on a tree.
    """
    def generate_dag(self):
        
        for node in self.nodes:
            node_names = [node.name for node in self.nodes]
            random.shuffle(node_names)
            for _ in range(self.extra_links_per_node):
                if len(node.children) > 0:                    
                    for target_name in node_names:
                        target = self.get_node_by_name(target_name)
                        if self.check_link_constraint(node, target) and not self._form_cycle(node, target):
                            node.children.append(target)
                            break
        
        self.sorted_node_names = self.topological_sort()
        valid = self.update_values()
        return valid

    """
    Collect nodes.
    """
    def collect_nodes(self, node):
        nodes = []
        stack = [node]

        while stack:
            current = stack.pop()
            nodes.append(current)
            stack.extend(child for child in current.children)

        return nodes

