import random
import pandas as pd
# from src.game import *
from db import *


class Board():

    def __init__(self, width, height, number_of_players):
        super().__init__
        self.width = width
        self.height = height
        self.col = int(width/2)
        self.row = int(height/2)
        self.user_answer = 0
        self.correct_answer = 0
        # self.score = []
        # self.dico_score = {}
        # self.numbers_of_players = number_of_players
        self.row = [str(i+1) for i in range(0, self.width+1)]
        self.grid = [list(self.row) for j in range(0, self.height+1)]

    def create_boardgame(self):

        # Création des lignes (avec des nombres de 1 à 11)
        row = [str(i+1) for i in range(0, self.width+1)]

        # Création de la grille (ajout de colonnes)
        grid = [list(row) for j in range(0, self.height+1)]
        self.grid = grid

        # Ajout de valeurs 0 "False" sur lesquelles on ne peut pas jouer
        for i in range(1, 12):  # ce range = columns
            for index in range(1, 6):
                grid[i][index] = "0"
            for index in range(7, 12):
                grid[i][index] = "0"

        # Dictionnaire des catégories avec leurs couleurs correspondantes
        categories = {"0": [0, "⬛️", 0],
                      "1": ["python", "🟩", 1],
                      "2": ["sql", "🟪", 2],
                      "3": ["git", "🟨", 3],
                      "4": ["terminal", "🟥", 4],
                      "5": ["actu_ia", "🟦", 5],
                      "6": ["soft_skills", "🟧", 6],
                      "7": ["python", "🟩", 1],
                      "8": ["soft_skills", "🟧", 6],
                      "9": ["actu_ia", "🟦", 5],
                      "10": ["terminal", "🟥", 4],
                      "11": ["git", "🟨", 3],
                      "12": ["sql", "🟪", 2],
                      "13": ["python", "🟩", 1],
                      "14": ["start", "⬜️", 0]}

        # Modification de la ligne du milieu de la grille
        grid[6] = grid[0].copy()

        # Modification des colonnes 0, 5 et -1
        # (elles affichaient une seule et unique valeur, maintenant elles s'affichent comme les lignes)
        for row_index in range(len(grid)):
            grid[row_index][0] = str(row_index + 1)
            grid[row_index][-1] = str(row_index + 1)
            grid[row_index][6] = str(row_index + 1)

        # Modification des nombres dans la grille avec les couleurs correspondantes
        for row in grid:
            for col_index in range(len(row)):
                number = row[col_index]
                if number in categories:
                    row[col_index] = categories[number][1]

        # DIAGONALES
        # Création des diagonales
        for i in range(1, 12):
            grid[i][i] = categories[str(i+1)][1]
            grid[i][self.width - i] = categories[str(self.width - i + 1)][1]

        # Modification du centre de la grille    #START
        grid[6][6] = categories["14"][1]

        # test d'affichage
        # old_value = grid[7][12]
        # #grid[7][12] = "X"
        # old_value

        # Affichage de la grille
        for row in grid:
            print("".join(row))

    def show_title(self):
        return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       TRIVIA PURSUIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    def ask_question(self):

        self.ids = []  # à mettre dans le init de la classe

        self.score = ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]

        self.categories = {"0": [0, "⬛️", 0],
                           "1": ["python", "🟩"],
                           "2": ["sql", "🟪"],
                           "3": ["git", "🟨"],
                           "4": ["terminal", "🟥"],
                           "5": ["actu_ia", "🟦"],
                           "6": ["soft_skills", "🟧"],
                           "7": ["python", "🟩"],
                           "8": ["soft_skills", "🟧"],
                           "9": ["actu_ia", "🟦"],
                           "10": ["terminal", "🟥"],
                           "11": ["git", "🟨"],
                           "12": ["sql", "🟪"],
                           "13": ["python", "🟩"],
                           "14": ["start", "⬜️"]}

        # categories["1"][0]

        # retourne la catégorie de la case sur laquelle le joueur se trouve
        categ = self.categories[str(self.col)][0]

        dictionnaire_avec_question = read_table(categ, self.ids)
        # print(dictionnaire_avec_question)
        self.ids.append(dictionnaire_avec_question["id"])

        # afficher la question (sortie de manière aléatoire via SQL)
        print(dictionnaire_avec_question["question"])

        # randomiser et afficher les réponses (pour éviter que ce soit toujours la réponse A la réponse correcte)
        i = 0
        for j in random.sample(["correct_answer", "incorrect_answer_1", "incorrect_answer_2", "incorrect_answer_3"], 4):
            i += 1
            print(f"{i}. {dictionnaire_avec_question[j]}")

            if j == "correct_answer":
                self.correct_number = i

        # demander de choisir une réponse à l'utilisateur
        self.user_answer = input(
            "Merci de taper le chiffre correspondant à la réponse que vous souhaitez donner : ")

        if int(self.user_answer) == self.correct_number:

            print("Bravo! Bonne réponse")

            if self.categories[str(self.col)][1] not in self.score:
                self.score = self.score.pop()
                self.score = self.score.append(
                    self.categories[str(self.col)][1])
            else:
                pass

        else:

            print("Raté.")

        self.update_score()

    def update_score(self):

        self.ask_question()

        # besoin de la variable nombre_de_joueurs pour générer leurs scores respectifs

        for i in range(1, self.number_of_players+1):
            self.dico_score.update({f"player {i}": self.score})

        for i in self.dico_score:
            while len(self.dico_score[i]) < 6:
                self.dico_score[i].append("⬛️")

        if int(self.user_answer) == self.correct_number and self.categories[str(self.col)][1] not in self.score:
            self.score.pop()
            # remplace une case noire par la couleur gagnée en 1ère position dans la liste
            self.score.insert(0, self.categories[str(self.col)][1])

        else:
            pass

        print(f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    CLASSEMENT DES JOUEURS
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

        for key, value in self.dico_score.items():
            print(f"{key} : {''.join(value)}")
