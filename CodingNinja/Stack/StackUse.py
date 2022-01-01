#from StackUsingArray import Stack
from StackUsingLinkedList import Stack

ele = Stack()

ele.push(10)
ele.push(20)
ele.push(30)

print(ele.size())

while ele.is_empty() is not True:
    print(ele.pop())

print(ele.size())
print(ele.top())