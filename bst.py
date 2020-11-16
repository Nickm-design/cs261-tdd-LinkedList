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

   def search(self, value):
      if self.key == value:
         return self
      elif value < self.key and self.left != None:
         return self.left.search(value)
      elif value > self.key and self.right != None:
         return self.right.search(value)
      else:
         return None
      

   def delete(self, key):
      if (key < self.key and self.search(key) == None) or (key > self.key and self.search(key) == None):
         return self
      if key < self.key:
         self.left = self.left.delete(key)
         return self
      elif key > self.key:
         self.right = self.right.delete(key)
         return self
      elif key == self.key:
         self.is_leaf()
         if self.left != None and self.right != None:
            return self.right
         elif self.left != None or self.right != None:
            if self.left != None:
               return self.left
            elif self.right != None:
               return self.right     
      else:
         return self
   
   def is_leaf(self):
      return self.left == None and self.right == None
   
   def has_left_child(self):
      return self.left
   
   def has_right_child(self):
      return self.right
   
   def minimum(self):
      if self.left != None:
         self.left.minimum()
      else:
         return self
            

