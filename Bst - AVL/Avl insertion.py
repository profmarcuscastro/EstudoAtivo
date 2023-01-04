#The above tree is AVL because the differences between the 
#heights of left and right 
#subtrees for every node are less than or equal to 1.

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):
 
    #Height
    def getHeight(self,root):
        if not root:
            return 0
        return root.height

    #balance of node
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    # Recursive function to insert key in
    # subtree rooted with 
    def insert(self,root,key):

        #step1 - As BST
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key)
        # in the end return root
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.left))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

         # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def preOrder(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
 
 
# Driver program to test above function
myTree = AVL_Tree()
root = None
 
root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)
 
"""The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50"""
 
# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")
myTree.preOrder(root)
print()
 
# This code is co
        
