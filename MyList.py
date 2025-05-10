import ctypes
class MyList:

    def __init__ (self):
        self.size=1
        self.n=0
        self.A= self.make_array(self.size)

    def make_array(self,size):
        return (size*ctypes.py_object)()

    def __len__(self):
        return self.n

    def append(self,item):
        if self.n==self.size:
            B=self.make_array(self.size*2)
            for i in range(0,self.n):
                B[i]=self.A[i]
            self.A=B
            self.size=self.size*2

        self.A[self.n]=item
        self.n=self.n+1

    def pop(self):
        self.n=self.n-1

    def __str__(self):
        result=""
        for i in range(self.n):
            result = result + str(self.A[i])+ ","

        return "[" + result[:-1] + "]"

    def __getitem__(self,item):
        if 0<=item<self.n:
         return self.A[item]
        else: print('Invalid Index')

    def clear(self):
       self.n=0

    def max(self):
  
      if self.n == 0:
          return None 
      a=self.A[0]
      for i in range(1,self.n):
          if self.A[i]>a:
              a=self.A[i]
      return a
    
    def min(self):
      
      if self.n == 0:
          return None 
      a=self.A[0]
      for i in range(1,self.n):
          if self.A[i]<a:
              a=self.A[i]
      return a

    def del_item(self,index):
        if 0<=index<self.n:
            for i in range(index,self.n-1):
                self.A[i]=self.A[i+1]
            self.n=self.n-1
        else: print("Invalid Index")
      
    
    def find(self,item):
        for i in range(self.n):
            if self.A[i]==item:
                return i

        print("Item not found")
    
    def remove(self,item):
        a=self.find(item)
        self.del_item(a)


    def insert(self,item,index):
      
      if self.n==0:
        self.append(item)
        return

      if self.size==self.n:
        B=self.make_array(self.size*2)
        for i in range(0,self.n):
            B[i]=self.A[i]
        self.A=B
        self.size=self.size*2

      for i in range (self.n-1,index,-1):
        self.A[i+1]=self.A[i]

      self.A[index+1]=item
      self.n=self.n+1

    def sum(self):
      result=0
      for i in range(self.n):
        result=result+self.A[i]

      return result

    def __add__(self,other):
        result=" "
        for i in range(self.n):
            result=result+ str(self.A[i])+','
        for i in range(other.n):
          result=result+str(other.A[i])+','

        return '['+ result[:-1]+']'


            
                
            
    

    
