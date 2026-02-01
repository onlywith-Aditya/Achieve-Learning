def find_words(file_path):
    with open(file_path,'r') as file:
        content = file.read()
        words = content.split()

        words_with = [word for word in words if len(word) == 3]
        
        return words_with


file_name = "File_Handling\GFG.txt"
result = find_words(file_name)

print("Words containing three characters:")
print(result)