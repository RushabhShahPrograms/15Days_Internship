sym=input("Choose any one of this + - * / // : ")
x=int(input("Now enter first value: "))
y=int(input("Now enter second value: "))

if sym=='+':
    print("Addition: ",(x+y))
elif sym=='-':
    print("Subtraction: ",(x-y))
elif sym=='*':
    print("Multiplication: ",(x*y))
elif sym=='/':
    print("Division: ",(x/y))
elif sym=='//':
    print("Modulo: ",(x//y))
else:
    print("Please enter correct symbol")