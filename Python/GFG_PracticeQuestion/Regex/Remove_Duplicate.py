import re

def rmvDup(input):
    # Regex to matching repeated words.
    regex = r'\b(\w+)(?:\W+\1+\b)+'
    return re.sub(regex, r'\1', input, flags= re.IGNORECASE)



str1 = "Good bye bye world world"
print(rmvDup(str1))
str2 = "Ram went went to to his home"
print(rmvDup(str2))
