days = int(input("Enter number of days: "))

years = days//365
months = (days-years*365)//30
remaining_days=(days-years*365-months*30)

print("Years: ",years,"\nMonths: ",months,"\nDays: ",remaining_days)