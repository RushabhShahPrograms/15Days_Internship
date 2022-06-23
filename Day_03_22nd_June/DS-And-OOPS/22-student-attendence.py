def Exam(classes_held,classes_attended):
    per=(classes_attended/classes_held)*100
    print("Percentage:",per)
    
    if per>=75:
        return "Student is allowed to sit in exam"
    else:
        return "Student is not allowed to sit in exam"

classes_held=int(input("Enter number of classes held: "))
classes_attended=int(input("Enter number of classes attended: "))
print(Exam(classes_held,classes_attended))