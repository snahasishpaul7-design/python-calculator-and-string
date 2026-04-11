print("___________ WELCOME TO STUDENT MANAGER PROGRAM______________________")

students = {}

while True:
    print("Press 1 for add result\n")
    print("Press 2 for view  result\n")
    print("Press 3 for check result\n")
    print("Press 4 for stop program\n")
    
    choice = input("Enter which operation you want to do:-")
    
    if choice == "1":
        name = input("Enter student  name:-")
        marks = int(input("Enter the mark of student:-"))
        students[name]= marks
        print(f"{name} successfully added")
    
    elif choice  == "2":
        if not name:
            print("No data found")
        else:
            
            for name,marks in students.items():
            
                print("NAME IS",name )
                print("MARKS IS" ,marks)
    
    elif choice == "3":
        name = input("Enter the name of student:-")
        if name in students:
            marks = students[name]
            if marks > 40:
                print(f"{name} is PASS")
            else:
                print("Sorry you are fail")
        else:
            print("No name found")
            
    elif choice == "4":
        
        print("See you soon")
        break
    else:
        print("Invalid expression")