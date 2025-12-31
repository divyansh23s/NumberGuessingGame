from datetime import datetime
import os

def save_score(username, level, remaining_attempts):
    """
    Save player score with username to scores.txt
    
    Args:
        username: Name of the player
        level: Difficulty level (Easy, Medium, Hard)
        remaining_attempts: Number of attempts left when player won
    """
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    with open("data/scores.txt", "a") as file:
        file.write(
            f"{datetime.now()} | Username: {username} | Level: {level} | Remaining Attempts: {remaining_attempts}\n"
        )
