import math
print("What to you want to do....\n"
      "press 1  for Multiplication table\n"
      "press 2 for Area\n"
      "press 3 for get power or value\n"
      "press 4 to get square\n"
      "press 5 to get mod\n"
      "press 6 to get floor division\n"
      "press 7 to get value of py\n"
      "press 8 to quite this program")
while True:
       
      user_input = int(input("Which type  calculation you want? press 1 2 or 3 ...."))
      if user_input == 1:
             number = int(input("Enter the value for multiplication:-"))
             for i in range (1,11):
              print(f"{number} * {i} = {number * i }")
      elif user_input == 2:
            pie = 3.1416 
            r = int(input("Enter a value to find area:-"))
            print(f" Area is = {pie * r * r}")    
      elif user_input == 3:
            value = int(input("Enter a value to find power:-"))
            print(f"The result is = {value * value * value}")
            
      elif user_input == 4:
            sq =int(input("Enter the value for square :-"))
            print(f"Square is {sq * sq}")
     
      elif user_input == 5:
            md = int(input("Enter value for mod:-"))
            md2 = int(input("Enter another value for mod:-"))
            print(f"The mod is {md % md2}")
      elif user_input == 6:
            fl = int(input("Enter first value :-"))
            fl2 = int(input("Enter second value:-"))
            print(f"Floor division is  = {fl // fl2}")
      elif user_input == 7:
       print(math.pi)
      else:
            break