class myIterator:
        def __init__(self,maxSize):
            self.maxSize=maxSize
            self.count=0
        def __iter__(self):
              return self
        
        def __next__(self):
              if self.count<self.maxSize:
                   val=self.count
                   self.count+=1
                   return val
              else:
                    raise StopAsyncIteration
obj=myIterator(5)

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

        