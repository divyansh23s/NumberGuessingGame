import tkinter as tk
import random
import sys

try:
    DIFFICULTIES = {
        "Easy": (50, 10),
        "Medium": (100, 7),
        "Hard": (200, 5)
    }
    
    number = None
    max_number = 100
    attempts = 7
    level = "Medium"

    def choose_difficulty(difficulty):
        """Set game parameters based on difficulty choice"""
        global max_number, attempts, level, number
        level = difficulty
        max_number, attempts = DIFFICULTIES[difficulty]
        number = random.randint(1, max_number)
        
        # Hide difficulty selection screen
        for widget in difficulty_frame.winfo_children():
            widget.destroy()
        difficulty_frame.pack_forget()
        
        # Show game screen
        start_game()

    def start_game():
        """Initialize and display the game screen"""
        global entry, button, result, attempts_label, game_frame
        
        game_frame = tk.Frame(app)
        game_frame.pack(pady=20)
        
        title_label = tk.Label(game_frame, text=f"Difficulty: {level}", font=("Arial", 12, "bold"))
        title_label.pack(pady=5)
        
        range_label = tk.Label(game_frame, text=f"Guess a number (1-{max_number})")
        range_label.pack(pady=10)

        entry = tk.Entry(game_frame)
        entry.pack(pady=5)
        entry.focus()

        button = tk.Button(game_frame, text="Guess", command=check_guess)
        button.pack(pady=5)
        
        entry.bind('<Return>', lambda event: check_guess())

        result = tk.StringVar()
        tk.Label(game_frame, textvariable=result).pack(pady=5)

        attempts_label = tk.StringVar(value=f"Attempts left: {attempts}")
        tk.Label(game_frame, textvariable=attempts_label).pack(pady=5)

    def check_guess():
        global attempts
        guess = entry.get()

        if not guess.isdigit():
            result.set("Enter a valid number")
            return

        guess = int(guess)
        
        if guess < 1 or guess > max_number:
            result.set(f"Please enter a number between 1 and {max_number}")
            return

        attempts -= 1

        if guess == number:
            result.set("🎉 You Win!")
            button.config(state="disabled")
            entry.config(state="disabled")
        elif attempts <= 0:
            result.set(f"❌ Game Over! Number was {number}")
            button.config(state="disabled")
            entry.config(state="disabled")
        elif guess > number:
            result.set("Too High!")
        else:
            result.set("Too Low!")

        attempts_label.set(f"Attempts left: {attempts}")

    # Create the main window
    app = tk.Tk()
    app.title("Number Guessing Game")
    
    # Center the window
    app.update_idletasks()
    width = 350
    height = 300
    x = (app.winfo_screenwidth() // 2) - (width // 2)
    y = (app.winfo_screenheight() // 2) - (height // 2)
    app.geometry(f"{width}x{height}+{x}+{y}")

    # Difficulty selection screen
    difficulty_frame = tk.Frame(app)
    difficulty_frame.pack(pady=30)
    
    tk.Label(difficulty_frame, text="Choose Difficulty", font=("Arial", 14, "bold")).pack(pady=15)
    
    easy_btn = tk.Button(difficulty_frame, text="Easy (1-50, 10 attempts)", 
                         command=lambda: choose_difficulty("Easy"), width=25)
    easy_btn.pack(pady=8)
    
    medium_btn = tk.Button(difficulty_frame, text="Medium (1-100, 7 attempts)", 
                           command=lambda: choose_difficulty("Medium"), width=25)
    medium_btn.pack(pady=8)
    
    hard_btn = tk.Button(difficulty_frame, text="Hard (1-200, 5 attempts)", 
                         command=lambda: choose_difficulty("Hard"), width=25)
    hard_btn.pack(pady=8)

    # Bring window to front
    app.lift()
    app.attributes('-topmost', True)
    app.after_idle(app.attributes, '-topmost', False)

    app.mainloop()

except tk.TclError as e:
    print(f"Tkinter error: {e}")
    print("Make sure you have a display server running (X11 or native macOS display)")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
