import tkinter as tk
from tkinter import messagebox
import random

# ------------------- Main Game Logic -------------------
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# ------------------- UI Logic -------------------
def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    user_label.config(text=f"🧍 You chose: {user_choice.capitalize()}")
    comp_label.config(text=f"💻 Computer chose: {computer_choice.capitalize()}")
    result_label.config(text=result)

    # Optional popup
    messagebox.showinfo("Result", f"You: {user_choice}\nComputer: {computer_choice}\n\n{result}")

def reset_game():
    user_label.config(text="🧍 You chose: ")
    comp_label.config(text="💻 Computer chose: ")
    result_label.config(text="Result will appear here!")

# ------------------- Tkinter Window Setup -------------------
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x450")
root.config(bg="#282C34")

title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 18, "bold"), bg="#282C34", fg="white")
title_label.pack(pady=15)

frame = tk.Frame(root, bg="#282C34")
frame.pack(pady=20)

# Buttons for User Choices
rock_btn = tk.Button(frame, text="🪨 Rock", font=("Arial", 14), bg="#61AFEF", fg="white", width=10, command=lambda: play('rock'))
paper_btn = tk.Button(frame, text="📄 Paper", font=("Arial", 14), bg="#98C379", fg="white", width=10, command=lambda: play('paper'))
scissors_btn = tk.Button(frame, text="✂ Scissors", font=("Arial", 14), bg="#E06C75", fg="white", width=10, command=lambda: play('scissors'))

rock_btn.grid(row=0, column=0, padx=10, pady=10)
paper_btn.grid(row=0, column=1, padx=10, pady=10)
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

# Labels to Show Choices and Result
user_label = tk.Label(root, text="🧍 You chose: ", font=("Arial", 12), bg="#282C34", fg="white")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="💻 Computer chose: ", font=("Arial", 12), bg="#282C34", fg="white")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="Result will appear here!", font=("Arial", 14, "bold"), bg="#282C34", fg="#FFD700")
result_label.pack(pady=20)

# Reset Button
reset_btn = tk.Button(root, text="🔄 Reset", font=("Arial", 12), bg="#C678DD", fg="white", width=10, command=reset_game)
reset_btn.pack(pady=10)

# Exit Button
exit_btn = tk.Button(root, text="❌ Exit", font=("Arial", 12), bg="#BE5046", fg="white", width=10, command=root.destroy)
exit_btn.pack(pady=5)

root.mainloop()
import tkinter as tk
from tkinter import messagebox
import random

# ------------------- Main Game Logic -------------------
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# ------------------- UI Logic -------------------
def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    user_label.config(text=f"🧍 You chose: {user_choice.capitalize()}")
    comp_label.config(text=f"💻 Computer chose: {computer_choice.capitalize()}")
    result_label.config(text=result)

    # Optional popup
    messagebox.showinfo("Result", f"You: {user_choice}\nComputer: {computer_choice}\n\n{result}")

def reset_game():
    user_label.config(text="🧍 You chose: ")
    comp_label.config(text="💻 Computer chose: ")
    result_label.config(text="Result will appear here!")

# ------------------- Tkinter Window Setup -------------------
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x450")
root.config(bg="#282C34")

title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 18, "bold"), bg="#282C34", fg="white")
title_label.pack(pady=15)

frame = tk.Frame(root, bg="#282C34")
frame.pack(pady=20)

# Buttons for User Choices
rock_btn = tk.Button(frame, text="🪨 Rock", font=("Arial", 14), bg="#61AFEF", fg="white", width=10, command=lambda: play('rock'))
paper_btn = tk.Button(frame, text="📄 Paper", font=("Arial", 14), bg="#98C379", fg="white", width=10, command=lambda: play('paper'))
scissors_btn = tk.Button(frame, text="✂ Scissors", font=("Arial", 14), bg="#E06C75", fg="white", width=10, command=lambda: play('scissors'))

rock_btn.grid(row=0, column=0, padx=10, pady=10)
paper_btn.grid(row=0, column=1, padx=10, pady=10)
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

# Labels to Show Choices and Result
user_label = tk.Label(root, text="🧍 You chose: ", font=("Arial", 12), bg="#282C34", fg="white")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="💻 Computer chose: ", font=("Arial", 12), bg="#282C34", fg="white")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="Result will appear here!", font=("Arial", 14, "bold"), bg="#282C34", fg="#FFD700")
result_label.pack(pady=20)

# Reset Button
reset_btn = tk.Button(root, text="🔄 Reset", font=("Arial", 12), bg="#C678DD", fg="white", width=10, command=reset_game)
reset_btn.pack(pady=10)

# Exit Button
exit_btn = tk.Button(root, text="❌ Exit", font=("Arial", 12), bg="#BE5046", fg="white", width=10, command=root.destroy)
exit_btn.pack(pady=5)

root.mainloop()