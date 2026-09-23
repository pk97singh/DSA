def circular_next_greater(arr1):
    n = len(arr1)
    stack = []
    res = [-1] * n

    for i in range(2 * n - 1, -1, -1):

        while stack and stack[-1] <= arr1[i % n]:
            stack.pop()

        if i < n:
            if stack:
                res[i] = stack[-1]

        stack.append(arr1[i % n])

    return res


print(circular_next_greater([1, 2, 3, 4, 3]))
