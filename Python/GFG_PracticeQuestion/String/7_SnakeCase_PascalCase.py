# Converting snake case to pascal case involves tranforming a format where words are separated by underscore  into a single  string where each word starts with uppercase.
# Ex-> greeksforgreek_is_best -> GeeksforgeeksIsBest

# 1.title()
# s= "greeksforgreek_is_best"
# res = s.replace("_"," ").title().replace(" ", "")
# print(res)

# 2. Split()
# s= "greeksforgreek_is_best"
# res= ''.join(word.capitalize() for word in s.split('_'))
# print(res)

# 3. Loop
# s= "greeksforgreek_is_best"
# res= ""
# capNext= True
# for char in s:
#     if char == "_":
#         capNext = True
#     elif capNext:
#         res+=char.upper()
#         capNext=False
#     else:
#         res+=char
# print(res)

# Take input from the user
name = input("Please enter your name: ")

# Print the name
print("Hello,", name)