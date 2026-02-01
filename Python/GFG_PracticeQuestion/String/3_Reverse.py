# We have to reverse the words in a string. 
# Ex-> Hello Aditya-> Aditya Hello.

# 1. Split() and Join()
# s= "Hello Aditya"
# reversed_words = ' '.join(s.split()[::-1])
# print(reversed_words)

# 2. Loop
# s = "Hello Aditya"
# words= s.split()
# reversed_words=" "
# for word in reversed(words):
#     reversed_words += word + " "
# reversed_words = reversed_words.strip()
# print(reversed_words)