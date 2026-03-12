
import random

import string 

import time

print("WELCOME TO OUR PLATFORM, CURRENTLY UNDER DEVELOPMENT, DESIGNED TO CHALLENGE AND ENHANCE YOUR INTELLIGENCE. ENTER THE PASSWORD, GUESS THE NUMBER, AND PARTICIPATE IN THE QUIZ TO TEST YOUR BRAINPOWER!")

time.sleep(2) 
while True:
    d= input("DO YOU WANT TO PARTICIPATE IN THIS GAME? :-")

    if d.lower() in  ["yes","yeap","of course","ofcourse"]:

        time.sleep (1)

        print("ENTER THE QUIZ WORLD...")

        time.sleep (2)

    else:
        ("COME AGAIN NEXT TIME :(")
        quit
        break
        

print("PASSWORD GENERATING PLEASE BE PATIENT...")

time.sleep(5)

e =random.randint(1, 8)

length = 8
c = string.ascii_uppercase + string.digits + '#@'

password = ''.join(random.choice(c))
for i in range(length):
    password = password + random.choice(c)

print ("GENARATED PASSWORD IS:-" + " " + password)

time.sleep(1)

dinput = input("ENTER THE PASSWORD :- ")

if dinput.upper() == password:

    print("GENARATING A RANDOME NUMBER FOR PLAYER :)")

    time.sleep(5)

else:
    print("ENTER THE VALID PASSWORD!")

    quit()

print("PLEASE WAIT WHILE WE ASSIGN YOU A RANDOM PLAYER NUMBER :)")

time.sleep(5)

random4 = random.randint(1,20000)

print("PLAYER NUMBER IS ", random4)

time.sleep(2)

print("WELCOME PLAYER NUMBER", random4)
 
time.sleep(2)

o = input("DO YOU WANT TO PLAY A GUESSING GAME? :-")

time.sleep(2)

if o.upper() == "YES":

    print("OK LETS PLAY THIS GAME :) PLAYER NUMBER", random4)

elif o.upper()=="YEAP":

    print("OK LETS PLAY THIS GAME :) PLAYER NUMBER", random4)

elif o.upper() =="OFCOURSE":

    print("OK LETS PLAY THIS GAME :) PLAYER NUMBER", random4)

elif o.upper()=="OF COURSE":

    print("OK LETS PLAY THIS GAME :) PLAYER NUMBER", random4)
    
elif o.upper()=="YEP":

    print("OK LETS PLAY THIS GAME :) PLAYER NUMBER", random4)

elif o.upper()=="YEA":

    print("OK LETS PLAY THIS GAME :) PLAYER NUMBER", random4)

    time.sleep(3)

else:

    print("COME AGAIN LATER :( PLAYER  NUMBER", random4)

    quit()



upper_value = int(input("INPUT UPPER VALUE PLAYER :-"))

time.sleep(3)

lower_value = int(input("INPUT LOWER VALUE PLAYER :-"))

random_number = random.randint(lower_value , upper_value)

time.sleep(2)

while True:
    range1 = int(input("GUESS THE NUMBER PLAYER :-"))

    if range1 != random_number:
        print("GUESS THE CORRECT NUMBER")
        time.sleep(1)
    else:
        print("YOU ARE CORRECT!")
        break

time.sleep(2)

print("The number is:", random_number)

if range1 == random_number:

    print("PLAYER NUMBER", random4, "HAS BEEN ASSIGNED. THE PROGRAM WILL NOW BEGIN THE QUIZ GAME FOR YOU.")

    time.sleep(2)

else:
    print("TRY AGAIN LATER ,GIVE YOUR BEST SHOT ")

s =(input("DO YOU WANT TO PLAY QUIZ GAME ? :-"))

if s.upper() == "YEAP":

    time.sleep(4)

    print ("BEST OF LUCK :)")

elif s.upper() == "YES":

    time.sleep(4)

    print ("BEST OF LUCK :)")

elif s.upper() == "OF COURSE":

    time.sleep(4)

    print ("BEST OF LUCK :)")

elif s.upper() == "OFCOURSE":   

    time.sleep(4)

    print ("BEST OF LUCK :)")

    time.sleep(4)

else:
    print("TRY AGAIN,FAIL AGAIN, FAIL BETTER :) ")

    quit()

score=0

time.sleep (2)

print("WHAT IS THE CAPITAL OF FRANCE ?")

print("A = ROME")

print("B = PARIS")

answer = input("WRITE YOUR ANSWER :-")

if answer.upper() == "PARIS":

    print("CORRECT")

    score+=1

else:

    print("INCORRECT")

b = print("Which planet is known as the Red Planet? ")
print("A = VENUS")
print("B = MARS")
Answer_1 =input("WRITE YOUR ANSWER:-")

if Answer_1.upper()== "MARS":
    print("CORRECT,YOU GET TWO STAR. GREAT!")
    score+=1 #increment of score
else:
    print("Incorrect")

print("Who invented the light bulb?")
print("A = EDISON")
print("B = NEWTON")
Answer_4 = input("WRITE YOUR ANSWER:- ")
if Answer_4.upper() == "EDISON":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which is the longest river?")
print("A = AMAZON")
print("B = NILE")
Answer_5 = input("WRITE YOUR ANSWER:- ")
if Answer_5.upper() == "AMAZON":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which animal is known as King of Jungle?")
print("A = TIGER")
print("B = LION")
Answer_6 = input("WRITE YOUR ANSWER:- ")
if Answer_6.upper() == "LION":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the freezing point of water?")
print("A = 0")
print("B = 100")
Answer_7 = input("WRITE YOUR ANSWER:- ")
if Answer_7 == "0":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which gas do plants use for photosynthesis?")
print("A = CO2")
print("B = OXYGEN")
Answer_8 = input("WRITE YOUR ANSWER:- ")
if Answer_8.upper() == "CO2":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which planet is closest to the sun?")
print("A = MERCURY")
print("B = VENUS")
Answer_9 = input("WRITE YOUR ANSWER:- ")
if Answer_9.upper() == "MERCURY":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the chemical symbol for water?")
print("A = H2O")
print("B = CO2")
Answer_10 = input("WRITE YOUR ANSWER:- ")
if Answer_10.upper() == "H2O":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which country has the most population?")
print("A = INDIA")
print("B = CHINA")
Answer_11 = input("WRITE YOUR ANSWER:- ")
if Answer_11.upper() == "INDIA":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which color is a mix of red and blue?")
print("A = PURPLE")
print("B = ORANGE")
Answer_12 = input("WRITE YOUR ANSWER:- ")
if Answer_12.upper() == "PURPLE":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")


print("Which continent is Egypt in?")
print("A = AFRICA")
print("B = ASIA")
Answer_13 = (input("WRITE YOUR ANSWER:-"))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
if Answer_13.upper() == "AFRICA":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which is the largest desert?")
print("A = SAHARA")
print("B = ARABIAN")
Answer_14 = input("WRITE YOUR ANSWER:- ")
if Answer_14.upper() == "SAHARA":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which fruit has seeds on its outside?")
print("A = STRAWBERRY")
print("B = BANANA")
Answer_15 = input("WRITE YOUR ANSWER:- ")
if Answer_15.upper() == "STRAWBERRY":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Who discovered gravity?")
print("A = NEWTON")
print("B = GALILEO")
Answer_16 = input("WRITE YOUR ANSWER:- ")
if Answer_16.upper() == "NEWTON":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the capital of Japan?")
print("A = TOKYO")
print("B = BEIJING")
Answer_17 = input("WRITE YOUR ANSWER:- ")
if Answer_17.upper() == "TOKYO":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What do bees produce?")
print("A = HONEY")
print("B = MILK")
Answer_18 = input("WRITE YOUR ANSWER:- ")
if Answer_18.upper() == "HONEY":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which is the tallest mountain?")
print("A = K2")
print("B = EVEREST")
Answer_19 = input("WRITE YOUR ANSWER:- ")
if Answer_19.upper() == "EVEREST":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which planet is famous for rings?")
print("A = JUPITER")
print("B = SATURN")
Answer_20 = input("WRITE YOUR ANSWER:- ")
if Answer_20.upper() == "SATURN":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")


print("Which is the fastest land animal?")
print("A = CHEETAH")
print("B = LION")
Answer_21 = input("WRITE YOUR ANSWER:- ")
if Answer_21.upper() == "CHEETAH":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which part of the plant makes food?")
print("A = ROOT")
print("B = LEAF")
Answer_22 = input("WRITE YOUR ANSWER:- ")
if Answer_22.upper() == "LEAF":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which instrument is used to see small things?")
print("A = MICROSCOPE")
print("B = TELESCOPE")
Answer_23 = input("WRITE YOUR ANSWER:- ")
if Answer_23.upper() == "MICROSCOPE":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("How many continents are there?")
print("A = 7")
print("B = 5")
Answer_24 = input("WRITE YOUR ANSWER:- ")
if Answer_24 == "7":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which metal is liquid at room temperature?")
print("A = MERCURY")
print("B = IRON")
Answer_25 = input("WRITE YOUR ANSWER:- ")
if Answer_25.upper() == "MERCURY":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which organ pumps blood?")
print("A = LUNGS")
print("B = HEART")
Answer_26 = input("WRITE YOUR ANSWER:- ")
if Answer_26.upper() == "HEART":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("How many bones in the human body?")
print("A = 206")
print("B = 210")
Answer_27 = input("WRITE YOUR ANSWER:- ")
if Answer_27 == "206":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which animal has a trunk?")
print("A = ELEPHANT")
print("B = GIRAFFE")
Answer_28 = input("WRITE YOUR ANSWER:- ")
if Answer_28.upper() == "ELEPHANT":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the main gas we breathe?")
print("A = OXYGEN")
print("B = NITROGEN")
Answer_29 = input("WRITE YOUR ANSWER:- ")
if Answer_29.upper() == "OXYGEN":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which day comes after Friday?")
print("A = SUNDAY")
print("B = SATURDAY")
Answer_30 = input("WRITE YOUR ANSWER:- ")
if Answer_30.upper() == "SATURDAY":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which shape has three sides?")
print("A = TRIANGLE")
print("B = RECTANGLE")
Answer_31 = input("WRITE YOUR ANSWER:- ")
if Answer_31.upper() == "TRIANGLE":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the capital of Bangladesh?")
print("A = DHAKA")
print("B = CHITTAGONG")
Answer_32 = input("WRITE YOUR ANSWER:- ")
if Answer_32.upper() == "DHAKA":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which is the smallest planet?")
print("A = MARS")
print("B = MERCURY")
Answer_33 = input("WRITE YOUR ANSWER:- ")
if Answer_33.upper() == "MERCURY":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What does H2O stand for?")
print("A = WATER")
print("B = SALT")
Answer_34 = input("WRITE YOUR ANSWER:- ")
if Answer_34.upper() == "WATER":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which bird cannot fly?")
print("A = PENGUIN")
print("B = CROW")
Answer_35 = input("WRITE YOUR ANSWER:- ")
if Answer_35.upper() == "PENGUIN":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is used to write on blackboards?")
print("A = CHALK")
print("B = PEN")
Answer_36 = input("WRITE YOUR ANSWER:- ")
if Answer_36.upper() == "CHALK":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which food is made from milk?")
print("A = CHEESE")
print("B = BREAD")
Answer_37 = input("WRITE YOUR ANSWER:- ")
if Answer_37.upper() == "CHEESE":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which planet has a big storm called the Great Red Spot?")
print("A = JUPITER")
print("B = MARS")
Answer_38 = input("WRITE YOUR ANSWER:- ")
if Answer_38.upper() == "JUPITER":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")


print("How many legs does a spider have?")
print("A = 6")
print("B = 8")
Answer_39 = input("WRITE YOUR ANSWER:- ")
if Answer_39 == "8":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What color is the sky?")
print("A = BLUE")
print("B = GREEN")
Answer_40 = input("WRITE YOUR ANSWER:- ")
if Answer_40.upper() == "BLUE":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("How many hours are in a day?")
print("A = 24")
print("B = 12")
Answer_41 = input("WRITE YOUR ANSWER:- ")
if Answer_41 == "24":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which gas is used in balloons?")
print("A = HELIUM")
print("B = HYDROGEN")
Answer_42 = input("WRITE YOUR ANSWER:- ")
if Answer_42.upper() == "HELIUM":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which part of the body helps you to see?")
print("A = EYES")
print("B = EARS")
Answer_43 = input("WRITE YOUR ANSWER:- ")
if Answer_43.upper() == "EYES":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which shape has four equal sides?")
print("A = SQUARE")
print("B = TRIANGLE")
Answer_44 = input("WRITE YOUR ANSWER:- ")
if Answer_44.upper() == "SQUARE":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What do you use to hear music?")
print("A = EARS")
print("B = EYES")
Answer_45 = input("WRITE YOUR ANSWER:- ")
if Answer_45.upper() == "EARS":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which animal gives us wool?")
print("A = SHEEP")
print("B = COW")
Answer_46 = input("WRITE YOUR ANSWER:- ")
if Answer_46.upper() == "SHEEP":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which planet is known for having life?")
print("A = EARTH")
print("B = VENUS")
Answer_47 = input("WRITE YOUR ANSWER:- ")
if Answer_47.upper() == "EARTH":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which season is the coldest?")
print("A = WINTER")
print("B = SUMMER")
Answer_48 = input("WRITE YOUR ANSWER:- ")
if Answer_48.upper() == "WINTER":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which month has 28 or 29 days?")
print("A = FEBRUARY")
print("B = MARCH")
Answer_49 = input("WRITE YOUR ANSWER:- ")
if Answer_49.upper() == "FEBRUARY":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the opposite of 'cold'?")
print("A = HOT")
print("B = COOL")
Answer_50 = input("WRITE YOUR ANSWER:- ")
if Answer_50.upper() == "HOT":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the national flower of Bangladesh?")
print("A = Water Lily")
print("B = Rose")
Answer_51 = input("WRITE YOUR ANSWER:- ")
if Answer_51.upper() == "WATER LILY":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the capital city of Bangladesh?")
print("A = Dhaka")
print("B = Chittagong")
Answer_52 = input("WRITE YOUR ANSWER:- ")
if Answer_52.upper() == "DHAKA":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which river is known as the 'Old Ganges' in Bangladesh?")
print("A = Padma")
print("B = Jamuna")
Answer_53 = input("WRITE YOUR ANSWER:- ")
if Answer_53.upper() == "PADMA":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Who is known as the 'Father of the Nation' in Bangladesh?")
print("A = Sheikh Mujibur Rahman")
print("B = Ziaur Rahman")
Answer_54 = input("WRITE YOUR ANSWER:- ")
if Answer_54.upper() == "SHEIKH MUJIBUR RAHMAN":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("In which year did Bangladesh gain independence?")
print("A = 1971")
print("B = 1947")
Answer_55 = input("WRITE YOUR ANSWER:- ")
if Answer_55 == "1971":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the currency of Bangladesh?")
print("A = Taka")
print("B = Rupee")
Answer_56 = input("WRITE YOUR ANSWER:- ")
if Answer_56.upper() == "TAKA":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")


print("Which sea borders Bangladesh to the south?")
print("A = Bay of Bengal")
print("B = Arabian Sea")
Answer_57 = input("WRITE YOUR ANSWER:- ")
if Answer_57.upper() == "BAY OF BENGAL":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the national animal of Bangladesh?")
print("A = Royal Bengal Tiger")
print("B = Elephant")
Answer_58 = input("WRITE YOUR ANSWER:- ")
if Answer_58.upper() == "ROYAL BENGAL TIGER":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which language is officially spoken in Bangladesh?")
print("A = Bengali")
print("B = Hindi")
Answer_59 = input("WRITE YOUR ANSWER:- ")
if Answer_59.upper() == "BENGALI":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which is the largest island in Bangladesh?")
print("A = Bhola Island")
print("B = Saint Martin Island")
Answer_60 = input("WRITE YOUR ANSWER:- ")
if Answer_60.upper() == "BHOLA ISLAND":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Who proposed the theory of relativity?")
print("A = EINSTEIN")
print("B = NEWTON")
Answer_61 = input("WRITE YOUR ANSWER:- ")
if Answer_61.upper() == "EINSTEIN":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which element has the atomic number 26?")
print("A = IRON")
print("B = COBALT")
Answer_62 = input("WRITE YOUR ANSWER:- ")
if Answer_62.upper() == "IRON":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the capital of Australia?")
print("A = SYDNEY")
print("B = CANBERRA")
Answer_63 = input("WRITE YOUR ANSWER:- ")
if Answer_63.upper() == "CANBERRA":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which gas is most abundant in Earth's atmosphere?")
print("A = OXYGEN")
print("B = NITROGEN")
Answer_64 = input("WRITE YOUR ANSWER:- ")
if Answer_64.upper() == "NITROGEN":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the square root of 256?")
print("A = 14")
print("B = 16")
Answer_65 = input("WRITE YOUR ANSWER:- ")
if Answer_65.upper() == "16":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which planet has the most moons?")
print("A = SATURN")
print("B = JUPITER")
Answer_66 = input("WRITE YOUR ANSWER:- ")
if Answer_66.upper() == "SATURN":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Who wrote 'The Origin of Species'?")
print("A = DARWIN")
print("B = MENDEL")
Answer_67 = input("WRITE YOUR ANSWER:- ")
if Answer_67.upper() == "DARWIN":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the smallest prime number?")
print("A = 1")
print("B = 2")
Answer_68 = input("WRITE YOUR ANSWER:- ")
if Answer_68.upper() == "2":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which part of the brain controls balance?")
print("A = CEREBELLUM")
print("B = MEDULLA")
Answer_69 = input("WRITE YOUR ANSWER:- ")
if Answer_69.upper() == "CEREBELLUM":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the chemical formula for table salt?")
print("A = NaCl")
print("B = KCl")
Answer_70 = input("WRITE YOUR ANSWER:- ")
if Answer_70.upper() == "NACL":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which year did World War II end?")
print("A = 1945")
print("B = 1946")
Answer_71 = input("WRITE YOUR ANSWER:- ")
if Answer_71.upper() == "1945":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the next number in the Fibonacci sequence: 21, 34, ?")
print("A = 55")
print("B = 53")
Answer_72 = input("WRITE YOUR ANSWER:- ")
if Answer_72.upper() == "55":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which country has the largest population?")
print("A = INDIA")
print("B = CHINA")
Answer_73 = input("WRITE YOUR ANSWER:- ")
if Answer_73.upper() == "INDIA":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is H2SO4 commonly known as?")
print("A = SULFURIC ACID")
print("B = NITRIC ACID")
Answer_74 = input("WRITE YOUR ANSWER:- ")
if Answer_74.upper() == "SULFURIC ACID":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which organ filters blood in the human body?")
print("A = LIVER")
print("B = KIDNEY")
Answer_75 = input("WRITE YOUR ANSWER:- ")
if Answer_75.upper() == "KIDNEY":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the value of π (pi) to 2 decimal places?")
print("A = 3.14")
print("B = 3.15")
Answer_76 = input("WRITE YOUR ANSWER:- ")
if Answer_76.upper() == "3.14":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which country hosted the 2020 Summer Olympics?")
print("A = JAPAN")
print("B = CHINA")
Answer_77 = input("WRITE YOUR ANSWER:- ")
if Answer_77.upper() == "JAPAN":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Who painted the Mona Lisa?")
print("A = LEONARDO DA VINCI")
print("B = PICASSO")
Answer_78 = input("WRITE YOUR ANSWER:- ")
if Answer_78.upper() == "LEONARDO DA VINCI":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the hardest natural substance?")
print("A = DIAMOND")
print("B = QUARTZ")
Answer_79 = input("WRITE YOUR ANSWER:- ")
if Answer_79.upper() == "DIAMOND":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which language has the most native speakers?")
print("A = ENGLISH")
print("B = MANDARIN")
Answer_80 = input("WRITE YOUR ANSWER:- ")
if Answer_80.upper() == "MANDARIN":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which vitamin is produced when a person is exposed to sunlight?")
print("A = VITAMIN D")
print("B = VITAMIN C")
Answer_81 = input("WRITE YOUR ANSWER:- ")
if Answer_81.upper() == "VITAMIN D":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the largest internal organ in the human body?")
print("A = LIVER")
print("B = LUNGS")
Answer_82 = input("WRITE YOUR ANSWER:- ")
if Answer_82.upper() == "LIVER":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which scientist is known for the uncertainty principle?")
print("A = HEISENBERG")
print("B = BOHR")
Answer_83 = input("WRITE YOUR ANSWER:- ")
if Answer_83.upper() == "HEISENBERG":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which is the smallest bone in the human body?")
print("A = STAPES")
print("B = ULNA")
Answer_84 = input("WRITE YOUR ANSWER:- ")
if Answer_84.upper() == "STAPES":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which country invented paper?")
print("A = EGYPT")
print("B = CHINA")
Answer_85 = input("WRITE YOUR ANSWER:- ")
if Answer_85.upper() == "CHINA":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which is the longest river in the world?")
print("A = NILE")
print("B = AMAZON")
Answer_86 = input("WRITE YOUR ANSWER:- ")
if Answer_86.upper() == "NILE":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the unit of electric current?")
print("A = AMPERE")
print("B = VOLT")
Answer_87 = input("WRITE YOUR ANSWER:- ")
if Answer_87.upper() == "AMPERE":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("What is the currency of Japan?")
print("A = YUAN")
print("B = YEN")
Answer_88 = input("WRITE YOUR ANSWER:- ")
if Answer_88.upper() == "YEN":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Who invented the telephone?")
print("A = GRAHAM BELL")
print("B = EDISON")
Answer_89 = input("WRITE YOUR ANSWER:- ")
if Answer_89.upper() == "GRAHAM BELL":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")

print("Which gas is used in balloons to make them float?")
print("A = HELIUM")
print("B = HYDROGEN")
Answer_90 = input("WRITE YOUR ANSWER:- ")
if Answer_90.upper() == "HELIUM":
    print("CORRECT!")
    score += 1
else:
    print("Incorrect")


print ("YOUR SCORE IS"" " +     str(score)   +  " " "OUT OF 58")

print("YOU GOT" " "  +  str((score/88)*100) + "%")

print("YOUR SCORE IS" + " " + str(score))