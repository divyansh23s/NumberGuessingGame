from datetime import datetime

def save_score(level, remaining_attempts):
    with open("data/scores.txt","a") as file:
        file.write(
            f"{datetime.now()} | Level: {level} | Remaining Attempts: {remaining_attempts}\n"
        )