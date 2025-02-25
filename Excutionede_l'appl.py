import tkinter as tk
import random

root = tk.Tk()
root.title("Jeu Pierre-Papier-Ciseaux")

choices = ["Pierre", "Papier", "Ciseaux"]

def check_winner(player, computer):
    if player == computer:
        return "Égalité !"
    elif (player == "Pierre" and computer == "Ciseaux") or \
         (player == "Ciseaux" and computer == "Papier") or \
         (player == "Papier" and computer == "Pierre"):
        return "Vous avez gagné !"
    else:
        return "Vous avez perdu !"

player_choice = tk.StringVar()
result = tk.StringVar()

def play(choice):
    player_choice.set(choice)
    computer_choice = random.choice(choices)
    result.set(f"Joueur : {choice} - Ordinateur : {computer_choice}\n{check_winner(choice, computer_choice)}")

def reset_game():
    player_choice.set("")
    result.set("")

def quit_game():
    root.quit()

tk.Label(root, text="Choisissez Pierre, Papier ou Ciseaux").pack()

tk.Button(root, text="Pierre", command=lambda: play("Pierre")).pack()
tk.Button(root, text="Papier", command=lambda: play("Papier")).pack()
tk.Button(root, text="Ciseaux", command=lambda: play("Ciseaux")).pack()

result_label = tk.Label(root, textvariable=result, font=("Arial", 12))
result_label.pack(pady=10)

play_button = tk.Button(root, text="PLAY", command=lambda: play(player_choice.get()))
play_button.pack(pady=5)

reset_button = tk.Button(root, text="RESET", command=reset_game)
reset_button.pack(pady=5)

exit_button = tk.Button(root, text="EXIT", command=quit_game)
exit_button.pack(pady=5)

root.mainloop()