# Time Complexity-> O(n^2)
#------------------------
# It is comparison based sorting algo.
# It is sorts an array by repeatedly selecting the smallest(or largest).
# Unsorted portion and swapping it with the first unsorted element.
# Process continues  until the entire array is sorted.
#------------------
'''
1. First find smallest element and swap it with the first element.
    This way we get the samllest element at its correct position.
2. Then we find the smallest among remaining elements and swap it with the second element.
3. We keep doing this until we get all element moved to correct position.
'''
#----------------------------|

def selectionSort(arr,size):

    for ind in range(size):
        min_index = ind
        for j in range(ind+1,size):
                # Select the minimum element in every iteration.
                if arr[j] < arr[min_index]:
                    min_index = j   
                    # Swapping the element to sort the array.
        (arr[ind], arr[min_index]) = (arr[min_index],arr[ind])


arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr,size)
print("Array after sorting in Ascending Order: \n", arr)