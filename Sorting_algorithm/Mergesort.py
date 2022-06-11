# Combining part for the merge sort algorthm

def mergesortProsedure(arr, i, mid, j):
    n1 = mid - i + 1
    n2 = j - mid

    arr1 = [0] * n1
    arr2 = [0] * n2

    for m in range(n1):
        arr1[m] = arr[i + m]

    for q in range(n2):
        arr2[q] = arr[mid + 1 + q]

    p = 0
    q = 0
    k = i

    while p < n1 and q < n2:  # pointers for 1st and 2nd sub array and we perform the comparison to update the elements to original position
        if arr1[p] < arr2[q]:
            arr[k] = arr1[p]
            p += 1
        else:
            arr[k] = arr2[q]
            q += 1
        k += 1

    while p < n1:
        arr[k] = arr1[p]
        p += 1
        q += 1
    while q < n2:
        q += 1
        k += 1


# Merge sort method code

def mergesort(arr, i, j):
    # Dividing the arr
    if i < j:
        mid = i + (j - i) // 2

        # conquer the divided part
        mergesort(arr, i, mid)
        mergesort(arr, mid + 1, j)

        # combined the conquered part
        mergesortProsedure(arr, i, mid, j)
    return arr


# Driver code
arr = [50, 30, 20, 90, 80, 11, 12]
n = len(arr)
result = mergesort(arr, 0, n - 1)
print(result)
