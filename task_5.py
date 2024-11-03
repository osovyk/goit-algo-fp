import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


# Клас для вузла дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


# Додає зв'язки між вузлами та їх позиції
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (x - 1 / 2 ** layer, y - 1)
            add_edges(graph, node.left, pos, x=x - 1 / 2 ** layer, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (x + 1 / 2 ** layer, y - 1)
            add_edges(graph, node.right, pos, x=x + 1 / 2 ** layer, y=y - 1, layer=layer + 1)
    return graph


# Малює дерево з кольорами вузлів
def draw_tree(tree_root, step, pos):
    tree = nx.DiGraph()
    tree = add_edges(tree, tree_root, pos)

    # Отримуємо кольори та значення вузлів для відображення
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(f"Step {step}")
    plt.show()


# Алгоритм обходу в ширину (BFS) з візуалізацією
def bfs(root):
    queue = deque([root])  # Використовуємо чергу
    step = 1
    pos = {root.id: (0, 0)}

    total_nodes = count_nodes(root)

    while queue:
        node = queue.popleft()
        # Змінюємо колір поточного вузла
        node.color = get_color(step, total_nodes)

        # Візуалізуємо дерево на кожному кроці
        draw_tree(root, step, pos)

        # Додаємо дочірні вузли до черги
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        step += 1


# Алгоритм обходу в глибину (DFS) з візуалізацією
def dfs(root):
    stack = [root]  # Використовуємо стек
    step = 1
    pos = {root.id: (0, 0)}

    total_nodes = count_nodes(root)

    while stack:
        node = stack.pop()
        # Змінюємо колір поточного вузла
        node.color = get_color(step, total_nodes)

        # Візуалізуємо дерево на кожному кроці
        draw_tree(root, step, pos)

        # Додаємо дочірні вузли до стека
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        step += 1

# Змінюємо колір від темного до світлого
def get_color(step, total_steps):
    intensity = int(255 * (step / total_steps))
    return f'#{intensity:02x}{intensity:02x}ff'

# Функція для підрахунку кількості вузлів у дереві
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    bfs(root)
    # dfs(root)
