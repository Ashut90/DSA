
def minmax(arr, low, high, maximum, minimum):
    if low == high:  # single element present in array
        minimum = arr[low]
        maximum = arr[high]
        return maximum, minimum

    elif low == (high - 1):  # when array have two elements
        if arr[low] < arr[high]:
            maximum = arr[low]
            minimum = arr[high]
        else:
            maximum = arr[high]
            minimum = arr[low]

        return maximum, minimum

    mid = (low + high) // 2

    max1, min1 = minmax(arr, low, mid, maximum, minimum)
    max2, min2 = minmax(arr, mid + 1, high, maximum, minimum)

    return maximum, minimum

    if min1 < min2:
        min = min1
    else:
        min = min2

    if max1 < max2:
        max = max1
    else:
        max = max2

    return min, max


# Driver code
arr = [20, 0, 79, 100, 121, 2, 23, 90, 1 , -1]
n = len(arr)
(max, min) = minmax(arr, 0, n - 1 , maximum, minimum)
print(max)
print(max)
