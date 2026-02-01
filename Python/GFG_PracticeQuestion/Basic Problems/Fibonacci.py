# Fn=Fn-1 + Fn-2
# Ex-> 0,1,1,2,3,5,8,13,21,34

#Recursion----------------------|

# def Fibonacci(n):
#     if n<=0:
#         print("Incorrect Input! Out of Range")
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# x=int(input())
# for i in range(x):
#     print(Fibonacci(i), end=" ")

#Using other variable---------------------------|

# def Fibonacci(n):
#     a,b=0,1
#     for i in range(n):
#         print(a, end=" ")
#         a,b=b,a+b

# x=int(input())
# Fibonacci(x)