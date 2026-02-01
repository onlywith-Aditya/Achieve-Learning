# To find the largest element in an array, iterate over each element and compare it with the current largest element


# Native approach-------------------------------|

# def large(arr):
#     max=arr[0]
#     for i in range(1,len(arr)):
#         if arr[i]>max:
#             max=arr[i]
#     return max
# arr=[10,20,30,40,100]
# ans=large(arr)
# print(f"Larges element is: {ans}")

# max() Function-------------------------------|

# arr=[10,20,30,40,100]
# print(max(arr))

# sort() Function-------------------------------|

# arr=[10,200,300,40,100]
# arr.sort()
# length=len(arr)
# print(arr[length-1])

#Exit----------------------------------------------------------------|

