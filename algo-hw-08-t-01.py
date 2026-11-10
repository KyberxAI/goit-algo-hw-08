'''
Завдання 1

Напишіть алгоритм (функцію), який знаходить найменше значення
у двійковому дереві пошуку або в AVL-дереві.
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
'''

from avl_tree import insert

# Функція знаходження мінімального значення в AVL-дереві


def tree_min_value(node):
    if node is None:
        return None
    current = node
    while current.left is not None:
        current = current.left
    return current.key


# Приклад
avl_tree_01 = None
keys = [4, 10, 8, 6, 1, 5, 7, 9, 2, 3]

for key in keys:
    avl_tree_01 = insert(avl_tree_01, key)
print(avl_tree_01)

print(f"Мінімальне значення в дереві: "
      f"{tree_min_value(avl_tree_01)}\n")
