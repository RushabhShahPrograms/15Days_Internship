from binascii import b2a_base64


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Before swapping","\na: ",a,"b: ",b)
temp=a
a=b
b=temp

print("After swapping","\na: ",a,"b: ",b)