class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle_node(head):
    slow = head  # Slow pointer starts at the head
    fast = head  # Fast pointer also starts at the head

    # Move the fast pointer two steps at a time, slow pointer one step at a time
    while fast and fast.next:
        slow = slow.next  # Slow pointer moves one step
        fast = fast.next.next  # Fast pointer moves two steps

    # When fast pointer reaches the end, slow pointer will be at the middle
    return slow


head = Node(1)  # Create a sample linked list
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

middle_node = find_middle_node(head)
print("Middle node data:", middle_node.data)
