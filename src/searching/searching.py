def linear_search(arr, target):
    # Your code here
    for i, item in enumerate(arr):
        if item == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    left_items = 0
    right_items = len(arr) - 1
    
    while left_items <= right_items:
        mid_item = (right_items + left_items) // 2
        
        if target == arr[mid_item]:
            return mid_item
        elif target < arr[mid_item]:
            right_items = mid_item - 1
        else:
            left_items = mid_item + 1

    return -1  # not found
