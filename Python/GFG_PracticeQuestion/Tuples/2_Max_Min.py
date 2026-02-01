# we can have problem in which we need to extract only extreme K elements, i.e maximum and minimum K elements in Tuple. This problem can have applications across domains such as web development and Data Science.


# Input : test_tup = (3, 7, 1, 18, 9), k = 2 
# Output : (3, 1, 9, 18)


# 1. sorted() + loop
test_tup = (5, 20, 3, 7, 6, 8)
print("The original tuple is : " + str(test_tup))

k=2
res = []
test_tup = list(sorted(test_tup)) # Sorted Tuple.

for idx, val in enumerate(test_tup):
    if idx< k or idx>=len(test_tup) - k:
        res.append(val)
res = tuple(res)
print('The extracted values: ' + str(res))