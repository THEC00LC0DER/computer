arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def findMe(target, start, end):
    if (start > end):
        return 'NotFound'

    middle = int((start+end) / 2)

    if arr[middle] == target:
        return middle

    if arr[middle] > target:
        return findMe(target, start, middle-1)

    if arr[middle] < target:
        return findMe(target, middle+1, end)


value = findMe(5, 1, 10)
print(value)
