class Node:
  def __init__(self,value):
    self.data=value
    self.next=None

class Stacks:
  def __init__(self):
    self.top=None

  def is_empty(self):
    return self.top==None

  def peek(self):
    if self.is_empty():
      return "Empy stack"
    return self.top.data

  def push(self,value):
    new=Node(value)
    new.next=self.top
    self.top=new

  def pop(self):
    if self.is_empty():
      return "Empty stack"

    value=self.top.data
    self.top=self.top.next
    return value


  def traverse(self):
    curr=self.top
    while curr!=None:
      print(curr.data)
      curr=curr.next

  def search(self,value):
    counter=0
    curr=self.top
    while curr!=None:
      if curr.data==value:
        return counter
      curr=curr.next
      counter=counter+1

    return "Not found"

  def __getitem__(self,index):
    counter=0
    curr=self.top
    while curr!=None:
      if counter==index:
        return curr.data
      curr=curr.next
      counter=counter+1
    return "Invalid Index"
