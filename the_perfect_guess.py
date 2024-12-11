from random import randint

number = randint( 1 , 100 )
guesses = 1

while True :
    user_guess = int( input(" Guess a number between 1 and 100 : ") )
    if user_guess == number :
        break
    elif user_guess > number :
        print(" Too high ")
        guesses += 1
    elif user_guess < number :
        print(" Too low ")
        guesses += 1
    else :
        print(" Invalid input ")
        break

print(f" You guessed it right in {guesses} guesses ")
