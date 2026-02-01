# We have to just count no. of time same sequences from the string.

import re
from collections import Counter

s = 'geek55of55gee4ksabc3dr2x'

a = re.findall(r'\d+',s)
freq = Counter(a)
mx, res = 0,0
for x in freq:
    if freq[x] >= mx:
        mx = freq[x]
        res = int(x)
    print(res)