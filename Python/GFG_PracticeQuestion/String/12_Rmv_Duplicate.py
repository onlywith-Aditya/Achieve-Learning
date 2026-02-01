# You have to remove all duplicate character from your string.

# 1. Using set()
# str= "Greeksforgreek"
# res= "".join([char for i, char in enumerate(str) if char  not in str[:i]])
# print(res)

# 2. Using Loop
# str= "Greeksforgreek"
# seen= set()
# res= ""
# for char in str:
#     if char not in seen:
#         seen.add(char)
#         res+=char
# print(res)

# 3. Using Dict
# str= "Greeksforgreek"
# res= "".join(dict.fromkeys(str))
# print(res)

# 4. Dict.fromkey
# from collections import OrderedDict

# s = "geeksforgeeks"
# res = "".join(OrderedDict.fromkeys(s))
# print(res)