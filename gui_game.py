import tkinter as tk
import random
import sys
from game.score import save_score

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
    username = ""

    def center_window(width=None, height=None):
        """Center the window on screen"""
        if width is None or height is None:
            app.update_idletasks()
            width = app.winfo_width()
            height = app.winfo_height()
        x = (app.winfo_screenwidth() // 2) - (width // 2)
        y = (app.winfo_screenheight() // 2) - (height // 2)
        app.geometry(f"{width}x{height}+{x}+{y}")

    def login_user():
        """Handle user login/name input"""
        global username
        entered_username = username_entry.get().strip()
        
        if not entered_username:
            username_label.config(text="Please enter your name!", fg="white")
            return
        
        username = entered_username
        
        # Hide login screen
        for widget in login_frame.winfo_children():
            widget.destroy()
        login_frame.pack_forget()
        
        # Show difficulty selection screen
        show_difficulty_selection()

    def show_difficulty_selection():
        """Show difficulty selection screen"""
        global difficulty_frame
        difficulty_frame = tk.Frame(app)
        difficulty_frame.pack(pady=30)
        
        welcome_label = tk.Label(difficulty_frame, text=f"Welcome, {username}!", font=("Arial", 12, "bold"))
        welcome_label.pack(pady=5)
        
        tk.Label(difficulty_frame, text="Choose Difficulty", font=("Arial", 14, "bold")).pack(pady=15)
        
        # Use consistent width for all buttons (width in characters)
        button_width = 30
        
        easy_btn = tk.Button(difficulty_frame, text="Easy (1-50, 10 attempts)", 
                             command=lambda: choose_difficulty("Easy"), width=button_width)
        easy_btn.pack(pady=8)
        
        medium_btn = tk.Button(difficulty_frame, text="Medium (1-100, 7 attempts)", 
                               command=lambda: choose_difficulty("Medium"), width=button_width)
        medium_btn.pack(pady=8)
        
        hard_btn = tk.Button(difficulty_frame, text="Hard (1-200, 5 attempts)", 
                             command=lambda: choose_difficulty("Hard"), width=button_width)
        hard_btn.pack(pady=8)
        
        # Resize window for difficulty selection screen
        center_window(400, 350)

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

        entry = tk.Entry(game_frame, width=20)
        entry.pack(pady=5)
        entry.focus()

        button = tk.Button(game_frame, text="Guess", command=check_guess, width=15)
        button.pack(pady=5)
        
        entry.bind('<Return>', lambda event: check_guess())

        result = tk.StringVar()
        tk.Label(game_frame, textvariable=result, fg="white").pack(pady=5)

        attempts_label = tk.StringVar(value=f"Attempts left: {attempts}")
        tk.Label(game_frame, textvariable=attempts_label).pack(pady=5)
        
        # Resize window for game screen
        center_window(400, 300)

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
            # Save score with username
            save_score(username, level, attempts)
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
    app.resizable(False, False)  # Prevent window resizing
    
    # Set initial window size for login screen (larger size)
    center_window(450, 320)
    
    # Login screen (first screen)
    login_frame = tk.Frame(app)
    login_frame.pack(pady=40)
    
    tk.Label(login_frame, text="Enter Your Name", font=("Arial", 14, "bold")).pack(pady=15)
    
    username_entry = tk.Entry(login_frame, width=25)
    username_entry.pack(pady=10)
    username_entry.focus()
    
    username_label = tk.Label(login_frame, text="", fg="white")
    username_label.pack(pady=5)
    
    login_btn = tk.Button(login_frame, text="Start Game", command=login_user, width=30)
    login_btn.pack(pady=10)
    
    # Allow Enter key to login
    username_entry.bind('<Return>', lambda event: login_user())

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
