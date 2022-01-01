from Node import Node
class Stack:

    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self,elem):
        new_node = Node(elem)
        new_node.next = self.__head
        self.__head = new_node
        self.__count = self.__count + 1

    def pop(self):
        if self.is_empty() is True:
            print("Stack is empty")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count - 1
        return data

    def top(self):
        if self.is_empty() is True:
            print("Stack is empty")
            return
        data = self.__head.data
        return data


    def size(self):
        return self.__count

    def is_empty(self):
        return self.size() == 0
