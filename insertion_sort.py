# Assignment: insertion Sort
# WRITE AN INSERTION SORT ALGORITHM

def insertion_sort(arr):
    for i in range(1, len(arr)):
        sort_value = arr[i]

        while arr[i-1] > sort_value and i > 0:# we do i > 0 because python allows negative indexing

            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1# after the swap, keep checking index value to the left
    return arr

print(insertion_sort([5, 2, 10, 7, 108, 74, 59, 60, 58]))
