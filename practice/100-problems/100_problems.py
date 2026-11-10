# Level 1 — Variables & Type Casting
# PROBLEM 1
# Data Type Identification
# Create variables for:
# your name
# your age
# your height in cm
# whether you are currently studying
# Print each value and its data type.
# Goal: Understand what Python actually stores.
"""
# [PRIVACY: original personal name 'nikhil' replaced with fake placeholder 'student1']
name = 'student1'
age = 19
height = 179.0
is_student = True

print(f"value : {name} , dtype : " ,type(name))
print(f"value : {age} , dtype : " ,type(age))
print(f"value : {height} , dtype : " ,type(height))
print(f"value : {is_student} , dtype : " ,type(is_student)) """

#------------------------------------------------------------------------------

# Unit Conversion
# A system receives a distance:
# distance_km = 7.35
# Convert it to:
# meters
# centimeters
# Print all three.
# Constraint: Don't modify distance_km .

"""distance_km = 7.35

conversion1 = distance_km * 1000
conversion2 = distance_km * 1000000

print(f"The distance in km : {distance_km}km \nThe distance in meters : {conversion1}\nThe distance in cm : {conversion2}")"""

#------------------------------------------------------------------------------------
# PROBLEM 3
# Time Conversion
# A video is:
# total_seconds = 7385
# Calculate:
# total minutes
# remaining seconds
# Then calculate:
# total hours
# remaining minutes
# remaining seconds
# Example format:
# 2 hours 3 minutes 5 seconds
# Think carefully about integer division and remainder.

'''total_seconds = int(input("Enter seconds : "))
ttl_seconds = total_seconds % 60
ttl_minutes = (total_seconds / 60)
ttl_hrs = (total_seconds / 360)

while ttl_minutes >= 60:
    ttl_minutes1 = ttl_minutes/60
    ttl_hrs += 1
    ttl_minutes=ttl_minutes1
    if ttl_minutes1 >= 60 :
        ttl_minutes2 = ttl_minutes1/60
        ttl_hrs += 1
    else:
        pass

print(f"Remaining time : {round(ttl_hrs)} hours : {round(ttl_minutes)} minutes : {ttl_seconds} seconds ")

'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM   4 / 100 — Salary Breakdown
#   Level 1 — Variables & Type Casting
#═══════════════════════════════════════════════════════════════════════════════
#

#    An employee has:
#    monthly_salary = 45000
#    Calculate:
#    annual salary
#    monthly salary after ₹5000 fixed expenses
#    annual amount remaining after those expenses
#    Don't manually type the calculated answers.

# monthly_salary = float(input("Enter your monthly salary : "))
# annual_salary = monthly_salary * 12

'''month_sal = float(input("Enter your salary : "))
expenses = float(input("Enter your expenses : "))
annual_sal = month_sal * 12
remained_month_sal = month_sal - expenses
remained_annual_sal = remained_month_sal * 12

print("################################")
print(f"Your monthly salary : {month_sal}rs\nYour annual salary : {annual_sal}rs\nYour expenses : {expenses}")
print("################################")
print(f"Your monthly salary after subtracting expenses : {remained_month_sal }rs\nYour annual salary after subtracting expenses: {remained_annual_sal}rs")
'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM   5 / 100 — Swap Without Guessing
#   Level 1 — Variables & Type Casting
#═══════════════════════════════════════════════════════════════════════════════
#

#    Given:
#    a = 27
#    b = 91
#    Swap them. Then print:
#    Before:
#    a = 27
#    b = 91
#    After:
#    a = 91
#    b = 27
#    Interview question: try solving it without simply retyping the values
#    manually.


'''a = 27
b = 91

c = b
d = a

print(f"Before swapping : {a},{b}")
print(f"After swapping : {c},{d}")
'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM   6 / 100 — Age in the Future
#   Level 2 — User Input + Type Casting
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask the user for their current age. Ask how many years into the future
#    they want to calculate. Print their age at that time.
#    Example:
#    Current age: 18
#    Years later: 7
#    Age then: 25


'''
curr_age = int(input("Enter your current age : "))
fut_years = int(input("how many years into the future you want to calculate : "))
print(f"Your age after {fut_years} is : ", curr_age+fut_years )





#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM   7 / 100 — Shopping Receipt
#   Level 2 — User Input + Type Casting
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask the user for:
#    product name
#    price
#    quantity
#    Calculate total = price × quantity. Print a clean receipt.
#    Product: Keyboard
#    Price: ₹1500
#    Quantity: 2
#    Total: ₹3000

'''
p_name = input("Enter the product name : ")
price = float(input(f"Enter the price of {p_name} : "))
qty = int(input("Enter the quantity (N) : "))

total = float(price * qty)
x = "####### RECIEPT #######"
y = "#######################"
z = "###### THANK YOU ######"

print(f"{y:^10}")
print(f"{x:^10}")
print(f"Product you have taken : {p_name:^10}")
print(f"Price of the product : {price:^10}")
print(f"Quantity of the product : {qty:^10}")
print(f"Total price : {total:^10}")
print(f"{z:^10}")

'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM   8 / 100 — Electricity Bill
#   Level 2 — User Input + Type Casting
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask the user for electricity units consumed and price per unit. Calculate
#    the bill, then add a fixed service charge of ₹75. Print:
#    Units:
#    Energy charge:
#    Service charge:
#    Final bill:



'''Units = int(input("Enter the units consumed : "))
price = float(input(f"Enter the price per 1 unit : "))
total =float(Units * price)
service_charge = 75

extra = float(total + service_charge)

x = "####### RECIEPT #######"
y = "#######################"
z = "###### THANK YOU ######"

print(f"{y:^10}")
print(f"{x:^10}")
print(f"Units consumed    : {Units:>10}")
print(f"Energy charge     : {total:>10}")
print(f"Service charge    : {service_charge:>10}")
print("------------------------------------------")
print(f"Final bill        : {extra:>10}")
print(f"{z:^10}")

'''


#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM   9 / 100 — Speed Calculator
#   Level 2 — User Input + Type Casting
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for distance in kilometres and time in hours. Calculate speed in km/h
#    and m/s.
#    You need to correctly convert the units.



'''km_dist = input("Enter the distance in (Km) : ")
time = input("Enter time in (Hrs) : ")

speed = km_dist/time


conversion1 = speed
conversion2 = time/3600

print(f"")'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  10 / 100 — Temperature Input
#   Level 2 — User Input + Type Casting
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask the user for a temperature in Celsius. Convert it to Fahrenheit. Print
#    both.
#    Do not reuse a temperature-conversion project you've already seen. Build
#    it yourself
#    from the formula.
# (9*temp)/5+32
# (temp-32)*5/9

'''temp = float(input("Enter the temperature : "))
value = input("Is this Celsius or Fahraneit (C/F) ? : ")

if value == "C":
    conversion = (9*temp)/5+32
    print(f"The value after converting it to Fahraneit : {conversion}")

else:
    conversion = (temp-32)*5/9
    print(f"The value after converting it to Fahraneit : {conversion}")

'''




#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  11 / 100 — Circle Analysis
#   Level 3 — Arithmetic & Mathematical Reasoning
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask the user for the radius of a circle. Calculate diameter,
#    circumference, and area
#    using math.pi. Print all three.


'''
import math

radius = float(input("Enter the radius of circle : "))
circumference = radius * 2 * math.pi
area = math.pi * radius * radius

print(f"Radius : {radius}\nCircumference : {circumference}\nArea : {area}")

'''


#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  15 / 100 — Two-Digit Number Analysis
#   Level 3 — Arithmetic & Mathematical Reasoning
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask the user for a two-digit integer. Extract the tens digit and ones
#    digit. Calculate the sum of digits and product of digits.
#    Input: 47
#    Tens: 4
#    Ones: 7
#    Sum: 11
#    Product: 28
#    This tests whether you understand arithmetic rather than just using
#    built-in tricks.=\
#

'''
value = int(input("Enter a 2-DIGIT integer : "))
ones = value % 10
tens = value // 10 ----------------------------------------------------------------------------------- #rounds off to the nearest whole number / REMOVES THE DECIMAL POINT
sum = ones + tens
product = ones * tens
print(f"Input: {value}\nTens: {tens}\nOnes: {ones}\nSum: {sum}\nProduct: {product}")------------------------------------------------------------------------------------------------------------------------------------

'''







#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  19 / 100 — Smallest of Three
#   Level 4 — if / elif / else
#═══════════════════════════════════════════════════════════════════════════════
#

#    (Follows P18 — same setup, one change.)
#    Same idea, but determine the smallest.
#    Interview-style variation: make sure your program handles equal values
#    correctly, e.g.
#    10, 10, 5.


'''val1 = float(input("Enter the first value : "))
val2 = float(input("Enter the second value : "))
val3 = float(input("Enter the third value : "))

if val1>val2>val3:
    print(f"{val3} is smallest")
elif val1>val3>val2:
    print(f"{val2} is smallest")
elif val3>val1>val2:
    print(f"{val2} is smallest")
elif val2>val1>val3:
    print(f"{val3} is smallest")
elif val2>val3>val1:
    print(f"{val1} is smallest")
elif val3>val2>val1:
    print(f"{val1} is smallest")
elif val1 == val2 and val2>val3:
    print(f"value 1 : {val1} and value 2 : {val2} are equal but value 3 : {val3} is smallest")
elif val3 == val2 and val2>val1:
    print(f"value 2 : {val2} and value 3 : {val3} are equal but value 1 : {val1} is smallest")
elif val1 == val3 and val3>val2:
    print(f"value 1 : {val1} and value 3 : {val3} are equal but value 2 : {val2} is smallest")


elif val1 == val2 and val2<val3:
    print(f"value 1 : {val1} and value 2 : {val2} are equal but they are smallest")
elif val3 == val2 and val2<val1:
    print(f"value 2 : {val2} and value 3 : {val3} are equal but they are smallest")
elif val1 == val3 and val3<val2:
    print(f"value 1 : {val1} and value 3 : {val3} are equal but they are smallest")


elif val1 == val2 == val3:
    print(f"All are equal !!")
else:
    print(f"{val1} or {val2} or {val3} is invalid")

'''




#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  24 / 100 — ATM Withdrawal Decision
#   Level 5 — Logical Operators
#═══════════════════════════════════════════════════════════════════════════════
'''


import time

# [PRIVACY: original personal name 'nikhil' replaced with fake placeholder 'student1']
name = "student1"
attempts = 5
balance = 1000
valid = 0


print("############ WELCOME ############")
print("*** *** *** XYZ BANK *** *** *** ")
print(" ")


password = input("Set password : ")
while password == "" :
    print("Can't be empty")
    password = input("Set password : ")
pass

phone_no = input("Enter phone number : ")
while phone_no == "" or 10 > len(phone_no) > 0:
    print("")
    print("Can't be empty")
    print("Phone number should be 10 digits long")
    print("")
    phone_no = input("Enter your phone number : ")

time.sleep(2)
print("*** *** *** *** *** *** ")
passcode = input("Enter the password : ")
time.sleep(3)

while not password == passcode :
        attempts -= 1
        print(f"Invalid password !! ATTEMPTS LEFT : {attempts}")
        passcode = input("Enter the password : ")
        if attempts <= 0 :
              print("SYSTEM LOCKED")
        else:
              pass
value = int(input("Press '1': Check Balance\nPress '2': Withdraw money\nPress '3': Exit\n"))
if value == 1:
        time.sleep(1)
        print(f"Your balance is : {balance}")
        time.sleep(0.5)
        withdraw = input("Do you want to withdraw ? (Y/N): ")
        if withdraw == "Y" or withdraw == "y":
              time.sleep(0.5)
              amt = float(input("Enter money to be withdrawn : "))
              time.sleep(1)
              if not amt > balance or amt <= 0 or amt == "" :
                  balance -= amt
                  print("TRANSACTION SUCCESSFUL !! ")
                  print(f"Current balance : {balance}")
                  exit

              else:
                  print("Can't withdraw amount greater than balance !")
                  print("Can't be empty or zero")
                  amt = float(input("Enter money to be withdrawn : "))
        else:
                print(f"Your balance was : {balance}")
                print("############ THANK YOU ############")
                exit

elif value == 2:
        time.sleep(0.5)
        amt = float(input("Enter money to be withdrawn : "))
        time.sleep(1)
        if amt > balance or amt <= 0 or amt == "" :
            print("Can't withdraw amount greater than balance !")
            print("Can't be empty or zero")
        else:
            balance -= amt
            print("TRANSACTION SUCCESSFUL !! ")
            print(f"Current balance : {balance}")
            exit
elif value == 3:
        print("############ THANK YOU ############")
        exit
else:
        print("Invalid input , restart again !!")

'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  25 / 100 — Scholarship Eligibility
#   Level 5 — Logical Operators
#═══════════════════════════════════════════════════════════════════════════════
#

#    A student qualifies if CGPA ≥ 8.5 AND attendance ≥ 75%. Ask for both
#    values. Print Scholarship eligible or Not eligible.

'''
name = input("Enter your name : ")
eligible1 = float(input("Enter your marks including decimal points : "))
eligible2 = int(input("Enter your attendence : "))

if eligible1 >= 8.5 and eligible2 >= 75 :
      print(f"{name}, you are eligible for getting Scholarship")
elif eligible1 <= 0 or eligible2 <= 0 :
      print(f"{eligible1}, {eligible2} are invalid")
else:
      print(f"{name}, you are NOT eligible for getting Scholarship")
'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  26 / 100 — Free Delivery
#   Level 5 — Logical Operators
#═══════════════════════════════════════════════════════════════════════════════
#

#    An online store gives free delivery if order amount ≥ ₹999 OR the customer
#    is a premium member. Ask for order amount and premium membership status.
#    Determine the delivery charge.


'''premium_memb = input("Are you a premium member (Y/N) ? : ")
if premium_memb == "y" or premium_memb =="Y":
    free_delivery = 1
else:
    free_delivery = 0
order_amt = float(input("Enter the order amount : "))

eligible = order_amt >= 999

if eligible and free_delivery:
    print("########## BILL ##########")
    print(f"Order amount: {order_amt}")
    print("FREE DELIVERY: +0")
    print(f"Total amount to be paid: {order_amt}")
else:
    print("########## BILL ##########")
    print(f"Order amount: {order_amt}")
    print("Delivery charges: +59")
    print(f"Total amount to be paid: {order_amt+59.0}")
'''








#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  29 / 100 — Adult / Minor
#   Level 6 — Conditional Expressions
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for age. Create a variable status using a conditional expression,
#    containing
#    either "Adult" or "Minor".


'''age = int(input("Enter your age: "))
print("You are adult" if age >= 18 else "You are minor")
'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  30 / 100 — Pass / Fail
#   Level 6 — Conditional Expressions
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for marks. Use a conditional expression to assign "Pass" or "Fail" to
#    a
#    variable, then print it.


'''marks = float(input("What's your marks: "))
a = print("Pass" if marks >= 38 else "Fail")
'''




#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  31 / 100 — Maximum of Two
#   Level 6 — Conditional Expressions
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for two numbers. Use a conditional expression to determine the larger
#    number.
#    Don't use max().


'''num1 = int(input("Enter first munber: "))
num2 = int(input("Enter second number: "))
print(f"{num1} is greater than {num2}" if num1>num2 else f"{num2} is greater than {num1}")-----------------------------------------------------------------------------------------------------------------------------------------------'''







#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  33 / 100 — Sign Detector
#   Level 6 — Conditional Expressions
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a number. Using a conditional expression, determine "Positive" or
#    "Negative".
#    You should also decide how you want to handle 0.


'''num = int(input("Enter 'Positive' or 'Negative' number: "))
print(f"{num} is positive" if num>0 else f"{num} is negative" f"{num} is negative" if num<0 else "It's a zero"  ) ---------------------------------------------------------------------------------------------'''




#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  37 / 100 — Second Largest of Three Numbers
#   Level 8 — Mixed Interview Problems
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for three numbers. Determine the second-largest value.
#    10, 40, 20 → 20
#    50, 20, 30 → 30
#    10, 10, 5 → 10
#    No lists. No sorting. No max() / min(). This is a proper logic problem.


'''num1 = int(input("Enter the first number: "))
num2 = float(input("Enter the units consumed: "))
num3 = int(input("Enter the third number: "))

if num1>num2>num3 or num3>num2>num1:
    print(f"{num2} is second smallest")
elif num1>num3>num2 or num2>num3>num1:
    print(f"{num3} is second smallest")
elif num2>num1>num3 or num3>num1>num2:
    print(f"{num1} is second smallest")
else:
    print("INVALID INPUT/s")'''




#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  38 / 100 — Electricity Bill Slab
#   Level 8 — Mixed Interview Problems
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for electricity consumption. Use:
#    0–100 units → ₹5/unit
#    101–200 units → ₹7/unit
#    201–300 units → ₹10/unit
#    Above 300 → ₹15/unit
#    Calculate the bill.
#    Decide whether the slab rate applies to the entire consumption or
#    progressively. State
#    your assumption and implement it.


'''units_used = float(input("Enter the units consumed: "))
a = units_used*5
b = (100*5) + units_used*7
c = (100*5) + (100*7) + units_used*10
d = (100*5) + (100*7) + (100*10) + units_used*15


print(f"{a}" if 100>=units_used>=1 else "" f"{b}" if 200>=units_used>=101 else "" f"{c}" if 300>=units_used>=201 else "" f"{d}" if 1000>=units_used>=300 else f"Can't use {units_used}units for personal use. Please enquire BSCOM for using more units")
'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  39 / 100 — Employee Overtime
#   Level 8 — Mixed Interview Problems
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for hours worked and hourly wage. First hours at normal rate; above
#    40 hours at 1.5× rate. Calculate total pay.
#    No loops.


'''wage = 0
worked_hrs = float(input("Enter hours worked per week: "))
hourly_wage = float(input("Enter wage per hour: "))

if 0<=worked_hrs<=40:
    wage = hourly_wage * worked_hrs
    wage_per_week = wage * 7
    print(f"Your hourly wage: {hourly_wage}, you work for: {worked_hrs}hrs per week")
    print(f"Your salary/wage: {wage}")
    print(f"Your salary/wage per week: {wage_per_week}")
elif 41<=worked_hrs<=60:
    wage = hourly_wage * worked_hrs * 1.5
    wage_per_week = wage * 7
    print(f"Your hourly wage: {hourly_wage}, you work for: {worked_hrs}hrs per week")
    print(f"Your salary/wage: {wage}")
    print(f"Your salary/wage per week: {wage_per_week}")
else:
    print(" ")
    print(f"####### Scientifically no human can work for {worked_hrs} !!")
    feedback = input("1: If you work more than 60hrs please give us information and feedback\n2: Press 'ENTER' to exit:\n")
    print("\nThank you for feedback" if feedback else "" "THANK YOU, visit again" if feedback=="" else "")

'''









#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  41 / 100 — ATM Withdrawal
#   Level 8 — Mixed Interview Problems
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for account balance, withdrawal amount, and whether the account is
#    active.
#    Withdrawal is allowed only if:
#    account is active
#    AND withdrawal amount > 0
#    AND withdrawal amount <= balance
#    AND withdrawal amount is a multiple of 100
#    If successful, calculate the remaining balance. Otherwise explain why it
#    failed.
#    Hard part: you need to reason about multiple independent conditions.


" i have answered this in the previous question of ATM "






#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  43 / 100 — Smart Fan Controller
#   Level 9 — Real-World System Logic
#═══════════════════════════════════════════════════════════════════════════════
#

#    A fan has three modes:
#    temperature < 20 → OFF
#    20–29 → LOW
#    30–39 → MEDIUM
#    40+ → HIGH
#    But if the room is unoccupied, the fan must be OFF. Ask for temperature
#    and whether someone is present. Determine the fan state.

'''
occupancy = input("Are you inside the room? (Y/N) : ")
if occupancy == "n" or occupancy == "N":
    print("Fan is off cuz no one is there in the room !!")
elif occupancy == "y" or occupancy == "Y":
    temp = float(input("Enter the temperature in the room: "))
    if temp<=20:
        print(f"Fan OFF, not required for temperature : {temp}")
    elif 21<=temp<=29:
            print(f"Sir, I have turned on the fan. It's setted for LOW as the temperature in the room is {temp}")
    elif 31<=temp<=39:
             print(f"Sir, I have turned on the fan. It's setted for MEDIUM as the temperature in the room is {temp}")
    elif 40>=temp>=50:
            print(f"Sir, I have turned on the fan. It's setted for HIGH as the temperature in the room is {temp}")
    else:
        print(f"A human can't handle {temp}, you will be killed")
else:
    print("INVALID INPUT !!")

'''







#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  44 / 100 — Laptop Battery Warning System
#   Level 9 — Real-World System Logic
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for battery percentage and whether the laptop is plugged in. Rules:
#    Battery < 20 AND not plugged in → Critical
#    Battery < 40 AND not plugged in → Low
#    Battery >= 40 → Normal
#    Plugged in → Charging
#    Deliberately tricky: think about which condition should take priority.


'''
max_battery = 100
user_battery = int(input("Enter the current laptop/mobile battery value: "))
plugged = input("Is the device plugged in / charging? (Y/N): ")
plugged_lower = plugged.lower()

if plugged_lower == "n" and user_battery < 20:
    print("CRITICAL !! PLEASE PLUG IN YOUR DEVICE")
elif plugged_lower == "n" and user_battery < 40:
    print("LOW !! I recommend to keep your battery more than 60%")
elif plugged_lower == "n" and user_battery >= 40:
    print("Battery is in NORMAL CONDITION ")
elif user_battery == 0 and plugged =="":
    print("Your phone is Dead-ass my boy. How tf are you typing out the battery percentage?")
elif user_battery <= -1 and plugged =="y":
    print(f"How the fk can anybody's battery value be {user_battery}")
elif user_battery <= -1 and plugged =="n":
    print(f"How the fk can anybody's battery value be {user_battery}")

if plugged_lower == "y" and 1 <= user_battery <= 39:
    remaining_battery = max_battery - user_battery
    print("CRITICAL !!")
    print("Charging..")
    print(f"Do not remove the charger, Remaining battery to be charged: {remaining_battery}%")

elif plugged_lower == "y" and 40 <= user_battery <= 59:
    remaining_battery = max_battery - user_battery
    print("LOW !! I recommend to keep your battery more than 60%")
    print("Charging..")
    print(f"Do not remove the charger, Remaining battery to be charged: {remaining_battery}%")

elif plugged_lower == "y" and 60<=user_battery<=99:
    remaining_battery = max_battery - user_battery
    print("LOW !! I recommend to keep your battery more than 60%")
    print("Charging..")
    print(f"Do not remove the charger, Remaining battery to be charged: {remaining_battery}%")

elif plugged_lower == "y" and user_battery==100:
    remaining_battery = max_battery - user_battery
    print("Charging..")
    print("Battery full, remove the charger")

else:
    print("INVALID INPUT !")

    '''




#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  46 / 100 — College Attendance Warning
#   Level 9 — Real-World System Logic
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for attendance percentage and whether the student has an approved
#    medical exception. Rules:
#    attendance >= 85 → Safe
#    attendance 75–84 → Warning
#    attendance < 75 AND no exception → Shortage
#    attendance < 75 AND exception → Review required
#    Mainly a condition-ordering problem.


#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  47 / 100 — Ride Fare Calculator
#   Level 9 — Real-World System Logic
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for distance in km, whether it is raining, and whether it is peak
#    hour. Base fare ₹50, distance charge ₹15/km, peak hour adds 20%, rain adds
#    10%. Calculate the
#    final fare.
#    Work out the order of the calculations yourself.



#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  48 / 100 — Mini Smart Assistant
#   Level 9 — Real-World System Logic
#═══════════════════════════════════════════════════════════════════════════════
#

#    Build a small command-decision system. Ask the user for temperature, battery
#    percentage, whether internet is available, whether it is raining, and whether
#    the user is at home. Produce decisions for:
#    · Environment: Cold / Comfortable / Hot
#    · Battery: Critical / Low / Normal
#    · Internet: Online / Offline
#    · Suggested action: your call, based on the combination of states. For example:
#    If battery is critical and internet is unavailable:
#        → "Reduce system activity"
#    If it is raining and user is outside:
#        → "Carry an umbrella"
#    If temperature is hot and user is at home:
#        → "Consider turning on the fan"
#    You create the rules.
#    Requirements:
#    • Use variables and user input, with type casting where appropriate
#    • Use if / elif / else
#    • Use and / or / not
#    • Use at least one chained comparison
#    • Use at least one conditional expression
#    • No loops, no lists, no dictionaries, no functions
#    This isn't about building a sophisticated AI. It's about proving you can take
#    raw inputs → conditions → decisions, the foundation underneath much larger
#    software systems.



#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  49 / 100 — Username Normalizer
#   Part A — String Methods
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask the user for a username that may contain leading spaces, trailing
#    spaces, and inconsistent uppercase/lowercase. Convert it into a clean
#    standardized username.
#    " NiKhIl123 " → "nikhil123"


"""mineeeeee below"""
# user_name = input("Enter your username: ")
# user_name_lower = user_name.lower()
# clean_username = user_name_lower.strip()
# a = clean_username.find(" ")

# while not a==-1:
#     print("Can't use spaces inbetween or starting !! try again")
#     user_name = input("Enter your username: ")
#     user_name_lower = user_name.lower()
#     clean_username = user_name_lower.strip()
#     a = clean_username.find(" ")
#     if not a==-1:
#         print("Can't use spaces inbetween or starting !! try again")
#     else:
#         print(clean_username)


"""Ai's belowwwwwwww"""
'''while True:
    user_name = input("Enter your username: ")
    user_name_lower = user_name.lower()

    if user_name_lower != user_name_lower.strip():
        print("No leading/trailing spaces allowed!! Try again.")
        continue
    if " " in user_name_lower:
        print("Don't use spaces")
    else:
        print("VERFIED")
        break


'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  50 / 100 — Email Validator — Basic
#   Part A — String Methods
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for an email address. Determine whether it is valid according to your
#    own clearly defined basic rules — for example: one @, something before @,
#    something after @,
#    a., no spaces.
#    Don't try to build a production-grade email validator. This is a
#    string-reasoning exercise.


'''# [PRIVACY: original email 'nikhil@gmail.com' replaced with fake placeholder 'student@example.com']
email = "student@example.com"
rule1 = "@"
rule2 = email.find("@")
length = len(email)
valid1 = email.count("@")
valid2 = " "

while valid2 in email:
      print("DO NOT USE SPACES!")
      email = input("Enter your E-mail: ")
if '@' not in email:
    print("Please include '@'")
elif rule2 == 0:
     print("Please include something before writing '@' !!")
     if rule2 == length:
          print("Please include something after writing '@' !!")
     else:
      print''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''mineeeeeee'''


# email = input("Enter an email address: ")

# if " " in email:
#     print("Invalid")
# elif email.count("@") != 1:
#     print("Invalid")
# else:
#     local, domain = email.split("@")
#     if local == "" or domain == "":
#         print("Invalid")
#     else:
#         print("Valid")
######################################################################################################################## AIIIIIII##########

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  51 / 100 — Character Counter
#   Part A — String Methods
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask the user for a string and a character. Count how many times that
#    character
#    appears.
#    Use a loop. Don't use a built-in counting method.

'''string = input("Write a word: ")
character = input(f"Enter a character which is in the word {string}: ")
count = 0

for i in string:
    if character == i:
        count+=1
print(f"The number of times {character} is repeated is: {count}")
'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  52 / 100 — Vowel Counter
#   Part A — String Methods
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a sentence. Count a e i o u, ignoring uppercase/lowercase
#    differences.

# sentence = input("Type any sentence: ")
# sentence = sentence.lower()

# vowel1,vowel2,vowel3,vowel4,vowel5 = "a","e","i","o","u"

# counting1 = sentence.count(vowel1)
# counting2 = sentence.count(vowel2)
# counting3 = sentence.count(vowel3)
# counting4 = sentence.count(vowel4)
# counting5 = sentence.count(vowel5)
# total = counting1+counting2+counting3+counting4+counting5
# print(total) ############################################################################################# mineeeeeeeeeeeee ############

"""s = input("Type any sentence: ").lower()
print(s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u"))
"""\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"   AI \"\"\"

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  53 / 100 — Password Masking
#   Part A — String Methods
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask the user for a password. Print it as a row of * characters.
#    The number of stars must correspond to the password length. Don't use a
#    hardcoded
#    number of stars.

'''password = input("Enter your password: ").lower()
length = len(password)

print(length*"*")'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  54 / 100 — Remove Spaces
#   Part A — String Methods
#═══════════════════════════════════════════════════════════════════════════════
#F
#    Ask for a sentence. Produce a version with all spaces removed.
#    "I love Python" → "IlovePython"
#    Do it using iteration rather than a single replacement method.


'''sentence = input("Write a sentence: ").lower()
final = ""

for i in sentence:
    if i != " ":
        final += i
print(final)
'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  55 / 100 — First / Last Character
#   Part B — String Indexing
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a string. Print the first character and the last character. Handle
#    the situation where the input contains only one character.


'''string = input("Enter a word: ")
length = len(string)

first = string[0]
last = string[-1]

if length == 1:
    print("Input contains only one character")
elif length >= 1:
    print(first,last)
else:
    print("INVALID INPUT!!")

'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  56 / 100 — Middle Character
#   Part B — String Indexing
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a word. If it has an odd number of characters, print the middle
#    character.
#    A word like PYTHON should not be treated as having one middle character,
#    since its length is even. Decide what your program should do for even
#    lengths.

'''import math
word = input("Enter a word: ")
length = len(word)
odd = input("Is the number of letters in the word odd (Y/N)?: ")

if odd == "Y" or odd =="y":
    middle = length/2
    middle = math.floor(middle)
    middle_alpha = word[middle]
    print(f"The middle alphabet of {word} is: {middle_alpha}")
elif odd == "N" or odd == "n":
    middle1 = int(length/2)
    middle2 = int((length/2)-1)
    middle_alpha1 = word[middle1]
    middle_alpha2 = word[middle2]
    print(f"The middle letters are: {middle_alpha2} & {middle_alpha1}")
else:
    print("INVALID INPUT!!")'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''mineeeeeeeeeeee ( i wrote it )'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  57 / 100 — First and Last Three
#   Part B — String Indexing
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a string. Print the first 3 characters and the last 3 characters.
#    Also consider what happens when the string is shorter than 3 characters.


'''string = input("Enter some sentence: ").strip().replace(" ","")

if len(string) > 3:
    print("first 3 characters are: ",string[0],string[1],string[2])
    print("last 3 characters are: ", string[-3],string[-2],string[-1])
elif len(string) <= 3:
    print("The sentence count is only 3 letters")
    print("The first character is: ",string[0])
    print("The second charater is: ",string[-1])
else:
    print("INVALID INPUT!!")'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  58 / 100 — Reverse a String
#   Part B — String Indexing
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a string. Print it backwards.
#    Do not use a built-in reverse function.

'''str = input("Enter anything: ")
print(str[::-1])
'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  59 / 100 — Palindrome Detector
#   Part B — String Indexing
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a word. Determine whether it reads the same forwards and
#    backwards,
#    ignoring case.
#    madam → palindrome
#    python → not palindrome


# word = input("Enter a word: ").lower()
# if "" == word or " " in word:
#         print("DO NOT USE SPACES")
#         print("INVALID INPUT")
# elif word == word[::-1]:
#     print(f"{word} is a palindrome")
# elif not word == word[::-1]:
#     print(f"{word} is not a palindrome")
# else:
#     pass

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  60 / 100 — Username Extraction
#   Part B — String Indexing
#═══════════════════════════════════════════════════════════════════════════════
#

#    Given email = "nikhil@gmail.com", extract only nikhil.
#    Don't hardcode the username.

'''# [PRIVACY: original email 'nikhil@gmail.com' replaced with fake placeholder 'student@example.com']
email = "student@example.com"
print(email[0:6])
'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  61 / 100 — Professional Receipt
#   Part C — Format Specifiers
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for product name, quantity, and price. Print a properly formatted
#    receipt where prices always display with 2 decimal places.


'''p_name = input("Enter the product name: ")
qty = int(input("Enter the qty: "))
price = float(input(f"Enter the price of {p_name} of quantity {qty}: "))

print("############ RECIPT ############")
print(f"Product name : {p_name:<10}")
print(f"Quantity     : {qty:<10}")
print(f"Price        : {price:<10.2f}")
'''







#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  65 / 100 — Number Guessing Game
#   Part D — While Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Choose a secret number in your code. Keep asking the user to guess until
#    they get it correct. After every wrong guess, tell them whether the guess
#    is Too high or Too
#    low.


'''secret_num = 45
num = int(input("Enter a number below 100: "))

while num != 45:
    print("Incorrect Guess !!")
    num = int(input("Enter a number below 100: "))
print("Guess is right")

'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  66 / 100 — Password Retry System
#   Part D — While Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Store a correct password. Give the user a maximum of 3 attempts. Output
#    Access
#    granted or Account locked.
#    You must actually stop accepting attempts after the limit.


'''# [PRIVACY: original stored password 'nikhilu2111' replaced with fake placeholder 'fake_password_123']
correct_pass = "fake_password_123"
attempts = 3

while attempts:
    password = input("Enter your password: ")
    if correct_pass != password:
        attempts-=1
        print(f"Incorrect password!, attempts left: {attempts}")
        if attempts <= 0:
            print("TOO MANY TRIES !! SYSTEM LOCKED")
        else:
            continue
    else:
        print("Password correct. ACCESS GRANTED")
        break
'''









#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  68 / 100 — Running Total
#   Part D — While Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Keep asking the user for numbers and add them together. Stop when the user
#    enters
#    0. Print the total.


'''num = int(input("Enter a number: "))
total = 0
total += num

while num != 0:
    num = int(input("Enter a number: "))
    total += num
    print(total)
'''







#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  71 / 100 — Multiplication Table
#   Part E — For Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a number. Print its multiplication table from 1 to 10, cleanly
#    formatted.


'''num = int(input("Enter a number for knowing it's table: "))


for i in range(10):
    print(f"{i} X {num} =",i * num)

'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  72 / 100 — Sum from 1 to N
#   Part E — For Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for N. Calculate 1 + 2 + 3 +... + N using a loop.


'''n = int(input("Enter a number: "))
total = 0

for i in range(n+1):
    if i>0:
       total += i
    else:
        pass
print(total)
'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  73 / 100 — Factorial
#   Part E — For Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a positive integer. Calculate its factorial using a loop.
#    Don't use a factorial function.


'''num = int(input("Enter a positive integer: "))
total = 1

for i in range(num+1):
    if i>0:
      total*=i
    else:
        pass
print(total)
'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  74 / 100 — Count Digits
#   Part E — For Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for an integer. Determine how many digits it contains.
#    Input: 58291 → Output: 5 digits

'''num = input("Enter any number: ")
digits = 0

for i in num:
    digits+=1
print(digits)
'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  75 / 100 — Sum of Digits
#   Part E — For Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for an integer. Calculate the sum of its digits.
#    583 → 16


'''num = input("Enter any number: ")
total =0

for ch in num:
    total += int(ch)
print(total)

'''





#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  76 / 100 — Product of Digits
#   Part E — For Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    (Follows P75 — same setup, one change.)
#    Same idea, but multiply the digits.
#    234 → 24


'''num = input("Enter a number: ")
total = 1

for ch in num:
    total*=int(ch)
print(total)
'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  77 / 100 — Largest Digit
#   Part E — For Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for an integer. Find the largest digit without using max().



#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  79 / 100 — Armstrong Number
#   Part F — Interview Numbers
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a number. Determine whether it is an Armstrong number.
#    153 because 1³ + 5³ + 3³ = 153


'''num = input("Any number: ")
total = 0

for ch in num:
    value=int(ch)**3
    total+=value
if int(num) == total:
    print("ITS A AMSTRONG NUMBER")
else:
    print("Not an AMSTRONG number")
'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  80 / 100 — Prime Number
#   Part F — Interview Numbers
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for an integer. Determine whether it is prime.
#    Don't use a prime-checking library/function. Think about how many numbers
#    you actually
#    need to test.


'''number = int(input("Enter an integer: "))

if number < 2:
    print("Not prime")
else:
    prime = True

    i = 2
    while i * i <= number:
        if number % i == 0:
            prime = False
            break
        i = i + 1

    if prime:
        print("Prime")
    else:
        print("Not prime")'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  81 / 100 — Prime Numbers in a Range
#   Part F — Interview Numbers
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for start and end. Print every prime number in that range.
#    This is a loop inside a loop problem.

'''
start = int(input("Enter the starting value: "))
end = int(input("Enter the Final value: "))
is_prime = True

for num in range(start,end+1):

    if num > 1:
        is_prime = True

        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num,end=",")
'''








#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  82 / 100 — Perfect Number
#   Part F — Interview Numbers
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for an integer. Determine whether it is a perfect number.
#    6 → proper divisors 1 + 2 + 3 = 6


'''num = int(input("Enter a integer: "))
divisor = 0

for i in range(1,num):
    while num % i == 0:
        divisor += i
        i+=1
        if divisor == num:
            print(f"{num} is a perfect number")'''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  83 / 100 — Factor List
#   Part F — Interview Numbers
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a number. Print all of its factors.
#    12 → 1 2 3 4 6 12


'''num = int(input("Enter a number: "))

for i in range(1,num+1):
    if num % i == 0:
        factor = i
        print(i,end=" ")
        i+=1'''




#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  85 / 100 — Loan Payment Simulation
#   Part G — Real-World Calculators
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for loan amount and monthly payment. Calculate how many complete
#    monthly payments are needed to pay off the loan. Assume no interest and
#    payment is always
#    positive.
#    Use a loop.


'''loan_amt = float(input("Enter your total loan amount: "))
monthly_payment = float(input("Enter the monthly amount assigned to pay: "))
months = 0

while loan_amt > 0:
    loan_amt-=monthly_payment
    months +=1

print("The months to be paid is: ",months)






'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  87 / 100 — Shopping Cart Simulation — No Lists
#   Part G — Real-World Calculators
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask repeatedly for item name, price, and quantity. After each item, ask
#    Add another item? (Y/N). At the end print the number of items purchased
#    and total cost.
#    You cannot store an actual collection yet. Work with aggregate variables.


'''item_name = input("Enter the name of item: ")
price = float(input("Enter the price of the item: "))
quantity = int(input(f"Enter the quantity of the {item_name}: "))
total = quantity*price
add_item = input("Add another item? (Y/N): ")

while add_item == "Y" or add_item =="y":
    item_name = input("Enter the name of item: ")
    price = float(input("Enter the price of the item: "))
    quantity = int(input(f"Enter the quantity of the {item_name}: "))
    total = total+(quantity*price)
    add_item = input("Add another item? (Y/N): ")

print("TOTAL: ",total)'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  88 / 100 — Cinema Ticket Counter
#   Part G — Real-World Calculators
#═══════════════════════════════════════════════════════════════════════════════
#

#    A cinema has 50 seats. Repeatedly ask whether the user wants to book a
#    seat. Every successful booking decreases available seats. Stop when all
#    seats are booked or the user chooses to stop. Print remaining seats.


'''seats = 50
booking = input("Do you want to book a seat for this cinema? (Y/N): ")

while booking == "y" or booking == "Y":
    print("###### WELCOME ######")
    print(f"Available seats: {seats}")

    for i in range(1,51):
        print(i,end="│")
    blocked = int(input("\nEnter seat number for booking: "))
    print(f"success !! seat number: {blocked} is blocked")
    seats-=1
    booking = input("Do you want to book another seat? (Y/N): ")
print("Thank you !!")'''




#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  89 / 100 — Character Frequency — One Character
#   Part H — Loops + Strings
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a sentence and a character. Count how many times the character
#    occurs,
#    case-insensitively.


'''sentence = input("Enter any sentence: ").lower().replace("","")
character = input("Enter a character to find it's frequency: ")
freq = 0

for ch in sentence:
    if ch == character:
        freq+=1

print(f"Total number of occurance of character '{character}' is: {freq}")
print(sentence)'''

#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  90 / 100 — Word-like Token Counter
#   Part H — Loops + Strings
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a sentence. Count how many spaces it contains, and use that to
#    estimate the
#    number of words.
#    "I love learning Python" → 4 words
#    You need to think about multiple spaces and leading/trailing spaces.


'''sentence = input("Enter any sentence: ")
total = sentence.split()

print(f"The estimate of total words would be: {len(total)}")'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' AI ''''''






#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  91 / 100 — Uppercase / Lowercase Counter
#   Part H — Loops + Strings
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a sentence. Count uppercase letters, lowercase letters, and
#    digits. Ignore spaces and punctuation for these counts.


'''sentence = input("Enter a sentence: ").replace("","")
up_count = 0
low_count = 0
digits = 0
punctuation = 0

for ch in sentence:
    if ch.isdigit() :
        digits+=1
    elif ch == ch.lower():
        low_count+=1
    elif ch == ch.upper():
        up_count+=1
    else:
        punctuation+=1

print(f"The number of UPPERCASE letters: {up_count}\nThe number of LOWERCASE letters: {low_count}\nThe number of DIGITS: {digits}\nThe number of EXTRAS/punctuation: {punctuation}"'''





#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  92 / 100 — Character Replacement
#   Part H — Loops + Strings
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for a sentence, a character to replace, and a replacement character.
#    Create the new string manually using iteration.
#    Don't use.replace().


'''sentence = input("Enter a sentence: ").lower().replace("","")
target = input("Select any character in your sentence to replace: ")
shot = input(f"What do you want to replace in the place of '{target}'?: ")
length = len(sentence)

for ch in sentence:
    while ch == target:
     edit1 = sentence.find(ch)
     edit2 = sentence[0:edit1]
     final = sentence[edit2:length]
'''############################################################################################################################## UP WAS MINE #########################

'''sentence = input("Enter a sentence: ")
old = input("Enter the character to replace: ")
new = input("Enter the new character: ")

answer = ""

for ch in sentence:
    if ch == old:
        answer = answer + new
    else:
        answer = answer + ch

print("New sentence:", answer)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' THIS UP IS AI"S '''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  93 / 100 — String Compression — Simple Version
#   Part H — Loops + Strings
#═══════════════════════════════════════════════════════════════════════════════
#

#    Input: aaabbcccc
#    Output: a3b2c4
#    You only need to handle consecutive repeated characters. This is
#    significantly harder than the previous string problems.


'''word = input("Enter a word/s with many repeated characters: ")
length = len(word)
answer = ""
count = 1

for i in range(length-1):
    if word[i] == word[i+1]:
        count+=1
    else:
        answer+=word[i]+str(count)
        count = 1

answer+=word[-1]+str(count)

print(answer)''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' ai , but i didnt understand this line :answer+=word[-1]+str(count)'''





#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  94 / 100 — Rectangle Pattern
#   Part I — Nested Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for rows and columns. Print a rectangle of *.
#    3 rows, 5 columns →
#    *****
#    *****
#    *****

'''
rows = int(input("Enter number of rows: "))
columns = int(input("Enter the number of columns: "))

for i in range(rows):
    for j in range(columns):
        print("*",end="")

    print()'''





#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  95 / 100 — Right Triangle
#   Part I — Nested Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Ask for height. Output:
#    *
#    **
#    ***
#    ****
#    *****


'''height = int(input("Enter height: "))
for i in range(1,height+ 1):
    print("*" * i)

'''



#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  96 / 100 — Number Triangle
#   Part I — Nested Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    For 5:
#    1
#    12
#    123
#    1234
#    12345


'''num = int(input("Enter a number: "))
for i in range(num+1):
    print(i)'''
'''
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()''''''''aiii'''''''''''''''''''''''''''''
#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  97 / 100 — Multiplication Table Grid
#   Part I — Nested Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Print multiplication tables from 1 to 10 in grid form:
#    1  2  3  4 ...
#    2  4  6  8 ...
#    3  6  9 12 ...
#    ...




#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  98 / 100 — Prime Number Grid
#   Part I — Nested Loops
#═══════════════════════════════════════════════════════════════════════════════
#

#    Print a multiplication-style grid where prime numbers are printed and
#    non-prime numbers are replaced with -. Conceptually:
#    2 - 3 -
#    - 5 - 7
#    ...
#    You determine the exact structure. This combines nested loops + prime
#    logic +
#    conditions.



#═══════════════════════════════════════════════════════════════════════════════
#   PROBLEM  99 / 100 — FizzBuzz
#   Part J — Hard Interview Logic
#═══════════════════════════════════════════════════════════════════════════════
#

#    The classic interview problem. For numbers from 1 to N:
#    divisible by 3 → Fizz
#    divisible by 5 → Buzz
#    divisible by both → FizzBuzz
#    otherwise → print the number
#    Important: condition ordering matters.


'''
n = int(input("Enter a number: "))

for i in range (1,n+1):
    if  i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
'''
