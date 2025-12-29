def get_user_guess(max_number):
    while True:
        user_input = (input("Enter Your Guess: "))
        if(user_input.isdigit()):
            guess = int(user_input)
            if 1 <= guess <= max_number:
                return guess
            else:
                print(f"Please enter a number between 1 & {max_number}")
        
        else:
            print("Invalid input. Please enter a number.")