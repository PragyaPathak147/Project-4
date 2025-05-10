class Node:
  def __init__(self,value):
    self.data=value
    self.next=None\

class Queues():
  def __init__(self):
    self.front=None
    self.rear=None

  def is_empty(self):
    return self.front==None

  def enqueue(self,value):
    new=Node(value)
    if self.is_empty():
      self.front=new
      self.rear=self.front
      return
  
    self.rear.next=new
    self.rear=new

  def dequeue(self):

    if self.is_empty():
      return "Empty queue"

    self.front=self.front.next

  def traverse(self):
    curr=self.front
    while curr!=None:
      print(curr.data,end=" ")
      curr=curr.next
