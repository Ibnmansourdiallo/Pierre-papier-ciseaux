import tkinter as tk
import random

# Initialisation de la fenêtre de jeu
root = tk.Tk()
root.title("Pierre-Papier-Ciseaux")
root.geometry("300x200")
root.configure(bg="lightblue")

# Créer une étiquette pour le titre du jeu et l'afficher
title_label = tk.Label(root, text="Jeu Pierre-Papier-Ciseaux", font=("Arial", 16), bg="lightblue")
title_label.pack(pady=10)

# Inviter l'utilisateur à choisir entre pierre, papier ou ciseaux
prompt_label = tk.Label(root, text="Choisissez : Pierre, Papier ou Ciseaux", bg="lightblue")
prompt_label.pack()

# Champ de saisie pour que l'utilisateur puisse saisir son choix
user_choice = tk.StringVar()
entry = tk.Entry(root, textvariable=user_choice)
entry.pack(pady=5)

# Générer une sélection aléatoire pour l'ordinateur
def computer_choice():
    return random.choice(['Pierre', 'Papier', 'Ciseaux'])

# Définir les fonctions pour la logique du jeu
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Égalité !"
    elif (user_choice == 'Pierre' and comp_choice == 'Ciseaux') or \
         (user_choice == 'Papier' and comp_choice == 'Pierre') or \
         (user_choice == 'Ciseaux' and comp_choice == 'Papier'):
        return f"Vous gagnez ! L'ordinateur a choisi {comp_choice}."
    else:
        return f"Vous perdez ! L'ordinateur a choisi {comp_choice}."

def play():
    user_pick = user_choice.get()
    comp_pick = computer_choice()
    result.set(determine_winner(user_pick, comp_pick))

# Fonction pour réinitialiser le jeu
def Reset():
    user_choice.set("")
    result.set("")

# Fonction pour quitter le jeu
def Exit():
    root.destroy()

# Boutons pour jouer, réinitialiser et quitter
play_button = tk.Button(root, text="Jouer", command=play)
play_button.pack(pady=5)

reset_button = tk.Button(root, text="Réinitialiser", command=Reset)
reset_button.pack(pady=5)

quit_button = tk.Button(root, text="Quitter", command=Exit)
quit_button.pack(pady=5)

# Variable pour afficher le résultat
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, bg="lightblue")
result_label.pack(pady=10)

# Exécuter l'application
root.mainloop()
