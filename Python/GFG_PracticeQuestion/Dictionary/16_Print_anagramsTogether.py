# An Anagram is a word or phrase formed by rearranging the letter of another word or phase,using all exactly once.
# # For example-> 
# given a list a = ['bat', 'nat', 'tan', 'ate', 'eat', 'tea'], the expected output would be:[['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']].

# Program- 1st
dict={}
a = ['bat', 'nat', 'tan', 'ate', 'eat', 'tea']
# Iterate through each word
for word in a:
    sort_word= ''.join(sorted(word))

    if sort_word in dict:
        dict[sort_word].append(word)
    else:
        dict[sort_word]=[word]
res= list(dict.values())
print(res)

# Explanation:
# sorted(word) arranges the letters of the word in alphabetical order and ''.join(sorted(word)) converts the sorted list of characters back into a string.
# If sort_word is already a key in dict, append the current word to its corresponding
# Otherwise, create a new entry in dict with sort_word as the key and the word as the first element of a new list.
# list(dict.values()) extracts those lists and stores them in res.