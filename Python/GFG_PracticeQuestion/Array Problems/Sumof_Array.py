# Give an array of integers and you have to sum of its elements.

#Function Method--------------------------------|

# def _sum(a):
#     sum=0
#     for _ in a:
#         sum = sum + _
#     return sum
# a= [10,20,30,40]
# cal= _sum(a)
# print(f"Sum of the Array Element: {cal}")

#sum() Function--------------------------------|

# arr=[10,20,30,40]
# print(sum(arr))

#Reduce Method--------------------------------|

# from functools import reduce
# def _sum(arr):
#     sum = reduce(lambda a, b: a+b, arr) 
#     return sum

# arr=[10,20,30,40]
# cal = _sum(arr)
# print(f"Sum of the array is: {cal}")

#EXIT-----------------------------------------------------------|