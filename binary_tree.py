# example to create a sorted binary tree
class Tree(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def printTree(self):
        
        # if there is smaller data, print that
        if (self.left != None):
            self.left.printTree()
        
        # print my own data
        print (self.data)

        # if there's bigger data, print that last
        if (self.right != None):
            self.right.printTree()
    
    # add a new branch to the tree
    def addData(self, value):
        
        # if the value is <= value of this node, it goes left
        if (value <= self.data):
            if (self.left == None):
                self.left = Tree(value)
            else: # if there's already a left branch, add it to that one
                self.left.addData(value)
                
        # if the value is > value of this node, it goes right
        else:
            if (self.right == None): # if there's already a right branch, add it to that one
                self.right = Tree(value)
            else:
                self.right.addData(value)
                


# create a list of random numbers up to maximum_value
maximum_value = 1000000
length_of_list = 1000000

from random import sample
alist = sample(range(maximum_value), length_of_list)
# alist = [2, 1, 3]

# start the timer
import time
start_time = time.clock()

# create the root of the tree
root = Tree(alist[0])
# add all the numbers to the tree
for i in range(1, len(alist)):
    root.addData(alist[i])

print ("It took " + str(time.clock() - start_time) + " seconds")

# traverse and print the tree
# root.printTree()
