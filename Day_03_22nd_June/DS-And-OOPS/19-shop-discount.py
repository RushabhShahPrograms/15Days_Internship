#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Assume each unit's cost is 100.
# Judge and print total cost for user. 

a=int(input("Enter the quantity: "))
total=a*100
print("Total cost is",total)

if(total>=1000):
    print("You will get 10 percent discount")
else:
    print("Please shop more to get 10 percent discount")
