'''
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for 
their salary and year of service and print the net bonus amount.
'''

service_year=int(input("Enter how many years you have done service: "))

if service_year>5:
    print("You are eligible for bonus!!!")
    salary=int(input("Enter your salary: "))

    bonus=salary*0.05
    print("Your bonus is of",bonus,"dollar")

else:
    print("Sorry You will not receive bonus.")