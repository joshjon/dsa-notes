# Sliding window

Used when the problem involves criteria to find a **valid** sub array.

### Criteria of valid subarray

There are 2 components which make a subarray **valid**:
  - A constraint metric, which is specific attribute of a subarray 
    - e.g. the sum, number of unique elements, frequency of a specific element, etc...
  - A numeric restriction on the constraint metric
    - e.g. less than or equal to 10

> Example criteria: a subarray is valid if it has a sum less than or equal to `10`

### Finding the valid subarray

Common tasks:

- Finding the **best** valid subarray
  - Requires some definition of a **better** subarray e.g. longest **valid** subarray
- Finding the number of valid subarrays

### Pseudocode template

```python
def fn(arr):
    left = ans = curr = 0

    for right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            left += 1

        # update ans

    return ans
```

### Example problems

- Find the longest subarray with a sum less than or equal to `k`
- Find the longest substring that has at most one `"0"`
- Find the number of subarrays that have a product less than `k`

### Example implementation

Find the longest subarray with a sum less than or equal to `k`

- Constraint metric: sum of the subarray window
- Numeric restriction: `sum <= k`

```python
def longest_subarray(nums, k):
    longest = curr_sum = left = 0

    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1
        curr_len = right - left + 1
        longest = max(longest, curr_len)

    return longest

# Input: nums=[3, 2, 1, 3, 1, 1], k=5
# Output: 3
```