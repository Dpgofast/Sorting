# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Takes the largest value and moves it right
        # once largestvalue is placed select next largest value
        # move next largest to the right until
        # smallest value is held at beginning of list
        cur_index = i
        # smallest_index = cur_index
        for j in range(i+1, len(arr)):
            if arr[cur_index] > arr[j]:
                cur_index = j

        # (hint, can do in 3 loc)
        # TO-DO: swap ✔
        temp = arr[i]
        arr[i] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for num in range(len(arr)-1, 0, -1):
        # Compare pairs in the list
        # Find if item at index is larger than next
        # If item at index is larger than current
        # Swap current item for largest and continue
        for k in range(num):
            if arr[k] > arr[k + 1]:
                temp = arr[k]
                arr[k] = arr[k + 1]
                arr[k + 1] = temp

    return arr


# STRETCH: implement the Count Sort function below
# What is count sort?

"""According to Wikipedia "In computer science, counting sort is an algorithm
for sorting a collection of objects according to keys that are small integers;
that is, it is an integer sorting algorithm. It operates by counting the number
of objects that have each distinct key value, and using arithmetic on those
counts to determine the positions of each key value in the output sequence. Its
running time is linear in the number of items and the difference between the
maximum and minimum key values, so it is only suitable for direct use in
situations where the variation in keys is not significantly greater than the
number of items. However, it is often used as a subroutine in another sorting
algorithm, radix sort, that can handle larger keys more efficiently"."""


def count_sort(arr, maximum=-1):
    # The range of possible positive integers given the max
    m = maximum + 1
    # init a counter with places for possible integers populated with zeros
    # ex:| 0 | 1 | 2 | 3 | 4 | 6 |
    #    | 0 | 0 | 0 | 0 | 0 | 0 |
    count = [0] * m
    # Loop through list and count occurences of a given int
    # save a running total to the corresponding column in count list
    for x in arr:
        count[x] += 1
    # initialize a counter from 0 to maximum
    i = 0
    # loop through items in range 0 to max +1
    for z in range(m):
        # for each item in the count list
        # set array equal to item if count is > 0
        # since our counting list ordered them from 0 to max
        # we just have to expel our collection to the array in order of index
        for _ in range(count[z]):
            arr[i] = z
            i += 1
    return arr
