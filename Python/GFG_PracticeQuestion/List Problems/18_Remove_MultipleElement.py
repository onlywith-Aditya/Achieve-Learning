# In this we will learn how to remove multiple elements.
# 1. Loop 
# 2. List Comprehension
# 3. Remove()
# 4. Filter()

a = [10, 20, 30, 40, 50, 60, 70]

# 1. Loop-> Move one element to another list.
# remove= [20,40,60]

# res=[]
# for val in a:
#     if val not in remove:
#         res.append(val)

# print(res)

# 2. List Comprehension
# remove= [20,40,60]
# res= (x for x in a if x not in remove)
# print(list(res))

# 3. Remove()
# remove= [10,20,30]
# for val in remove:
#     while val in a:
#         a.remove(val)
# print(a)

# 4. Filter()
# remove=[20,40,60]
# a= filter(lambda x:x not in remove, a)
# print(list(a))