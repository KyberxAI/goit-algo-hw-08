'''Завдання 2

Напишіть алгоритм(функцію),
який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві.
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
'''

from avl_tree import *


def avlsum(tree_node):
    if tree_node is None:
        return 0

    return tree_node.key + avlsum(tree_node.left) + avlsum(tree_node.right)


# Приклад використання avlsum
# Створення дерева
avl_tree_02 = None
keys = [4, 10, 8, 6, 1, 5, 7, 9, 2, 3]

for key in keys:
    avl_tree_02 = insert(avl_tree_02, key)
# print(avl_tree_02)

# Вивід результату avlsum
print(f"Сума елементів дерева: "
      f"{avlsum(avl_tree_02)}\n")

print(f"Сума елементів списку keys (контрольна): "
      f"{sum(keys)}\n")
