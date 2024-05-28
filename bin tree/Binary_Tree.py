class BinTree:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def addroot(self, n):
        if self.root is None:
            self.root = self.Node(n)
        else:
            raise Exception("Root already exists")

    def addleftchild(self, n, p=None):
        if p is None:
            raise ValueError("Parent key required")
        parent = self._find_node(self.root, p)
        if parent is None:
            raise ValueError("Parent key not found")
        if parent.left is None:
            parent.left = self.Node(n)
        else:
            raise Exception("Left child already exists")

    def addrightchild(self, n, p=None):
        if p is None:
            raise ValueError("Parent key required")
        parent = self._find_node(self.root, p)
        if parent is None:
            raise ValueError("Parent key not found")
        if parent.right is None:
            parent.right = self.Node(n)
        else:
            raise Exception("Right child already exists")

    def _find_node(self, node, key):
        if node is None:
            return None
        if node.data == key:
            return node
        left_result = self._find_node(node.left, key)
        if left_result:
            return left_result
        return self._find_node(node.right, key)

    def display(self):
        self._display_aux(self.root, 0)
        print()

    def _display_aux(self, node, level):
        if node is not None:
            print("    " * level, node.data, sep="")
            self._display_aux(node.left, level + 1)
            self._display_aux(node.right, level + 1)

    def iterative_traversal_by_queue(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.data, end=" ")
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        print()


def main():
    # Create a new BinTree
    t = BinTree()

    # Add the root element to the BinTree
    t.addroot(10)

    # Add child nodes to the BinTree
    t.addleftchild(30, 10)
    t.addrightchild(70, 10)
    t.addleftchild(90, 30)
    t.addrightchild(60, 30)
    t.addleftchild(50, 90)
    t.addleftchild(40, 70)
    t.addrightchild(20, 70)

    # Display BinTree data
    print("Display BinTree data")
    t.display()

    # Perform iterative traversal
    print("Iterative traversal by queue:")
    t.iterative_traversal_by_queue()


main()
