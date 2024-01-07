from model.player import Player
from model.weapon import Weapon

kniffe = Weapon("Couteau", 5)

player1 = Player("Ashuka Dior", 20, 3)
player2 = Player("Louis Litt", 30, 4)

player1.attack_player(player2)
print("-Pseudo : ", player1.get_pseudo(), "\n-Point de vie : ", player1.get_health(), "\n-Attaaue : ", player1.get_attack())
print("\n*************************")
print("-Pseudo : ", player2.get_pseudo(), "\n-Point de vie : ", player2.get_health(), "\n-Attaaue : ", player2.get_attack())