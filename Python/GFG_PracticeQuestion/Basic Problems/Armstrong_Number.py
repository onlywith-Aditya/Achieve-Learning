# Armstrong Number-> 153=1*1*1+5*5*5+3*3*3= 153.
# Armstrong aka <-> Narcissistic Number

# Function----------------------------------|

# def power(x, y): 
#     if y == 0:
#         return 1
#     if y % 2 == 0:
#         return power(x, y // 2) * power(x, y // 2) 
#     return x * power(x, y // 2) * power(x, y // 2)

# def order(x):
#     #Variable to store number.
#     n=0
#     while (x!=0):
#         n=n+1   #154,155,156
#         x=x//10 #15,1,0
#     return n    #156

# def isArmstrong(x):
#     n=order(x)  #156
#     temp=x      #156
#     sum1=0

#     while(temp!=0): 
#         r=temp%10              #6,5,1
#         sum1=sum1 + power(r,n) #
#         temp=temp//10          #15,1,0

#     return (sum1 == x)         #

# x=155
# print(isArmstrong(x))

# Short String Function----------------------------------|

def isArmstrong(x):
    n = len(str(x))
    sum1 = sum(int(digit) ** n for digit in str(x))
    return sum1 == x

print(isArmstrong(153))  # Output: True