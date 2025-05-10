class Heaps():
  def __init__(self):
    self.size=1
    self.arr=[None]*1

  def parent(self,index):
    return index//2

  def right(self,index):
    return 2*index+1

  def left(self,index):
    return 2*index

  def insert(self,value):
    self.arr.append(value)
    self.upheap(self.size)
    self.size=self.size+1

  def upheap(self,index):
    if index==1:
      return
    if self.arr[index]==None:
      return
    if self.arr[index]<self.arr[self.parent(index)]:
      self.arr[index],self.arr[self.parent(index)]=self.arr[self.parent(index)],self.arr[index]
      self.heap(self.parent(index))
  
  def downheap(self,index):

    if self.right(index)>=self.size and self.left(index)>=self.size:
      return
    if self.right(index)>=self.size:
      if self.arr[index]>self.arr[self.left(index)]:
        self.arr[index],self.arr[self.left(index)]=self.arr[self.left(index)],self.arr[index]
      return
    if self.left(index)>=self.size:
      if self.arr[index]>self.arr[self.right(index)]:
        self.arr[index],self.arr[self.right(index)]=self.arr[self.right(index)],self.arr[index]
      return

    if self.arr[index]>self.arr[self.right(index)] or self.arr[index]>self.arr[self.left(index)]:
      if self.arr[self.right(index)]<self.arr[self.left(index)]:
        self.arr[index],self.arr[self.right(index)]=self.arr[self.right(index)],self.arr[index]
        self.downheap(self.right(index))

      else:
        self.arr[index],self.arr[self.left(index)]=self.arr[self.left(index)],self.arr[index]
        self.downheap(self.right(index))
   

        


  def delete(self):
    if self.size==1:
      return
    self.arr[1],self.arr[self.size-1]=self.arr[self.size-1],self.arr[1]
    a=self.arr.pop()
    self.size=self.size-1
    self.downheap(1)
    return a

