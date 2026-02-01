# It is comparsion based sorting tech, based on a binary heap Ds.
# It is similar to select sort where we first find the maximum element and place the maximum element at the end.
# Convert the arrayt into a max heap using heapify.


'''
Process->

1. Rearrage the array elements so they form a max heap.
2. Repeat the content until the 1 element left.
3. Swap the root element of the heap, The largest element in current heap with last element of the heap.
4. Remove the last element of the heap, which is now at correct position. We mainly reudce the heap size and do not remove element from the actual array.
5. Heapify the remaining elements of the heap.
6. Finally we get sorted array.

'''

def heapify(arr,n,i):                                                   # Def Heapify
    largest = i                                                         # Largest = i
    l = 2 * i + 1                                                       # l 
    r = 2 * i + 2                                                       # r

    if l<n and arr[i] < arr[l]:                                         # l<n and arr[i]<arr[l]
        largest = l                                                     # largst = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i],arr[largest] ) = (arr[largest], arr[i])

        heapify(arr, n, largest)


def heapSort(arr):                                                    # Def heapSort
    n  = len(arr)                                                     # Len of array = 5              

    for i in range(n // 2, -1,-1):                                    # Range(2,-1,-1)
        heapify(arr, n, i)                                            # Call Heapify(arr, n,i)

    for i in range(n-1,0,-1):
        (arr[i], arr[0]) = (arr[0],arr[i])  
        heapify(arr,i,0)

    


arr = [12,11,13,5,6,7]                                                  # Array
heapSort(arr)                                                           # Call HeapSort
print('Sorted array is: ', arr)