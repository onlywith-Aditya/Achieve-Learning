import re

# re.findall-> Used to find all non-overlapping occurrences of a regular expression pattern within a stirng. It reutrns thess occurences as a list.

string = "ThisIsGreeksforGeeks !, 123"
uppercase_characters = re.findall(r"[A-Z]",string)
lowercase_characters = re.findall(r"[A-Z]",string)
numerical_characters = re.findall(r"[A-Z]",string)
special_characters = re.findall(r"[A-Z]",string)


print("The no. of uppercase character is: ", len(uppercase_characters))
print("The no. of lowercase character is: ", len(lowercase_characters))
print("The no. of numerical character is: ", len(numerical_characters))
print("The no. of special character is: ", len(special_characters))