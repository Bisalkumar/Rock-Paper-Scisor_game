import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize global variables
choices = ('r', 'p', 's')
cPoints = 0
pPoints = 0
rounds = 0
mode = None
max_rounds = 0

def get_player2_choice():
    while True:
        choice = simpledialog.askstring("Player 2's Turn", "Choose either rock (r), paper (p), or scissors (s):").lower()
        if choice in choices:
            return choice
        else:
            messagebox.showwarning("Invalid Choice", "Please choose either 'r', 'p', or 's'.")


def play_game(player1_choice):
    global cPoints, pPoints, rounds

    rounds += 1
    if mode == "single":
        player2_choice = random.choice(choices)
    else:
        player2_choice = get_player2_choice()

    result = ""

    if player1_choice == player2_choice:
        result = "It's a tie!"
    elif (player1_choice == "r" and player2_choice == "s") or (player1_choice == "s" and player2_choice == "p") or (player1_choice == "p" and player2_choice == "r"):
        result = "Player 1 won!" if mode == "double" else "You won!"
        pPoints += 1
    else:
        result = "Player 2 won!" if mode == "double" else "Computer won!"
        cPoints += 1

    # Display result message
    if mode == "single":
        messagebox.showinfo("Result", f"Computer chose: {player2_choice}\n{result}\n\nYour score: {pPoints}\nComputer's score: {cPoints}")
    else:
        messagebox.showinfo("Result", f"Player 2 chose: {player2_choice}\n{result}\n\nPlayer 1 score: {pPoints}\nPlayer 2 score: {cPoints}")
    
    if rounds == max_rounds:
        display_final_result()
        app.quit()

def display_final_result():
    if pPoints > cPoints:
        winner = "Player 1" if mode == "double" else "You"
        final_result = f"{winner} won the game!"
    elif pPoints < cPoints:
        winner = "Player 2" if mode == "double" else "Computer"
        final_result = f"{winner} won the game!"
    else:
        final_result = "It's a draw!"

    messagebox.showinfo("Game Over", f"Final Score\n\nPlayer 1 score: {pPoints}\nPlayer 2 score: {cPoints}\n\n{final_result}")

def show_game_interface():
    game_frame = tk.Frame(app)
    game_frame.pack(padx=10, pady=10)

    label = tk.Label(game_frame, text=f"Playing {'against Computer' if mode == 'single' else 'Player 1 vs Player 2'}", font=("Arial", 14))
    label.grid(row=0, columnspan=3, pady=10)

    btn_rock = tk.Button(game_frame, text="Rock", width=20, height=2, command=lambda: play_game('r'))
    btn_rock.grid(row=1, column=0, padx=5, pady=5)

    btn_paper = tk.Button(game_frame, text="Paper", width=20, height=2, command=lambda: play_game('p'))
    btn_paper.grid(row=1, column=1, padx=5, pady=5)

    btn_scissors = tk.Button(game_frame, text="Scissors", width=20, height=2, command=lambda: play_game('s'))
    btn_scissors.grid(row=1, column=2, padx=5, pady=5)

def start_game():
    global mode, max_rounds

    mode = mode_var.get()

    try:
        max_rounds = int(rounds_entry.get())
        if max_rounds <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive integer for the number of rounds.")
        return

    start_frame.destroy()
    show_game_interface()

app = tk.Tk()
app.title("Rock Paper Scissors Game")

mode_var = tk.StringVar()
mode_var.set("single")

start_frame = tk.Frame(app)
start_frame.pack(padx=10, pady=10)

label = tk.Label(start_frame, text="Select Game Mode", font=("Arial", 14))
label.grid(row=0, columnspan=2, pady=10)

single_player_radio = tk.Radiobutton(start_frame, text="Single Player (vs. Computer)", variable=mode_var, value="single")
single_player_radio.grid(row=1, column=0, pady=5)

double_player_radio = tk.Radiobutton(start_frame, text="Double Player", variable=mode_var, value="double")
double_player_radio.grid(row=1, column=1, pady=5)

rounds_label = tk.Label(start_frame, text="Enter the number of rounds to play:")
rounds_label.grid(row=2, column=0, padx=5)

rounds_entry = tk.Entry(start_frame)
rounds_entry.grid(row=2, column=1, padx=5)

start_button = tk.Button(start_frame, text="Start Game", command=start_game)
start_button.grid(row=3, columnspan=2, pady=10)

app.mainloop()
