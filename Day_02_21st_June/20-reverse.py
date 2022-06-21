num=1234
r=0

while(num!=0):
    digit=num%10
    r=r*10+digit
    num//=10

print("Reversed number is:",r)