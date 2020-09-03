def linear_search(arr, target):
    # linear search function will return the location in the arr of
    # the value searcehd, if it exists
    # loop thru the arr
    for i in range(len(arr)):
        # compare target
        if arr[i] == target:
            # if equal
            return i
        # else keep looping
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # start = the starting index of the subset of the array being searched
    start = 0
    # end = the end index of the subset
    end = len(arr) -1 

    while end >= start:
        # get the modpoint index and value
        middle_index = (start + end) // 2
        middle_value = arr[middle_index]
        # compare it to the target
        if target == middle_value:
            return middle_index

        if target > middle_value:
            # search the right side
            # set start = middle_index + 1
            start = middle_index + 1
        if target < middle_value:
            end = middle_index - 1

    return -1  # not found
