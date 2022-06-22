n = int(input("Enter base value: "))
p = int(input("Enter power value: "))
exponent = 0
temp=[]

while exponent < p+1:
  res = n ** exponent
  exponent = exponent + 1
  temp.append(res)


print(temp)