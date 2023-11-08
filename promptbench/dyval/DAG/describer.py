import random
from .dag import BaseDAG, GeneralDAG, TreeDAG

class BaseDAGDescriber:
    def __init__(self, dag_obj: BaseDAG, add_rand_desc=0, delete_desc=0):
        self.dag_obj = dag_obj
        self.add_rand_desc = add_rand_desc
        self.delete_desc = delete_desc
    
    def describe_node(self, node):
        # Describe a node in the DAG
        # return a string
        raise NotImplementedError

    def generate_rand_description(self):
        raise NotImplementedError

    def topological_traversal(self):
        node_names = self.dag_obj.topological_sort()

        descriptions = []
        for node_name in node_names:
            for node in self.dag_obj.nodes:
                if node.name == node_name:
                    descriptions.append(self.describe_node(node))
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
    
    def _describe(self):
        descriptions = {}

        topo_desc = self.topological_traversal()
        
        self.delete_description(topo_desc)
        self.add_rand_description(topo_desc)

        reversed_desc = self.reverse_topological_traversal(topo_desc)
        rand_desc = self.random_traversal(topo_desc)
        descriptions["topological"] = "\n".join(topo_desc)
        descriptions["reversed"] = "\n".join(reversed_desc)
        descriptions["random"] = "\n".join(rand_desc)
        
        return descriptions


class GeneralDAGDescriber(BaseDAGDescriber):
    def __init__(self, dag_obj: GeneralDAG, add_rand_desc=0, delete_desc=0):
        super().__init__(dag_obj, add_rand_desc, delete_desc)

    def describe_node(self, node):
        child_names = ", ".join([child.name for child in node.children])
        description = f"{node.name} points to: ({child_names if child_names else 'None'})."
        return description

    def generate_rand_description(self):
        rand_desc = []
        nodes = self.dag_obj.generate_dag(num_nodes=3)
        for node in nodes:
            rand_desc.append(self.describe_node(node))
        
        return rand_desc


class TreeDAGDescriber(BaseDAGDescriber):
    def __init__(self, dag_obj: TreeDAG, add_rand_desc=0, delete_desc=0):
        super().__init__(dag_obj, add_rand_desc, delete_desc)
    
    def generate_rand_description(self):
        rand_desc = []
        root = self.dag_obj.generate_tree(depth=2)
        rand_desc.append(self.describe_node(root))
        for child in root.children:
            rand_desc.append(self.describe_node(child))

        return rand_desc
    
    def describe(self):
        descriptions = self._describe()
        answer = self.dag_obj.root.value
        var = self.dag_obj.root.name
        if self.delete_desc > 0 or self.dag_obj.add_cycles > 0:
            answer = "N/A"
        
        return {'descriptions': descriptions, 'answers': answer, 'vars': var}