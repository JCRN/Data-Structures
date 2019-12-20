import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # Need to traverse the tree to find the spot to insert
    def insert(self, value):
        # If value is less than self.value go left, make a new tree/node if empty otherwise,
        # keep going (recursion)
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # If greater than or equal to then go right, make a new tree/node if empty otherwise,
        # keep going (recursion)
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value) 

    # Return True if the tree contains the value
    # False if it does not
    # Start from root and traverse the tree
    # Can stop at the first instance of a value
    def contains(self, target):
        # If target === self.value, return it otherwise,
        # go left or right based on smaller or bigger
        if (target is self.value):
            return True
        elif (target < self.value):
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise, return self.value
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is not None:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)

        while q.len() > 0:
            cur_node = q.dequeue()
            print(cur_node.value)
            if cur_node.left is True:
                q.enqueue(cur_node.left)
            if cur_node.right is True:
                q.enqueue(cur_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
    
        while stack.len() > 0:
            cur_node = stack.pop()
            print(cur_node.value)
            if cur_node.left is True:
                stack.push(cur_node.left)
            if cur_node.right is True:
                stack.push(cur_node.right)
            
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
