# BinarySearchTree: A binary search tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_bst.py.
# Nick Morris

class BinarySearchTree:
   
   def __init__(self, key = None):
      self.left = None
      self.right = None
      self.parent = None
      self.key = key

   def insert(self, node):
      if node.key <= self.key and self.left == None:
         self.left = node
      elif node.key > self.key and self.right == None:
         self.right = node
      elif node.key <= self.key and self.left != None:
         self.left.insert(node)
         return
      elif node.key > self.key and self.right != None:
         self.right.insert(node)
         return
      node.parent = self

   def search(self, key):
      if self.key == key:
         return self

   def delete(self, key):
      if self.key == key:
         self.key = None
         return self.key
      return self