#In this program we have to convert key-value list to flat dictionary.
#Dictonary -> List

# 1. Dict()

# a = [("name", "Alice"), ("age", 25), ("city", "New York")] 
# res= dict(a)
# print(res)

# 2. Loop
# a = [("name", "Alice"), ("age", 25), ("city", "New York")] 
# b= {}
# for key, value in a:
#     b[key]=value
# print(a)

# 3. List Comprehension
# a = [("name", "Alice"), ("age", 25), ("city", "New York")] 
# res= {key:value for key, value in a}
# print(res)
