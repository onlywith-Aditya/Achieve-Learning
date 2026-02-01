# It is non comparison based sorting algo.
# It is effective when the range of input value is small compared to the nubmer of element to be sorted.
# The basic idea behind Counting SSort is to sount the freq, of each distinct element in the input array.



def countSort(arr):                                    # Declaration of Array.
    output = [ 0 for i in range(256)]                  # output = 256 Values
    count  = [0 for i in range(256)]                   # coutn = 256 Values
    ans = ["" for _ in arr]                            # ans = Used to store resulting answer, string is immutable.
    for i in arr:                                     
        count[ord(i)] += 1
    for i in range(256):
        count[i] += count[i-1]
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

arr = "geeksforgreeks"                                  # String of Array
ans = countSort(arr)                                    # Call
print("Sorted: ", ans)                                  # Output