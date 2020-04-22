import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        #these are nodes
        self.value = value
        self.left = None
        self.right = None

    # # Insert the given value into the tree / Recursive
    # #Does not return anything
    # def insert(self, value):
    #     #need base case
    #     if self is None: #in an empty spot in the tree
    #         self = BinarySearchTreeNode(value)

    #     else: #Self is a node with a value
    #         #compare value to the value at this node
    #         if value < self.value:
    #             #move to the left
    #             self.left.insert(value)
    #     #if we are not at base case, move toward base case

    def insert(self, value):
        #Self.left and/or self.right need to be valid nodes for us to call insert

        if value < self.value:
            #check to see if valid node
            if self.left:
                self.left.insert(value)
                #left side is empty
            else:
                #we have found a valid parking spot
                self.left = BinarySearchTree(value)
        #otherwise, value >= self.value
        else: 
            #check if right is valid node
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #Is equal to root
        if target == self.value:
            return True

        #is less than root
        elif target < self.value:
            #If there is nothing to the left of root. Not in BST
            if self.left is None:
                return False
            #select value to the left and start over
            return self.left.contains(target)

        #is greater than root
        elif target > self.value:
            #if nothing to the right, NOt in BST
            if self.right is None:
                return False
            #select value to the right and start over
            return self.right.contains(target)
                
        


    # Return the maximum value found in the tree
    def get_max(self):
        #Get root value
        if self.right:
            return self.right.get_max()
        else:
            return self.value
        #Check to see if there is a self.right since that will be bigger. 

        #Go until there is no self.right. that value will be the highest in the tree

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #Set CB function for the value
        cb(self.value)
        #if there is a value to the right, do the cb function
        if self.right:
            self.right.for_each(cb)
        #if there is a value to the left, do the cb function
        if self.left:
            self.left.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
