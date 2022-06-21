num=int(input("Enter he number for checking palindrome:"))
t=num
r=0
while(num>0):
    digit=num%10
    r=r*10+digit
    num//=10

if(t==r):
    print("Palindrome")
else:
    print("Not Palindrome")