from typing import List


def assert_answer(want, got, *args):
    if len(args) > 0:
        if len(args) == 1:
            print(f"input: {args[0]}")
        else:
            print("inputs:")
            for data in args:
                print(f"\t- {data}")

    print(f"want: {want}\ngot:  {got}")

    if want != got:
        print("outcome:  failed")
        exit("FAIL")

    print("outcome: success")


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def gen_linked_list(*args) -> ListNode:
    """
    Generates a linked list from a series of values e.g. gen_linked_list(1, 2, 3)
    """
    if len(args) == 0:
        return ListNode()

    head = ListNode(args[0])
    curr_node = head
    for i in range(1, len(args)):
        curr_node.next = ListNode(args[i])
        curr_node = curr_node.next

    return head


def linked_list_to_array(head: ListNode) -> List:
    arr = list()
    while head:
        arr.append(head.val)
        head = head.next
    return arr


def assert_linked_lists_equal(want: ListNode, got: ListNode):
    want_arr = linked_list_to_array(want)
    got_arr = linked_list_to_array(got)
    assert_answer(want_arr, got_arr)
