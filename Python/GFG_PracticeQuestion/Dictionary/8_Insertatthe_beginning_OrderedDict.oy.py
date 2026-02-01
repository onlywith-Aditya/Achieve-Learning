# Given a ordered dict, write a program to insert items in the beginning of the ordered dict.

# Input: 
# original_dict = {'a':1, 'b':2}
# item to be inserted ('c', 3)
# Output:  {'c':3, 'a':1, 'b':2}

# 1. Dict.move_to_end()
# from collections import OrderedDict

# iniordered_dict= OrderedDict([('akshat','1'), ('nikil','2')])

# iniordered_dict.update({'manjeet': '3'})
# iniordered_dict.move_to_end('manjeet', last=False)

# print("Result Dictionary: " + str(iniordered_dict))


# 2. Using Naive Approach
from collections import OrderedDict

ini_dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
ini_dict2= OrderedDict([("manjeet", '4'), ("akash",'4')])

# Used just replace place with "+" operator.
both= OrderedDict(list(ini_dict2.items())+ list(ini_dict1.items()))
print(str(both))