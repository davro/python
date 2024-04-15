import graphviz

class BTreeNode:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []

class BTree:
    def __init__(self):
        self.root = BTreeNode()
        self.graph = graphviz.Digraph(comment='B-Tree')

    def visualize(self, node=None):
        if node is None:
            node = self.root

        # Visualize the current node with keys
        key_str = ', '.join(map(str, node.keys))
        self.graph.node(str(id(node)), label=f'[{key_str}]')

        if node.children:
            # Recursively visualize child nodes
            for child in node.children:
                self.visualize(child)

                # Visualize the edge between the current node and its child
                self.graph.edge(str(id(node)), str(id(child)))

# Example Usage
b_tree = BTree()

# Creating a more complex B-tree structure
root = BTreeNode(keys=[10, 30, 50], children=[
    BTreeNode(keys=[5, 8]),
    BTreeNode(keys=[20, 25]),
    BTreeNode(keys=[40, 45, 48]),
    BTreeNode(keys=[60, 70])
])

b_tree.root = root

# Visualize the B-tree
b_tree.visualize()
b_tree.graph.render(filename='b_tree_complex_visualization', format='png', cleanup=True)

