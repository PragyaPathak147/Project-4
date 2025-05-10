class Heaps():
  def __init__(self):
    self.size=1
    self.arr=[None]*2

  def insert_in_array(self,item):
    if self.size==1:
     self.arr[1]=item
     self.size=self.size+1
    else:
      if self.arr[self.size//2]<item:
        self.arr.append(item)
        self.size=self.size+1
      else:
        n=self.size
        self.arr.append(item)
        while self.arr[n]<self.arr[n//2]:
          self.arr[n],self.arr[n//2]=self.arr[n//2],self.arr[n]
          n=n//2
          if n==1:
            break
        self.size=self.size+1

  def delete(self):
    if self.size==1:
      return "empty heap"
    self.size=self.size-1
    self.arr[self.size],self.arr[1]=self.arr[1],self.arr[self.size]
    a=self.arr.pop()
    i=1
    if 2*i<=self.size-1 and 2*i+1<=self.size-1:
      while self.arr[i]>self.arr[2*i] or self.arr[i]>self.arr[2*i+1]:
            if self.arr[2*i]<self.arr[2*i+1]:
                  self.arr[i],self.arr[2*i]=self.arr[2*i],self.arr[i]
                  i=2*i
            else:
                self.arr[i],self.arr[2*i+1]=self.arr[2*i+1],self.arr[i]
                i=2*i+1
            if 2*i>self.size-1 or 2*i+1>self.size-1:
                break

    if 2*i>self.size-1 and 2*i+1<=self.size-1 :
              if self.arr[i]>self.arr[2*i+1]:
                  self.arr[i],self.arr[2*i+1]=self.arr[2*i+1],self.arr[i]

    if 2*i+1>self.size-1 and 2*i<=self.size-1 :
            if self.arr[i]>self.arr[2*i]:
                self.arr[i],self.arr[2*i]=self.arr[2*i],self.arr[i]

    return a

  def heapsort(self):
      for i in range(self.size):
        a=self.delete()
        print(a,end=" ")
            
                
               
            
