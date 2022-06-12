
# Quicksort method code for partition
def partition(arr, p, q):
    pivot = arr[p]
    i = p
    for j in range(p + 1, len(arr)):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[p] = arr[p], arr[i]
    return i


def quicksort(arr, i, j):
    if i == j:
        return arr[i]
    elif j < i:
        return -1
    else:
        m = partition(arr, i, j)
        quicksort(arr, i, m - 1)
        quicksort(arr, m + 1, j)
    return arr


# Driver code

arr = [50, 70, 80, 30, 40, 88, 19, 17, 69]
result = quicksort(arr, 0, len(arr) - 1)
print(result)
