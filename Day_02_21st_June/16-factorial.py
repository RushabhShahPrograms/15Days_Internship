j=int(input("Enter the number to find factorial: "))
f=1
if(j<0):
    print("Factorial of negative numbers is not possible")
elif(j==0):
    print("Factorial of zero is 1")
else:
    while(j>0):
        f=f*j
        j=j-1
print(f)