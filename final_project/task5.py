import uuid

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)


def generate_rgb_color(step, total_steps):
    r = int((255 * step) / total_steps)
    g = int((255 * (total_steps - step)) / total_steps)
    b = 0
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def depth_first_search(node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    node.color = generate_rgb_color(len(visited), 10)  # Змінюємо колір вузла
    if node.left:
        depth_first_search(node.left, visited)
    if node.right:
        depth_first_search(node.right, visited)

def breadth_first_search(root):
    visited = set()
    queue = []
    queue.append(root)
    root.color = generate_rgb_color(1, 10)  # Змінюємо колір кореневого вузла
    visited.add(root)
    while queue:
        node = queue.pop(0)
        if node.left:
            node.left.color = generate_rgb_color(len(visited), 10)  # Змінюємо колір вузла
            queue.append(node.left)
            visited.add(node.left)
        if node.right:
            node.right.color = generate_rgb_color(len(visited), 10)  # Змінюємо колір вузла
            queue.append(node.right)
            visited.add(node.right)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Виконуємо обхід у глибину
depth_first_search(root)
draw_tree(root)

# Виконуємо обхід у ширину
breadth_first_search(root)
draw_tree(root)
