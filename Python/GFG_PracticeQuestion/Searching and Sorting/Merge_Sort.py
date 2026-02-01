# It is divide and conquer algo.
# O(N log(N))
'''
It divides input array in two halves, calls itself for the two halves and then merges the two sorted haalves.
We can used merge() function to mergint two halves.
# Approach
1st divide the list or array recursively into two halves until it can no more be divided.
2nd Conquer the each subarray is sorted individually using the merge sort algo.
3rd Merge the sorted subarrays are merged back together in sorted order.

'''

def merge_sort(my_list):                                    # Function Argument-> Array
    if len(my_list)>1:                                      # Check len of array > 1 [True]
        mid = len(my_list)//2                               # mid = 8/2=4
        left_half = my_list[:mid]                           # Left_half = [35,22,90,4,50]
        right_half = my_list[mid:]                          # Right_half = [20,30,40,1]

        merge_sort(left_half)                               # Recall Merge_Sort with size(4) and repeat     process until len < 1.         
        merge_sort(right_half)
        
        i = j = k = 0                                       # Initialization of Variable.

        while i < len(left_half) and j<len(right_half):     # Loop-> i<Left and j<right.
            if left_half[i] < right_half[j]:                # left < right
                my_list[k] = left_half[i]                   # my_list[k] = left_half[i]
                i+=1                                        # Increasement till last element.
            
            else:                                                       
                my_list[k] = right_half[j]                  # my_list[k] = right_half[j]
                j +=1                                       # Increament j.
            k+=1

        while i < len(left_half):                           # i < len(left_half)
            my_list[k] = left_half[i]                       # k = left[i]
            i+=1                                            # Increment both i and j.
            k+=1

        while j < len(right_half):                          # Same with right also if j < len(right)
            my_list[k] = right_half[j]                      # k = right
            j+=1                                            # Increment both i and j.
            k+=1
                

my_list = [35,22,90,4,50,20,30,40,1]
print("Before  Sorting: ",my_list)                          # Print my_list before sorting.
merge_sort(my_list)                                         # Call Function.
print(my_list)                                              # Print After Sorting.

