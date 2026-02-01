# But Python strings are immutable, so removal operations cannot be performed in-place. Instead, they require creating a new string, which uses additional memory.

# 1. replace()
# s= 'hello world'
# s= s.replace("l", ""
# print(s)

# 2. Loop()
# s= 'hello world'
# s1=''
# for char in s:
#     if char != 'l':
#         s1 += char 
# print(s1)

# 3. List Comprehension
# s = "hello world"
# s = "".join([c for c in s if c != "o"])
# print(s)