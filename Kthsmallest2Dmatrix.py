from heapq import heappush, heappop
from re import L


def ksmallestelement(matrix, k):
    n_rows = len(matrix)
    n_col = len(matrix[0])

    min_heap = []

# travelling through the element present inside the matrix
    for i in range(n_rows):
        for j in range(n_col):
            heappush(min_heap, matrix[i][j])

    for i in range(k):
        result = heappop(min_heap)

    return result

# Driver Code

matrix = [[1, 4, 7], [3, 5, 9], [6, 8,11]]
k = 4
result = ksmallestelement(matrix, k)
print("kth smallest element in 2D Matrix is:", result)
