# Input-> 657 and expression contain 78653->VALID

'''

Algorithms
1. Define the patterns of the string using RegEx.
2. Match the strig with the specified pattern.
3. Print the Output

'''

import re

def check(str, pattern):
    if re.search(pattern, str):
        print("valid String")
    else:
        print("Invalid String")


pattern = re.compile('^[1234]+$')
check('1234', pattern)
check('349', pattern)