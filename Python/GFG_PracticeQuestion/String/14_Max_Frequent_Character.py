# Max Frequent Character in String.

# 1. Counter Collection
# from collections import Counter
# s= 'hello world'
# freq= Counter(s)
# max_char= max(freq, key=freq.get)
# print(max_char)

# 2. Dictionary
# s= 'hello world'
# d={}
# for char in s:
#     d[char]=d.get(char,0)+1
# max_char= max(d,key=d.get)
# print(max_char)

# 3. Lambda Function
# s= 'hello world'
# res= max(s,key=lambda char: s.count(char))
# print(res)