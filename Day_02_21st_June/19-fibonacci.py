z=int(input("Enter the number:"))
a,b=0,1
count=0
while(count<z):
    print(a)
    c=a+b
    a=b
    b=c
    count+=1