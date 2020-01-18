# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
            
        for index in range(i + 1, len(arr)):
            if (arr[index] < arr[smallest_index]):
                smallest_index = index

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    # loop through list 
    for cur_index in range(len(arr)):
        # loop through every value before the current one (excluding the final number)
        for index in range(0, len(arr) - cur_index - 1 ):
            # check if previous number is greater than the next number 
            if arr[index] > arr[index + 1]:
                # swap the previous number with the next number
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr