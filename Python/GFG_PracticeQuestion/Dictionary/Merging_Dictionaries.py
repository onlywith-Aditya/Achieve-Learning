# Merging or Concatenating two dictionaries in python.

# 1. Update()-> Value is same and it choose key with higher value.
# d1 = {'x': 1, 'y': 2}
# d2 = {'y': 3, 'z': 4}

# d1.update(d2)
# print(d1)

# 2. | Operator
# d1 = {'x': 1, 'y': 2}
# d2 = {'y': 3, 'z': 4}

# d3= d1 | d2
# print(d3)

# 3. Unpacking(**)
# d1 = {'x': 1, 'y': 2}
# d2 = {'y': 3, 'z': 4}
# d3= {**d1,**d2}
# print(d3)

# 4. Loop
# d1 = {'x': 1, 'y': 2}
# d2 = {'y': 3, 'z': 4}

# d3=d1.copy()
# for key, value in d2.items():
#     d3[key]=value

# print(d3)