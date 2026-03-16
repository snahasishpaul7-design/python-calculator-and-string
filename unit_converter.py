import time

print("Unit converter....")

while True:
    
    user_input = input("Do you need any conversion:-").lower()
    
    if user_input in ["yes" , "yeap" , "yea"]:
        
        time.sleep(2)
        
        print("Which conversion you need....\n"
              "1.meter to kilometer,press 1 or type km\n"
              "2.kilometer to meter ,press 2 or type m\n"
              "3.centimeter to meter , press 3 or type cm\n"
              "4.meter to centimeter ,press 4 or type cmm \n"
              "5.meter to inch ,press 5 or type inch\n"
              "6.inch to meter, press 6 or type imch\n"
              "7.meter to foot , press 7 or type foot\n"
              "8.foot to meter ,type 8 or fm\n"
              "9.meter to mile , type 9 or mile\n"
              "10.mile to meter ,type 10 or mmi\n"
              "11.meter to millimeter , type 11 or mili\n"
              "12.millimeter to meter , type 12 or militer\n"
              "13.if you need every unit conversion the code provide type (full)")
        
        user_input2 = input("Which type of conversion you want:-").lower()
        if user_input2 == "1"  or user_input2 == "km":
            meter = int(input("Enter the value of kilometer:-"))
            km = meter / 1000
            print(f"kilometer is = {km}")
            
        elif user_input2 == "2" or user_input2 == "m":
            time.sleep(0.5)
            kilometer = int(input("Enter the value of meter:-"))
            time.sleep(0.5)
            me = kilometer * 1000
            time.sleep(0.5)
            print(f"Meter is =  {me}")
        
        elif user_input2 == "3" or user_input2 == "cm":
            time.sleep(0.5)
            centimeter = int(input("Enter the value of centimeter:-"))
            time.sleep(0.5)
            cmm1 = centimeter / 100
            time.sleep(0.5)
            print(f"Meter is =  {cmm1}")
        
        elif user_input2 == "4" or user_input2 == "cmm":
            time.sleep(0.5)
            me = int(input("Enter the value of meter:-"))
            time.sleep(0.5)
            cmm2 = centimeter * 100
            time.sleep(0.5)
            print(f"Centimeter is =  {cmm2}")
        
        elif user_input2 == "5" or user_input2 == "inch":
            time.sleep(0.5)
            inch1 = int(input("Enter the value of meter:-"))
            time.sleep(0.5)
            m1 = inch1 * 39.3701
            time.sleep(0.5)
            print(f"Inch is =  {m1}")
        
        elif user_input2 == "6" or user_input2 == "imch":
            time.sleep(0.5)
            inch1 = float(input("Enter the value of inch:-"))
            time.sleep(0.5)
            m2 = inch1 * 0.0254
            time.sleep(0.5)
            print(f"Meter is {m2}")
        
        elif user_input2 == "7" or user_input2 == "foot":
            time.sleep(0.5)
            n1 = float(input("Enter the value of meter:-"))
            time.sleep(0.5)
            m3 =  n1 * 3.28084
            time.sleep(0.5)
            print(f"Foot is {m3}")
        
        elif user_input2 == "8" or user_input2 == "fm":
            time.sleep(0.5)
            n2 = float(input("Enter the value of foot:-"))
            time.sleep(0.5)
            m4 =  n2 / 0.3048
            time.sleep(0.5)
            print(f"Meter  is {m4}")
        
        elif user_input2 == "9" or user_input2 == "mile":
            time.sleep(0.5)
            n3 = int(input("Enter the value of meter:-"))
            time.sleep(0.5)
            m5 =  n3 * 0.000621371
            time.sleep(0.5)
            print(f"Mile  is {m5}")
        
        elif user_input2 == "10" or user_input2 == "mmi":
            time.sleep(0.5)
            n4 = int(input("Enter the value of mile:-"))
            time.sleep(0.5)
            m6 =  n4 * 1609.34
            time.sleep(0.5)
            print(f"Meter  is {m6}")
        
        elif user_input2 == "11" or user_input2 == "mili":
            time.sleep(0.5)
            n5 = int(input("Enter the value of meter:-"))
            time.sleep(0.5)
            m7 =  n5 * 1000
            time.sleep(0.5)
            print(f"Millimeter  is {m6}")
        
        elif user_input2 == "12" or user_input2 == "militer":
            time.sleep(0.5)
            n6 = int(input("Enter the value of millimeter:-"))
            time.sleep(0.5)
            m8 =  n6 / 1000
            time.sleep(0.5)
            print(f"Meter  is {m6}")
        
        elif user_input2 == "full":
            time.sleep(0.5)
            n7 = float(input("Enter the value:-"))
            time.sleep(0.5)
            km = n7 / 1000
            time.sleep(0.5)
            print(f"kilometer is = {km}")
            time.sleep(0.5)
            me = n7 * 1000
            time.sleep(0.5)
            print(f"kilometer to Meter is =  {me}")
            time.sleep(0.5)
            cmm1 = n7 / 100
            time.sleep(0.5)
            print(f"Centimeter to Meter is =  {cmm1}")
            time.sleep(0.5)
            cmm2 = n7 * 100
            time.sleep(0.5)
            print(f"Centimeter is =  {cmm2}")
            time.sleep(0.5)
            m1 = n7 * 39.3701
            time.sleep(0.5)
            print(f"Inch is =  {m1}")
            time.sleep(0.5)
            m2 = n7 * 0.0254
            time.sleep(0.5)
            print(f"Inch to Meter is {m2}")
            time.sleep(0.5)
            m3 =  n7 * 3.28084
            time.sleep(0.5)
            print(f"Foot is {m3}")
            time.sleep(0.5)
            m4 =  n7 / 0.3048
            time.sleep(0.5)
            print(f"Foot to Meter  is {m4}")
            time.sleep(0.5)
            m5 =  n7 * 0.000621371
            time.sleep(0.5)
            print(f"Mile  is {m5}")
            time.sleep(0.5)
            m6 =  n7 * 1609.34
            time.sleep(0.5)
            print(f"Mile to Meter  is {m6}")
            time.sleep(0.5)
            m7 =  n7 * 1000
            time.sleep(0.5)
            print(f"Millimeter  is {m6}")
            time.sleep(0.5)
            m8 =  n7 / 1000
            time.sleep(0.5)
            print(f"Millimeter to Meter  is {m6}") 
        
        else:
            time.sleep(0.5)
            print("Enter a valid int or float number not string or anything else......")
            
    elif user_input in ["no" , "never" , "nah"]:
        break 
    else:
        print("Bye see you soon")
        break
            
    