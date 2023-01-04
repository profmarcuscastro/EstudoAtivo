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
        
