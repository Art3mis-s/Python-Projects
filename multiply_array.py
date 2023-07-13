#the 'arr' parameter represents the non-empty array of integers \
def grow(arr):
    #this line initialize the 'product' variable to the first element of the 'arr' array 
    product = arr[0]
    #this line iterates over the remaining elements of the arr array, starting from the second element (index 1) up to the last element.
    for i in range(1, len(arr)):
        #this line multiplies the current element ('arr'[i]) with the 'product' variable, and then updates the variable
        product = arr[i]
    return product