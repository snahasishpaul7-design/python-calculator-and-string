import random

import time

while True:
    
    val = input("Do you want to play guessing game:-").strip().lower()
    
    if val in ["yes","yeap","yea","ok"]:
        
        upper_val = int(input("Enter the upper value:-"))
        
        lower_val = int (input("Enter the lower value:-"))
        
        ran = random.randint(lower_val , upper_val)
        
        guess= int(input("Enter the guessing number you have guess:-"))
        
        if ran == guess:
            print("You are correct...")
        else:
            print("Try again....")
    else:
        time.sleep(2)
        
        print("See you again......")
        
        break
    
time.sleep(1)    

print("Thank you......")