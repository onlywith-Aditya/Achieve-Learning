# Python is great for file handling.
# Built-in Functionn to make reading files easy.

# We want to read file word by word.

# We will use example_file.txt for Read_File operation.
#-----------------------------|

# Python program to read 
# file word by word

# opening the text file
with open('File_Handling\GFG.txt','r') as file:

    # reading each line    
    for line in file:

        # reading each word        
        for word in line.split():

            # displaying the words           
            print(word)