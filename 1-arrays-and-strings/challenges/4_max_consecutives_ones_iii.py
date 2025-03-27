from typing import List

from util import assert_answer


class Solution:
    @staticmethod
    def longest_ones(nums: List[int], k: int) -> int:
        """
        Given a binary array nums and an integer k, return the maximum number of
        consecutive 1's in the array if you can flip at most k 0's.
        """
        ans = left = num_flipped = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                num_flipped += 1

            while num_flipped > k:
                if nums[left] == 0:
                    num_flipped -= 1
                left += 1

            if num_flipped <= k:
                ans = max(ans, right - left + 1)

        return ans


if __name__ == '__main__':
    data = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    want = 6
    got = Solution.longest_ones(data, 2)
    assert_answer(want, got, data)

    data = [0, 0, 0, 1]
    want = 4
    got = Solution.longest_ones(data, 4)
    assert_answer(want, got, data)
