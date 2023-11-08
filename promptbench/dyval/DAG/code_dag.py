import random
from .dag import GeneralDAG
from .describer import GeneralDAGDescriber

class CodeDAG(GeneralDAG):

    def __init__(self, num_nodes, min_links_per_node=1, max_links_per_node=3):
        super().__init__(num_nodes, min_links_per_node, max_links_per_node, add_cycles=0)
    
    def reachability(self, start, end):
        descriptions = []
        visited = set()
        stack = [start]
        
        descriptions.append(f"Starting the search process from node {start.name} with the goal to reach node {end.name}.")
        
        while stack:
            node = stack.pop()
            
            descriptions.append(f"Checking node {node.name}.")
            
            if node == end:
                descriptions.append(f"Successfully reached the target node {end.name}.")
                return True, "\n".join(descriptions)
            if node not in visited:
                visited.add(node)
                unvisited_children = [child for child in node.children if child not in visited]
                if unvisited_children:
                    child_names = ', '.join(child.name for child in unvisited_children)
                    descriptions.append(f"Exploring children of node {node.name}: {child_names}.")
                else:
                    descriptions.append(f"Node {node.name} has no unvisited children. Moving back.")
                stack.extend(unvisited_children)
            else:
                descriptions.append(f"Node {node.name} has already been visited. Skipping.")
        
        descriptions.append(f"Exhausted all possible paths without reaching node {end.name}.")
        return False, "\n".join(descriptions)

    def max_sum_path(self, start, end):
        descriptions = []  # This will hold our natural language descriptions.
        queue = [(start, start.value)]  # Each element in the queue is a tuple (node, current_sum)
        max_sum = float('-inf')
        
        descriptions.append(f"Starting the search for the maximum sum path from node {start.name} to node {end.name}.")
        
        while queue:
            node, cur_sum = queue.pop(0)
            
            descriptions.append(f"Reaching node {node.name} with current sum of {cur_sum}.")
            
            if node == end:
                if cur_sum > max_sum:
                    max_sum = max(max_sum, cur_sum)
                    descriptions.append(f"Found a path to node {end.name} with a new maximum sum of {cur_sum}.")
                else:
                    descriptions.append(f"Found a path to node {end.name} with a sum of {cur_sum}, which is less than current maximum sum.")
                
            else:
                if len(node.children) == 0:
                    descriptions.append(f"Node {node.name} has no children. Moving back.")
                else:
                    child_names = ', '.join(child.name for child in node.children)
                    descriptions.append(f"Now, we explore the children of node {node.name}: {child_names}.")
                    
                    for child in node.children:
                        queue.append((child, cur_sum + child.value))
        
        if max_sum != float('-inf'):
            descriptions.append(f"The maximum sum from node {start.name} to node {end.name} is {max_sum}.")
        else:
            descriptions.append(f"There is no path from node {start.name} to node {end.name}.")
        
        return max_sum if max_sum != float('-inf') else "N/A", "\n".join(descriptions)


class CodeDAGDescriber(GeneralDAGDescriber):
    def __init__(self, dag_obj: CodeDAG, dataset_type, add_rand_desc=0):
        super().__init__(dag_obj, add_rand_desc, delete_desc=0)
        self.dataset_type = dataset_type

    def describe_reachability(self):
        start, end = random.sample(self.dag_obj.nodes, 2)
        answer, inference_steps = self.dag_obj.reachability(start, end)
        return f"Can {end.name} be reached starting from {start.name}?", answer, inference_steps
    
    def describe_max_sum_path(self):
        # Randomly select two distinct nodes
        node1, node2 = random.sample(self.dag_obj.nodes, 2)
        
        if self.dag_obj.sorted_node_names.index(node1.name) < self.dag_obj.sorted_node_names.index(node2.name):
            start, end = node2, node1
        else:
            start, end = node1, node2
            
        answer, inference_steps = self.dag_obj.max_sum_path(start, end)

        return f"What's the maximum sum path from {start.name} to {end.name}?", answer, inference_steps
    
    def describe_question(self):
        descriptions = self._describe_question()
        if self.dataset_type == "reachability":
            desc, answer, inference_steps = self.describe_reachability()

        elif self.dataset_type == "max_sum_path":
            value_desc = ""
            for node in self.dag_obj.nodes:
                value_desc += f"The value of {node.name} is {node.value}\n"
            desc, answer, inference_steps = self.describe_max_sum_path()            
            desc = value_desc + desc
        
        self.inference_steps = inference_steps
        
        for order, description in descriptions.items():
            descriptions[order] = description + "\n" + desc

        self.answer = answer
        return descriptions

    def describe_answer(self):
        return self.answer

    def describe_inference_steps(self):
        return self.inference_steps