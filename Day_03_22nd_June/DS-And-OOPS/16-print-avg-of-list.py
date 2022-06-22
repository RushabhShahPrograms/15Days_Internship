lst=[]
print("Add 10 numbers in list")

for n in range(10):
    numbers=int(input("Enter number: "))
    lst.append(numbers)

print("List:",lst)

avg=sum(lst)/len(lst)
print("Average of List:",avg)