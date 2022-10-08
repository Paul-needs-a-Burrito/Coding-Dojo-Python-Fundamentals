# Assignment: Selection Sort
# WRITE A SELECTION SORT ALGORITHM

def selection_sort(arr):
    for i in range(len(arr)):
        min_val = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_val]:
                min_val = j

        arr[i], arr[min_val] = arr[min_val], arr[i]

    return arr

selection_sort([8,1,5,3,2,0])

# here it is important to understand that we are simply finding the index position that holds the smallest value. Once 'j' iterations are done, then use python swap for indices. This one gave me a lot of trouble to do it correctly.