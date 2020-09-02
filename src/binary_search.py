import random
import time
random_range = 10000000
size = 15000000
nums = random.sample(range(size), size)
# nums = [28, 97, 84, 63, 66, 29, 90, 68, 96, 89, 15, 67, 8, 83, 46, 58, 49, 45, 26, 13]
my_target = 45
# sorted_nums = sorted(nums)
def linear_search(arr, target):
    """
    Returns true if target is in arr, else false
    """
    # Loop through the array
    for i in arr:
        # compare values
        if i == target:
            return True
        # else: keep looping
    # Finish looping:
    # We didn't find it. return False
    return False
# sorted = [8, 13, 15, 26, 28, 29, 45, 46, 49, 58, 63, 66, 67, 68, 83, 84, 89, 90, 96, 97]
def binary_search(arr, target):
    """
    Returns true if target is in arr, else false
    """
    # remember to check the empty case
    # start = the starting index of the subset of the array we're searching in. inclusive
    # end = the end index of the subset -- inclusive
    start = 0
    end = len(arr) - 1
    while end >= start:
        # Look at the middle
        # how do we get the midpoint?
        # for the whole array, it's len(arr) / 2 - 1
        # for a subset of the array: (start + end) // 2
        middle_index = (start + end) // 2
        middle_value = arr[middle_index]
        # Compare it to the target
        if target == middle_value:
            return True
        if target > middle_value:
            # search the right side
            # set start = middle_index + 1
            start = middle_index + 1
        if target < middle_value:
            # search the left side: set end = middle_index - 1
            end = middle_index - 1
        # Repeat
    # If not found, return False
    return False
    # How do we know if it's not found?
        # the subset that we're looking at has 0 or negative length
    # How to represent the subset / "window" that we're searching in?
        # store start and end index in variables
        # start index + length of the subarray
        # pass around slices of the array - creates a new array, would use extra memory and time. you also lose the original indices
# print(nums, my_target)
# print(linear_search(nums, my_target))
#
# print(sorted_nums, my_target)
# print(binary_search(sorted_nums, 92))
start = time.time()
linear_search(nums, my_target)
end = time.time()
print(f"Linear search array of length {len(nums)} took {end - start} seconds")
sorted_nums = sorted(nums)
start = time.time()
binary_search(sorted_nums, my_target)
end = time.time()
print(f"Binary search array of length {len(sorted_nums)} took {end - start} seconds")
