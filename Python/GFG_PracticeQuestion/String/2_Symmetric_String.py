# A string is symmetrical if its first half matches the second half, considering the middle character for odd-length strings. 
# For palindrome, the string is compared with its reversed version.
# For symmetry, the first half is compared with the second, skipping the middle character if the length is odd.


# 1. String Slicing

s="ababa"
half= len(s)//2
sym= s[:half] == s[half:]  if len(s) %2==0 else s[:half] == s[half+1:]

pal = s == s[::-1]
print("Symmetrical" if sym else "Not S")
print("Palindrome" if sym else "Not P")
