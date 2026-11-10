#star program

# star = '*'
# count = 10
# space = " "
# for i in range(count):
#     print(f"{star:^}")
#     star += '*'

# ---------------------------------------------------------------

#CHECK IF THE PASSWORD IS CORRECT AND ENTER HIM  (USING FORMAT SPECIFIER AND FOR LOOP)



# attempt = 5
# emp = "     "

# print(f"WELCOME !!{emp:>}")
# print("###############################")
# password = input("set a password : ")
# print("########### PASSWORD SET ############")
# for i in range(attempt) :
#     print("")
#     valid = input("Enter your password : ")
#     if password == valid :

#         print("Access granted !!")
#         change = input("Would you like to change the password (Y/N) : ")

#         if change=='Y':
#             password1 = input("Enter the new password : ")
#             print("###### PASSWORD CHANGED ######")
#             valid = input("Enter the password : ")

#             if valid == password1:
#                     print("ACCESS GRANTED")
#                     break
#             else:
#                     print(" INCORRECT , try again ")
#                     print(f"ATTEMPTS REMAINING : {attempt} ")

#         elif change =='N':
#             print("OK BYE !")
#             break
#         else :
#             print("Try again !!")
#             print("")

#     else:
#         attempt -= 1
#         print(f"INCORRECT , Try again !! \n          ATTEMPTS REMAINING : {attempt} ")
#         if attempt <= 0:
#             print("SYSTEM LOCKED")
#         else:
#             pass
