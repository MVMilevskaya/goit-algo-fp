import uuid
import matplotlib.pyplot as plt
import networkx as nx


class Node:
 
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Дерево"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(plt.title)
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


def generate_color_gradient(step, total_steps):

    if total_steps <= 1:
        return "#1296F0"

    intensity = int(
        20 + (180 / (total_steps - 1)) * step
    )
    r = min(255, intensity + 20)
    g = min(255, intensity + 80)
    b = 255

    return f"#{r:02X}{g:02X}{b:02X}"

def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def dfs_visualize(root):
    if not root:
        return

    total_nodes = count_nodes(root)
    stack = [root]
    visited_order = []

    while stack:
        current = stack.pop()
        if current not in visited_order:
            visited_order.append(current)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    for index, node in enumerate(visited_order):
        node.color = generate_color_gradient(index, total_nodes)

    draw_tree(root, title="Обхід у глибину (DFS - Стек)")


from collections import deque

def bfs_visualize(root):
    if not root:
        return

    total_nodes = count_nodes(root)
    queue = deque([root])
    visited_order = []

    while queue:
        current = queue.popleft()
        visited_order.append(current)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    for index, node in enumerate(visited_order):
        node.color = generate_color_gradient(index, total_nodes)

    draw_tree(root, title="Обхід у ширину (BFS - Черга)")

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    dfs_visualize(root)

    root_bfs = Node(0)
    root_bfs.left = Node(4)
    root_bfs.left.left = Node(5)
    root_bfs.left.right = Node(10)
    root_bfs.right = Node(1)
    root_bfs.right.left = Node(3)

    bfs_visualize(root_bfs)