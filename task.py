print("welcome to task management app")

print("  Type add or 1 for adding files in task\n"
        "Type update or 2 for update tasks.....\n"
        "Type del or 3 to delete files\n"
        "Type view or 4 to view files\n"
        "Type exit or e or 5 to exit files\n ")

user = input("Do you want to use this (yes /no):-").lower()
if user == "yes":
    
    task = []


    user_input   =  int(input("How many task you want to add:-"))

    for i in range(1 , user_input + 1 ):
        
        task_name = input("Enter the name of task:-")
        task.append(task_name)

    print(task)

    while True:
        first_input = input("which type of operation you want:-")

        if first_input == "1" or first_input == "add":
            new_task = input("Enter new task:-")
            task.append(new_task)
            print(task)

        elif first_input == "2" or first_input == "update":
            en_tas = input("Enter which task you want to update:-")

            if en_tas in task:
                nup_task = input("Enter new task:-")
                ind = task.index(en_tas)  
                task[ind] = nup_task
                print(f"Your updated task is {nup_task}")
            else:
                print("Task not found")
    
        elif first_input == "3" or first_input == "del":
            d_tas = input("Enter which task you want to delete:-")
            if d_tas in task:
                ind = task.index(d_tas) 
                del task[ind]   
                print(f"Task {d_tas} has been deleted")  
            
        elif first_input == "4" or first_input == "view":
            print(f"Total task {task}")
    
        elif first_input == "5" or first_input == "e":
            break
    
        else:
            print("Invalid input") 
            
elif user == "no":
    print("Bye Bye.. see you soon")
    quit
else:
    print("invalid expression")   
        

    

