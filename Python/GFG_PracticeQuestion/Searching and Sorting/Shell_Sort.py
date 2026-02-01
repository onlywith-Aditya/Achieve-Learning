# It is advance version of inertion sort, algo.
# It imporves its efficiency by comparing and sorting elemtn that are far apart.
# It break the original list into smller sublists, sort these sublist, and gradualy reduce the gap between the sublist element until the list is sorted.


'''

1. Start
2. Initilize the value of gap size, say h.
3. Divide the list into smaller sub-part. Each must have equal intervals to h.
4. Sort these sublist using insetion sort.
5. Repeat this step 2 until the list is sorted.
6. Print a sorted lsit.
7. Stop

'''


def shellSort(arr):                                             #  Function Declared
    n = len(arr)                                                # Len of Array= 4
    gap = n//2                                                  # Gap = 2

    while gap > 0:                                              # Gap > 0-> True

        for i in range(gap,n):                                  # Range(2, 4)
            temp = arr[i]                                       # temp = arr[i]

            j=i                                                 #  J=i
            while j>= gap and arr [j-gap]>temp:                
                arr[j] = arr[j-gap]
                j-=gap  
            
            arr[j] = temp
        gap = gap // 2



arr = [12,34,54,2,3]                                    # Array
print("Array Before Sorting: ", arr)                    
shellSort(arr)                                          # Call Function
print("Array after Sorting:",arr)