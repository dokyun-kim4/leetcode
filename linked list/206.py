# Reverse Linked List

from linked_list import *


def answer_iter(head: ListNode):
    prev, cur = None, head

    while cur:

        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print_linked_list(answer_iter(list_to_linked_list(arr)))
