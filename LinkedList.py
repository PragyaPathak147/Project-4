class Node:            
    def __init__(self,value):                                                                       
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0

    def __len__(self):
        return self.n

    def insert_head(self,value):
        new=Node(value)
        new.next=self.head
        self.head=new
        self.n=self.n+1


    def insert_tail(self,value):
        new=Node(value)
        curr=self.head
        while curr.next!=None:
            curr=curr.next

        curr.next=new
        self.n=self.n+1
    
    def insert_before(self,value,newvalue):

      if self.head.data==value:
          self.insert_head(newvalue)
          return

      new=Node(newvalue)
      curr=self.head
      while curr.next.data!=value:
          curr=curr.next

      new.next=curr.next
      curr.next=new
      self.n=self.n+1

    def delete_head(self):
        if self.head==None:
            return "Empty List"

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

    def __getitem__(self,index):
      counter=0
      curr=self.head
      while curr!=None:
          if counter==index:
              return curr.data
          counter=counter+1

    def traverse(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=" ")
            curr=curr.next

    def __str__(self):
       result=""
       curr=self.head
       while curr!=None:
        result= result + str(curr.data)+"->"
        curr=curr.next
       return result[:-2]

    def search(self,value):
      counter=0
      curr=self.head
      while curr!=None:
        if curr.data==value:
          return counter
        curr=curr.next
        counter=counter+1

      return "item not found"
      
        











        
            
            



















            
    
