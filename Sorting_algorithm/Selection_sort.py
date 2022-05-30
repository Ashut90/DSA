# Selection Sort
# Comparison based algorithm

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        mini = i

        for j in range(i + 1, n):
            if arr[mini] > arr[j]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

    return arr


arr = [80, -1, 1, 0, 45, 8, 0, -9]
results = selection_sort(arr)
print(results)
