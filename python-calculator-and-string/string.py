import time
print("ALL STRING FUNCTION GOING TO USE IN THIS CODE....")
print("Press 1 to get the upper form of text....\n"
      "Press 2 to get the lower form of text....\n"
      "Press 3 to get the title form of text....\n"
      "Press 4 to get the capitalize form of text\n"
      "Press 5 to get the swapcase form of text\n"
      "Press 6 to get  all form at a time...\n"
      "press 7  to stop the code........")
while True:
    time.sleep(2)
    text = input("Press 1 to 7 button to get any form of text:-")
    time.sleep(2)
    if text == "1":
        time.sleep(2)
        word = input(str("Enter the text:-"))
        time.sleep(2)
        print("The upper form of this sentence or word is:-" , word.upper())
        time.sleep(2)
    elif text == "2":
        time.sleep(2)
        word2 = input(str("Enter the text:-"))
        time.sleep(2)
        print("The lower form of this sentence or word is:-" , word2.lower())
        time.sleep(2)
    elif text == "3":
        time.sleep(2)
        word3 = input(str("Enter the text:-"))
        time.sleep(2)
        print("The  title of this sentence or word is:-" , word3.title())
        time.sleep(2)
    elif text == "4":
        time.sleep(2)
        word4 =  input(str("Enter the text:-"))
        time.sleep(2)
        print("The  capitalize form of this sentence or word is:-" , word4.capitalize())
        time.sleep(2)
    elif text == "5":
        time.sleep(2)
        word5 = input(str("Enter the text:-"))
        time.sleep(2)
        print("The swapcase this sentence or word is:-" , word5.swapcase())
        time.sleep(2)
    elif text =="6":
        time.sleep(2)
        
        word = input(str("Enter the text:-"))
        time.sleep(1)
        print("The upper form of this sentence or word is:-" , word.upper())
        time.sleep(1)
        print("The lower form of this sentence or word is:-" , word.lower())
        time.sleep(1)
        print("The  title of this sentence or word is:-" , word.title())
        time.sleep(1)
        print("The  capitalize form of this sentence or word is:-" , word.capitalize())
        time.sleep(1)
        print("The swapcase this sentence or word is:-" , word.swapcase())
        time.sleep(1)
    elif text  == "7":
        time.sleep(1)
        print("BYE BYE SE YOU NEXT TIME......")
        time.sleep(1)
        break
    else:
        time.sleep(1)
        print("PLEASE ENTER VALID STRING.........")
time.sleep(1)       
print("Thank you for using this.......")       

