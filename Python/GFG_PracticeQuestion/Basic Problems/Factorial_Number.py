#Factorial No-> Product of all positive integers less than or equal to that number.
#Ex-> 5!=5x4x3x2x1=120

#Simple Program--------------|

n=6

# fact=1
# for i in range(1, n+1):
#     fact*=i
# print(fact)

# Recursive Appraoch--------------|

# def fact(n):
#     return 1 if (n==1 or n==0) else n*fact(n-1)

# num = 5
# print(fact(num))

# math.factorial()--------------|

# import math

# def factorial(n):
#     return(math.factorial(n))

# n=5
# print(math.factorial(n))

# numpy.prod()--------------|

# import numpy
# n=5
# x=numpy.prod([i for i in range(1,n+1)])
# print(x)

# Prime Factorization--------------|

# def primeFact(n):
#     factors={}
#     i=2
#     while i*i<=n:
#         while n%i==0:
#             if i not in factors:
#                 factors[i]=0
#             factors[i] +=1
#             n//=i
#         i+=1
#     if n>1:
#         if n not in factors:
#             factors[n]=0
#             factors[n]+=1
#     return factors

# def fact(n):
#     result= 1
#     for i in range(2,n+1):
#         factors= primeFact(i)
#         for p in factors:
#             result *= p **factors[p]
#     return result

# num= 5
# print(fact(num))
