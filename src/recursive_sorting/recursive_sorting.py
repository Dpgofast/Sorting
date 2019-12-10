# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    i_a = 0  # Index of array A
    i_b = 0  # Index of array B
    merged_arr = []
    # while index of a is less than length of array a
    # And index of b is less than the length of array b
    while i_a < len(arrA) and i_b < len(arrB):
        # If the item in array A at current index a
        # is less than item at location index b in array B
        # Add lesser element in merged array
        if arrA[i_a] <= arrB[i_b]:
            merged_arr.append(arrA[i_a])
            # Increment index of a to next position
            i_a = i_a + 1
        else:
            # If condition 1 doesnt exist merge item
            # from array B at index b
            merged_arr.append(arrB[i_b])
            # increment index of b to next
            i_b = i_b + 1
    # when the end of an array is reached purge the rest of the arrays from
    # current index
    merged_arr.extend(arrA[i_a:])
    merged_arr.extend(arrB[i_b:])

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    split = len(arr) // 2
    left = arr[0:split]
    right = arr[split:len(arr)]
    new_left = merge_sort(left)
    new_right = merge_sort(right)
    arr = merge(new_left, new_right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out
#  https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
