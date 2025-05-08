import random

def welcome():
    print("Welcome to the 'Guess the Number' game!")
    print("I'll think of a number, and you try to guess it.")
    print("Choose a difficulty level:")
    print("1 - Easy (number between 1 and 10)")
    print("2 - Medium (number between 1 and 50)")
    print("3 - Hard (number between 1 and 100)")

def get_level():
    while True:
        choice = input("Your choice (1/2/3): ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 50
        elif choice == '3':
            return 100
        else:
            print("Please enter 1, 2, or 3.")

def play_game(max_number):
    secret = random.randint(1, max_number)
    attempts = 0

    print(f"\nI've chosen a number between 1 and {max_number}. Try to guess it!")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < secret:
                print("My number is higher.")
            elif guess > secret:
                print("My number is lower.")
            else:
                print(f"Congratulations! You guessed the number {secret} in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    welcome()
    max_num = get_level()
    play_game(max_num)

    while True:
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again == "yes":
            main()
            break
        elif again == "no":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please answer 'yes' or 'no'.")

main()

# 1000-7
# 993-7
