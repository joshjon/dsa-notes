from typing import Optional

from util import ListNode, gen_linked_list, assert_linked_lists_equal


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    Given the head of a singly linked list and two integers left and right where
    left <= right, reverse the nodes of the list from position left to position
    right, and return the reversed list.

    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]
    """

    return head


if __name__ == '__main__':
    data = gen_linked_list(1, 2, 3, 4, 5)
    left = 2
    right = 4
    want = gen_linked_list(1, 4, 3, 2, 5)
    assert_linked_lists_equal(want, reverse_between(data, left, right))

    print()
    data = gen_linked_list(3, 5)
    left = 1
    right = 2
    want = gen_linked_list(5,3)
    assert_linked_lists_equal(want, reverse_between(data, left, right))
