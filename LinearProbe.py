class Dictionary:
  def __init__(self,size):
    self.size=size
    self.keys=[None]*self.size
    self.value=[None]*self.size
  def cal_hash(self,key):
      return abs(hash(key))%self.size

  def put(self,key,item):
    hash_value=self.cal_hash(key)
    old_hash=hash_value
    while self.keys[hash_value]!= None and self.keys[hash_value]!= key:
        hash_value=self.rehash(hash_value)
        if hash_value==old_hash:
          print("Dict is full")
          return

    if self.keys[hash_value]==None:
         self.keys[hash_value]=key
         self.value[hash_value]=item
         return
    else:
        self.value[hash_value]=item
        return

  def rehash(self,old_hash):
    new_hash=(old_hash+1)%self.size
    return new_hash

  def __setitem__(self,key,item):
      self.put(key,item)

  def search(self,key):

      hash_value=self.cal_hash(key)
      old_hash=hash_value
      while self.keys[hash_value]!= key:
          hash_value=self.rehash(hash_value)
          if hash_value==old_hash:
              return "Not found"

      return self.value[hash_value]

  def __getitem__(self,key):
    item= self.search(key)
    return item

    
  def __str__(self):
    result=""
    for i in range(self.size):
          if self.keys[i]!=None:
            result = result + str(self.keys[i]) + ":" + str(self.value[i])+" "
          

    return result

  def delete(self,key):
    
      hash_value=self.cal_hash(key)
      old_hash=hash_value
      while self.keys[hash_value]!= key:
          hash_value=self.rehash(hash_value)
          if hash_value==old_hash:
              return "Not found"

      self.keys[hash_value]=None
      self.value[hash_value]=None
      return 
    




      
      
      
      
      
