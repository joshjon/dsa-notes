from typing import List
from util import assert_answer

"""
Write a function that reverses a string. The input string is given as an array 
of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

https://leetcode.com/problems/reverse-string/description/
"""


def reverse_string(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        left_old = s[left]
        s[left] = s[right]
        left += 1
        s[right] = left_old
        right -= 1


if __name__ == '__main__':
    data = ["H", "a", "n", "n", "a", "h"]
    want = ["h", "a", "n", "n", "a", "H"]
    reverse_string(data)
    assert_answer(want, data)
