'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 '''

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def unival_count(tree, parent):
    count = 0

    if tree.left is None and tree.right is None:
        return 1, True if tree.value == parent.value else False
    else:
        unival = True

        if tree.left is not None:
            n, matching = unival_count(tree.left, tree)
            count += n
            unival = unival and matching

        if tree.right is not None:
            n, matching = unival_count(tree.right, tree)
            count += n
            unival = unival and matching

        if unival is True:
            count += 1

        return count, True if tree.value == parent.value and unival is True else False


my_tree = BinaryTree(0,
    BinaryTree(1),
    BinaryTree(0,
        BinaryTree(1,
            BinaryTree(1),
            BinaryTree(1)),
        BinaryTree(0)))
assert unival_count(my_tree, my_tree)[0] == 5
