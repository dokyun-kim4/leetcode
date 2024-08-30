class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(lst):
    if not lst:  # Check if the list is empty
        return None

    # Create the head node
    head = ListNode(lst[0])
    current = head

    # Loop through the rest of the list and create nodes
    for item in lst[1:]:
        current.next = ListNode(item)
        current = current.next

    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
