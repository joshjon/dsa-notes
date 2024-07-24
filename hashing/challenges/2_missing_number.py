from typing import List

from util import assert_answer


def missing_number(nums: List[int]) -> int:
    """
    Given an array nums containing n distinct numbers in the range [0, n], return
    the only number in the range that is missing from the array.

    Input: nums = [3,0,1]
    Output: 2
    """

    seen = set(nums)

    for i in range(len(nums) + 1):
        if i not in seen:
            return i


if __name__ == '__main__':
    data = [3, 0, 1]
    want = 2
    assert_answer(want, missing_number(data))

    data = [0, 1]
    want = 2
    assert_answer(want, missing_number(data))
