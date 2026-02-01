import re
s1 = "Hello, World! 123 @Python$"
# r'[^a-zA-Z0-9]'-> Matching any character which is not a letter or number.
s2 = re.sub(r'[^a-zA-Z0-9]', '',s1)
print(s2)