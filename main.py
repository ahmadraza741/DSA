class EmptyStackError(Exception):
  pass
class FullStackError(Exception):
  pass

class stack:

  def __init__(self,size=10):
    self.data = [None] * size
    self.count = 0

  def is_empty(self):
    return self.count == 0

  def is_full(self):
    return self.count == len(self.data)
  
  def push(self,data):
    if self.count == len(self.data):
      raise FullStackError("Stack is Full")
    self.data[self.count] = data
    self.count+=1
  
  def pop(self):
    if self.is_empty():
      raise EmptyStackError("Stack is empty")
    x = self.data[self.count-1]
    self.data[self.count-1] = None
    self.count-=1
    return x
  
  def display(self):
    print(self.data)

s = stack()
s.push(7)
s.push(8)
s.push(4)
s.display()
s.pop()
s.display()
s.push(1)
s.display()
