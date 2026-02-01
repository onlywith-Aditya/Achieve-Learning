# It is simplest sorting algo, that works by repeatedly swapping the adjacent element.
# Time Complexity-> O(n2).
# Auxiliary Space-> O(1).
'''
Sorts an array by repeatedly  comparing adjacent elements and swapping them if they are in the wrong order.

The algo iterated through the array multiple times, with each pass pushing the largest unsorted element to its correct position at the end.

The code includeds an optimization: if no swaps are made during a pass, the array is already sorted,and the sorting process stop.

'''

def bubble_sort(arr):
    # Outer loop to iterate through the list n times.
    n = len(arr)
    for i in range(len(arr)-1,0,-1):
        # Initialize swapped to track if any swaps occur.
        swapped = False
        # Inner loop to comapre adjacent elements.
        for j in range(i):
            if arr[j] > arr[j+1]:
                # Swap elements if they are in the wrong order.
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # Mark that a swap has occuerred.
                swapped = True
        # If no swaps occurred, the list already sorted.
        if  not swapped:
            break

arr = [6,6,2]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)

# Why range(n-1,0,-1)
'''

It control how many passes are needed to sort the array.

n-1: Start from the last index(since after each pass, the largest element is already in place).

0: Stop before index 0(no need to compare a single element).

-1: Decrement by 1(move backward through the array).

'''

# Alternative Swappign Methods
'''
    temp = arr[j]        
    arr[j] = arr[j+1]
    arr[j+1] = temp   

    # XOR Swap
    arr[j] ^= arr[j+1]    # a = a ^ b
    arr[j+1] ^= arr[j]    # b = a ^ b
    arr[j] ^= arr[j+1]    # a = a ^ b

    Explaination-> 
    a = a^b -> XOR stores the differencce between a and b in a .
    b = a^b -> Result with b to recover the original a(now stored in b).
    a = a^b -> XOR Again to recover the original b(now stored in a). 
'''