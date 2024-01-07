maxtent = 3
Mp = input("Votre mot de passe (supérieur à 8 caractères) : ")

# Vérification de la longueur du mot de passe
while len(Mp) <= 8:
    print("Mot de passe incorrect ! Il doit contenir plus de 8 caractères.")
    Mp = input("Veuillez entrer un nouveau mot de passe : ")

print("Mot de passe correct !")

# Tentatives de connexion
tentative = 0

while True:
    user = input("Entrez votre username : ")
    login = input("Entrez votre mot de passe : ")

    if user == "Ashuka" and login == Mp:
        print(f"Authentification réussie !! Nombre de tentative : {tentative}")
        break
    else:
        print("Identifiants invalides !")
        tentative += 1

        if tentative == maxtent:
            print("Accès refusé. Au revoir !")
            break
