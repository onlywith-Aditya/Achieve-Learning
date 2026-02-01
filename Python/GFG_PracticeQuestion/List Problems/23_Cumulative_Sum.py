# Cumulative sum meaning running sum of the element.

l=[1,2,3,4]

# 1. itertools.accumulate()
# import itertools
# cum= list(itertools.accumulate(l))
# print(cum)

# 2. Numpy Cumsum
# import numpy as np
# cumulative_sum = np.cumsum(l)
# print(cumulative_sum)


# 3. List Comprehension
# div= [sum(l[:i+1]) for i in range(len(l))]
# print(div)