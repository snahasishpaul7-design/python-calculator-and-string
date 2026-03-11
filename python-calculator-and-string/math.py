import math
print("Using math library......")
print("1.To get ceil value type ceil...... or 1 \n"
      "2.To get floor value type floor or 2\n"
      "3.To get trunc value type trunc or 3n"
      "4.To get Absolute value type abs or 4\n"
      "5.To get power value type power or 5\n"
      "6.TO get square_root type root or 6\n"
      "7.To get factorial type factorial or 7\n"
      "8.TO get  the value of pie type pie or 8\n"
      "9.To get sin value type sin or 9\n"
      "10.To get cos value type cos or 10\n"
      "11.To get tan value type tan or 11\n"
      "12.To get radian  type rad or 11")
while True:
    
    user_input = input("Enter which one you want to do:-")
    if user_input == "ceil" or user_input == "1":
        value1 = float(input("Enter the value:-"))
        print(f"The ceil value is == {math.ceil(value1)}")

    elif user_input == "floor" or user_input == "2":
        value2 = float(input("Enter the value:-"))
        print(f"The floor value is == {math.floor(value2)}")

    elif user_input == "trunc" or user_input == "3":
        value3 = float(input("Enter the value:-"))
        print(f"The trunc value is == {math.trunc(value3)}")

    elif user_input == "abs" or user_input == "4":
        value4 = float(input("Enter the value:-"))
        print(f"The trunc value is == {math.fabs(value4)}") #fabs

    elif user_input == "power" or user_input == "5":
        value5 = float(input("Enter the base value:-"))
        value6 = float(input("Enter the exponent value:-"))
        print(f"The power is == {math.pow(value5,value6)}")
    
    elif user_input == "root" or user_input == "6":
        value7 = float(input("Enter the value:-"))
        print(f"The square_root value is == {math.sqrt(round(value7))}")
    
    elif user_input == "factorial" or user_input == "7":
        value8 =  float(input("Enter the value:-"))
        print(f"The square_root value is == {math.factorial(round(value8))}")

    elif user_input == "pie" or user_input == "8":
        print(f"The value of pie is",math.pi)
    
    elif user_input == "sin" or user_input == "9":
        value9 = float(input("Enter the value:-"))
        print(f"The value of sin  is == {math.sin(value9)}")

    elif user_input == "cos" or user_input == "10":
        value10 = float(input("Enter the value:-"))
        print(f"The value of cos is == {math.cos(value10)}")

    elif user_input == "tan" or user_input == "11":
        value11 = float(input("Enter the value:-"))
        print(f"The  value of tan is == {math.tan(value11)}")

    elif user_input == "rad" or user_input == "12":
        value12 = float(input("Enter the value:-"))
        print(f"The  value of radian is == {math.radians(value12)}")

    elif user_input == "stop" or user_input == "quit" or user_input == "13":
        break

    else:
      print("Enter a valid string or number.......")

print("Thank you.....") 

