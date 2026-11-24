"""Library Catalog — Recursive Binary Tree Traversals.

Enter the tree in level-order form. Use # for a missing child.
Example: A B C D E # F
This creates:
        A
       / \\
      B   C
     / \\   \\
    D   E   F
"""


from collections import deque


class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def build_level_order(self, values):
        """Build a general binary tree from level-order values; '#' means None."""
        if not values or values[0] == "#":
            self.root = None
            return

        self.root = Node(values[0])
        queue = deque([self.root])
        index = 1

        while queue and index < len(values):
            current = queue.popleft()

            if index < len(values) and values[index] != "#":
                current.left = Node(values[index])
                queue.append(current.left)
            index += 1

            if index < len(values) and values[index] != "#":
                current.right = Node(values[index])
                queue.append(current.right)
            index += 1

    def inorder(self, node):
        if node is None:
            return []
        return (self.inorder(node.left)
                + [node.book]
                + self.inorder(node.right))

    def preorder(self, node):
        if node is None:
            return []
        return ([node.book]
                + self.preorder(node.left)
                + self.preorder(node.right))

    def postorder(self, node):
        if node is None:
            return []
        return (self.postorder(node.left)
                + self.postorder(node.right)
                + [node.book])


def main():
    print("LIBRARY CATALOG — BINARY TREE TRAVERSALS")
    print("Enter book titles/IDs in level order, separated by spaces.")
    print("Use # to represent a missing child.")
    raw = input("Tree values: ").strip()

    values = raw.split() if raw else []
    tree = BinaryTree()
    tree.build_level_order(values)

    if tree.root is None:
        print("The binary tree is empty.")
        return

    print("\nInorder   (Left, Root, Right):", " -> ".join(tree.inorder(tree.root)))
    print("Preorder  (Root, Left, Right):", " -> ".join(tree.preorder(tree.root)))
    print("Postorder (Left, Right, Root):", " -> ".join(tree.postorder(tree.root)))


if __name__ == "__main__":
    main()