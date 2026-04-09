print("Welcome....To student management code")
students = []

useer_input = input("Do you want to use this :-").lower()
if useer_input == "yes":
    
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Show Total & Average")
        print("6. Exit")

        user_input = int(input("Which type operation you want:-"))
        
        
        if user_input == 1:
            n = input("Enter the name:-")
            s = input("Enter the subject:-")
            m = int(input("Enter the marks:-"))
            
            student = {
                "name" :n,
                
                "subject" : s,
                
                "marks" : m
                
            }
            
            students.append(student)
            print("Student added......")
        
        
        elif user_input == 2:
            if len(students) == 0:
                print("Student not found")
            else:
                for i, s in enumerate(students,start=1):
                    print(i , s["name"], "|" ,s["subject"],"|" ,s["marks"])
                    
        
        elif user_input == 3:
            name = input("Which one you want to update")
            for s in students:
                if s["name"] == name:
                    s["subject"] = input("Enter the new subject:-") 
                    s["marks"]  = input("Enter the new marks")
                    print("Updated successfully")
                    
        elif user_input == 4:
            name = input("Which thing you want delete:-")
            for s in students:
                if s["name"] == name:
                    students.remove(s)
                    print("Deleted successfully")
            
        elif user_input==5:
            if len(students)== 0:
                print("No data available")
            else:
                total = 0
                for s in students:
                    marks = s["marks"]
                total = total + marks    
                print("Total marks is " , total)
                avg = total/len(student)
                print("Average marks is " , avg)
        elif user_input == 6:
            print("Good bye")
            break
        else:
          print("Invalid expression")             
else:
    quit     