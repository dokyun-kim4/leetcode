# Palindrome Linked List

from linked_list import *


def answer(head: ListNode):
    # find middle
    mid, fast = head, head
    while fast.next is not None:
        fast = fast.next.next
        if fast is None:
            break
        mid = mid.next

    # reverse right side
    prev, cur = None, mid.next
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    # check
    while prev:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next

    return True


if __name__ == "__main__":
    head = list_to_linked_list([1, 2, 1])
    print(answer(head))
