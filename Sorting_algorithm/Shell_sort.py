# Shell sort

def shell_sort(l):
    gap = len(l) // 2
    while gap > 0:  # means gap reaches to 0 and swap pairs will be adjacent elements
        for i in range(gap, len(l)):
            temp = l[i]  # store the element in a temp variable
            j = i  # need to swap elements if the elements are smaller or bigger than the value they need to swap with
            while j >= gap and l[
                j - gap] > temp:  # to satisfy the above condition we are applying the logic for checking if element is bigger or smaller than the comparing element
                l[j] = l[j - gap]
                j = j - gap
            l[j] = temp
        gap = gap // 2
    return l

arr = list(map(int , input().split()))
print(shell_sort(arr))