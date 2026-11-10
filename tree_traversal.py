

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# # Створення дерева
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)


# Реалізація прямого обходу дерева:
def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# print("Прямий обхід:")
# preorder_traversal(root)


# Реалізація центрового обходу дерева:
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)


# print("Центровий обхід:")
# inorder_traversal(root)


# Реалізація зворотного обходу дерева:
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)


# print("Зворотний обхід:")
# postorder_traversal(root)
