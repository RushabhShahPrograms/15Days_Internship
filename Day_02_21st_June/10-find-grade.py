print("Enter marks of three subjects out of 100\n")

x=int(input("Marks of Maths: "))
y=int(input("Marks of English: "))
z=int(input("Marks of Computer: "))

total=x+y+z

if total>250:
    print("Grade A")
elif total>200:
    print("Grade B")
elif total>150:
    print("Grade C")
else:
    print("Grade D")