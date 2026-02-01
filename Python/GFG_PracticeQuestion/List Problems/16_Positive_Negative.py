# In this program we will print positive and negative number that are available in list.
# 1. Loop
# 2. List Comprehension
# 3. Filter()

a = [-10, 15, 0, 20, -5, 30, -2]

#1. Loop--if [Positive Number]
# print("Positive Number: ")
# for val in a:
#     if val>=0:
#         print(val)


#2. List Comprehension
# print("Positive Number: ")
# res= [i for i in a if i>=0]
# print(res)


#3. Filter() Function
# res = filter(lambda x: x>=0, a)
# print(list(res))