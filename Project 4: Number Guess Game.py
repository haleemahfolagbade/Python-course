import random

def generate_random_number(level): # to define the random numbers based on the difficulty_level
    if level == "easy":
        return random.randint(1, 50)
    elif level == "medium":
        return random.randint(1, 100)
    else:
        return random.randint(1, 200)

def check_guesses(user_guess, number): # to compare user guesses to the random number
    if user_guess < number:
        return "Your guess is too low"
    elif user_guess > number:
        return "Your guess is too high"
    else:
        return "Congratulations, you've guessed it!"

def play_game():
    level = input("Choose difficulty level (easy, medium, hard): ").lower()
    attempts = 10 if level == "easy" else 7 if level == "medium" else 5
    random_number = generate_random_number(level)
    score = 0

    while attempts > 0:
        user_guess = int(input("Enter your guess: "))
        attempts -=1
        result = check_guesses(user_guess, random_number)
        print(result)
        if result == "Congratulations, you've guessed it!":
            score += 50 # add score for each correct response
            break
        

    if attempts == 0 and not result == "Congratulations, you've guessed it!":
        print(f"You're out of tries. The correct number was {random_number}.")
    print(f"Your final score is: {score}.")

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? Enter 'yes' or 'no'): ").lower()

        if replay != "yes":
            print("Thanks for playing!")
            break

    
main() # always invoke the last function to run every function