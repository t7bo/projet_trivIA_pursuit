from board import *


class Player(Board):

    def __init__(self, width, height, number_of_players):

        super().__init__(width, height, number_of_players)

        self.user_answer

        tokens = ["🦊", "🐨", "🐼", "🐸", "🐱"]
        self.name = input(f"What's your name?: ")
        self.token = random.choice(tokens)
        # self.score = [0,0,0,0,0,0]
        self.x = 6
        self.y = 6
        # self.new_x = 0
        # self.new_y = 0
        self.number_of_players = number_of_players
        # self.board = board
        self.players = []
        self.score = []
        self.dico_score = {}
        self.grid

    def roll_dice(self):
        dice = random.randint(1, 7)
        return dice

    def show_available_cells(self, dice_number):

        self.dice_number = dice_number

        dico_available_cells = {}
        set_cells = {}

        past_color = self.grid[self.row][self.col]
        future_color = self.grid[self.row - self.dice_number][self.col]

        # ABOVE

        # possibilité dans la même colonne (plus haut)

        # déplacement normal sur les cellules au dessus (indices de lignes inférieurs)
        if self.grid[self.col][self.row-1] != "⬛️":
            if self.row - self.dice_number >= 0:
                # print(f"{(self.row - dice_number, self.col)}")
                set_cells.add((self.row - self.dice_number, self.col))
                future_color = self.grid[self.row - self.dice_number][self.col]

        if self.grid[self.col-1][self.row] != "⬛️":
            if self.col < self.height:
                # print(f"{self.row, (self.col + dice_number)}")
                set_cells.add((self.row, (self.col + self.dice_number)))
            else:
                # print(f"{self.row, (self.col - dice_number)}")
                set_cells.add((self.row, (self.col - self.dice_number)))

            difference = abs(self.dice_number - self.col)
            # difference = dice_number - self.col

            if (self.width-self.col)-(difference-self.row) < self.width:
                set_cells.add((self.row+difference, 0))
                # print(f"{(self.row+difference, 0)}")

            if self.row < self.height and self.width-(self.row+difference) < self.height:
                set_cells.add((self.row+difference, 0))
                # print(f"{(self.row+difference, 0)}")
                # print(f"{(self.col, self.width-(self.row+difference))}")

        # si jamais on arrive à la toute première ligne, on peut virer à gauche et à droite
        if self.row - self.dice_number < 0:  # and self.row != 6:

            difference = self.dice_number - self.row

            self.col_right = self.col + difference
            self.col_left = self.col - difference

            if self.width > self.col_right > 0:
                set_cells.add((0, self.col_right))
                # print(f"{(0, self.col_right)}") # possibilité à droite

            if self.col_left > 0:
                set_cells.add((0, self.col_left))
                # print(f"{(0, self.col_left)}") # possibilité à gauche

        # BELOW

        if self.row < self.height-1:
            if self.grid[self.col][self.row+1] != "⬛️" and self.row < self.height:
                if self.row + self.dice_number <= self.height:
                    set_cells.add((self.row + self.dice_number, self.col))
                    # print(f"{(self.row + dice_number, self.col)}")

            if self.row + self.dice_number > self.width and self.grid[self.col][self.row+1] != "⬛️":

                difference = (self.dice_number + self.row) - self.width

                # self.row = 12
                self.col_right = self.col + difference
                self.col_left = self.col - difference

                if self.width > self.col_right > 0:
                    set_cells.add((12, self.col_right))
                    # print(f"{(12, self.col_right)}") # possibilité à droite

                if self.col_left > 0:
                    set_cells.add((12, self.col_left))
                    # print(f"{(12, self.col_left)}") # possibilité à gauche

        # Proposer un dictionnaire de choix pour les coordonnées possibles à l'utilisateur
        j = 0
        for i in set_cells:
            j += 1
            dico_available_cells[j] = i

        for i, j in dico_available_cells.items():
            print(f"Choix {i} : {j}")

        user_choice = int(input(
            "Merci de taper le chiffre correspondant à la case où vous souhaitez vous déplacer : "))
        print(f"Vous avez choisi cette destination : {user_choice}")

        # récupère les coordonnées choisies par notre joueur
        return dico_available_cells[user_choice]

    def move(self, grid):

        if self.row == 6 and self.col == 6:
            self.grid[self.row][self.col] = "⬜️"
        else:
            self.grid[self.row][self.col] = color

        future_cell = self.show_available_cells()
        new_row, new_col = future_cell[0], future_cell[1]

        color = self.grid[new_row][new_col]  # cell where player will go
        color

        # remplacer la couleur par l'émoji du joueur
        self.grid[self.row][self.col] = self.token

        # return grid

    def update_score(self):

        self.ask_question()

        # besoin de la variable nombre_de_joueurs pour générer leurs scores respectifs

        for i in range(1, self.number_of_players+1):
            self.dico_score.update(
                {f"player {i} : {self.name}, {self.token}": self.score})

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


# taille maximale pour le moment, il faut optimiser la taille dans la méthode de la classe Grid
# boardgame = Board(12, 12)
# title = boardgame.show_title()
# print(title)
# boardgame.create_boardgame()
# score_result = players.update_score()
# print(score_result)
# players.show_available_cells()
# boardgame.ask_question()
