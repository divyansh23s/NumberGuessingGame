import random
from game.input_handler import get_user_guess
from game.hints import give_hint
from game.score import save_score

def choose_difficulty():
    print("\nchoose Difficulty:")
    print("1. Easy")
    print("2. Medium:")
    print("3. Hard:")

    choice = input("enter any choice 1/2/3: ")

    if choice == 1:
        return 50,10, "Easy"
    elif choice == "2":
        return 100, 7, "Medium"
    else:
        return 200, 5, "Hard"

def start_game():
    max_number,attempts,level = choose_difficulty()

    number = random.randint(1,max_number)
    
    print(f"\nDifficulty: {level}")
    print(f"I have selected a number between 1 and {max_number}.")
    print(f"You have {attempts} attempts.\n")

    while attempts > 0:
        guess = get_user_guess(max_number)
        attempts -= 1

        if guess == number:
            print("🎉 Congratulations! You guessed the correct number.")
            save_score(level, attempts + 1)

            return

        else:
            give_hint(guess,number)
            print(f"Attempts left: {attempts}\n")

    print(f"❌ Game Over! The correct number was {number}.")

