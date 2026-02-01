# Calculate how oftern words appear in giving string.

# 1. Collection Method
from collections import Counter
s= "Hello World Hello Aditya"
w_freq = Counter(s.split())
print(w_freq)


# 2. Collection Method with Loop
from collections import Counter
s= "Hello World Hello Aditya"
w_freq= Counter([word for word in s.split()])
print(w_freq)

# 3. Dict.get()
s= "Hello World Hello Aditya"
w_freq = {}
for x in s.split():
    w_freq[x]= w_freq.get(x,0) +1
print(w_freq)