# Python program for removing i-th character from a string.

# 1. For Loop
# s = "PythonProgramming"
# i=5
# res=""
# for rmv in range(len(s)):
#     if rmv == i:
#         res+=s[rmv]
# print(res)

# 2. Using replace method
# s = "PythonProgramming"
# i=5
# print(s.replace(s[i],""))

# 3. String Slicing
# s = "PythonProgramming"
# i = 5
# res= s[:i] + s[i+1:]
# print(res)

# 4. List Comprehension
s = "PythonProgramming"
i=6
res= "".join(s[j] for j in range(len(s)) if j!=i)
print(res)