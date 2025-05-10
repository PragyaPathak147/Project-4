class Node:
  def __init__(self,key,item):
    self.keys=key
    self.value=item
    self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0

    def __len__(self):
        return self.n

    def insert_head(self,key,item):
        new=Node(key,item)
        new.next=self.head
        self.head=new
        self.n=self.n+1


    def insert_tail(self,key,item):
        new=Node(key,item)
        if self.head==None:
          self.head=new
          self.n=self.n+1
          return

        curr=self.head
        while curr.next!=None:
            curr=curr.next

        curr.next=new
        self.n=self.n+1


    def delete_head(self):
        if self.head==None:
            return "Empty List"
        if self.n==1:
          self.head=None
          self.n=self.n-1
          return

        self.head=self.head.next
        self.n=self.n-1


    def delete_tail(self):
        if self.head==None:
            return "Empty List"
        if self.head.next==None:
           self.delete_head()
           return
        curr=self.head
        while curr.next.next!=None:
            curr=curr.next

        curr.next=None
        self.n=self.n-1
   
    def delete_index(self,index):
      counter=0
      curr=self.head
      if counter==index:
          self.delete_head()
          return
      while curr.next.next!=None:
          if counter+1==index:
              curr.next=curr.next.next
              self.n=self.n-1
              return
          curr=curr.next
          counter=counter+1


    def __getitem__(self,index):
      counter=0
      curr=self.head
      while curr!=None:
          if counter==index:
              return curr.value
          curr=curr.next
          counter=counter+1
      return -1

    def get_index(self,key):
        counter=0
        curr=self.head
        while curr!=None:
            if curr.keys==key:
                return counter
            curr=curr.next
            counter=counter+1
        return -1
    def __setitem__(self,index,item):
      counter=0
      curr=self.head
      while curr!=None:
          if counter==index:
               curr.value=item
               return
          curr=curr.next
          counter=counter+1
      return -1


    def traverse(self):
        curr=self.head
        while curr!=None:
            print(curr.keys,":",curr.value,end=" ")
            curr=curr.next

    def __str__(self):
       result=""
       curr=self.head
       while curr!=None:
        result= result + str(curr.keys)+"->"+str(curr.value)+" "
        curr=curr.next
       return result

    def search(self,item):
      counter=0
      curr=self.head
      while curr!=None:
        if curr.value==item:
          return counter
        curr=curr.next
        counter=counter+1

      return "item not found"


class Dictionary:

  def __init__(self,capacity):
    self.capacity=capacity
    self.size=0
    self.buckets=self.make_array(capacity)

  def make_array(self,capacity):
    L=[]
    for i in range(capacity):
      L.append(LinkedList())
    return L

  def cal_hash(self,key):
    return abs(hash(key))%self.capacity

  def put(self,key,item):

    bucket_index=self.cal_hash(key)

    a=self.buckets[bucket_index].get_index(key)
    b=self.load_factor()
    if a==-1:
      if b<2:
        self.buckets[bucket_index].insert_tail(key,item)
        self.size=self.size+1
        print(b)

      else:
        A=self.buckets
        self.buckets=self.make_array(self.capacity*2)
        self.capacity=self.capacity*2
        self.size=0

        for i in range(len(A)):
          curr=A[i].head
          while curr!=None:
           self.put(curr.keys,curr.value)
           curr=curr.next


    else: self.buckets[bucket_index][a]=item

  def delete(self,key):
    bucket_list=self.cal_hash(key)
    a=self.buckets[bucket_list].get_index(key)
    if a==-1:
      return"Not found"
    else: self.buckets[bucket_list].delete_index(a)
  
  def __getitem__(self,index):
    self.buckets[index].traverse()

  def __len__(self):
    return self.size

  def load_factor(self):
    return self.size/self.capacity

  


    








        
    
