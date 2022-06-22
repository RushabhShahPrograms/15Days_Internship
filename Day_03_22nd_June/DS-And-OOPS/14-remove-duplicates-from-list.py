lst=[]
print("Add 10 numbers in list")

for n in range(10):
    numbers=int(input("Enter number: "))
    lst.append(numbers)

print("List With Duplicate:",lst)

lst=list(set(lst))
print("List without duplicate:",lst)