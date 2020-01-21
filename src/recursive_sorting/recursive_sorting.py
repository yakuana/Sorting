# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    # index_A to iterate through arrA 
    # index_B to iterate through arrB
    # index to iterate through merged_arr 
    index_A, index_B, index = 0, 0, 0

    # sort using comparison until one list has been iterated through completely 
    while index_A < len(arrA) and index_B < len(arrB):
        if (arrA[index_A] <= arrB[index_B]):
            merged_arr[index] = arrA[index_A]
            index_A += 1
        else: 
            merged_arr[index] = arrB[index_B]
            index_B += 1 
        
        index += 1 

    # arrA > arrB so get the rest of A data 
    while index_A < len(arrA):
        merged_arr[index] = arrA[index_A]
        index_A += 1 
        index += 1 

    # arrB > arrA so get the rest of B data 
    while index_B < len(arrB):
        merged_arr[index] = arrB[index_B]
        index_B += 1 
        index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO; 

    if len(arr) <= 1: # base case 0 or 1 
        return arr 
    else: 
        # find the middle of the array 
        middle = len(arr) // 2

        # left_half arr equals arr[:middle]
        # right_half arr equals arr[middle:]
        left_half = merge_sort(arr[:middle])
        right_half = merge_sort(arr[middle:]) 

        return merge(left_half, right_half)

print(merge_sort([2, 1, 4, 98, 22]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
