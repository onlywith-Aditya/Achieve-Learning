# Least Frequent Character in String.

# 1. Collection.counter
# from collections import Counter
# s= "GreeksforGreeks"
# freq=Counter(s)
# res=min(freq,key=freq.get)
# print(str(res))

# 2. Dictionary
# s= "GreeksforGreeks"
# d={}
# for char in s:
#     d[char]=d.get(char,0)+1
# res=min(d,key=d.get)
# print(res)

# 3. Lambda
# s = "GeeksforGeeks"
# res = min(s, key=lambda char: 
#         s.count(char))
# print(str(res))