# Input : test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)] tup = (17, 23) K = 2 
# Output : (19, 23) 

# 1. Min() + lambda
# test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19,23)]

# print("The Original List: " + str(test_list))

# tup = (17,23)

# k=1

# res = min(range(len(test_list)), key = lambda sub : abs(test_list[sub][k-1] - tup[k-1]))

# print("The nearest tuple to Kth index element is: " + str(test_list[res]))

# 2. Lambda
test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19,23)]

tup = (17,23)

k = 1

res = min(test_list, key= lambda x:abs (x[k-1]-tup[k-1]))

print("The nearest tuple to Kth index element is: " + str(res))