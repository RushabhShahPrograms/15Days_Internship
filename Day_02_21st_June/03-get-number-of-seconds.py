seconds=int(input("Enter seconds: "))

hour = seconds // 3600 
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(hour,":",minutes,":",seconds)