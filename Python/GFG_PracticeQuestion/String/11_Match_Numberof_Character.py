# Count the Number of matching characters in a pair of string.

# 1. Set
# s1="Only With Aditya"
# s2="All"
# res= len(set(s1.lower()).intersection(set(s2.lower())))
# print(res)


# 2. Counter
# from collections import Counter
# s1="Only With Aditya"
# s2="All"
# c1= Counter(s1.lower())
# c2= Counter(s2.lower())
# res=sum((c1 & c2).values())
# print(res)

# 3.List Comprehension
# s1 = "VISHAKSHI"
# s2 = "VANSHIKA"
# res= len([char for char in set(s1.lower())
#             if char in set(s2.lower())]
#         )
# print(res)