import random 
# In this game, we are going to take the high int could be guess from user ( in range (0 to the user input int))
# then user start guass the random number, to know better what was the random number i print it out using print command.
# notice that the random number is changeing in every itteration and due to that i didn't use the estimation like grater or less than statements.
#but we give 5 chance to guess the correct number, if user didn't guess the correct number the game end.


# random.randrange(start, end(isn't include))
# random.randint(start, end(include))


user_number=int(input("Write the maximum number to guess: "))
#rnd_number=random.randint(0,user_number)/// we have to use it inside the loop to change in every itteration

guesses = 0;
while True:
        guesses +=1
        rnd_number=random.randint(0,user_number)
        user_guess = input("Make a guass : ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Write a number please.")

        if user_guess == rnd_number:
            print("you got it ")
            print("You did the correct guess in ",guesses, " times.")
            break
        elif user_guess>user_number:
            print("Please Write an smaller number, its bigger than your maximum number")
        else:
            print(rnd_number)
            print("Opps, you did wrong!")
            if guesses == 5:
                print("You lost your whole 5 chance for guessing!")
                break

    