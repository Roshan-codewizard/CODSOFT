import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose again.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

    return winner

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 1

    while True:
        print(f"\nRound {rounds}:")
        result = play_round()

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

        rounds += 1

    print("\nFinal Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
