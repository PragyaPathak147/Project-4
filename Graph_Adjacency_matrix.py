class Graphs:
  def __init__(self,vno):
    self.size=vno
    self.vertex=[i for i in range(self.size)]
    self.edges=[]
    self.visited=[0]*self.size
    self.q=Queues()
    self.s=Stacks()
    self.make_edges()

  def make_edges(self):
     for i in range(self.size):
        self.edges.append([0]*self.size)

  def add_edges(self,vertex1,vertex2,weight):
    self.edges[vertex1][vertex2]=self.edges[vertex2][vertex1]=weight
  
  def remove_edge(self,vertex1,vertex2):
     if self.edges[vertex1][vertex2]==0:
      return "Edge not found"
     self.edges[vertex1][vertex2]=self.edges[vertex2][vertex1]=0

  def has_edge(self,vertex1,vertex2):
    if self.edges[vertex1][vertex2]==0:
      return False
    else:
      return True
      
  def __str__(self):
    result=''
    for i in range(len(self.edges)):
      for j in range(len(self.edges[i])):
        result=result+str(self.edges[i][j])+" "
      
      result=result+"\n"
    return result

  def bfs(self,source):
      count=0
      for i in self.visited:
        if i==1:
          count=count+1
      if count==self.size:
        return
      if count==0:
        self.q.enqueue(source)

      if self.visited[source]==0:
        self.visited[source]=1
        print(source,end=" ")
        self.q.dequeue()
        for i in range(self.size):
          if self.edges[source][i]==1:
             self.q.enqueue(i)
      else: self.q.dequeue()

      self.bfs(self.q.front.data)

  def dfs(self,source):
      count=0
      for i in self.visited:
        if i==1:
          count=count+1
      if count==self.size:
        return
      if count==0:
        self.s.push(source)

      if self.visited[source]==0:
        self.visited[source]=1
        print(source,end=" ")
        self.s.pop()
        for i in range(self.size):
          if self.edges[source][i]==1:
             self.s.push(i)
      else: self.s.pop()

      self.dfs(self.s.top.data)

    
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


class Stacks:
  def __init__(self):
    self.top=None

  def is_empty(self):
    return self.top==None

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



