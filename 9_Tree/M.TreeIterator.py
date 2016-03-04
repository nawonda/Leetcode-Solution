'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
Try to optimize the additional space complexity apart from the amortized time complexity.
'''

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.path = []

        next_node = self.root
        while next_node:
            self.path.append(next_node)
            next_node = next_node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.path) != 0

    # @return an integer, the next smallest number
    def next(self):
        res = self.path.pop()
        if res.right:
            succ = res.right
            while succ:
                self.path.append(succ)
                succ = succ.left
        return res.val