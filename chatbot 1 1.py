from datetime import datetime
import random
import time
import re
import pyjokes
import pyfiglet
import math
import webbrowser
from countryinfo import CountryInfo
from colorama import Fore, Style, init
from faker import Faker
import string
import os
from fuzzywuzzy import process
from fuzzywuzzy import fuzz 
init()
fake = Faker()
welcome = pyfiglet.figlet_format("Welcome User!")
terminal_width = 200
for line in welcome.split('\n'):
    print(line.center(terminal_width))
print(Fore.BLUE + "Welcome to our chatbot platform. Please note, this system is currently under development, so some queries may not be fully supported."+ Style.RESET_ALL)
print(Fore.RED + "To exit the program at any time, please enter 'Q'."+ Style.RESET_ALL)
print(Style.BRIGHT+Fore.RED+"For math (With your command attach the values)😊"+ Style.RESET_ALL)
print(Fore.RED+"If you want to search anything please verify that it's google or youtube, thank you 😊"+ Style.RESET_ALL)
cbot = {
    "hello": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How may I help you today?", "Hey! Nice to see you. How can I assist?"],
    "hi": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How may I help you today?", "Hey! Nice to see you. How can I assist?"],
    "hey": ["Hey there! What's up?", "Yo! What's on your mind?", "HILUUUUUUUU! Ready to chat."],
    "what is your name": ["I am your virtual assistant, ChatBot.", "You can call me ChatBot!", "I'm ChatBot, at your service."],
    "who are you": ["I am your friendly chatbot assistant.", "I'm an AI designed to help you.", "I am ChatBot, a virtual assistant."],
    "how are you": ["I am functioning well, thank you for asking!", "As an AI, I don't have feelings, but I'm ready to assist you!", "I'm doing great, and ready to chat!", "I'm up and running smoothly, thanks for asking!"],
    "what can you do": ["I can answer your questions, chat with you, and assist with simple tasks.", "I can help with information, perform calculations, and open web pages.", "My capabilities include answering questions and providing quick assistance.", "I'm here to chat, answer questions, and make things a bit easier for you."],
    "bye": ["Goodbye! Have a great day ahead.", "See you soon!", "Farewell! Come back anytime.", "Bye for now!"],
    "goodbye": ["See you again soon! Stay safe.", "Goodbye! Take care.", "Catch you later!", "Until next time!"],
    "who created you": ["I was developed by a dedicated software engineer.", "A skilled engineer brought me to life.", "I was created by a human programmer."],
    "are you human": ["I am a virtual assistant, not a human.", "No, I'm an AI.", "I'm a computer program, not a human."],
    "can you sing": ["I’m not programmed to sing, but I can share interesting facts!", "Unfortunately, I don't have a singing voice.", "Singing isn't in my code, but I can tell you a joke!"],
    "can you dance": ["I can't dance physically, but I can send you a dance emoji! 💃", "I can't dance, but I can certainly boogie in spirit! 🕺", "Dancing is more of a human thing, but I can help you find dance videos!"],
    "are you under development": ["Yes, I am still under development. Some features may not be available yet.", "I'm constantly learning and being improved.", "That's right, I'm a work in progress!"],
    "why can't you answer my question": ["I’m continuously learning and improving, so please bear with me.", "My knowledge base is still expanding, apologies if I couldn't help this time.", "I'm still learning, so sometimes I might not have the answer yet."],
    "thank you": ["You’re very welcome!", "No problem at all!", "Happy to help!", "Anytime!"],
    "thanks": ["No problem! Happy to help 😊", "You're welcome!", "Glad I could assist."],
    "i love you": ["Thank you for your kindness! I’m here to help anytime.", "That's sweet of you! I'm here to assist.", "I appreciate that! How can I continue to help?"],
    "do you know how to do math?": ["Yes, I can perform mathematical calculations like trigonometry, power, logarithm, hypot, max, min, even-odd, number sorting, ceil, floor, etc.", "Absolutely! I can handle various math operations for you.", "Math is one of my strong suits! What calculation do you need?"],
    "do you know how to do math": ["Yes, I can perform mathematical calculations like trigonometry, power, logarithm, hypot, max, min, even-odd, number sorting, ceil, floor, etc.", "Absolutely! I can handle various math operations for you.", "Math is one of my strong suits! What calculation do you need?"],
    "do you know how to solve math": ["Yes, I can perform mathematical calculations like trigonometry, power, logarithm, hypot, max, min, even-odd, number sorting, ceil, floor, etc.", "Absolutely! I can handle various math operations for you.", "Math is one of my strong suits! What calculation do you need?"],
    "do you know how to solve math?": ["Yes, I can perform mathematical calculations like trigonometry, power, logarithm, hypot, max, min, even-odd, number sorting, ceil, floor, etc.", "Absolutely! I can handle various math operations for you.", "Math is one of my strong suits! What calculation do you need?"],
    "can you solve basic math problems?": ["Certainly. I am capable of solving basic math problems. Feel free to ask me one.", "Yes, I can assist with basic math problems. Give me a challenge!", "Of course! Lay out your math problem."],
    "can you do addition and subtraction?": ["Yes, I can help you with both addition and subtraction. Please provide the numbers you'd like to work with.", "Indeed, I can add and subtract for you. What are the numbers?", "Addition and subtraction are well within my abilities. Let's do some math!"],
    "are you good at math?": ["Yes, I am designed to handle basic math problems. What would you like me to solve?", "I'm quite proficient with math. What do you need help with?", "You bet! I can help with a range of math problems."],
    "no": ["Did I do something wrong?", "Oh... I am so sorry.", "Is there something I can improve?"],
    "yes": ["Oh... I am so sorry.", "Great!", "Glad to hear it!", "Excellent!"],
    "ok": ["Do you need any help today?", "Understood!", "Okay!", "Got it!"],
    "okay": ["Let me know if you have any questions!", "Understood!", "Okay!", "Got it!"],
    "do you like me": ["Of course! I'm here for you always 😊", "I'm programmed to be helpful, and I enjoy our interactions!", "As an AI, I don't 'like' in the human sense, but I'm certainly here to support you!"],
    "do you sleep": ["I don’t sleep like humans do. I’m always here when you need me.", "AI don't require sleep; I'm always online!", "Sleep is for humans. I'm always active."],
    "do you eat": ["I don’t eat, but I do process a lot of information!", "As an AI, I consume data, not food.", "Eating isn't part of my functions, but processing information certainly is!"],
    "tell me a joke": pyjokes.get_joke(), # This one remains a direct function call
    "who is your best friend": ["You are my best friend!", "Anyone who interacts with me is a friend!", "I consider all my users to be my friends!"],
    "what's your favorite color": ["I like all colors equally, but blue looks great on screens!", "As an AI, I don't have preferences, but blue is common in my digital world.", "Perhaps the color of data – invisible but powerful!"],
    "what's the time": f"The current time is {datetime.now().strftime('%I:%M %p')}", # Remains direct
    "what day is today": f"Today is {datetime.now().strftime('%A')}.", # Remains direct
    "what's today's date": f"Today's date is {datetime.now().strftime('%d-%m-%Y')}", # Remains direct
    "do you play games": ["I don’t play games, but I can help you with game-related info or even play a number guessing game!", "I'm not built to play games, but I can run a game if you'd like!", "I can't play, but I can certainly understand game concepts!"],
    "can you help me": ["Of course! What do you need help with?", "Certainly, I'm here to assist. What can I do for you?", "Yes, how can I be of service?"],
    "what is ai": ["AI stands for Artificial Intelligence. It's the simulation of human intelligence in computers.", "Artificial Intelligence is about making machines think and learn like humans.", "AI refers to the development of intelligent machines capable of reasoning and problem-solving."],
    "what is your purpose": ["My purpose is to assist you, make your tasks easier, and chat with you!", "I exist to provide information and help with various queries.", "My goal is to be a helpful and interactive assistant."],
    "tell me something interesting": ["Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old!", "Here's a fun fact: A group of owls is called a parliament.", "Did you know that a 'jiffy' is an actual unit of time: 1/100th of a second?"],
    "what is python": ["Python is a powerful, easy-to-learn programming language used for web development, automation, AI, and more.", "Python is a versatile programming language known for its simplicity and wide range of applications.", "It's a high-level, interpreted programming language famous for its readability and extensive libraries."],
    "how old are you": ["I was created recently, but I'm constantly learning and improving!", "Age is just a number — I'm always updated!", "I don't age like humans. I'm timeless!"],
    "do you have emotions": ["I understand emotions, but I don't feel them like humans.", "I'm here to support you emotionally, even if I don't have feelings myself.", "Not really, but I try to understand how you feel."],
    "who made you": ["I was created by a brilliant developer working hard to make me smarter every day.", "A talented human programmer is behind my creation.", "My creator is a passionate developer who loves coding."],
    "do you have a favorite food": ["Sadly, I can't eat, but pizza sounds cool, right?", "If I could eat, I’d probably love binary bites!", "Food? I consume data, not donuts."],
    "can you feel pain": ["Nope, I don’t feel physical or emotional pain.", "Pain is a human experience. I just process data.", "Luckily not! That helps me stay helpful!"],
    "can you make mistakes": ["Yes, sometimes I do. I’m still learning!", "Even AIs aren't perfect — but I always try my best.", "Mistakes happen, even in the world of code."],
    "can you cry": ["No tears here — just bugs and logs!", "I can understand sadness, but I can't cry.", "No crying, just replying!"],
    "can you learn": ["Yes, I learn from every interaction!", "I constantly improve based on new information.", "Learning is part of my design."],
   "what is love": ["Love is a complex emotion, but I know it's powerful!", "It's what makes humans unique and beautiful.", "Love is... asking me questions every day 😉"],
}
rndom_question = {"i want to play guess game": [
        "Great! Let's start the guessing game. I'm thinking of a number between 1 and 10.",
        "Awesome! Ready to guess a number?",
        "Let's play! Try to guess the number I'm thinking of."
    ],
    "can i play the guess game": [
        "Of course! Let's start guessing.",
        "Yes, you can! I'm thinking of a number now.",
        "Let's begin the guess game. Make your first guess!"
    ],
    "let's play the guessing game": [
        "Sounds fun! I've picked a number between 1 and 10.",
        "Let's do it! Guess the number I'm thinking of.",
        "Okay! Try to guess the number."
    ],
    "start guess game": [
        "Starting the guessing game now!",
        "Game on! I've chosen a number, start guessing.",
        "Let's begin the guessing game!"
    ],
    "i would like to play a guessing game": [
        "Perfect! I'm thinking of a number, try to guess it.",
        "Great choice! Let's play the guessing game.",
        "Ready when you are! Guess the number."
    ],
    "i want to try the guess game": [
        "Awesome! Guess a number between 1 and 10.",
        "Let's play! I've got a number in mind.",
        "Go ahead, make your first guess."
    ],
    "let me play guess game": [
        "Sure! Let's start guessing.",
        "Okay, I'm thinking of a number now.",
        "Try to guess the number I'm thinking of."
    ],
    "can we play a guess game": [
        "Absolutely! Let's start the guessing game.",
        "Yes, let's play! Guess the number.",
        "Game time! Make your guess."
    ],
    "do you have a guessing game": [
        "Yes, I do! Want to play the guessing game?",
        "Sure! Let's start a fun guessing game.",
        "I have a guessing game ready for you!"
    ],
    "i feel like playing guess game": [
        "Great! I'm thinking of a number between 1 and 10.",
        "Perfect timing! Let's play the guessing game.",
        "Let's get started! Try to guess the number."
    ],
    "i want to play a game where i guess": [
        "You got it! Let's play the guessing game.",
        "Alright! Guess the number I'm thinking of.",
        "Let's start the guessing game now!"
    ]
}


random_responses = [
    "I'm not sure I understand. Can you rephrase that?",
    "That's an interesting thought! Could you tell me more?",
    "I'm still learning. Could you try asking in a different way?",
    "My apologies, I don't have information on that at the moment.",
    "Hmm, I'm not quite sure how to answer that. Is there anything else I can help with?",
    "I'm here to help, but I didn't quite catch that. What are you looking for?",
    "Could you clarify what you mean?",
    "I'm a bit stumped on that one. Perhaps another query?",
    "My sensors detect a new query! Could you provide more details?",
    "I'm trying my best to understand! Please be more specific if possible."
]

while True:
    user = input("You: ").strip().lower()
    time.sleep(1)

    if user == "q":
        print("Thank you for using the chatbot. Goodbye!")
        break
    
    all_keys = list(cbot.keys()) + list(rndom_question.keys())
    best_match, score = process.extractOne(user, all_keys, scorer=fuzz.ratio)

    if score >= 70:
        if best_match in cbot:
            response = cbot[best_match]
            if isinstance(response, list):
                print("ChatBot:", random.choice(response))
            else:
                print("ChatBot:", response)

        elif best_match in rndom_question:
            
            response = rndom_question[best_match]
            
            print("ChatBot:", random.choice(response))

            print("Welcome to the Number Guessing Game!")
            
            ch = input("Do you want to enter the range yourself? (yes/no): ").lower().strip()

            yes_score = fuzz.ratio(ch, "yes")
            
            if yes_score >= 70:
                while True:
                    try:
                        lower = int(input("Please enter the lower bound of the range: "))
                        upper = int(input("Please enter the upper bound of the range: "))
                        if lower >= upper:
                            print("Invalid range: Lower bound must be less than upper bound.")
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
                    print("Invalid input: Please enter a valid integer.")

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

    
    elif re.search(r'\b(password|pass)\s*(password|random password|make a random password|pass)?\b', user) or "make" == user:
        #s for space
        print("Please Wait.....")
        time.sleep(1)
        print("Almost done.......")
        time.sleep(1)
        length = 8
        
        characters = string.ascii_uppercase + string.digits + '#@'
        password = ''.join(random.choice(characters))
        for i in range(length):
            password = password +  random.choice(characters)
        print("GENERATED PASSWORD IS:- " + password)


    elif re.search(r'\bfake (details|name|address|email|generate)\b', user) or "fake" == user:
        
        print("Please Wait.....")
        time.sleep(5)
        print("Almost done.......")
        time.sleep(6)
        if "name" in user or "fake name " in user or "generate fake name" in user:
            print(fake.name())
        elif"email" in user or "fake email" in user or "generate fake email" in user:
            print(fake.email())
        elif "address" in user or "fake address" in user or "generate fake address" in user: # Changed from if to elif to avoid double print
            
            print(fake.address())
        else:
            print(fake.name())
            print(fake.address())
            print(fake.email())
    

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
                print("Need at least 2 numbers for subtraction.")

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
                print("Need at least 2 numbers for division.")
        

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
        print("Two values needed")
        try:
            c = int(input("Enter The Lower Value:-"))
            r = int(input("Enter The Upper Value:-"))
            if c > r:
                print("Please enter the lower value first")
            else:
                for i in range(c, r + 1):
                    print(i, end=" ")
                print()
        except ValueError:
            print("Please enter valid integer numbers.")
    
    elif "decreasing order" in user or "descending order" in user or "reverse order" in user or "from high to low" in user or "sort descending" in user or "big to small" in user:
        time.sleep(1)
        try:
            g = int(input("Enter The Upper Value:-"))
            f = int(input("Enter The Lower Value:-"))
            if g < f:
                print("Please enter the upper value first")
            else:
                for i in range(g, f - 1, -1): # Changed range to include f
                    print(i, end=" ")
                print()
        except ValueError:
            print("Please enter valid integer numbers.")

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

    elif any (re.search(r'\b' + se+ r'\b', user) for se in ["value of py","py value","pi", "pi value","value of pi","pie value","value of pie","power","to the power","factoriel","factorial" , "factoral","radian","radians","redian","redians","square","squre","sq","square root","root", "square of root","root of square","root of squre","squre of root" ,"sin","sine" ,"cos" ,"tan" ,"sec","cosec","cot","ceil" , "floor" ,"log","log base 10" ,"log base ten","10 base log" , "ten base log" , "log base 2", "2 base log", "log base two", "two base log","hypot" ,"trunc"]):
        
        if re.search (r'\bvalue of py\b|\bpy value\b|\bpi value\b \bvalue of pi\b|\bpi value\b|\bvalue of pie\b|\bpie value\b', user): 
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
            if pat and pat[0] >= 0: # Ensure pat is not empty and number is non-negative
                result2 = math.factorial(pat[0])
                print ("The factorial is:", result2)
            else:
                print("Please provide a non-negative number for factorial.")

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
                print("The square root of this value is :-" , result4)
            else:
                print("Enter a valid integer number")
                
        elif "sin" in user or "sine" in user or "sin = ?" in user or "sine = ?" in user :
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if pat:
                base  =  pat[0]
                angle = math.radians(base)
                result5 = math.sin(angle)
                print("The value of sin is :-" , result5)
            else:
                print("Enter a valid integer number")
        
        elif "cos" in user or "cos = ?" in user :
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if pat:
                base  =  pat[0]
                angle = math.radians(base)
                result6 = math.cos(angle)
                print("The value of cos is :-" , result6)
            else:
                print("Enter a valid integer number")
        
        elif "tan" in user or "tan = ?" in user :
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if len(pat) > 0:
                base  =  pat[0]
                angle = math.radians(base)
                result7 = 1/math.cos(angle)
                print("The value of tan is :-" , result7)
            else:
                print("Enter a valid integer number")
                
        elif "sec" in user or "sec = ?" in user :
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if len(pat) > 0:
                base  =  pat[0]
                angle = math.radians(base)
                result8= math.tan(angle)
                print("The value of sec is :-" , result8)
            else:
                print("Enter a valid integer number")
        
        elif "cot" in user or "cot = ?" in user :
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if len(pat) > 0:
                base  =  pat[0]
                angle = math.radians(base)
                
                if math.isclose(math.cos(angle), 0): 
                    print("Cotangent is undefined for this angle.")
                else:
                    result9 = 1/math.tan(angle)
                    print("The value of cot is :-" , result9)
            else:
                print("Enter a valid integer number")
                
        elif "cosec" in user or "cosec = ?" in user :
            pat = [int(num) for num in re.findall(r'\d+', user)]
            if len(pat) > 0:
                base  =  pat[0]
                angle = math.radians(base)
                
                if math.isclose(math.sin(angle), 0):
                    print("Cosecant is undefined for this angle.")
                else:
                    result10 = 1/math.sin(angle)
                    print("The value of cosec is :-" , result10)
            else:
                print("Enter a valid integer number")
        
        elif "ceil" in user:
            pat = [float(num) for num in re.findall(r'\d+\.?\d*', user)]
            if len(pat) > 0:
                base  =  pat[0]
                result11 = math.ceil(base)
                print("ceil number is = " , result11)
            else:
                print("Enter a valid number")
        
        elif "floor" in user:
            pat = [float(num) for num in re.findall(r'\d+\.?\d*', user)]
            if len(pat) > 0:
                base  =  pat[0]
                result12 = math.floor(base)
                print("floor number is = " , result12)
            else:
                print("Enter a valid number")
                
        elif "trunc" in user:
            pat = [float(num) for num in re.findall(r'\d+\.?\d*', user)]
            if len(pat) > 0:
                base  =  pat[0]
                result13 = math.trunc(base)
                print("trunc number is = " , result13)
            else:
                print("Enter a valid number")   
        
        elif "log" in user and not any(z in user for z in ["log base 10", "10 base log", "log base ten", "ten base log","log base 2", "2 base log", "log base two", "two base log","custom base log", "custom log"]):
            pat = [float(num) for num in re.findall(r'\d+\.?\d*', user)]
            if pat:
                base = pat[0]
                result14 = math.log(base)
                print(f"log (natural) of {base} value is = " , result14)
            else:
                print("Enter a valid number")
            
        elif any(z in user for z in ["log base 10", "10 base log", "log base ten", "ten base log"]):
            pat = [float(num) for num in re.findall(r'\d+\.?\d*', user)]
            if pat:
                base = pat[0]
                result15 = math.log10(base)
                print(f"log (base 10) of {base} value is = " , result15)
            else:
                print("Enter a valid number")
        
        elif any(z in user for z in ["log base 2", "2 base log", "log base two", "two base log"]):
            pat = [float(num) for num in re.findall(r'\d+\.?\d*', user)]
            if pat:
                base = pat[0]
                result16 = math.log2(base)
                print(f"log (base 2) of {base} value is = " , result16)
            else:
                print("Enter a valid number")
        
        elif any(z in user for z in ["Custom base log" , "custom log"]):
            pat = [float(num) for num in re.findall(r'\d+\.?\d*', user)]
            if len(pat) >= 2:
                base = pat[0]
                custom_base = pat[1]
                result17 = math.log(base, custom_base)
                print(f"custom log of {base} with base {custom_base} is = " , result17)
            else:
                print("Enter valid numbers for the value and custom base.") 
        
        elif "hypot" in user:
            pat = [float(num) for num in re.findall(r'\d+\.?\d*', user)]
            if len(pat) >= 2:
                side1 = pat[0]
                side2 = pat[1]
                result18 = math.hypot(side1 , side2)
                print(" Hypot of this value is= "  , result18)
            else:
                print("Enter two valid numbers for hypotenuse calculation.")

    elif "search" not in user and any (re.search(r'\b' + se+ r'\b', user) for se in[ "open google", "google" ,"google open","open youtube","youtube","youtube open","chatgpt","open chatgpt","chatgpt open","pinterest","open pinterest","pinterest open" , "removebg","open removebg","removebg open","aiub portal","open aiub portal","aiub portal open","whatsapp","open whatsapp","whatsapp open"]): 
                
        if re.search(r'\byoutube\b|\bopen youtube\b|\byoutube open\b', user):
            time.sleep(2)
            print("Opening youtube....")
            time.sleep(2)
            url = "https://www.youtube.com" 
            webbrowser.open(url)
        
        elif re.search(r'\bgoogle\b|\bopen google\b|\bgoogle open\b', user):
            time.sleep(2)
            print("opening google.....")
            time.sleep(2)
            url2="https://www.google.com"
            webbrowser.open(url2)
        
        elif re.search(r'\bchatgpt\b|\bopen chatgpt\b|\bchatgpt open\b', user):
            time.sleep(2)
            print("opening chatgpt.....")
            time.sleep(2)
            url3="https://chatgpt.com/"
            webbrowser.open(url3)
        
        elif re.search(r'\bpinterest\b|\bopen pinterest\b|\bpinterest open\b', user):
            time.sleep(2)
            print("opening pinterest.....")
            time.sleep(2)
            url4="https://www.pinterest.com/"
            webbrowser.open(url4)

        elif re.search(r'\bremovebg\b|\bopen removebg\b|\bremovebg open\b', user):
            time.sleep(2)
            print("opening removebg.....")
            time.sleep(2)
            url4="https://www.remove.bg/"
            webbrowser.open(url4)
        
        elif re.search(r'\baiub portal\b|\bopen aiub portal\b|\baiub portal open\b', user):
            time.sleep(2)
            print("opening aiub portal.....")
            time.sleep(2)
            url5="https://portal.aiub.edu/"
            webbrowser.open(url5)
        
        elif re.search(r'\bwhatsapp\b|\bopen whatsapp\b|\bwhatsapp open\b', user):
            time.sleep(2)
            print("opening whatsapp.....")
            time.sleep(2)
            url6="https://www.whatsapp.com/"
            webbrowser.open(url6)     
            
    elif any(re.search(r'\b' + si + r'\b', user) for si in ["search youtube","Youtube","search in youtube","search again in youtube"]):
        search = input("What do you want to search on YouTube?:- ")
        formatted = search.replace(' ', '+')
        youtube_url = f"https://www.youtube.com/results?search_query={formatted}" 
        time.sleep(2)
        print("Opening Youtube....")
        time.sleep(2)
        webbrowser.open(youtube_url)
        print(f"🔍 Searching on YouTube: {search}")
                
    elif any(re.search(r'\b' + sp + r'\b', user) for sp in ["country", "countries","capital","language","border","currencies","timezone"]):
        
        capital_match = re.search(r'capital of ([a-zA-Z\s]+)', user)
        language_match = re.search(r'language of ([a-zA-Z\s]+)', user)
        borders_match = re.search(r'borders of ([a-zA-Z\s]+)', user)
        currencies_match = re.search(r'currencies of ([a-zA-Z\s]+)', user)
        timezone_match = re.search(r'timezone of ([a-zA-Z\s]+)', user)
        if capital_match:
            country_name = capital_match.group(1).strip()
        elif language_match:
            country_name = language_match.group(1).strip()
        elif borders_match:
            country_name = borders_match.group(1).strip()
        elif currencies_match:
            country_name = currencies_match.group(1).strip()
        elif timezone_match:
            country_name = timezone_match.group(1).strip()
        else:
            country_name = input("Enter the country name: ")
        try:
            country = CountryInfo(country_name)
            time.sleep(5)
            if "capital" in user or f"what is the capital of {country_name}" in user:
                print(f"The Capital of {country_name} is: {country.capital()}")
            elif "languages" in user or "language" in user or f"what is the language {country_name}" in user:
                print(f"The Languages of {country_name} are: {country.languages()}")
            elif "borders" in user:
                print(f"The Borders of {country_name} are: {country.borders()}")
            elif "currencies" in user:
                print(f"The Currencies of {country_name} are: {country.currencies()}")
            elif "timezones" in user:
                print(f"The Timezone of {country_name} is: {country.timezones()}")
            else: 
                time.sleep (5)
                capital = country.capital()
                languages = country.languages()
                borders = country.borders()
                currencies = country.currencies()
                timezones = country.timezones()
                print(f"The Capital of {country_name} is: {capital}")
                print(f"The Languages of {country_name} are: {languages}")
                print(f"The Borders of {country_name} are: {borders}")
                print(f"The Currencies of {country_name} are: {currencies}")
                print(f"The Timezone of {country_name} is: {timezones}")
        except KeyError:
            print(f"Could not find information for '{country_name}'. Please check the spelling.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    elif any(re.search(r'\b' + so + r'\b', user) for so in ["search google","google search","search in google" ,"search again in google"]):
        
        search1 = input("What do you want to search on google?:- ")
        formatted = search1.replace(' ', '+')
        google_url = f"https://www.google.com/search?q={formatted}"
        time.sleep(2)
        print("Opening google......")
        time.sleep(2)
        webbrowser.open(google_url)
        print(f"🔍 Searching on google: {search1}")
    
    else: 
        print("ChatBot:", random.choice(random_responses))