class node:
    def __init__(self,info):
        self.data=info
        self.left=None
        self.right=None
class BinaryTree:
    def createnode(self,data):
        return node(data)

    def insert(self,node,data):
        if node is None:
            return self.createnode(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node

    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.data,end="  ")
            self.inorder(node.right)

    def preorder(self,node):
        if node is not None:
            print(node.data,end="  ")
            self.inorder(node.left)
            self.inorder(node.right)

    def postorder(self,node):
        if node is not None:
            self.inorder(node.left)
            self.inorder(node.right)
            print(node.data,end="  ")


    def height(self,node):
        if node is None:
            return -1
        return max(self.height(node.left),self.height(node.right))+1

    def level(self,node):
        q=[]
        q.append(node)
        while len(q) > 0:
            root = q.pop(0)
            print(root,end='  ')
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    def swap(self,node):
        if node is None:
            return 0
        temp= node.left
        node.left = node.right
        node.right=temp

    def invert(self,node):
        if node is None:
            return
        q=[]
        q.append(node)
        while len(q) >0:
            cur = q.pop()
            self.swap(cur)
            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)

    def findpairs(self,node,k):
        self.values = set()
        return self.Deepsearch(node,k,self.values)
    def Deepsearch(self,node,k,values):
        if node is None:
            return False
        if (k - node.data) in values:
            return True

        self.values.add(node.data)
        return self.Deepsearch(node.left,k,self.values) or self.Deepsearch(node.right,k,self.values)



def main():
    tree = BinaryTree()
    root=tree.createnode(5)
    print(root.data)
    tree.insert(root,10)
    tree.insert(root,6)
    tree.insert(root,3)
    print("In_Order: ",end = " ")
    tree.inorder(root)
    print()
    print("Pre_Order: ",end = " ")
    tree.preorder(root)
    print()
    print("Post_Order: ",end = " ")
    tree.postorder(root)
    print()
    print("Height: ", tree.height(root))
    print()
    tree.invert(root)
    print()
    print("In_Order: ",end = " ")
    tree.inorder(root)
    print()
    print(tree.findpairs(root,13))
main()
