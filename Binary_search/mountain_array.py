arr=[1,2,4,5,7,6,4,3]


def mountain_array(arr):
    n=len(arr)-1
    rslt=-1
    
    for i in range(n):
        if arr[i]>arr[i+1]:
            return arr[i]
            
    return rslt

print(mountain_array(arr))



def mountain_array(arr):
    l = 0
    r = len(arr) - 1

    while l < r:
        mid = (l + r) // 2

        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            r = mid

    return arr[l]

print(mountain_array([1, 2, 4, 5, 7, 6, 4, 3]))
