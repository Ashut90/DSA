# count sort
# sorts the elements of an array by counting the number of occurrences
# Here I added the two programs for the same algorithm where logic are same, but I've written it different


'program 1'


def count_sort(num):
    n = len(num)
    res = [0] * n  # size will be same as the size of original arr
    c = [0] * 10
    for i in range(0, n):
        c[num[i]] = c[num[i]] + 1
    for i in range(1, 10):
        c[i] = c[i] + c[i - 1]

    i = n - 1
    while i >= 0:
        res[c[num[i]] - 1] = num[i]
        c[num[i]] -= 1
        i = i - 1
    return res


num = list(map(int, input().split()))
print(count_sort(num))


# program 2


def count_sort(l):
    n = len(l)
    out = [0] * n
    count = [0] * 10

    for i in range(0, n):
        count[l[i]] += 1

    for j in range(1, 10):
        count[j] += count[j - 1]

    a = n - 1
    while a >= 0:
        out[count[l[a] - 1]] = l[a]
        count[l[a]] -= 1
        a -= 1
    for k in range(0, n):
        l[k] = out[k]


l1 = [1, 8, 9, 2, 5, 1, 90, 1]

result = count_sort(l1)
print(result)
