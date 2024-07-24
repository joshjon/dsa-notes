from collections import Counter

from util import assert_answer


def max_number_of_balloons(text: str) -> int:
    """
    Given a string text, you want to use the characters of text to form as many
    instances of the word "balloon" as possible.

    You can use each character in text at most once. Return the maximum number of
    instances that can be formed.

    Input: text = "nlaebolko"
    Output: 1
    """

    # Note: the obvious fastest solution would involve storing individual counter
    # var for each letter in 'balloon', using O(1) space. However, this solution
    # uses a hash map as the problem is part of the 'Hashing' section in the DSA
    # course.
    counts = Counter(text)

    lowest_single = min(counts["b"], counts["a"], counts["n"])
    if lowest_single == 0:
        return 0

    lowest_double = min(counts["l"], counts["o"])
    if lowest_double < 2:
        return 0

    if lowest_double >= lowest_single * 2:
        return lowest_single
    else:
        return lowest_double // 2


if __name__ == '__main__':
    data = "nlaebolko"
    want = 1
    assert_answer(want, max_number_of_balloons(data), data)

    print()
    data = "loonbalxballpoon"
    want = 2
    assert_answer(want, max_number_of_balloons(data), data)

    print()
    data = "leetcode"
    want = 0
    assert_answer(want, max_number_of_balloons(data), data)

    print()
    data = "blloo"
    want = 0
    assert_answer(want, max_number_of_balloons(data), data)
