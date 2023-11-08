import random
from .dag import GeneralDAG
from .describer import GeneralDAGDescriber

class CodeDAG(GeneralDAG):

    def __init__(self, num_nodes, min_links_per_node=1, max_links_per_node=3):
        super().__init__(num_nodes, min_links_per_node, max_links_per_node, add_cycles=0)

    def reachability(self, start, end):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node == end:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(child for child in node.children if child not in visited)

        return False

    def max_sum_path(self, start, end):
        queue = [(start, start.value)]  # Each element in the queue is a tuple (node, current_sum)
        max_sum = float('-inf')

        while queue:
            node, cur_sum = queue.pop(0)

            if node == end:
                max_sum = max(max_sum, cur_sum)
                continue

            for child in node.children:
                queue.append((child, cur_sum + child.value))

        return max_sum if max_sum != float('-inf') else "N/A"


class CodeDAGDescriber(GeneralDAGDescriber):
    def __init__(self, dag_obj: CodeDAG, dataset_type, add_rand_desc=0):
        super().__init__(dag_obj, add_rand_desc, delete_desc=0)
        self.dataset_type = dataset_type

    def describe_reachability(self):
        start, end = random.sample(self.dag_obj.nodes, 2)
        reachable = self.dag_obj.reachability(start, end)
        answer = "Yes" if reachable else "No"
        return f"Can you reach {end.name} starting from {start.name}?", answer
    
    def describe_max_sum_path(self):
        # Randomly select two distinct nodes
        node1, node2 = random.sample(self.dag_obj.nodes, 2)
        
        if self.dag_obj.sorted_node_names.index(node1.name) < self.dag_obj.sorted_node_names.index(node2.name):
            start, end = node2, node1
        else:
            start, end = node1, node2
            
        answer = self.dag_obj.max_sum_path(start, end)

        return f"What's the maximum sum path from {start.name} to {end.name}?", answer
    
    def describe(self):
        descriptions = self._describe()
        if self.dataset_type == "reachability":
            desc, answer = self.describe_reachability()

        elif self.dataset_type == "max_sum_path":
            value_desc = ""
            for node in self.dag_obj.nodes:
                value_desc += f"The value of {node.name} is {node.value}\n"
            desc, answer = self.describe_max_sum_path()            
            desc = value_desc + desc
        
        for order, description in descriptions.items():
            descriptions[order] = description + "\n" + desc

        return {"descriptions": descriptions, "answers": answer}
