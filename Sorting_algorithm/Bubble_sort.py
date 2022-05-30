def bububblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [70, 20, 50, 30, 15, 5, 90, 75]
result = bububblesort(arr)
print("sorted array : ", result)


# Bubble sort without any sorting algorithm

# method code
def bubble_sort(arr):
    n = len(arr)
    zerocount = 0
    onecount = 0

    for i in range(n):
        if arr[i] == 0:
            zerocount += 1
        if arr[i] == 1:
            onecount += 1

    for i in range(zerocount):
        arr[i] = 0
    for i in range(zerocount, zerocount + onecount):
        arr[i] = 1
    for i in range(zerocount + onecount, n):
        arr[i] = 2
    return arr


# driver code
arr = [0, 1, 0, 1, 0, 2, 1, 2]
result = bubble_sort(arr)
print("we are printing bubble sort algo without any sorting algo", result)

