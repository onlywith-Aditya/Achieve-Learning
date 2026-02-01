# The goal here is to split a string into smaller parts based on a delimiter and then join those parts back together with a different delimi
# Ex-> "Hello, how are you?"
# Output-> Hello,-how-are-you?

# 1. Using replace
# s= "Hello, how are you?"
# print(s.split())
# print(s.replace(" ",'-'))

# 2. Using join and split()
# s= "Hello, how are you?"
# print(s.split())
# c="-".join(s.split())
# print(c)

# 3. Using Loop
# s= "Hello, how are you?"
# str= s.split()
# print(str)
# rev=""
# for i in s:
#     if (i==" "):
#         i= "-"
#         rev+=i
#     else:
#         rev+=i
# print(rev)