# Ex-> Input[1,2,3]-> Output[(1,1),(2,8),(3,27)]

# 1. List Comprehension
# a = [1, 2, 3, 4, 5]
# res= [(n,n**3) for n in a]
# print(res)

# 2. map()
# a = [1, 2, 3, 4, 5]
# res=  list(map(lambda n: (n,n**3),a))
# print(res)

# 3. Append()
# a = [1, 2, 3, 4, 5]
# res= []
# for n in a:
#     res.append((n,n**3))
# print(res)

# 4. List()
# a = [1, 2, 3, 4, 5]
# res= list((n,n**3) for n in a )
# print(res)