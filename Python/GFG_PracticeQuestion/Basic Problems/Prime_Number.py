# You have to find all prime number lie between two number(x,y)
# Prime Number-> Who are divisiable by 1 and itself.

#Trial Division-------------------------|

# x, y = 2, 7
# res = []
# for n in range(x, y + 1):
#     if n <= 1:
#         continue
#     is_prime = True
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         res.append(n)
# print(res if res else "No")

#Naive Approach-------------------------|

# x, y = 2, 7  # range [x, y]
# res = []  # list to store primes

# for i in range(x, y + 1):
#     if i <= 1:
#         continue  # skip non-primes <= 1
#     for j in range(2, i // 2 + 1):
#         if i % j == 0:
#             break  # not a prime
#     else:
#         res.append(i)  # prime found

# print(res if res else "No")

