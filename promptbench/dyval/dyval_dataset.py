from tqdm import tqdm
from .dyval_utils import process_dyval_training_sample

class DyValDataset:
    def __init__(self, 
                 dataset_type,
                 is_trainset=False,
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
        self.is_trainset = is_trainset
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
        data = {}
        # data = {"descriptions": {}, "answers": []}
        for _ in tqdm(range(self.num_samples)):
            sample = self._generate_sample()
            processed = {}
            # first record all the keys except "descriptions"
            for key in sample.keys():
                if key != "descriptions":
                    processed[key] = sample[key]
            
            for key in sample.keys():
                if key == "descriptions":
                    for order, desc in sample[key].items():     
                        if order not in data:
                            data[order] = []
                        new = processed.copy()
                        new["descriptions"] = desc
                        data[order].append(new)
        
        return data

    def get_fewshot_examples(self, shots):
        if shots == 1:
            examples = f"\n\nHere is an example of problem related to {self.dataset_type} task and their corresponding inference steps."
        else:
            examples = f"\n\nHere are {shots} examples of problems related to {self.dataset_type} task and their corresponding inference steps."
        if self.dataset_type in ["linear_equation"]:
            shots = 1
        if self.dataset_type in ["max_sum_path"]:
            shots = 2
        for _ in range(shots):
            if self.dataset_type in ["linear_equation"]:
                depth = 2
            else:
                depth = 3
            sample = self._generate_sample(is_trainset=True, num_nodes_per_sample=7, min_links_per_node=1, max_links_per_node=3, depth=depth, num_children_per_node=2, extra_links_per_node=0, add_rand_desc=0, delete_desc=0, add_cycles=0)
            examples += "\n\nQ:\n" + sample["descriptions"]["random"]
            examples += "\n\nA:\n" + sample["inferences"]
        
        return examples
    
    def _generate_sample(self, **kwargs):
        sample = {}
        dataset_type = kwargs.get("dataset_type", self.dataset_type)
        is_trainset = kwargs.get("is_trainset", self.is_trainset)
        num_nodes_per_sample = kwargs.get("num_nodes_per_sample", self.num_nodes_per_sample)
        min_links_per_node = kwargs.get("min_links_per_node", self.min_links_per_node)
        max_links_per_node = kwargs.get("max_links_per_node", self.max_links_per_node)
        depth = kwargs.get("depth", self.depth)
        num_children_per_node = kwargs.get("num_children_per_node", self.num_children_per_node)
        extra_links_per_node = kwargs.get("extra_links_per_node", self.extra_links_per_node)
        add_rand_desc = kwargs.get("add_rand_desc", self.add_rand_desc)
        delete_desc = kwargs.get("delete_desc", self.delete_desc)
        add_cycles = kwargs.get("add_cycles", self.add_cycles)
        num_dags = kwargs.get("num_dags", self.num_dags)

        if dataset_type in ["arithmetic", "bool_logic"]:
            from .DAG.math_dag import ArithmeticDAG, ArithmeticDAGDescriber
            from .DAG.logic_dag import BoolDAG, BoolDAGDescriber

            if dataset_type == "arithmetic":
                ops = ["+", "-", "*", "/", "sqrt", "**"]
                uni_ops = ["sqrt", "**"]
                DAGType, DAGDescriber = ArithmeticDAG, ArithmeticDAGDescriber

            elif dataset_type == "bool_logic":
                ops = ['and', 'or', 'not']
                uni_ops = ['not']
                DAGType, DAGDescriber = BoolDAG, BoolDAGDescriber

            dag = DAGType(ops, uni_ops, depth, num_children_per_node, extra_links_per_node, add_cycles)
            describer = DAGDescriber(dag, ops, uni_ops, add_rand_desc, delete_desc)

        elif dataset_type == "linear_equation":
            from .DAG.math_dag import LinearEq
            ops = ["+", "-", "*", "/", "sqrt", "**"]
            uni_ops = ["sqrt", "**"]
            describer = LinearEq(ops, uni_ops, depth, num_dags, num_children_per_node, extra_links_per_node, add_rand_desc)

        elif dataset_type in ["deductive_logic", "abductive_logic"]:
            from .DAG.logic_dag import DeductionDAG, DeductionDAGDescriber, AbductionDAG, AbductionDAGDescriber
            if dataset_type == "deductive_logic":
                DAGType, DAGDescriber = DeductionDAG, DeductionDAGDescriber
                probs = [0.2, 0.6, 0.2]
            elif dataset_type == "abductive_logic":
                DAGType, DAGDescriber = AbductionDAG, AbductionDAGDescriber
                probs = [0.07, 0.66, 0.27]
            
            ops = ['and', 'or', 'not']
            uni_ops = ['not']
            dag = DAGType(ops, uni_ops, depth, probs, num_children_per_node)
            describer = DAGDescriber(dag, ops, uni_ops, add_rand_desc)

        elif dataset_type in ["reachability", "max_sum_path"]:
            from .DAG.code_dag import CodeDAG, CodeDAGDescriber
            # CodeDAG is not allowed to add cycles and delete descriptions
            dag = CodeDAG(num_nodes_per_sample, min_links_per_node, max_links_per_node)
            describer = CodeDAGDescriber(dag, dataset_type, add_rand_desc)
        
        question = describer.describe_question()
        answer = describer.describe_answer()
        sample["descriptions"] = question
        sample["answers"] = answer
        if dataset_type in ["arithmetic", "bool_logic", "deductive_logic"]:
            sample["vars"] = dag.root.name
        
        if is_trainset:
            inference_desc = describer.describe_inference_steps()
            sample["inferences"] = inference_desc
            sample = process_dyval_training_sample(sample, dataset_type)

        return sample