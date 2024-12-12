from math import log10, ceil

# Function to calculate the number of digits in a number
def num_digits(num: int):
    if num == 0:
        return 1
    return ceil(log10(num + 1))

# Function to split a number down the middle if it has an even number of digits
def split_int_down_middle(num: int):
    nd = num_digits(num)
    assert nd % 2 == 0, "Behavior not defined for splitting numbers with an odd number of digits"
    middle_power_of_10 = nd // 2
    left = num // 10**middle_power_of_10
    right = num % 10**middle_power_of_10
    return (left, right)

# Function to apply transformation rules to a number
def apply_rules(num):
    if num == 0:
        return [1]
    elif num_digits(num) % 2 == 0:
        return split_int_down_middle(num)
    else:
        return [num * 2024]

# Class to manage unique node IDs and labels
class NodeManager:
    def __init__(self):
        self.counter = 0
        self.nodes = {}  # Maps unique ID to label

    def add_node(self, label):
        unique_id = f"node{self.counter}"
        self.nodes[unique_id] = label
        self.counter += 1
        return unique_id

# Set to store unique edges (parent -> child) as tuples of unique IDs
edges = set()

# Initialize NodeManager
node_manager = NodeManager()

# Starting node
start_label = 0
start_id = node_manager.add_node(start_label)

# Recursive function to traverse the tree and record edges
def traverse(num, unique_id, depth):
    if depth == 0:
        return
    children = apply_rules(num)
    for child_num in children:
        child_id = node_manager.add_node(child_num)
        edges.add((unique_id, child_id))
        # **Stop traversing if the child node's label is 0**
        if child_num != 0:
            traverse(child_num, child_id, depth - 1)

# Function to generate Mermaid diagram syntax from the recorded edges and nodes
def generate_mermaid(nodes, edges):
    mermaid = "graph TD\n"
    for parent_id, child_id in edges:
        parent_label = nodes[parent_id]
        child_label = nodes[child_id]
        mermaid += f"    {parent_id}([{parent_label}]) --> {child_id}([{child_label}])\n"
    return mermaid

# Parameters
max_depth = 14 # Adjust as needed

# Perform the traversal starting from the root node
traverse(start_label, start_id, max_depth)

# Generate and print the Mermaid diagram code
mermaid_code = generate_mermaid(node_manager.nodes, edges)
print(mermaid_code)

