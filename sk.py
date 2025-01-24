class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example Usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
reversed_list = reverse_linked_list(head)
while reversed_list:
    print(reversed_list.value, end=" -> ")
    reversed_list = reversed_list.next