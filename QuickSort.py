def quicksort(A, first, last):
    if first < last:
        splitpoint = partition(A, first, last)
        quicksort(A, first, splitpoint-1)
        quicksort(A, splitpoint+1, last)


def partition(A, first, last):
    done, pivotvalue, leftmark, rightmark = False, A[first], first+1, last

    while not done:

        while (leftmark <= rightmark) and (A[leftmark] <= pivotvalue):
            leftmark += 1

        while (rightmark >= leftmark) and (A[rightmark] >= pivotvalue):
            rightmark -= 1

        if leftmark > rightmark:
            done = True
        else:
            temp = A[leftmark]
            A[leftmark] = A[rightmark]
            A[rightmark] = temp

    temp = A[first]
    A[first] = A[rightmark]
    A[rightmark] = temp

    return rightmark

print '1'


if __name__ == "__main__":
    pass
