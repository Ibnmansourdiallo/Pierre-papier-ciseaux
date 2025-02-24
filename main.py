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

comp_pick = computer_choice()

# Exécuter l'application
root.mainloop()
