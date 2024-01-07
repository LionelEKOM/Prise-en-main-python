from typing import Any

#Declaration d'une classe
class Player:

    # #Attributs declaration
    # pseudo = "Ashuka"
    # health = 20
    # attack = 3

    #Declaration du constructeur, c'est une methode qui octroie des caracteristiques par defauts a un objet lors de ca creation
    def __init__(self, pseudo, health, attack) -> None:
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenu au joueur ", pseudo, "/ Point de vie : ", health, "/ Attaque : ", attack)

    #Definission des Getters pour pouvoir recuperer les valeurs
    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    #D'autres fonctions ou setters
    def damage(self, damage):
        self.health -= damage
        print("Aie...vous vennez de subir", damage, "degats !!")
    
    def attack_player(self, target_player):
        target_player.damage(self.attack)

class Warrios(Player):

    def __init__(self, pseudo, health, attack) -> None:
        super().__init__(pseudo, health, attack)
        self.armor = 3
    
    #D'autres fonctions ou setters
    def damage(self, damage):
        
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        super().damage(damage)

    def blade(self):
        self.armor = 3
        print("Les pnts d'armur ont ete recharges !!")

    def get_armor_point(self):
        return self.armor

warrior = Warrios("Stephen Curry", 50, 5)
warrior.damage(4)
print("-Vie : ", warrior.get_health(), "\n-Armure : ", warrior.get_armor_point())