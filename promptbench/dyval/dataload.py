from tqdm import tqdm
"""

dataset[0]

__getitem__ implementation?
since we have 3 orders here...
dataset["topological"][0]?
"""
class Dataset:
    def __init__(self, 
                 dataset_type, 
                 num_samples=100, 
                 num_nodes_per_sample=10,
                 min_links_per_node=1,
                 max_links_per_node=3,
                 depth=3, 
                 num_children_per_node=2, 
                 extra_links_per_node=1, 
                 add_rand_desc=0, 
                 delete_desc=0,
                 add_cycles=0,
                 num_dags=1,
                ):
        
        self.dataset_type = dataset_type
        self.num_samples = num_samples
        self.num_nodes_per_sample = num_nodes_per_sample
        self.min_links_per_node = min_links_per_node
        self.max_links_per_node = max_links_per_node

        self.depth = depth
        self.num_children_per_node = num_children_per_node
        self.extra_links_per_node = extra_links_per_node

        self.add_rand_desc = add_rand_desc
        self.delete_desc = delete_desc
        self.add_cycles = add_cycles

        self.num_dags = num_dags

        self.data = self.create_dataset()
    
    def __len__(self):
        return self.num_samples
    
    def __getitem__(self, key):
        return self.data[key]
    
    def create_dataset(self):
        data = {"descriptions": {}, "answers": []}
        for _ in tqdm(range(self.num_samples)):
            sample = self._generate_sample()
            for key in sample.keys():
                if key not in data:
                    data[key] = []

                if key == "descriptions":
                    for order, desc in sample[key].items():
                        if order not in data[key]:
                            data[key][order] = []
                        data[key][order].append(desc)
                else:
                    data[key].append(sample[key])
        
        return data

    def get_fewshot_examples(self, shots):
        examples = f"Here are {shots} examples."
        for _ in range(shots):
            sample = self._generate_sample()
            raise NotImplementedError
        
        return examples
    
    def _generate_sample(self):
        sample = {}

        if self.dataset_type in ["arithematic", "bool_logic"]:
            from DAG.math_dag import ArithematicDAG, ArithematicDAGDescriber
            from DAG.logic_dag import BoolDAG, BoolDAGDescriber

            if self.dataset_type == "arithematic":
                ops = ["+", "-", "*", "/", "sqrt", "**"]
                uni_ops = ["sqrt", "**"]
                DAGType, DAGDescriber = ArithematicDAG, ArithematicDAGDescriber

            elif self.dataset_type == "bool_logic":
                ops = ['and', 'or', 'not']
                uni_ops = ['not']
                DAGType, DAGDescriber = BoolDAG, BoolDAGDescriber

            dag = DAGType(ops, uni_ops, self.depth, self.num_children_per_node, self.extra_links_per_node, self.add_cycles)
            describer = DAGDescriber(dag, ops, uni_ops, self.add_rand_desc, self.delete_desc)

        elif self.dataset_type == "linear_equation":
            from DAG.math_dag import LinearEq
            ops = ["+", "-", "*", "/", "sqrt", "**"]
            uni_ops = ["sqrt", "**"]
            describer = LinearEq(ops, uni_ops, self.depth, self.num_dags, self.num_children_per_node, self.extra_links_per_node, self.add_rand_desc)

        elif self.dataset_type in ["deductive_logic", "abductive_logic"]:
            from DAG.logic_dag import DeductionDAG, DeductionDAGDescriber, AbductionDAG, AbductionDAGDescriber
            if self.dataset_type == "deductive_logic":
                DAGType, DAGDescriber = DeductionDAG, DeductionDAGDescriber
                probs = [0.14, 0.53, 0.33]
            elif self.dataset_type == "abductive_logic":
                DAGType, DAGDescriber = AbductionDAG, AbductionDAGDescriber
                probs = [0.62, 0.1, 0.28]
            
            ops = ['and', 'or', 'not']
            uni_ops = ['not']
            dag = DAGType(ops, uni_ops, self.depth, probs, self.num_children_per_node)
            describer = DAGDescriber(dag, ops, uni_ops, self.add_rand_desc)

        elif self.dataset_type in ["reachability", "max_sum_path"]:
            from DAG.code_dag import CodeDAG, CodeDAGDescriber
            # CodeDAG is not allowed to add cycles and delete descriptions
            dag = CodeDAG(self.num_nodes_per_sample, self.min_links_per_node, self.max_links_per_node)
            describer = CodeDAGDescriber(dag, self.dataset_type, self.add_rand_desc)
        
        sample = describer.describe()
        # print("topological order:")
        # print(sample["descriptions"]["topological"])
        # print()
        # print("reversed order:")
        # print(sample["descriptions"]["reversed"])
        # print()
        # print("random order:")
        # print(sample["descriptions"]["random"])
        # print()
        # print("answer:")
        # print(sample["answers"])
        return sample
    

if __name__ == "__main__":
    # dataset = Dataset("max_sum_path", num_samples=1, num_nodes_per_sample=7, min_links_per_node=1, max_links_per_node=3, add_rand_desc=0)
    # dataset = Dataset("linear_equation", num_samples=1, num_dags=2, depth=2, num_children_per_node=2, extra_links_per_node=0, add_rand_desc=0)
    dataset = Dataset("abductive_logic", num_samples=1000, depth=3, num_children_per_node=2, add_rand_desc=0)
    true, false, na = 0, 0, 0
    for ans in dataset["answers"]:
        if ans == True:
            true += 1
        elif ans == False:
            false += 1
        else:
            na += 1
    
    print(f"true: {true}, false: {false}, na: {na}")
