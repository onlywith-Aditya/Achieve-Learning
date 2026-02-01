# Ways to remove a key from dictionary.

# 1. Pop()
# a = {"name": "Nikki", "age": 25, "city": "New York"}
# rev = a.pop("age")
# print(a)
# print(rev)

# 2. Del()
# a = {"name": "Nikki", "age": 25, "city": "New York"}
# del a["city"]
# print(a)

# 3. Popitem()-> Remove from -n element.
# a = {"name": "Nikki", "age": 25, "city": "New York"}
# c= a.popitem()
# print(a)
# print(c)

# 4. Dict.pop()-> Missing element.
# a = {"name": "Nikki", "age": 25, "city": "New York"}
# rv = a.pop("Country","Key not found")
# print(a)
# print(rv)