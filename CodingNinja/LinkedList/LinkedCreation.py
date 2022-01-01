

# Node Creation in the Liked List
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def take_input_1():
    input_list = [int(ele) for ele in input().split()]
    head = None
    for ele in input_list:
        if ele == -1:
            break
        new_node = Node(ele)
        # For First Node as it contains the head is None this is our first node
        if head is None:
            head = new_node
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    return head

def take_input_optimized():
    input_list = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for ele in input_list:
        if ele == -1:
            break
        new_node = Node(ele)
        # For First Node as it contains the head is None this is our first node
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head
def print_linked_list(head):

    curr = head
    while curr is not None:
        print(str(curr.data)+"->",end="")
        curr = curr.next
    print("None")
    return

if __name__ == '__main__':
    head = take_input_1()
    head = take_input_optimized()
    print_linked_list(head)