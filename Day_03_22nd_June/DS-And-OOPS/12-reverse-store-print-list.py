lst=[]
print("Add 10 numbers in list")

for n in range(10):
    numbers=int(input("Enter number: "))
    lst.append(numbers)

#reverse
lst.reverse()
print("Reverse List:",lst)

lst2=lst
print(lst2)
