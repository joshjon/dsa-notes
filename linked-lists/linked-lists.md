# Linked lists

### Singly linked list

- Each node only has a pointer to the next node.
- You can only move forward in the list when iterating.

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Let prev_node be the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add


# Let prev_node be the node at position i - 1
def delete_node(prev_node):
    prev_node.next = prev_node.next.next
```

### Doubly linked list

- Similar to singly linked list, but each node also contains a pointer to the previous node.
- In a singly linked list, we needed a reference to the node at `i - 1` (`prev_node`) if we wanted to add or remove
  at `i`.
- With a doubly linked list, we only need a reference to the node at `i`.
- This is because we can reference the `prev` pointer of that node to get the node at `i - 1`.

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Let node be the node at position i
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

# Let node be the node at position i
def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
```

### Mechanics of a linked list

When you assign a pointer to an existing linked list node, the pointer refers to the object in memory.

Let's say you have a node head:

```python
ptr = head
head = head.next
head = None
```

- After these lines of code, `ptr` still refers to the original head node, even though the `head` variable changed.
- Variables remain at nodes unless they are modified directly.
- E.g. `ptr = something` is the only way to modify `ptr`.

### Traversal

Iterating forward through a linked list can be done with a simple loop:

```python
def get_sum(head):
    ans = 0
    while head:  # ends when head is null
        ans += head.val
        head = head.next

    return ans
```

Recursive alternative:

```python
def get_sum(head):
    if not head:
        return 0

    return head.val + get_sum(head.next)
```

## Fast and slow pointers

### Pseudocode template

```python
def fn(head):
    slow = head
    fast = head
    ans = 0

    while fast and fast.next:
        # do logic
        slow = slow.next
        fast = fast.next.next

    return ans
```

## Reversing

### Pseudocode template

```python
def fn(head):
    curr = head
    prev = None
    while curr:
      next_node = curr.next # first, make sure we don't lose the next node
      curr.next = prev      # reverse the direction of the pointer
      prev = curr           # set the current node to prev for the next node
      curr = next_node      # move on

    return prev
```