def reverse_seq(n):
    # This empty list stores the reversed sequence 
    result = []
    # This loop iteraes from "n" down to '0' excluding 
    for i in range(n, 0, -1):
        # This line appeanding each number to the "result" function 
        result.append(i)
    return result  