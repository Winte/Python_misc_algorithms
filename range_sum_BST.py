"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
Ex:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

    def sum_tree(root, L, R, total):
      if root.left:       # in case there is a left noode
        sum_tree(root.left, L, R, total)        # call sum_tree on the left node

      if root.val >= L and root.val <= R:     # if value between L and R inclusive 
        total.append(root.val)      # add it to the list
      if root.right:
        sum_tree(root.right, L, R, total)       # if there's right node, call function on it

      return total        # when there isn't right and left node, just return a list 

    total = []
    return sum(sum_tree(root, L, R, total))     # return the sum of the list        