from typing import Optional

from util import ListNode, gen_linked_list, assert_linked_lists_equal


def middle_of_the_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
   Given the head of a sorted linked list, delete all duplicates such that each
   element appears only once. Return the linked list sorted as well.

    Input: head = [1,1,2,3,3]
    Output: [1,2,3]
    """
    current = head
    while current and current.next:
        if current.next.val == current.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


if __name__ == '__main__':
    data = gen_linked_list(1, 2, 3, 4, 4)
    want = gen_linked_list(1, 2, 3, 4)
    assert_linked_lists_equal(want, middle_of_the_linked_list(data))

    print()
    data = gen_linked_list(1, 1, 2, 3, 3, 3, 4, 4)
    want = gen_linked_list(1, 2, 3, 4)
    assert_linked_lists_equal(want, middle_of_the_linked_list(data))
