from util import assert_answer


def simplify_path(path: str) -> str:
    """
    Given an absolute path for a Unix-style file system, which begins with a
    slash '/', transform this path into its simplified canonical path.

    In Unix-style file system context, a single period '.' signifies the current
    directory, a double period ".." denotes moving up one directory level, and
    multiple slashes such as "//" are interpreted as a single slash. In this
    problem, treat sequences of periods not covered by the previous rules
    (like "...") as valid names for files or directories.

    The simplified canonical path should adhere to the following rules:

        - It must start with a single slash '/'.
        - Directories within the path should be separated by only one slash '/'.
        - It should not end with a slash '/', unless it's the root directory.
        - It should exclude any single or double periods used to denote current or
          parent directories.

    Return the new path.

    Input: path = "/.../a/../b/c/../d/./"
    Output: "/.../b/d"
    """

    """
    Requirements:
    - "."  : signifies current dir
    - ".." : signifies moving up a dir
    - "//" : should be treated as "/"
    - "." > 2 : valid dir name
    """
    if len(path) <= 1:
        return path

    parts = path.split("/")

    stack = ["/"]

    for p in parts:
        top = stack[-1]

        if p == "" or (p == "/" and top == "/") or p == ".":
            continue

        if p == "..":
            if len(stack) == 1:
                continue
            elif len(stack) >= 3:
                stack.pop()
                stack.pop()
        else:
            stack.append(p)
            stack.append("/")

    if len(stack) > 1:
        stack.pop()

    return "".join(stack)


if __name__ == '__main__':
    data = "/.../a/../bz/c/../d/./"
    want = "/.../bz/d"
    assert_answer(want, simplify_path(data), data)

    data = "/../"
    want = "/"
    assert_answer(want, simplify_path(data), data)
