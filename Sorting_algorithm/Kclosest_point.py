

from heapq import heappop, heappush
import math


def kclosestpoints(points, k):

    # we try to get the Euclidian distance from the origin
    def get_distance(x, y):
        return math.sqrt(x ** 2 + y ** 2)

    min_heap = []
    n = len(points)

    # we tried to traverse through all the points
    for i in range(n):
        x = points[i][0]
        y = points[i][1]

        # inserting the distance and the points inside a minheap
        heappush(min_heap, (get_distance(x, y), points[i]))

    result = []

    for i in range(k):
        result.append(heappop(min_heap)[1])
    return result


points = [[2, -1], [3, 2], [4, 1], [-1, -1], [-2, 2]]
k = 3
result = kclosestpoints(points, k)
print("closest points to the origin are : ", result)
