# You have to take input as number and you inverted star pattern will print.
#    *****
#     ****
#      ***
#       **
#        *

n=11

for i in range(n,0,-1):
    print((n-1) * ' ' + i * '*')