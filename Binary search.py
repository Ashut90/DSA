def binarysearch(arr, i, j, target):
    if i == j:
        if arr[i] == target:
            return i
        else:
            return -1

    else:

        mid = i + (j - i) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binarysearch(arr, mid + 1, j, target)
        else:
            return binarysearch(arr, i, mid - 1, target)
    return -1


# Driver code

arr = [10, 20, 30, 40, 50, 60, 70]
target = 70
i = 0
j = len(arr) - 1
result = binarysearch(arr, i, j, target)
print(result)
