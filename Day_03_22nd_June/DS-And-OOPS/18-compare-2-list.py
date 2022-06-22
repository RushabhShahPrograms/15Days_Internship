lst1=[1,2,3,4,5]
lst2=[]
print("Add 5 numbers in list")

for n in range(5):
    numbers=int(input("Enter number: "))
    lst2.append(numbers)

if(lst1==lst2):
    print("Both are same")
else:
    print("Both are not same")
