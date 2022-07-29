# create binary tree

#node
class Node:
    
    def __init__(self,data):
        self.left = None
        self.right= None
        self.data = data

    #insert node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else :
                    self.right.insert(data)
        else:
            self.data = data
    #print tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.insert(43)
root.insert(15)
print(root.printTree())