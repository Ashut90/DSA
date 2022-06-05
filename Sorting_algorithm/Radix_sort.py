# Driver Code

# counting sort

def counting_sort(arr, P):
    n = len(arr)
    Res = [0] * n
    c = [0] * 10
    for i in range(0, n):
        temp = arr[i] // P
        c[temp % 10] += 1
    for i in range(1, 10):
        c[i] = c[i] + c[i - 1]
    i = n - 1
    while i >= 0:
        temp = arr[i] // P
        Res[c[temp % 10] - 1] = arr[i]
        c[temp % 10] -= 1
        i = i - 1
    for i in range(0, n):
        arr[i] = Res[i]


# Radix sort algorithm
def radix_sort(arr):
    maximum = max(arr)
    N = 1
    while maximum // N > 0:
        counting_sort(arr, N)
        N = N * 10


# method code
arr = list(map(int, input().split()))
radix_sort(arr)
print(arr)
