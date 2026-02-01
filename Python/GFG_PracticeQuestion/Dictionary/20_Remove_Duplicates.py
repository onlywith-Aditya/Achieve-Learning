# Goal is to process a sentence such that all duplicate words are removed, leaving only the first occurrence of each word.

# 1. Join()
# s1 = "Geeks for Geeks"
# s2 = s1.split() 

# s3= list(set(s2))
# s4= ''.join(s3)
# print(s4)

# 2. List Comprehension
# s1 = "Geeks for Geeks"
# a = s1.split() 
# seen= set()# It is used to track unique words
# res = [word for word in a if not(word in seen or seen.add(word))]
# s2=''.join(res)
# print(s2)

# 3. Dict.fromkeys()
# s1 = "Geeks for Geeks"
# s2 = s1.split()  # Split the sentence into words

# # Use a dictionary to remove duplicates and preserve order
# s3 = list(dict.fromkeys(s2))

# # Join the list back into a sentence
# s4 = ' '.join(s3)
# print(s4)

# 4. Simple Loop
# s1 = "Geeks for Geeks"
# s2 = s1.split()  # Split the sentence into words
# res = [] 

# for word in s2:
#     if word not in res:
#         res.append(word)

# s3= "".join(res)
# print(s3)