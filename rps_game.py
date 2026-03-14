import random
print("Just type rock, paper or scissor")
while True:
    play = input("Press 1 to play, 2 to stop: ").strip()
    
    if play == "1":
        computer_choice = ["rock", "paper", "scissor"]
        user_choice = input("Enter your choice: ").strip().lower()
        take = random.choice(computer_choice)
        print(f"Computer chose: {take}")

        if user_choice not in computer_choice:
            print("Please check spelling or try again.\n")
            continue  
        elif user_choice == take:
            print("It's a tie!\n")
        elif (user_choice == "rock" and take == "scissor") or  (user_choice == "paper" and take == "rock") or(user_choice == "scissor" and take == "paper"): 
            print("The winner is You\n")
        else:
            print("Winner is computer\n")
            
    elif play == "2":
        print("Game stopped. Bye!")
        break
    else:
        print("Invalid input. Please press 1 or 2.\n")