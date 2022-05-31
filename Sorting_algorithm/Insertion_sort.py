# Insertion Sort
# Method code

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):  # started with 1 (1 is index no.) because we consider 0 index element is already sorted
        key = arr[i]
        j = i - 1

        # Two condition will be applied
        # since we are discriminating the value which will not go beyond 0 and the
        # new value(next element) which is smaller than the previous value(last element) will get replaced

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # I tried to replace the next element with previous element
            j = j - 1
        arr[j + 1] = key
    return arr


arr = []
n = int(input("Enter the number of element :  "))
for i in range(n):
    element = int(input())
    arr.append(element)
print("original array before sorting :  ", arr)

result = insertionSort(arr)

print("Array after sorted :  ", result)