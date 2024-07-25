from typing import Optional

from util import assert_linked_lists_equal, ListNode, gen_linked_list


def swap_nodes_in_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given a linked list, swap every two adjacent nodes and return its head.
    You must solve the problem without modifying the values in the list's nodes
    (i.e., only nodes themselves may be changed.)

    Input:  [A,B,C,D,E,F]
    Output: [B,A,D,C,F,E]

    Steps:
        1. Perform an edge swap from A -> B -> C -> ... to A <-> B C -> ....
        2. Make sure we can still access the rest of the list beyond the current
           pair (saves C).
        3. Now that A <-> B is isolated from the rest of the list, save a pointer
           to A to connect it with the rest of the list later. Move to the next pair.
        4. Connect the previous pair to the rest of the list. In this case
           connecting A -> D.
        5. Use a dummy pointer to keep a reference to what we want to return.
        6. Handle the case when there's an odd number of nodes.
    """
    if not head or not head.next:
        return head

    dummy = head.next  # B
    prev = None

    # Note: comments below represent the first 2 iterations in the loop
    while head and head.next:
        if prev:
            prev.next = head.next   # NOP                        | B -> A -> D -> E -> F
        prev = head                 # A                          | C
        next_node = head.next.next  # C                          | E
        head.next.next = head       # B <-> A   C -> D -> E -> F | B -> A -> D -> C    E -> F
        head.next = next_node       # B -> A -> C                | B -> A -> C -> D -> E -> F
        head = next_node            # C                          | E

    return dummy


if __name__ == '__main__':
    print("-- swap nodes in pairs")
    data = gen_linked_list("A", "B", "C", "D", "E", "F")
    want = gen_linked_list("B", "A", "D", "C", "F", "E")
    assert_linked_lists_equal(want, swap_nodes_in_pairs(data))
