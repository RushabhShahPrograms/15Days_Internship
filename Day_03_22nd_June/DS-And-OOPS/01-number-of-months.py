days = int(input("Enter number of days: "))

years = days//365
months = (days-years*365)//30

print("Months: ",months)