# Add Tuples(4,5) and List[1,2,3]-> Result[1,2,3,(4,5)]or[1,2,3,4,5] .
# Add Another tuples-> (4,5,6,7)

# 1. extend() and + Operator
# a = [1,2,3] #List
# b = (4,5) #Tuple
# c = [6,7] # List of add

# # Add tuple to list a 
# a.extend(b)
# print(a)

# # Add list to tuple b
# d = b + tuple(c)
# print(d)

# 2. Append() and * operator
# a = [1, 2, 3,]
# b = (4,5)
# c = [6, 7]

# a.append(b)
# print(a)

# d = (*b,*c)
# print(d)
