"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# First "trivial" easy recursive solution

class Solution:
  def preorder(self, root: 'Node') -> List[int]:
    if not root:
      return []       # return empty list in case of empty Node object
    result = [root.val]     # add first node
    for child in root.children:     # iterate through all children
      result.extend(self.preorder(child))     # repeat the process but root is now child
                          # this way you can go through the whole tree
    return result

# Second Iterative solution

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = [root]
        result = []
        
        while stack:
            cur = stack.pop(0)
            if cur:
                result.append(cur.val)
                stack = cur.children + stack
            
        return result

       
       