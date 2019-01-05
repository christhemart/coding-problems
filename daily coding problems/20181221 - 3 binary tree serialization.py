'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes 
the tree into a string, and deserialize(s), which deserializes the string back 
into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))

# first cheese try, just serialize as python code recursively, 
# deserialize using eval(), bit of a security issue

def serialize(node):
    serial = 'Node(' + "'" + node.val + "',"
    serial += serialize(node.left)  if node.left  != None else 'None'
    serial += ',' 
    serial += serialize(node.right) if node.right != None else 'None'
    serial += ')'
    return serial

def deserialize(serial):
    return eval(serial)

assert deserialize(serialize(node)).left.left.val == 'left.left'

# second try without eval(), less text recursive serialize, 
# deserialize by parsing with a stack

def serialize(node):
    serial = node.val + ','
    serial += serialize(node.left)  if node.left  != None else ''
    serial += ',' 
    serial += serialize(node.right) if node.right != None else ''
    serial += ',;'
    return serial
    
def deserialize(serial):
    stack = []
    split = serial.split(',')
    for item in split:
        if item == ';':
            right = stack.pop()
            left  = stack.pop() 
            stack.append(
                Node(
                    stack.pop(), 
                    left  if left  != '' else None, 
                    right if right != '' else None))
        else:
            stack.append(item)
    return stack.pop()

assert deserialize(serialize(node)).left.left.val == 'left.left'
