# Time Complexity-> O(log N)

def binary_Search(arr, low, high, x):
    # Check base case

    if high >= low: # 
        mid = (high + low) // 2 

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_Search(arr, low, mid-1,x)
        
        # Else the element can only be present in right subarray
        else:
            return binary_Search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1

# Test Array
arr = [10,20,30,40,50,60]
x = 30

# Function Call
result = binary_Search(arr, 0, len(arr)-1,x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in the array")

#------------------------------------------------|
# There is build it binary search using the built-in module.

import bisect
def binary_search_bisect(arr,x):
    i = bisect.bisect_left(arr,x)
    if i != len(arr) and arr[i] == x:
        return i
    else: 
        return -1


arr = [2,3,4,10,40]
x = 10
# Function Call
result = binary_search_bisect(arr,x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
