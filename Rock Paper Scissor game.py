import tkinter as tk
import random


def determine_winner(player_choice):
    global player_score, computer_score, round_count

    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        result.set("It's a tie! Computer chose " + computer_choice)
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
            (player_choice == "Paper" and computer_choice == "Rock") or \
            (player_choice == "Scissors" and computer_choice == "Paper"):
        result.set("You win this round! Computer chose " + computer_choice)
        player_score += 1
    else:
        result.set("You lose this round! Computer chose " + computer_choice)
        computer_score += 1

    # Update scores
    score.set(f"Player: {player_score} | Computer: {computer_score}")
    round_count += 1
    round.set(f"Round {round_count}")


    if round_count > 5:
        if player_score > computer_score:
            result.set("Game Over! You won the game!")
        elif computer_score > player_score:
            result.set("Game Over! The computer won the game!")
        else:
            result.set("Game Over! It's a tie!")

        # Disable buttons after the game is over
        rock_button.config(state="disabled")
        paper_button.config(state="disabled")
        scissors_button.config(state="disabled")


# reset the game
def reset_game():
    global player_score, computer_score, round_count
    player_score = 0
    computer_score = 0
    round_count = 1
    score.set(f"Player: {player_score} | Computer: {computer_score}")
    round.set(f"Round {round_count}")
    result.set("")

    # Re-enable buttons
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")


# application window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize score 
player_score = 0
computer_score = 0
round_count = 1

# Result display 
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=('Helvetica', 14), pady=10)
result_label.pack()

# Score displa
score = tk.StringVar()
score.set(f"Player: {player_score} | Computer: {computer_score}")
score_label = tk.Label(root, textvariable=score, font=('Helvetica', 14))
score_label.pack()

# Round display 
round = tk.StringVar()
round.set(f"Round {round_count}")
round_label = tk.Label(root, textvariable=round, font=('Helvetica', 14), pady=10)
round_label.pack()

# Buttons for Rock, Paper, Scissors
button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", width=15, command=lambda: determine_winner("Rock"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(button_frame, text="Paper", width=15, command=lambda: determine_winner("Paper"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=15, command=lambda: determine_winner("Scissors"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Reset button
reset_button = tk.Button(root, text="Restart Game", width=15, command=reset_game)
reset_button.pack(pady=20)


root.mainloop()
