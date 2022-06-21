n=int(input("Enter the number:"))
s=0
while n>0:
    n1=n%10
    if(n1%2==1):
        s=s+n1
    n=n//10

print("Sum of odd numbers in given number:",s)