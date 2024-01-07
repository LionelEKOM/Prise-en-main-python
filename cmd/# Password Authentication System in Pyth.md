 # Système d'authentification par mot de passe en Python

Ce script Python implémente un système d'authentification par mot de passe simple. Il invite l'utilisateur à saisir un mot de passe, vérifie qu'il répond à certains critères, puis permet à l'utilisateur de se connecter avec un nom d'utilisateur et un mot de passe.

### Explication étape par étape

1. **Saisie et validation du mot de passe** :
    - Le script demande d'abord à l'utilisateur de saisir un mot de passe.
    - Il vérifie ensuite si le mot de passe comporte plus de 8 caractères. Si ce n'est pas le cas, il invite l'utilisateur à saisir un nouveau mot de passe jusqu'à ce que la condition soit remplie.

```python
maxtent = 3
Mp = input("Votre mot de passe (supérieur à 8 caractères) : ")

# Vérification de la longueur du mot de passe
while len(Mp) <= 8:
    print("Mot de passe incorrect ! Il doit contenir plus de 8 caractères.")
    Mp = input("Veuillez entrer un nouveau mot de passe : ")

print("Mot de passe correct !")
```

2. **Tentatives de connexion** :
    - Le script entre dans une boucle qui permet à l'utilisateur de saisir un nom d'utilisateur et un mot de passe.
    - Si le nom d'utilisateur est "Ashuka" et que le mot de passe correspond à celui saisi précédemment, le script imprime un message de réussite et sort de la boucle.
    - Si les informations d'identification ne sont pas valides, le script imprime un message d'erreur et incrémente le compteur « provisoire ».
    - Si le compteur `tentative` atteint le nombre maximum de tentatives (3 dans ce cas), le script imprime un message d'accès refusé et sort de la boucle.

```python
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
```

### Conclusion

This script demonstrates a basic password authentication system in Python. It includes input validation, login attempts, and a maximum number of attempts before denying access.
