# In this we will used to find positve and negative number which are fall into range you will provide.
# 1. Loop-if
# 2. List Comprehension
# 3. Filter()

start= -5
end= 3


# 1. Loop-if

# print("Positive Number: ")
# for i in range(start, end+1):
#     if i <0:
#         print(i)

# 2. List Comprehension
# rev= (val for val in range(start, end+1) if val < 0)
# print(list(rev))

# 3. Filter()
# rev = filter(lambda val: val < 0, range(start, end+1))
# print(list(rev))