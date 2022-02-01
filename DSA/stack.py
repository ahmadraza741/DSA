class EmptyStackError(Exception):
  pass

class Node:
  
  def __init__(self,data):
    self.data = data
    self.next = None

class stack:

  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None

  def push(self,data):
    newnode = Node(data)
    newnode.next = self.head
    self.head = newnode
  
  def pop(self):
    if self.is_empty():
      raise EmptyStackError("Stack is empty")
    x = self.head.data
    self.head = self.head.next
    return x
  
  def peek(self):
    if self.is_empty():
      raise EmptyStackError("Stack is empty")
    return self.head.data

  def display(self):
    if self.is_empty():
      raise EmptyStackError("stack is Error")
      return
    temp = self.head
    while(temp!=None):
      print(temp.data)
      temp = temp.next

s = stack()
s.push(6)
s.push(4)
s.push(9)
s.display()
s.pop()
s.display()