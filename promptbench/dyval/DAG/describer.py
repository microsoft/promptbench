# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import random
from .dag import BaseDAG, GeneralDAG, TreeDAG

class BaseDAGDescriber:
    """
    Base class for creating descriptions of Directed Acyclic Graphs (DAGs).

    This class provides methods to traverse and describe DAGs in various orders and to manipulate descriptions.

    Parameters:
    -----------
    dag_obj : BaseDAG
        The DAG object to be described.
    add_rand_desc : int, optional
        The number of random descriptions to add.
    delete_desc : int, optional
        The number of descriptions to delete.

    Methods:
    --------
    describe_question_node(node)
        Describes a node in the DAG for question formation.
    generate_rand_description()
        Generates random descriptions based on the DAG type.
    topological_traversal(desc_func)
        Traverses the DAG in topological order and applies a description function.
    reverse_topological_traversal(topo_desc)
        Reverses the order of topological descriptions.
    random_traversal(topo_desc)
        Shuffles the topological descriptions randomly.
    add_rand_description(desc)
        Adds random descriptions to the existing description list.
    delete_description(desc)
        Deletes descriptions from the existing description list.
    _describe_question()
        Describes the DAG for question formation in various traversal orders.
    """

    def __init__(self, dag_obj: BaseDAG, add_rand_desc=0, delete_desc=0):
        self.dag_obj = dag_obj
        self.add_rand_desc = add_rand_desc
        self.delete_desc = delete_desc
    
    def describe_question_node(self, node):
        # Describe a node in the DAG to form a question for test set
        # return a string
        raise NotImplementedError
    
    def generate_rand_description(self):
        raise NotImplementedError

    def topological_traversal(self, desc_func):
        node_names = self.dag_obj.topological_sort()

        descriptions = []
        for node_name in node_names:
            for node in self.dag_obj.nodes:
                if node.name == node_name:
                    descriptions.append(desc_func(node))
        return descriptions
    
    def reverse_topological_traversal(self, topo_desc):
        reversed_desc = topo_desc.copy()
        reversed_desc.reverse()
        return reversed_desc

    def random_traversal(self, topo_desc):
        rand_desc = topo_desc.copy()
        random.shuffle(rand_desc)
        return rand_desc
    
    def add_rand_description(self, desc):
        # Generate a random description, the generation depends on the type of DAG
        for _ in range(self.add_rand_desc):
            rand_desc = self.generate_rand_description()
            for cur_desc in rand_desc:
                desc.insert(random.randint(0, len(desc)), cur_desc)

    def delete_description(self, desc):
        for _ in range(self.delete_desc):
            desc.pop(random.randint(0, len(desc) - 1))
    
    def _describe_question(self):
        descriptions = {}

        topo_desc = self.topological_traversal(self.describe_question_node)
        
        self.delete_description(topo_desc)
        self.add_rand_description(topo_desc)

        reversed_desc = self.reverse_topological_traversal(topo_desc)
        rand_desc = self.random_traversal(topo_desc)
        descriptions["topological"] = "\n".join(topo_desc)
        descriptions["reversed"] = "\n".join(reversed_desc)
        descriptions["random"] = "\n".join(rand_desc)
        
        return descriptions


class GeneralDAGDescriber(BaseDAGDescriber):
    """
    A describer class for GeneralDAG instances.

    Inherits from BaseDAGDescriber and provides specific implementations for describing GeneralDAG nodes.

    Parameters:
    -----------
    dag_obj : GeneralDAG
        The GeneralDAG instance to describe.
    add_rand_desc : int, optional
        The number of random descriptions to add (inherited).
    delete_desc : int, optional
        The number of descriptions to delete (inherited).

    Methods:
    --------
    describe_question_node(node)
        Provides a description for a GeneralDAG node.
    generate_rand_description()
        Generates random descriptions specific to GeneralDAG.
    describe_answer()
        Describes the DAG for answer formation (not implemented yet).
    """

    def __init__(self, dag_obj: GeneralDAG, add_rand_desc=0, delete_desc=0):
        super().__init__(dag_obj, add_rand_desc, delete_desc)

    def describe_question_node(self, node):
        child_names = ", ".join([child.name for child in node.children])
        description = f"{node.name} points to: ({child_names if child_names else 'None'})."
        return description

    def generate_rand_description(self):
        rand_desc = []
        nodes = self.dag_obj.generate_dag(num_nodes=3)
        for node in nodes:
            rand_desc.append(self.describe_question_node(node))
        
        return rand_desc

    def describe_answer(self):
        # Describe the DAG to form a answer for training set
        # return a string
        raise NotImplementedError


class TreeDAGDescriber(BaseDAGDescriber):
    """
    A describer class for TreeDAG instances.

    Inherits from BaseDAGDescriber and provides specific implementations for describing TreeDAG nodes.

    Parameters:
    -----------
    dag_obj : TreeDAG
        The TreeDAG instance to describe.
    add_rand_desc : int, optional
        The number of random descriptions to add (inherited).
    delete_desc : int, optional
        The number of descriptions to delete (inherited).
    trainset : bool
        Indicates if the describer is used for training set generation.

    Methods:
    --------
    describe_inference_node(node)
        Provides a description for a TreeDAG node for inference.
    generate_rand_description()
        Generates random descriptions specific to TreeDAG.
    describe_inference_steps()
        Describes the inference steps based on the DAG's topology.
    describe_answer()
        Provides the answer based on the root value of the TreeDAG.
    describe_question()
        Describes the DAG for question formation in various traversal orders.
    """

    def __init__(self, dag_obj: TreeDAG, add_rand_desc=0, delete_desc=0, trainset=False):
        self.trainset = trainset
        super().__init__(dag_obj, add_rand_desc, delete_desc)
    
    def describe_inference_node(self, node):
        # Describe a node in the DAG to form a answer for training set
        # return a string
        raise NotImplementedError
    
    def generate_rand_description(self):
        rand_desc = []
        root = self.dag_obj.generate_tree(depth=2)
        rand_desc.append(self.describe_question_node(root))
        for child in root.children:
            rand_desc.append(self.describe_question_node(child))

        return rand_desc
    
    def describe_inference_steps(self):
        return "\n".join(self.topological_traversal(self.describe_inference_node))

    def describe_answer(self):
        return self.dag_obj.root.value
    
    def describe_question(self):
        return self._describe_question()