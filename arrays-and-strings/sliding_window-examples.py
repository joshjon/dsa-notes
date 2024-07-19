from util import assert_answer


def longest_subarray(nums, k):
    """
    Find the longest subarray with a sum less than or equal to `k`

    # Input: nums=[3, 2, 1, 3, 1, 1], k=5
    # Result: 3
    """
    longest = curr_sum = left = 0

    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1
        curr_len = right - left + 1
        longest = max(longest, curr_len)

    return longest


def find_length(s):
    """
    You are given a binary string s (a string containing only "0" and "1").
    You may choose up to one "0" and flip it to a "1".
    What is the length of the longest substring achievable that contains only "1"?

    # Input: s="1101100111"
    # Result: 5
    """
    # curr_zeroes is the current number of zeros in the window
    left = curr_zeroes = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr_zeroes += 1
        while curr_zeroes > 1:
            if s[left] == "0":
                curr_zeroes -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans


if __name__ == '__main__':
    print("-- longest_subarray")
    assert_answer(3, longest_subarray([3, 2, 1, 3, 1, 1], 5))

    print("\n-- find_length")
    assert_answer(5, find_length("1101100111"))
