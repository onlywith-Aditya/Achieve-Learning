# Python dictionaries with keys having multiple inputs.
# Example-1
import random as rn
dict={}
x,y,z= 10,20,30
dict[x,y,z]=x+y-z
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z
print(dict)
# Output-> {(10,20,30):0 (5,2,4):3}
