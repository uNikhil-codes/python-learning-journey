#python quiz game by bro code:

# questions = ("1.Who is also called as the 'FIRST AVENGER': ",
#              "2.What's the name of Thor's adopted daughter: ",
#              "3.How many total number of web combinations does spider suit have in the movie 'SPIDERMAN: HOMECOMING': ")

# options = (("A-Iron man","B-Hulk","C-Thor","D-Captain America"),
#            ("A-Love","B-Hela","C-Gamora","D-Thunder"),
#            ("A-298","B-554","C-576","D-273"))

# answers = ("D","A","C")
# guesses = []

# score = 0
# q_num =0

# for question in questions:
#     print("-----------------------")
#     print(question)
#     for option in options[q_num]:
#          print(option)

#     guess = input("Enter (A,B,C,D): ").upper()
#     guesses.append(guess)
#     if guess == answers[q_num]:
#             score+=1
#             print("CORRECT !")
#     else:
#              print("INCORRECT !")
#              print(f"{answers[q_num]} is the correct answer")
#     q_num +=1

# score = score/len(questions) * 100
# print(f"{round(score,2)}%")
#----------------------------------------------------------------------

# my own SMART quiz game

'''questions1 = ("1.What is colour of Iron man's suit: ",
              "2.What's the name of Thor's father: ",
              "3.What's spiderman's gf short name: ")
options1 = (("a. Red-Gold","b. Silver-Blue","c. Gold-black","d. Silver-Green"),
            ("a. Hela","b. Loki","c. Odin","d. Marcus"),
            ("a. K.O","b. M.J","c. D.J","d. F.J"))
answers1 = ("a","c","b")

questions2 = ("2.Which is the THIRD stone that Thanos fought for: ")
options2 = (("a. Reality stone","b. Time stone","c. Soul stone","d. Mind stone"))
answers2 = ("b")

questions3 = ("3.In Captain America: The Winter Soldier, what exact phrase does Steve Rogers use as his password to access Natasha’s secret file: ")
options3 = (("a. Hail Hydra","b. I am Steve Rogers","c. Bucky Barnes","d. On your left"))
answers3 = ("b")

score = 0
question_num = 0
answers = []

print("--- WELCOME ---")
for question in questions1:
      print("----------------")
      print(question)
      for option in options1[question_num]:
          print(option)
      answer = input("Enter (A,B,C,D): ").lower()
      answers.append(answer)
      if answer == answers1[question_num]:
           print("CORRECT !")
           score+=1
           if score >= 1:
                question_num = 0
                for question in questions2:
                     print(question)
                     answer = input("Enter (A,B,C,D): ").lower()
                     answers.append(answer)
                     if answer == answers2[question_num]:
                          print("CORRECT !!")
                          score+=1
                     else:
                          continue
      else:
           print(f"{answers1[question_num]} is correct answer")
      question_num+=1
'''

# questions1 = ("1. What is the colour of Iron Man's suit: ",
#     "2. What's the name of Thor's father: ",
#     "3. What's Spider-Man's girlfriend's short name: ")
# options1 = (("a. Red-Gold", "b. Silver-Blue", "c. Gold-Black", "d. Silver-Green"),
#     (("a. Hela", "b. Loki", "c. Odin", "d. Marcus"),
#     (("a. K.O", "b. M.J", "c. D.J", "d. F.J"))
# answers1 = ("a", "c", "b")


# questions2 = ("4. Which is the THIRD stone that Thanos fought for: ",)
# options2 = (("a. Reality Stone", "b. Time Stone", "c. Soul Stone", "d. Mind Stone"),)
# answers2 = ("b",)


# questions3 = ("5. In Captain America: The Winter Soldier, what exact phrase does Steve Rogers use as his password to access Natasha's secret file: ",)
# options3 = (("a. Hail Hydra", "b. I am Steve Rogers", "c. Bucky Barnes", "d. On your left"),)
# answers3 = ("b",)


# score = 0

# print("--- WELCOME TO THE MARVEL QUIZ ---")


# # Level 1: Easy questions
# for question_num, question in enumerate(questions1):
#     print("----------------")
#     print(question)

#     for option in options1[question_num]:
#         print(option)

#     ans = input("Enter (A, B, C, D): ").lower().strip()

#     if ans == answers1[question_num]:
#         print("CORRECT!")
#         score += 1

#         # Correct answer = move to harder level
#         break

#     else:
#         print(f"{answers1[question_num]} is the correct answer")
#         print("Try the next easy question!")

#         # Wrong answer = continue the easy questions
#         continue


# # Level 2: Medium question
# else:
#     print("\nYou did not answer any easy question correctly.")
#     print("Game over!")
#     print(f"Your final score is {score}")
#     exit()


# print("\nLEVEL 2 UNLOCKED!")

# for question_num, question in enumerate(questions2):
#     print("----------------")
#     print(question)

#     for option in options2[question_num]:
#         print(option)

#     ans = input("Enter (A, B, C, D): ").lower().strip()

#     if ans == answers2[question_num]:
#         print("CORRECT!")
#         score += 1

#         # Correct answer = move to Level 3
#         break

#     else:
#         print(f"{answers2[question_num]} is the correct answer")
#         print("Game over!")
#         print(f"Your final score is {score}")
#         exit()


# # Level 3: Hard question
# print("\nLEVEL 3 UNLOCKED!")

# for question_num, question in enumerate(questions3):
#     print("----------------")
#     print(question)

#     for option in options3[question_num]:
#         print(option)

#     ans = input("Enter (A, B, C, D): ").lower().strip()

#     if ans == answers3[question_num]:
#         print("CORRECT!")

#     else:
#         print(f"{answers3[question_num]} is the correct answer")


# print("----------------")
# print(f"Your final score is {score}")
