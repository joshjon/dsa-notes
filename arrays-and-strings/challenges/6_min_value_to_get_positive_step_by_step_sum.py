import sys
from typing import List

from util import assert_answer


class Solution:
    @staticmethod
    def min_start_value(nums: List[int]) -> int:
        """
        Given an array of integers nums, you start with an initial positive value startValue.
        In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
        Return the minimum positive value of startValue such that the step by step sum is never less than 1.

        Input: nums = [-3,2,-3,4,2]
        Output: 5
        Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
        step by step sum
        startValue = 4 | startValue = 5 | nums
          (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
          (1 +2 ) = 3  | (2 +2 ) = 4    |   2
          (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
          (0 +4 ) = 4  | (1 +4 ) = 5    |   4
          (4 +2 ) = 6  | (5 +2 ) = 7    |   2
        """
        m = nums[0]

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
            m = min(m, nums[i])

        if m >= 0:
            return 1

        return abs(m) + 1


if __name__ == '__main__':
    data = [-3, 6, 2, 5, 8, 6]
    want = 4
    got = Solution.min_start_value(data)
    assert_answer(want, got, data)
