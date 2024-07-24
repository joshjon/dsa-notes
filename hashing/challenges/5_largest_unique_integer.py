from typing import List

from util import assert_answer


def largest_unique_number(nums: List[int]) -> int:
    """
    Given an integer array nums, return the largest integer that only occurs once.
    If no integer occurs once, return -1.

    Input: nums = [5,7,3,9,4,9,8,3,1]
    Output: 8
    """
    largest = -1

    if len(nums) == 0:
        return largest

    counts = {}

    # Note: can achieve the same via `counts = Counter(nums)`.
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num, count in counts.items():
        if count == 1:
            largest = max(largest, num)

    return largest


if __name__ == '__main__':
    data = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    want = 8
    assert_answer(want, largest_unique_number(data), data)
