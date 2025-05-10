class Node:
  def __init__(self,item):
    self.data=item
    self.left=None
    self.right=None
class BST:
  def __init__(self):
    self.root=None
    self.n=0
  
  def insert_node(self,value):
    new=Node(value)
    a=0
    if self.root==None:
        self.root=new
        self.n=self.n+1
        return
    curr=self.root
    while curr!=None:
        if curr.data==value:
            print("value already exist")
            return
        if curr.data>value:
            a=curr
            curr=curr.left
        else:
            a=curr
            curr=curr.right
    if a.data>value:
      a.left=new
    else:
      a.right=new
    self.n+=1

  def __len__(self):
    return self.n

  def search(self,value):
    curr=self.root
    while curr!=None:
        if value==curr.data:
            print('Found')
            return curr
        if value<curr.data:
            curr=curr.left
        else:
            curr=curr.right
    return "Not found"

  def maxm(self):
    curr=self.root
    while curr.right!=None:
        curr=curr.right
    return curr.data

  def minm(self):
    curr=self.root
    while curr.left!=None:
        curr=curr.left
    return curr.data

  def inorder(self,curr):
    if curr==None:
        return 0
    self.inorder(curr.left)
    print(curr.data,end=" ")
    self.inorder(curr.right)

  def preorder(self,curr):
    if curr==None:
        return 0
    print(curr.data,end=" ")
    self.preorder(curr.left)
    self.preorder(curr.right)

  def postorder(self,curr):
    if curr==None:
        return 0
    self.postorder(curr.left)
    self.postorder(curr.right)
    print(curr.data,end=" ")
  
  def no_nodes(self,curr):
    if curr==None:
      return 0
    x=self.no_nodes(curr.left)
    y=self.no_nodes(curr.right)
    return x+y+1

  def find_inorder(self,curr):
    curr=curr.right
    while curr.left!=None:
        curr=curr.left

    return curr
    

  def delete(self,value):
    if self.root.data==value:
      self.root=None
    curr=self.root
    while curr!=None:
      if value==curr.data:
        if curr.left==None and curr.right==None:
            if a.left.data==value:
                a.left=None
            else:
                a.right=None
            self.n=self.n-1
            return
        if curr.left==None or curr.right==None:
            if curr.left==None:
                a.right=curr.right
                self.n=self.n-1
                return
            else:
                a.left=curr.left
                self.n=self.n-1
                return
        o=self.find_inorder(curr)
        curr=o
        self.delete(o.value)
              
      if value>curr.data:
        a=curr
        curr=curr.right
      else:
          a=curr
          curr=curr.left

    return "Not Found"


  def hgt(self,curr):
    if curr==None:
      return 0
    x=self.hgt(curr.left)
    y=self.hgt(curr.right)
    return max(x,y)+1











