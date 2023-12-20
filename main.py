from player import *
from board import *
from db import *
from game import Game
# from src.ihm import Ihm

# grille = Grid(10,10) #taille maximale pour le moment, il faut optimiser la taille dans la méthode de la classe Grid
# grille.create_boardgame()

# Création de l'interface utilisateur avec une fenêtre de 800x600
# if __name__ == "__main__":
#     interface = Ihm(1100, 800)
#     interface.afficher_board()

if __name__ == "__main__":

    # Initialisation du jeu et des objets board, game et players

    nb_player = int(input(
        "Combien de joueurs souhaitez-vous créer pour cette partie? (5 joueurs max)"))

    boardgame = Board(12, 12, nb_player)
    title = boardgame.show_title()
    print(title)

    while nb_player != "1" and nb_player != "2" and nb_player != "3" and nb_player != "4" and nb_player != "5":
        nb_player = input("Nombre de joueur : (max 5) ")

    players = Player(12, 12, int(nb_player))

    # players.print_players()
    player_turn = 0

    boardgame.create_boardgame()
    score_result = boardgame.update_score()
    print(score_result)
    players.show_available_cells()
    boardgame.ask_question()
    game = Game(int(nb_player), boardgame)


# while players.game_continue():
while players:

    # Affiche la grille
    print(title)
    boardgame.create_boardgame()

    # Affiche le score des joueurs
    players.update_score()

    # Lance un dé pour sélectionner les cases disponibles pour le déplacement
    dice = players.roll_dice()
    players.show_available_cells()

    # Affichage des possibilités de déplacement, déplacement joueur et affichage grille
    players.move()

    # Pose une question au joueur
    boardgame.ask_question()

    # Affichage et mise à jour du score
    players.update_score()

    # Joueur suivant
    game.next_player()
