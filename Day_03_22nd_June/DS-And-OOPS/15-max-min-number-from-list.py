lst=[]
print("Add 10 numbers in list")

for n in range(10):
    numbers=int(input("Enter number: "))
    lst.append(numbers)

lmax=max(lst)
print("Max value:",lmax)
lmin=min(lst)
print("Min value:",lmin)
