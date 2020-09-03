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

    # Your code here


    return -1  # not found
