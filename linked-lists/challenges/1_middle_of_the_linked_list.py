from typing import Optional

from util import ListNode, gen_linked_list, assert_linked_lists_equal


def middle_of_the_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given the head of a singly linked list, return the middle node of the linked list.
    If there are two middle nodes, return the second middle node.

    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == '__main__':
    data = gen_linked_list(1, 2, 3, 4, 5)
    want = gen_linked_list(3, 4, 5)
    assert_linked_lists_equal(want, middle_of_the_linked_list(data))
