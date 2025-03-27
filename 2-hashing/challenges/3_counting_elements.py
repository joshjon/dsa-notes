from typing import List

from util import assert_answer


def count_elements(arr: List[int]) -> int:
    """
    Given an integer array arr, count how many elements x there are, such that
    x + 1 is also in arr. If there are duplicates in arr, count them separately.

    Input: arr = [1,2,3]
    Output: 2
    """
    seen = set(arr)
    total = 0

    for num in arr:
        if num + 1 in seen:
            total += 1

    return total


if __name__ == '__main__':
    data = [1, 2, 3]
    want = 2
    assert_answer(want, count_elements(data))

    data = [1, 1, 3, 3, 5, 5, 7, 7]
    want = 0
    assert_answer(want, count_elements(data))

    data = [1, 3, 2, 3, 5, 0]
    want = 3
    assert_answer(want, count_elements(data))
