import random
import time
while True:
    user_input  = input(str("Do you want to generate password:-"))
    if user_input in ["yes" , "yeap" , "ok"]:
        
        
        a = int(input("Enter the length: "))

        st = "abcdefghijklmnopqrstuvwxyz"
        num = "123456789"
        sch = "#@$"
        ch = st + num + sch
        password = "" 

        for i in range(a):
            password += random.choice(ch) 
        time.sleep(2)
        print("Password is:", password)
    else:
        print("Thank you....")
        break