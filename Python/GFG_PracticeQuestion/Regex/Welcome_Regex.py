'''
Regex-> It is a powerful way to search, match and manipulate stringsbasde don complex pattern.
- Also knowns as Regular Expression.
- It is a special seq of character that uses a search pattern to find a string or set of strings.
- Build in module name -> re
import re



'''

import re
s = "GeeksforGreekL A computer sicence portal for greeks"

match= re.search(r'portal',s)
# r-> Used tfor character stand for raw and not regex.
print("Start Index:", match.start())
print("End Index:", match.end())
