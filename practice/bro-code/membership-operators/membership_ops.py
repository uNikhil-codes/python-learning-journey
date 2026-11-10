# membership operators (simple hangman game)

# mineeeee -------------------------------------------------------------------------

# word = "SPIDERMAN"
# trials = 0
# end = 5

# print("###### WELCOME ######")
# print(f"Chances left: {end}")

# while trials<end:
#     length = len(word)
#     guess = input("Guess a letter : ").upper()
#     if guess not in word:
#         end -= 1
#         trials+=1
#         print(f"{guess} is not in the word")
#         print(f"TRY AGAIN, chances left: {end}")
#     elif guess in word:
#         for ch in word:
#           new_word = word.replace(ch,"-")
#           print(new_word)






'''ai's -----------------------------------------------------------------------------------------------------'''
'''word = "SPIDERMAN"
trials = 0
end = 5
guessed_letters = []

print("###### WELCOME ######")
print(f"Chances left: {end}")

while trials < end:
    length = len(word)
    guess = input("Guess a letter : ").upper()

    if guess in guessed_letters:
        print("You already guessed that letter")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        trials += 1
        end -= 1
        print(f"{guess} is not in the word")
        print(f"TRY AGAIN, chances left: {end}")
    else:
        new_word = ""

        for ch in word:
            if ch in guessed_letters:
                new_word += ch
            else:
                new_word += "-"

        print(new_word)

        if "-" not in new_word:
            print("YOU WIN!")
            break

if trials == end:
    print("GAME OVER")


'''
