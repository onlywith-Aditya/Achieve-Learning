# Appending dictionary keys and values in order ensures that the sequence in which they are added is preserved.

# 1. Zip and Constructor
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]

# d= dict(zip(keys,values))
# print(d)

# 2. Loop
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]

# d={}
# for k,v in zip(keys, values):
#     d[k] = v
# print(d)

# 3. Dictionary Comprehension
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]

# d={}

# d.update({k:v for k, v in zip(keys, values)})
# print(d)


# 4. OrderedDict

# from collections import OrderedDict

# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]

# d= OrderedDict(zip(keys, values))

# print(d)

# 5. List of Tuples andn Dict Constructor

keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]

d = dict([(k,v) for k,v in zip(keys, values)])
print(d)