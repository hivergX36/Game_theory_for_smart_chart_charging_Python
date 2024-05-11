from Player import player
from Agent import agent
from Player import player

game1 = agent()
game1.read_data("data.txt")

game_player = [player for i in range(game1.nb_player)]
print(game_player)

