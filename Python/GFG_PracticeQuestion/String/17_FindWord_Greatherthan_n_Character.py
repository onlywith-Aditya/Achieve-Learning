# Find words which are greater than given length k.

# 1. Using Classic Method
# def string_k(k,str):
#     string=[]
#     text=str.split(" ")
#     for x in text:
#         if len(x) >= k:
#             string.append(x)
#     return string

# k= 3
# str= "Geek for in Geeks"
# print(string_k(k,str))

# 2. List Comprehension
# str= "hello geeks for geeks is computer science portal"
# length= 6
# print([word for word in str.split() if len(word)>length])

# 3. Lambda Function
# str= "hello geeks for geeks is computer science portal"
# k=5
# s=str.split(" ")
# l= list(filter(lambda x: (len(x)> k),s))
# print(l)

# 4. Enumerate Function
# str= "hello geeks for geeks is computer science portal"
# length = 4
# s= str.split()
# print([a for i, a in enumerate(s) if len(a)>length])