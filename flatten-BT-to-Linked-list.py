'''

flatten a binary tree to a linkedlist in preorder traversal
We use the right pointer in the treenode as the next point in list node

EX:
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
'''

class Solution:
    # param: root of the binary tree
    # return: nothing

    def flatten(self, root):
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        p = root
        if p.left == None:
            return
        p = p.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None
