
def find_target(arr, tar):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        if arr[m] == tar:
            return m
        elif arr[m] < tar:
            l = m + 1
        else:
            r = m - 1

    return -1


def search_rotated_array(arr):
    l = 0
    r = len(arr) - 1
    n = len(arr)

    while l <= r:
        m = (l + r) // 2

        if arr[m] > arr[n - 1]:
            l = m + 1
        else:
            r = m - 1

    return l


def idx(arr, tar):
    pivot = search_rotated_array(arr)

    arr2 = arr[:pivot]
    arr3 = arr[pivot:]

    rslt2 = find_target(arr2, tar)

    if rslt2 != -1:
        return rslt2

    rslt3 = find_target(arr3, tar)

    if rslt3 != -1:
        return rslt3 + pivot

    return -1


print(idx([50,60,70,80,90,100,10,20,30,40], 30))
