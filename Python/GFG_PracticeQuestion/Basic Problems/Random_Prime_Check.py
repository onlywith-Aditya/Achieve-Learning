#Check a postive number is prime or not

#Hardcore Method-------------------|

x=int(input())
if x<=1:
    print("Out of Range")
else:
    is_true= True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            is_true=False
            print("Not Prime")
            break
        print("Prime Number")