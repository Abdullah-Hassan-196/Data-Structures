class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None

    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):
        if root is None:
            return self.Node(val)
        if val > root.data:
            root.right = self._insert(root.right, val)
        elif val < root.data:
            root.left = self._insert(root.left, val)
        return root

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, root, val):
        if root is None:
            return False
        if val == root.data:
            return True
        elif val > root.data:
            return self._search(root.right, val)
        return self._search(root.left, val)

    def traverse_inorder(self):
        self._traverse_inorder(self.root)
        print()

    def _traverse_inorder(self, root):
        if root:
            self._traverse_inorder(root.left)
            print(root.data, end=" ")
            self._traverse_inorder(root.right)

    def traverse_preorder(self):
        self._traverse_preorder(self.root)
        print()

    def _traverse_preorder(self, root):
        if root:
            print(root.data, end=" ")
            self._traverse_preorder(root.left)
            self._traverse_preorder(root.right)

    def traverse_postorder(self):
        self._traverse_postorder(self.root)
        print()

    def _traverse_postorder(self, root):
        if root:
            self._traverse_postorder(root.left)
            self._traverse_postorder(root.right)
            print(root.data, end=" ")


def main():
    b = BST()
    b.insert(30)
    b.insert(40)
    b.insert(10)
    b.insert(35)
    b.insert(60)
    b.insert(90)
    b.insert(0)
    b.insert(800)

    print("Inorder Traversal:")
    b.traverse_inorder()

    print("Preorder Traversal:")
    b.traverse_preorder()

    print("Postorder Traversal:")
    b.traverse_postorder()

    print("Search for 35:", b.search(35))
    print("Search for 350:", b.search(350))


main()
