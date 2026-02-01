def counter(fname):
    num_words = 0
    num_lines = 0
    num_char = 0
    num_space = 0

    with open(fname, 'r') as f:
        for line in f:
            num_lines += 1  # Fixed: was 'num_line' instead of 'num_lines'
            
            # Count spaces in this line
            num_space += line.count(' ')
            
            # Count characters (excluding newlines)
            num_char += len(line.replace('\n', ''))
            
            # Count words by splitting the line
            words = line.split()
            num_words += len(words)
                    
    # printing total word count
    print("Number of words in text file:", num_words)
    
    # printing total line count
    print("Number of lines in text file:", num_lines)
    
    # printing total character count
    print('Number of characters in text file:', num_char)
    
    # printing total space count
    print('Number of spaces in text file:', num_space)


# Driver Code:
if __name__ == '__main__':
    fname = 'File1.txt'
    try:
        counter(fname)
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'An error occurred: {e}')