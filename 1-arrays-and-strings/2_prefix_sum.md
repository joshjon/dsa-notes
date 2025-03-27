# Prefix sum

- Prefix sum is a technique used on arrays (of numbers) to find the sum of any subarray
- It only costs _O(n)_ to build the data structure but allows future subarray queries to be _O(1)_.
- The idea is to create an array prefix where prefix[i] is the sum of all elements up to the index i (inclusive).
- For example, given `nums = [5, 2, 1, 6, 3, 8]`, we would have `prefix = [5, 7, 8, 14, 17, 25]`.
- The sum of a subarray from `i` to `j` (inclusive) is `prefix[j] - prefix[i - 1]`.
    - Or `prefix[j] - prefix[i] + nums[i]` to avoid dealing with out-of-bounds case when `i = 0`.
- This works because `prefix[i - 1]` is the sum of all elements before index `i`.

### Pseudocode template

```python
def fn(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])

# do logic here with prefix sum
```

### Example implementation

Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a
sum greater than or equal to the sum of the second section. The second section should have at least one number.

```python
def ways_to_split_array(nums) -> int:
    n = len(nums)

    prefix = [nums[0]]
    for i in range(1, n):
        prefix.append(nums[i] + prefix[-1])

    ans = 0
    for i in range(n - 1):
        left_section = prefix[i]
        right_section = prefix[-1] - prefix[i]
        if left_section >= right_section:
            ans += 1

    return ans

# Input: nums=[10, 4, -8, 7]
# Output: 2
```

#### Do we need the array?

- Space complexity of the above can be simplified from _O(n) to _O(1)_.
- Instead of using an array for the prefix sum, we can simply use integers.
- Initialize `left_section = 0` and then calculate it on the fly by adding the current element to it at each
  iteration.
- For `right_section`, pre-compute the sum of the entire input as `total`, then calculate `right_section`
  as `total - left_section`.

```python
def ways_to_split_array(nums) -> int:
    ans = left_section = 0
    total = sum(nums)

    for i in range(len(nums) - 1):
        left_section += nums[i]
        right_section = total - left_section
        if left_section >= right_section:
            ans += 1

    return ans

# Input: nums=[10, 4, -8, 7]
# Output: 2
```
