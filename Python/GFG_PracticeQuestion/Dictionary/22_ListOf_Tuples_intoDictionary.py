# Converting a list of tuples into a dictionary.

# 1. Using dict()

# a = [("a", 1), ("b", 2), ("c", 3)]
# res= dict(a)
# print(res)

# 2. Dictionary Comprehension
# a = [("a", 1), ("b", 2), ("c", 3)]  
# res = {key: value for key, value in a} 
# print(res)

# 3. Loop
a = [("a", 1), ("b", 2), ("c", 3)]  
res= {}

for key, value  in a:
    res[key] = value
print(res)