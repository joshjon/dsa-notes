from typing import List

from util import assert_answer


def length_of_longest_substring(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.

    Input: s = "abcabcbb"
    Output: 3
    """
    if len(s) <= 1:  # Check if can end early
        return len(s)

    ans = left = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.discard(s[left])
            left += 1

        seen.add(s[right])

        window_len = right - left + 1
        ans = max(ans, window_len)

        if ans > len(s) - left:
            return ans

    return ans


if __name__ == '__main__':
    data = "abcabcbb"
    want = 3
    assert_answer(want, length_of_longest_substring(data), data)

    data = "bbbbb"
    want = 1
    assert_answer(want, length_of_longest_substring(data), data)

    data = "pwwkew"
    want = 3
    assert_answer(want, length_of_longest_substring(data), data)

    data = "aaaabcdefghhhefkll"
    want = 8
    assert_answer(want, length_of_longest_substring(data), data)
