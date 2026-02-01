# We are given a list that contains tuples with the pairs of key and values we need to convert that list into a flat dictionary.
# List->Dictionary.

# 1. dict()
# a = [("name", "Alice"), ("age", 25), ("city", "New")]
# res= dict(a)
# print(res)

# 2. Loop
# a = [("name", "Alice"), ("age", 25), ("city", "New")]
# b={}
# for key, value in a:
#     b[key]=value
# print(b)

# 3. List Comprehension
# a = [("name", "Alice"), ("age", 25), ("city", "New")]
# res= {key: value for key, value in a }
# print(res)

#  4. Using Zip
# a = ["name", "age", "city"]  
# b = ["Alice", 25, "New York"]  
# res= dict(zip(a,b))
# print(res)