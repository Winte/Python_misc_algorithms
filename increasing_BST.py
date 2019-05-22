"""
Increasing Order Search Tree
Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.
Ex:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

"""


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorderTraversal(root):
            res = []    # nodes values will be stored here
            if root:    # if there is any root, otherwise it's None
                # go to the left and run the function again
                res = inorderTraversal(root.left)
                # when there's no left, add value to the list
                res.append(root.val)
                # add right side to the values from left
                res = res + inorderTraversal(root.right)
            return res

        nodes = inorderTraversal(root)      # returns values in-order

        # now the inly thing is to add them as required
        result_tree = TreeNode(nodes[0])        # creates new tree
        node = result_tree      # set node as the beginning of the tree

        # it's important to start iterate from the second element, that's way range(1, len(nodes))
        for i in range(1, len(nodes)):
            # always add new node to the right
            node.right = TreeNode(nodes[i])
            node = node.right       # set node to the one on the right

        return result_tree
