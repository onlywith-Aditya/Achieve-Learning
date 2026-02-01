# There are two elements in a Python dictionary-keys and values. You can sort the dictionary by keys, values, or both.


# 1. Using Sort()
# d= {'ravi': 10, 'rajnish':9, 'sanjeev':8}
# myKeys= list(d.keys())
# myKeys.sort()
# sd= {i:d[i] for i in myKeys}
# print(sd)

# 2. Sorted ORder using sorted()
# d = {2: 56, 1: 2, 5: 12, 4: 24}
# print("Dict: ", d)

# for i in sorted(d.keys()):
#     print(i,end=' ')

# 3. Collections
# from collections import OrderedDict
# d = {'ravi': '10', 'rajnish': '9', 'abc': '15'}
# d1 = OrderedDict(sorted(d.items()))
# print(d1)