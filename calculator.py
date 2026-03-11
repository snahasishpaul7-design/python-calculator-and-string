print("Today we learn how to use if else and can't divide by 0..")
print("Welcome......")
val1 = int(input("Enter the first number:-"))
val2 = int(input("Enter the second number:-"))
add = val1 +  val2
print("The addition is:-" , add)
minus = val1 - val2
print("The subtraction is:-" , minus)
mult = val1 * val2
print("The multiplication is:-" , mult)
if val2 == 0:
    print("Can't divide by 0")
else:
    div = val1 / val2
    print("THe division is", div)
print("Thank you for using my calculator........")