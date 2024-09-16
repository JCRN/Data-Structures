import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        # the value at the current node
        self.value = value
        # reference to this node's left child
        self.left = None
        # reference to this node's right child
        self.right = None
    def insert(self, value):
        # check if the new node's value is less than our current node's value
        if value < self.value:
            # if there's no left child here already, place the new node here
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # otherwise, repeat the process!
                self.left.insert(value)
        # check if the new node's value is greater than or equal to our 
        # current node's value
        elif value >= self.value:
            # if there's no right child here already, place the new node here
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                # otherwise, repeat the process!
                self.right.insert(value)
    def contains(self, target):
        # if the value of the current node we're looking at matches the target, we've found a match!
        if self.value == target:
            return True
        # if there's a left child, call its contains method to repeat the whole process
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        # if there's a right child, call its contains method to repeat the whole process
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
    def get_max(self):
        # no point in doing anything if our tree is empty
        if not self:
            return None
        # Recursive approach
        # if not self.right:
        #   return self.value
        # return self.right.get_max()
        # initialize max_value variable; this will be updated as we traverse the tree
        max_value = self.value
        # get a reference to the node we're currently at; update this variable as we traverse the tree
        current = self
        # check to see if we're still at a valid tree node
        while current:
            # if current value is greater than max_value, update the max_value
            if current.value > max_value:
                max_value = current.value
            # move on to the next right node in the tree
            current = current.right
        return max_value
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
    def iterative_depth_first_for_each(self, cb):
        stack = []
        stack.append(self)
        while len(stack):
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)
    def breadth_first_for_each(self, cb):
        q = []
        q.append(self)
        while len(q):
            current_node = q.pop(0)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node.value)
    # Pre-order DFT
    def pre_order_dft(self, node):
        if node is None:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)
    # In-order DFT (Can be used to copy the tree)
    def in_order_dft(self, node):
        if node is None:
            return
        self.in_order_dft(node.left)
        print(node.value)
        self.in_order_dft(node.right)
    # Post-order DFT (Can be used to delete the tree)
    def post_order_dft(self, node):
        if node is None:
            return
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)
    # Graph Like BFT
    def bft_print(self, starting_node):
        """
        Print each vertex in breadth-first order
        beginning from starting_node.
        """
        qq = Queue()
        qq.enqueue(starting_node)
        while qq.len() > 0:
            current = qq.dequeue()
            print(current.value)
            if current.left:
                qq.enqueue(current.left)
            if current.right:
                qq.enqueue(current.right)
    # Graph Like DFT
    def dft_print(self, starting_node):
        """
        Print each vertex in breadth-first order
        beginning from starting_node.
        """
        s = Stack()
        s.push(starting_node)
        while s.len() > 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.push(current.left)
            if current.right:
                s.push(current.right)