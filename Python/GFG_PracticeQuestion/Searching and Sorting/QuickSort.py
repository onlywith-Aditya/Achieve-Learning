# It is based on divide and conquer.
'''

1. Select an element from the array as the pivot.
    It can be vary.
2. Rearrange the array around.
    After partitioning, all elements smaller than the pivot will be on its right.
3. Recursively Call
    It apply two partitioned sub-array(left and right of the pivot).
4. Base Case
    The recursion stops when there is only one element left in the sub-array.

'''
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

# Example
arr = [1, 7, 4, 1, 10, 9, -2]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)
