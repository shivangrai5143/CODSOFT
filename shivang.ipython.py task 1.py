
# ROCK-PAPER AND SCISSORS GAME PLAY


import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nLet's play Rock, Paper, Scissors!")
        print("Type 'rock', 'paper', or 'scissors' to make your choice.")

        user_choice = input("Your choice: ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            user_choice = input("Your choice: ").lower()

        computer_choice = get_computer_choice()
        print(f"\nComputer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            print("Invalid input. Please try again.")
            play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again == "no":
            break

    print("\nThanks for playing!")

play_game()