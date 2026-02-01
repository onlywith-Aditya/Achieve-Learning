# Input: 
# string = "engineers rock"
# pattern = "er";
# Output: true
# Explanation: 
# All 'e' in the input string are before all 'r'.

# 1. Using Pointers

def checkOrder(string, pattern):
    i,j=0,0
    for char in string:
        if char == pattern[j]:
            j+=1
        if j==len(pattern):
            return True
        i=+1
string= 'engineers rock'
pattern= 'er'
print(checkOrder(string, pattern))