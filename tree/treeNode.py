class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def insert(self, element):
      if self.data:
         if element < self.data:
            if self.left is None:
               self.left = Node(element)
            else:
               self.left.insert(element)
         elif element > self.data:
            if self.right is None:
               self.right = Node(element)
            else:
               self.right.insert(element)
               

   



root = Node(1)
root.insert(5)
root.insert(7)
root.insert(-1)

def preorder(root):
   if root == None:
      return
   preorder(root.left)
   preorder(root.right)
   print(root.data)

preorder(root)