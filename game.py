import random
from player import Player
from board import Board


class Game:
    def __init__(self, numbers_of_players, boardgame):
        self.numbers_of_players = numbers_of_players
        # self.players = [Player(i, boardgame) for i in range(numbers_of_players)]
        self.players = []
        self.categories = ["⬛️", "🟩", "🟪", "🟨", "🟥", "🟦", "🟧"]
        self.perfect_score = [1, 2, 3, 4, 5, 6]
        self.actual_player = 0

    def next_player(self):
        self.actual_player += 1
        self.actual_player = self.actual_player % self.numbers_of_players

    def game_continue(self):
        for num_player in range(self.numbers_of_players):
            if (self.players[num_player].score == self.perfect_score):
                print("Bravo, " +
                      self.players[num_player].token + " gagne la parite !")
                return False
        return True

    def print_players(self):
        for player in self.players:
            print(player.name + " " + player.token)
