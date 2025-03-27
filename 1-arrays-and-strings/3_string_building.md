# String building

- Strings are immutable in most languages e.g. Python and Java, but not c++.
- For immutable strings, concatenating a single character is an _O(n)_ operation.
- Many problems ask to return a string, where the string is built during the algorithm. 
  - For these problems, building a string one character at a time is _O(n<sup>2</sup>)_.
  - The operations needed at each step would be `1 + 2 + 3 + ... + n`.

### Efficient algorithm

Steps in Python:

1. Declare a list
2. When building the string, add the characters to the list. 
   - This is _O(1)_ per operation and _O(n)_ in total for all.
3. Once finished, convert the list to a string using `"".join(list)`. This is _O(n)_.
4. Total cost is _O(n + n) = O(2n) = O(n)_.

```python
def build_string(s):
    arr = []
    for c in s:
        arr.append(c)

    return "".join(arr)
```
