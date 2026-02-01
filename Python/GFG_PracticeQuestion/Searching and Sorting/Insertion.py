# It i simple sorting algo, that works by iteratively inseting each element of an unsorted list into its correct position in a sorted portion of the list.


def insertionSort(arr):
    n = len(arr)
    if n<=1:
        return # If the array has 0 or 1 element, it is already sorted, so return.
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
arr = [12,11,13,5,6]
insertionSort(arr)
print(arr)

#--------------
'''
4<=1: No
key = 12
j = 0
j>= 0 and key < arr[j]
arr[1]=arr[2]
key=arr[2]
'''