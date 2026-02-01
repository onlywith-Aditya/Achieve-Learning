# But in many applications, the user doesn't know all the keys present in the dictionaries. In such instances, if the user tries to access a missing key, an error is popped indicating missing keys. 


# Handling Missing keys in Python Dictionaries

# d = { 'a' : 1 , 'b' : 2 }
# print("The values associated with 'c' is: ")
# print(d['c'])
# Throw Error Value Not Found

# 1. Using Key
# ele = {'a': 5, 'c': 8, 'e': 2}
# if "q" in ele:
#     print(ele['d'])
# else:
#     print("key Not found")

# 2. Using get()
# country_code = {'India' : '0091',
#                 'Australia' : '0025',
#                 'Nepal' : '00977'}

# print(country_code.get('India', 'Not Found'))
# print(country_code.get('Japan', 'Not Found'))

# 3. Set Default
# country_code = {'India' : '0091',
#                 'Australia' : '0025',
#                 'Nepal' : '00977'}

# country_code.setdefault('Japand', 'Not Found')

# print(country_code.get('India'))
# print(country_code.get('Japan'))


# 4. Try and Except
# country_code = {'India': '0091',
#                 'Australia': '0025',
#                 'Nepal': '00977'}

# try: 
#     print(country_code['India'])
#     print(country_code['USA'])
# except KeyError:
#     print("Not Found")