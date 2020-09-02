nums = [29, 35, 64, 84, 97, 8, 83, 46, 58, 49, 45, 26, 13]
# selection sort:
# find the smallest, put it at the front. find the next smallest, put it in 2nd place, and so on so forth
# bubble sort:
# compare adjacent elements and swap them if out of order
# "bubbles up" the largest elements to the end
# insertion sort:
def insertion_sort(arr):
    # you have part of the array that is sorted
    # the boundary between sorted/unsorted is an index to the first element that's unsorted
    first_unsorted_index = 1
    while first_unsorted_index < len(arr):  # for idx in range(1, len(arr)):
        # take the next unsorted element and "insert" it into the sorted part of the array:
        # store the element we're trying to insert into a variable
        current_element = arr[first_unsorted_index]
        # compare it to each of the elements in the sorted part of the array, going from biggest --> smallest
        sorted_index = first_unsorted_index - 1
        while sorted_index >= 0:
            # if the sorted element is bigger than the current, shift the sorted element right by 1
            if arr[sorted_index] > current_element:
                print(sorted_index, "greater")
                arr[sorted_index + 1] = arr[sorted_index]
            # otherwise if sorted element is < current:
            elif arr[sorted_index] <= current_element:
                print(sorted_index, "less")
                # we found the right place for it and we can insert it there.
                arr[sorted_index + 1] = current_element
                # Don't continue looping
                break
            # if you're at the beginning of the array, there's no where else to go. Insert the current element there:
            if sorted_index == 0:
                print("beginning")
                arr[sorted_index] = current_element
            # decrement sorted_index and loop again
            sorted_index = sorted_index - 1
        # increment the "boundary" between sorted and unsorted parts of the array
        first_unsorted_index += 1
        print(arr)
    return arr
def insertion_sort_2(arr):
    # Keep a boundary between sorted/unsorted parts of the array.
    # unsorted index points to the first unsorted element in the array
    for unsorted_index in range(1, len(arr)):
        # current element is the first unsorted element that we're trying to insert into the sorted part of the array
        current_element = arr[unsorted_index]
        # loop through the sorted part of the array backwards (biggest --> smallest)
        sorted_index = unsorted_index - 1
        # Stop when we reach the beginning of the array or the sorted element is <= the current element
        while sorted_index >= 0 and arr[sorted_index] > current_element:
            # if the sorted element > current element, shift it right by 1
            arr[sorted_index + 1] = arr[sorted_index]
            # decrement sorted index to keep looping backwards
            sorted_index -= 1
        # At this point sorted_index is the index where current element belongs
        # insert the current element into the array
        arr[sorted_index + 1] = current_element
    return arr
# print(insertion_sort(nums))
print(insertion_sort_2(nums))