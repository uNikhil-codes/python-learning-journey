# # SIMPLE CALCULATOR



# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# operator = input("Enter the operator (+, -, *, /): ")

# if operator == "+":
#     print(num1+num2)

# elif operator == "-":
#     print(num1 - num2

# elif operator == "*":
#     print(f"the answer is : {num1 * num2}")

# elif operator == "/":
#     if num2 == 0:
#         print("Cannot divide by zero")
#     else:
#         print(num1 / num2)

# else:
#     print("Invalid operator")

# -------------------------------------------------------------------------


# # PYTHON WEIGHT CONVERTER (my version)

# weight = float(input("Enter the weight in gram : "))
# conversion = input(f"Select the conversion \n1: {weight}g to KiloGram (KG) \n2: {weight}g to MilliGram (MG) \n3: {weight}g to Ton (T) \n ")

# if conversion == "1":
#     print(f"The {weight}g in KG is : {weight/1000}kg" )
# elif conversion == "2":
#     print(f"The {weight}g in MG is : {weight*1000}mg")
# elif conversion == "3":
#     print(f"The {weight}g in Ton is : {weight/1000000}t ")
# else:
#     print("Conversion Invalid !!")

# -------------------------------------------------------------------

# # PYTHON WEIGHT CONVERTER (bro code version)

# weight = float(input("Enter the weight : "))
# unit = input("Kilogram or Ton ? (kg or t) :  ")

# if unit == "kg":
#     weight = weight/1000
#     unit = "Kgs"
#     print(f"The weight is {weight} {unit}")
# elif unit == "t":
#     weight = weight/1000000
#     unit = "Ton"
#     print(f"The weight is {round(weight , 2)} {unit}")
# else:
#     print(f"{unit} was not valid!")

# -------------------------------------------------------------------


# # temperature converter
# val = input("is the value Celsius degree or Fahrenheit ( C/F ? ) : ")
# temp = float(input("Enter a value of temperature : "))

# if val == "c":
#     temp = round((9*temp)/5+32 , 1)
#     print(f"The temperature converted from {val} to Fahrenheit is : {temp}F")

# elif val == "f":
#     temp = round((temp-32)*5/9, 1)
#     print(f"The temperature converted from {val} to Celsius is : {temp}C")

# else:
#     print(f"{val} is Invalid !!!")

# -------------------------------------------------------------------

# # Wanna go out for playing ??

# out_temp = int(input("Enter the temperature : "))
# is_raining = input("Is it raining (Y/N) ? : ")

# if out_temp >= 35 and is_raining == "Y":
#     print("BROOOOO IN high temp RAIN WON'T COME !!")
# elif out_temp <= 17 and is_raining == "Y":
#     print("BROOOO RAIN WILL Freezeeee in this temperature !!!")
# elif out_temp <= 17 and is_raining == "N":
#     print("you can go , but wear sweater !!!")
# elif out_temp >= 35 and is_raining == "N":
#     print("You cannot go out for playing 😭 !")
# else:
#     print("You can go out")

# -------------------------------------------------------------------

# # SPENT MORE OR NOT (using conditional statements)

# spent = float(input("How much did you spend ?: "))
# print("you spent more !!" if not 500>=spent>=0 else "you spent less")

# # Switch on or off

# status = input ("Is Bulb Glowing ? (Y/N) : ")
# print("Please off the switch" if not status=="N" else " switch is off !")
