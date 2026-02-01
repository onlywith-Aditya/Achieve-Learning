# In this we will learn how to print duplicates from a list of integers.

a = [1, 2, 3, 1, 2, 4, 5, 6, 5]

# 1. Set-> Set will only store things which is not duplicates and other are stored in dup list.
# s= set()
# dup = []

# for n in a:
#     if n in s:
#             dup.append(n)
#     else:
#         s.add(n)
# print(dup)


# 2. Dictionary
# d={}
# for n in a:
#     d[n] = d.get(n,0)+1
# dup = [n for n, c in d.items() if c>1]
# print(dup)