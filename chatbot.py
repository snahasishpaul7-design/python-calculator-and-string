from datetime import datetime
import random
import time
import re
import pyjokes
import pyfiglet
import math
import webbrowser

print(pyfiglet.figlet_format("Welcome User!"))

print("Welcome to our chatbot platform. Please note, this system is currently under development, so some queries may not be fully supported.")
print("To exit the program at any time, please enter 'Q'.")

print("For math (With your  command attach the values)😊")

cbot = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hello! How can I assist you today?",
    "hey": "Hey there! What's up?",
    "what is your name": "I am your virtual assistant, ChatBot.",
    "who are you": "I am your friendly chatbot assistant.",
    "how are you": "I am functioning well, thank you for asking!",
    "what can you do": "I can answer your questions, chat with you, and assist with simple tasks.",
    "bye": "Goodbye! Have a great day ahead.",
    "goodbye": "See you again soon! Stay safe.",
    "who created you": "I was developed by a dedicated software engineer.",
    "are you human": "I am a virtual assistant, not a human.",
    "can you sing": "I’m not programmed to sing, but I can share interesting facts!",
    "can you dance": "I can't dance physically, but I can send you a dance emoji! 💃",
    "are you under development": "Yes, I am still under development. Some features may not be available yet.",
    "why can't you answer my question": "I’m continuously learning and improving, so please bear with me.",
    "thank you": "You’re very welcome!",
    "thanks": "No problem! Happy to help 😊",
    "i love you": "Thank you for your kindness! I’m here to help anytime.",
    "do you know how to do math?": "Yes, I can perform mathematical calculations like trigonometry, power, logarithm, hypot, max, min, even-odd, number sorting, ceil, floor, etc.",
    "do you know how to do math": "Yes, I can perform mathematical calculations like trigonometry, power, logarithm, hypot, max, min, even-odd, number sorting, ceil, floor, etc.",
    "can you solve basic math problems?": "Certainly. I am capable of solving basic math problems. Feel free to ask me one.",
    "can you do addition and subtraction?": "Yes, I can help you with both addition and subtraction. Please provide the numbers you'd like to work with.",
    "are you good at math?": "Yes, I am designed to handle basic math problems. What would you like me to solve?",
    "no": "Did I do something wrong?",
    "yes": "Oh... I am so sorry.",
    "ok": "Do you need any help today?",
    "okay": "Let me know if you have any questions!",
    "do you like me": "Of course! I'm here for you always 😊",
    "do you sleep": "I don’t sleep like humans do. I’m always here when you need me.",
    "do you eat": "I don’t eat, but I do process a lot of information!",
    "tell me a joke": pyjokes.get_joke(),
    "who is your best friend": "You are my best friend!",
    "what's your favorite color": "I like all colors equally, but blue looks great on screens!",
    "what's the time": f"The current time is {datetime.now().strftime('%I:%M %p')}",
    "what day is today": f"Today is {datetime.now().strftime('%A')}.",
    "what's today's date": f"Today's date is {datetime.now().strftime('%d-%m-%Y')}",
    "do you play games": "I don’t play games, but I can help you with game-related info or even play a number guessing game!",
    "can you help me": "Of course! What do you need help with?",
    "what is ai": "AI stands for Artificial Intelligence. It's the simulation of human intelligence in computers.",
    "what is your purpose": "My purpose is to assist you, make your tasks easier, and chat with you!",
    "tell me something interesting": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old!",
    "do you know bangladesh": "Yes! Bangladesh is a beautiful country in South Asia known for its rich culture, rivers, and resilience.",
    "what is python": "Python is a powerful, easy-to-learn programming language used for web development, automation, AI, and more."
}
rndom_question = {
    "i want to play guess game",
    "can i play the guess game",
    "let's play the guessing game",
    "start guess game",
    "i would like to play a guessing game",
    "i want to try the guess game",
    "let me play guess game",
    "can we play a guess game",
    "do you have a guessing game",
    "i feel like playing guess game",
    "i want to play a game where i guess",
}

while True:
    user = input("You: ").strip().lower()
    time.sleep(1)

    if user == "q":
        print("Thank you for using the chatbot. Goodbye!")
        break

    elif user in cbot:
        print("ChatBot:", cbot[user])

    elif user in rndom_question:
        print("Welcome to the Number Guessing Game!")
        ch = input("Do you want to enter the range yourself? (yes/no): ").lower().strip()
        try:
            if ch == "yes":
                while True:
                    try:
                        lower = int(input("Please enter the lower bound of the range: "))
                        upper = int(input("Please enter the upper bound of the range: "))
                        if lower >= upper:
                            print("Invalid range: Lower bound must be less than upper bound. Please try again.")
                        else:
                            break
                    except ValueError:
                        print("Please enter valid integers.")
            else:
                lower = random.randint(1, 50)
                upper = random.randint(51, 100)
                print(f"I have generated a random range for you: {lower} to {upper}")

            number_to_guess = random.randint(lower, upper)

            while True:
                try:
                    guess = int(input("Please guess the number: "))
                    if guess < number_to_guess:
                        print("Your guess is too low. Please try again.")
                    elif guess > number_to_guess:
                        print("Your guess is too high. Please try again.")
                    else:
                        print("🎉 Congratulations! You have guessed the correct number.")
                        break
                except ValueError:
                    print("Invalid input: Please enter a valid integer for your guess.")
        except ValueError:
            print("Invalid input: Please enter valid integers for the range values.")

    elif "time" in user and any(word in user for word in ["what", "which", "can", "today", "now"]):
        choice = input("Which time format do you prefer? Please enter 12 or 24: ").strip()
        now = datetime.now()
        if choice == "24":
            print("The current time (24-hour format) is:", now.strftime("%H:%M:%S"))
        elif choice == "12":
            print("The current time (12-hour format) is:", now.strftime("%I:%M:%S %p"))
        else:
            print("Invalid choice. Please enter either 12 or 24.")

    elif "date" in user and any(word in user for word in ["what", "which", "can", "today" , "current","now"]):
        now = datetime.now()
        print("Today's date is:", now.strftime("%Y-%m-%d"))

    elif any(op in user for op in ["+", "-", "*", "/", "sum", "plus", "addition", "add", "minus", "subtraction", "sub", "mult", "multiplication", "into", "div", "divide"]):
        numbers = [int(num) for num in re.findall(r'\d+', user)]
        if "+" in user or "plus" in user or "sum" in user or "add" in user or "addition" in user:
            print("The Result is:", sum(numbers))

        elif "-" in user or "minus" in user or "subtraction" in user or "sub" in user:
            if len(numbers) >= 2:
                result = numbers[0]
                for num in numbers[1:]:
                    result -= num
                print("Result:", result)
            else:
                print("Need at least 2 numbers.")

        elif "*" in user or "mult" in user or "multiplication" in user or "into" in user:
            result = 1
            for num in numbers:
                result *= num
            print("Result:", result)

        elif "/" in user or "div" in user or "divide" in user:     
            if len(numbers) >= 2:
                result = numbers[0]                         
                for num in numbers[1:]:
                    if num != 0:
                        result /= num
                    else:
                        print("Cannot divide by zero!")
                        result = None
                        break
                if result is not None:
                    print("Result:", result)
            else:
                print("Need at least 2 numbers.")

    elif "even" in user or "odd" in user:
        numbers = [int(num) for num in re.findall(r'\d+', user)]
        if len(numbers) >= 1:
            print("Analyzing numbers...\n")
            for num in numbers:
                if num % 2 == 0:
                    print(num, "is an even number")
                else:
                    print(num, "is an odd number")
        else:
            print("No numbers provided to check.")

    elif "max" in user or "maximum" in user:
        numbers = [int(num) for num in re.findall(r'\d+', user)]
        if len(numbers) >= 2:
            print("Analyzing The Numbers...... \n")
            print("The Maximum Number Is", max(numbers))
        else:
            print("No numbers found in your input.")

    elif "min" in user or "minimum" in user:
        numbers = [int(num) for num in re.findall(r'\d+', user)]
        if len(numbers) >= 2:
            print("Analyzing The Numbers...... \n")  
            print("The Minimum Number Is ", min(numbers)) 
        else:
            print("No numbers found in your input.")
    
    elif "arrange in order" in user or "arange in order"  in user or "put in order" in user or "sort in order" in user or "organize sequentially" in user or "arrange sequentially" in user or "arrange in number" in user:
        time.sleep(1)
        print("Two value needed")
        c = int(input("Enter The Lower Value:-"))
        r = int(input("Enter The upper Value:-"))
        if c > r:
            print("Please enter the lower value first")
        else:
            for i in range(c, r + 1):
                print(i, end=" ")
            print()
 
    elif "decreasing order" in user or "descending order" in user or "reverse order" in user or "from high to low" in user or "sort descending" in user or "big to small" in user:
        time.sleep(1)
        g = int(input("Enter The upper Value:-"))
        f = int(input("Enter The lower Value:-"))
        if g < f:
            print("Please enter the upper value first")
        else:
            for i in range(g, f, -1):
                print(i, end=" ")
            print()

    elif "joke" in user:
        jokes = pyjokes.get_joke()
        print("Here Is Joke For You")
        print(jokes)

    elif any(re.search(r'\b' + x + r'\b', user) for x in ["traffic light system", "tell me about traffic light", "understand me about traffic light system", "red", "red light", "yellow", "yellow light", "amber", "green", "green light"]):
        if re.search(r'\bred\b|\bred light\b', user):
            print("\nTraffic Light System \n")
            print(" RED LIGHT – Stop")
            print("When the light is red, vehicles must stop completely.")

        elif re.search(r'\byellow\b|\byellow light\b|\bamber\b', user):
            print("\U0001F7E1 YELLOW/AMBER LIGHT – Get Ready")
            print("The light is about to change. Prepare to stop or proceed with caution.")

        elif re.search(r'\bgreen\b|\bgreen light\b', user):
            print("GREEN LIGHT – Go")
            print("You can move now, but ensure the road is clear.")

        else:
            print("\nTraffic Light System \n")
            print(" RED LIGHT – Stop")
            print(" YELLOW/AMBER LIGHT – Get Ready")
            print(" GREEN LIGHT – Go")

    elif any(y in user for y in ["value of py","py value","pi", "pi value","value of pi","pie value","value of pie","power","to the power","factoriel","factorial" , "factoral","radian","radians","redian","redians","square","squre","sq","square root","root", "square of root","root of square","root of squre","squre of root" ,"sin","sine" ,"cos" ,"tan" ,"cot" ,"ceil" , "floor" ,"log","log base 10" ,"log base ten","10 base log" , "ten base log" , "log base 2", "2 base log", "log base two", "two base log","hypot" ]):
       

        if "value of py" in user or "py value" in user or "pi value" in user or "value of pi" in user or "pie value" in user or "value of pie" in user or "pi" in user:
            print(math.pi)

        elif "power" in user or "to the power" in user:
            pat = [float(num) for num in re.findall(r'\d+', user)]
            if len(pat) >= 2:
                base = pat[0]
                ex = pat[1]
                result = math.pow(base, ex)
                print("The power is:", result)
            else:
                print("Please enter at least two numeric values 😄")

        elif "factorial" in user or "factoriel" in user or "factoral" in user:
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if pat[0] >= 0:
                result2 = math.factorial(pat[0])
                print ("The factorial is:", result2)
            else:
                print("Factorial of negative numbers and 0 is not defined.")

        elif "radian" in user or "radians" in user or "redian" in user or "redians" in user:
            pat = [float(num) for num in re.findall(r'\d+\.?\d*', user)]
            if pat:
                base = pat[0]
                result3 = math.radians(base) 
                print("The radian of this value is", result3)
            else:
                print("Please enter a number to convert to radians.")
        
        elif "square" in user or "squre" in user or "sq" in user or "square root" in user or "root" in user or "square of root" in user or "root of square" in user or "root of squre" in user or "squre of root" in user:
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if pat:
                base  =  pat[0]
                result4 = math.sqrt(base)
                print("The square of this value is :-" , result4)
            else:
                print("Enter a valid integer number")
                
        elif "sin" in user or "sine" in user :
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if pat:
                base  =  pat[0]
                angle = math.radians(base)
                result5 = math.sin(angle)
                print("The value of sin is :-" , result5)
            else:
                print("Enter a valid integer number")
        
                    
        elif "cos" in user :
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if pat:
                base  =  pat[0]
                angle = math.radians(base)
                result6 = math.cos(angle)
                print("The value of cos is :-" , result6)
            else:
                print("Enter a valid integer number")
        
        elif "tan" in user :
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if len(pat) > 0:
                base  =  pat[0]
                angle = math.radians(base)
                result7 = math.tan(angle)
                print("The value of tan is :-" , result7)
            else:
                print("Enter a valid integer number")
        
        elif "cot" in user :
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if len(pat) > 0:
                base  =  pat[0]
                angle = math.radians(base)
                result8 = 1/math.tan(angle)
                print("The value of cot is :-" , result8)
            else:
                print("Enter a valid integer number")
        
        elif "ceil" in user:
            pat = [float(num) for num in re.findall(r'\d+', user)]
            if len(pat) > 0:
                base  =  pat[0]
                result9 = math.ceil(base)
                print("ceil number is = " , result9)
            else:
                print("Enter a valid integer number")
        
        elif "floor" in user:
            pat = [float(num) for num in re.findall(r'\d+', user)]
            if len(pat) > 0:
                base  =  pat[0]
                result10 = math.floor(base)
                print("floor number is = " , result10)
            else:
                print("Enter a valid integer number")
                
        elif "trunc" in user:
            pat = [float(num) for num in re.findall(r'\d+', user)]
            if len(pat) > 0:
                base  =  pat[0]
                result11 = math.trunc(base)
                print("trunc number is = " , result11)
            else:
                print("Enter a valid integer number")   
        
        elif "log" in user and not  any(z in user for z in ["log base 10", "10 base log", "log base ten", "ten base log","log base 2", "2 base log", "log base two", "two base log","custom base log", "custom log"]):
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if pat:
                base = pat[0]
                result10 = math.log(base)
                print(f"log (natural) of {base} value is = " , result10)
            else:
             print("Enter a valid integer number")
             
        elif any(z in user for z in ["log base 10", "10 base log", "log base ten", "ten base log"]):
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if pat:
                base = pat[0]
                result11 = math.log10(base)
                print(f"log (base 10) of {base} value is = " , result11)
            else:
                print("Enter a valid integer number")
        
        elif any(z in user for z in ["log base 2", "2 base log", "log base two", "two base log"]):
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if pat:
                base = pat[0]
                result12 = math.log2(base)
                print(f"log (base 2) of {base} value is = " , result12)
            else:
                print("Enter a valid integer number")
        
        elif any(z in user for z in ["Custom base log" , "custom log"]):
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if pat:
                base = pat[0]
                ex = pat[1]
                result13 = math.log(base,ex)
                print(f"custom log  of {base} value is = " , result13)
            else:
                print("Enter a valid integer number") 
        
        elif "hypot" in user:
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if pat:
                base = pat[0]
                ex = pat[1]
                result12 = math.hypot(base , ex)
                print(" Hypot of this value is= "   , result12)
            else:
                print("Enter a valid integer number")
    elif any (re.search(r'\b' + se+ r'\b', user) for se in[ "open google", "google" ,"google open","open youtube","youtube","youtube open"]): 
         if re.search(r'\byoutube\b|\bopen youtube\b|\byoutube open\b', user):
             youtube="https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
             print("Opening Youtube.....")
             webbrowser.open("Opening Youtube.....",youtube)        
    
    else:
      print("I can't understand sorry")   
      
  
            
    

            
                
            
       
          

