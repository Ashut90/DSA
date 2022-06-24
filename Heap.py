# problem to find the Kth smallest element in 2D matrix
# Time complexity require = O(n^2Logn)
from heapq import heappush, heappop


def ksmallest(matrix, k):
    n_rows = len(matrix)
    n_col = len(matrix[0])

    min_heap = []

# travers the elements inside the matrix
    for i in range(n_rows):
        for j in range(n_rows):
            heappush(min_heap, matrix[i][j])

    # pop k number of times to get kth smallest element

    for i in range(k):
        result = heappop(min_heap)

    return result


matrix = [[1, 4, 7],
          [3, 5, 9],
          [6, 8, 11]]
k = 5
res = ksmallest(matrix, k)
print("kth smallest element in 2D Matrix is : ", res)
