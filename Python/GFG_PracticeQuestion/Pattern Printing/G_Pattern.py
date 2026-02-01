# How to print pattern 'G'.
# Time Complexity-> O(n^2)
# Space Complexity-> O(1)

'''

With the help of 2-D we will selectively choose number which are useful for us to make pattern.

We will choose rows and column which we want to make pattern 'G'.


'''

def Pattern(line):                                                  
    pat=""                                                          
    for i in range(0,line):                                         
        for j in range(0,line):                                             
            if ((j == 1 and i != 0 and i != line-1) or          
                                                                
                ((i == 0 or                                         
                i == line-1) and                                    
                j > 1 and 
                j < line-2) or 
                (i == ((line-1)/2) and 
                j > line-5 and 
                j < line-1) or 
                (j == line-2 and
                i != 0 and 
                i != line-1 and 
                i >=((line-1)/2))):  
                pat=pat+"*"   
            else:      
                pat=pat+" "   
        pat=pat+"\n"   
    return pat

# Driver Code
line = 7                                            # Line=
print(Pattern(line))                                # Print-> Pattern(7)