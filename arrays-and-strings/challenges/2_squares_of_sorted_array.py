from typing import List

from util import assert_answer


class Solution:
    @staticmethod
    def sorted_squares(nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = len(result) - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1

            result[i] = square ** 2

        return result


if __name__ == '__main__':
    data = [-7, -3, 2, 3, 11]

    want = [4, 9, 9, 49, 121]
    got = Solution.sorted_squares(data)

    assert_answer(want, got, data)
