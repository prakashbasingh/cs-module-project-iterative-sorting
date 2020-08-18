# def binary_search(my_list, search_item):
#     low = 0
#     high = len(my_list) - 1
#     while low <= high:
#         middle = (low + high) // 2
#         guess = my_list[middle]
#         if guess == search_item:
#             return middle
#         if guess > search_item:
#             high = middle - 1
#         else:
#             low = middle + 1
#     return None

# test_list = [2,4,7,8,9,10,12,34,45]
# binary_search(test_list, 7)
# 2
# binary_search(test_list, 34)
# 7

def selection_sort(items):
    # Outer Loop
    for i in range(0, len(items) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j

        items[smallest_index], items[cur_index] = items[cur_index], items[smallest_index]

    return items


our_numbers = [5, 9, 3, 6, 2, 1, 7, 8, 4]
print(selection_sort(our_numbers))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
