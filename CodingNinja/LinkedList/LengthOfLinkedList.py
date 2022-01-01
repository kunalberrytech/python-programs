from LinkedCreation import take_input_optimized

def length_of_linked_list(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count

head = take_input_optimized()
print("Length Of List")
print(length_of_linked_list(head))