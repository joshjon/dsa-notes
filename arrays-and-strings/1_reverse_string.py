from typing import List

from util import assert_answer


class Solution:
    @staticmethod
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
    Solution.reverse_string(data)

    assert_answer(want, data)
