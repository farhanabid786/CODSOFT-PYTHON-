import random
import tkinter as tk
from tkinter import messagebox

# Function to determine the winner
def winner(user_choice, system_choice):
    if user_choice == system_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and system_choice == "Scissors") or \
         (user_choice == "Paper" and system_choice == "Rock") or \
         (user_choice == "Scissors" and system_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

# Function to handle the user's choice
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    system_choice = random.choice(choices)
    result = winner(user_choice, system_choice)
    result_label.config(text=f"You chose {user_choice}\nComputer chose {system_choice}\n\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create and place buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"))
rock_button.pack(side=tk.LEFT, padx=30, pady=30)

paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"))
paper_button.pack(side=tk.LEFT, padx=30, pady=30)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=30, pady=30)

# Add instructions
instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors to play against the computer.")
instructions.pack(pady=16)

# Add result label
result_label = tk.Label(root, text="", font=("Helvetica", 24))
result_label.pack(pady=30)

# Run the main loop
root.mainloop()