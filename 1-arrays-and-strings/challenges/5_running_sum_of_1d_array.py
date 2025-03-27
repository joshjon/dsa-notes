from typing import List
from util import assert_answer

"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
"""

def running_sum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    return nums


if __name__ == '__main__':
    data = [3, 1, 2, 10, 1]
    want = [3, 4, 6, 16, 17]
    got = running_sum(data)
    assert_answer(want, got, data)
