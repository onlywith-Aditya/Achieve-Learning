# String read same way as backward.


# 1. Using Loop and Pointer

# s="malayalam"
# i,j=0,len(s)-1
# pal= True
# while i<j:
#     if s[i] != s[j]:
#         pal=False
#         break
#     i+=1
#     j-=1
# if pal == True:
#     print("Yes")
# else:
#     print("NO")


# 2. Slicing Method

# s= 'malayalam'
# if s==s[::-1]:
#     print("True")
# else:
#     print("No")


# 3. Reversed Method

s='greek'
rev=''.join(reversed(s))
if s==rev:
    print("True")
else:
    print("False")


# 4. Recursion

def is_pal(s,i,j):            #greek | 0 | 4 ; greek | 1 | 3 ; 
    if i>j:                            # 0>4 ;            1>3;
        return True                   # True ;           True;
    if s[i] != s[j]:                  # g!=k ;           r!=e;
        return False                 # False ;          False;
    return is_pal(s,i+1,j-1)  #greek | 1 | 3 ; greek | 2 | 2 ;


s='greek'
if is_pal(s, 0, len(s)-1): #greek | 0 | 4
    print("Yes")
else:
    print("No")


