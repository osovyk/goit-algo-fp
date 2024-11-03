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
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Функція для вставки у бінарну мін-купу (для мінімізації значень)
def insert_min_heap(root, key):
    # Використаємо рекурсивний алгоритм для вставки елементів у бінарну мін-купу
    if root is None:
        return Node(key)
    # Вставляємо вузол у ліве або праве піддерево за принципом рівномірного заповнення
    if root.left is None:
        root.left = insert_min_heap(root.left, key)
    elif root.right is None:
        root.right = insert_min_heap(root.right, key)
    else:
        if height(root.left) <= height(root.right):
            root.left = insert_min_heap(root.left, key)
        else:
            root.right = insert_min_heap(root.right, key)

    # Підтримка властивостей мін-купи (батько менше або рівний дочірніх вузлів)
    if root.left and root.left.val < root.val:
        root.left.val, root.val = root.val, root.left.val
    if root.right and root.right.val < root.val:
        root.right.val, root.val = root.val, root.right.val

    return root


# Функція для обчислення висоти дерева
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


if __name__ == "__main__":
    # Створення бінарної купи
    root = Node(10)
    root = insert_min_heap(root, 15)
    root = insert_min_heap(root, 30)
    root = insert_min_heap(root, 40)
    root = insert_min_heap(root, 50)
    root = insert_min_heap(root, 100)
    root = insert_min_heap(root, 40)

    # Візуалізуємо дерево купи
    draw_tree(root)
