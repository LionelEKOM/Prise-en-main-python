import statistics
from random import shuffle

# import random
# import string

# def password_generator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
#     """Generate a random password."""
#     return ''.join(random.choice(chars) for _ in range(size))

# Générer un mot de passe aléatoire de taille 12
# password = password_generator(12)
# print("Generated Password : ", password)

# A, B, C = 10, 20, 30
# A, B, C = B, C, A
# print(A, B, C)

# txt = "The best things in life are free!"
# print("free" in txt)

# Ternaire
# wallet = 5000
# price = 1000
# text = ("l'achat est possible", "l'achat est impossible")[price <= 500]
# print(text)

# password = input("Votre mot de passe : ")
# alert = ("Mot de passe valide", "Votre mot de passe est trop court")[len(password) < 7]
# print(alert)

# liste = [
#     "Ashuka",
#     'Dior',
#     'IAI-CAMEROUN'
# ]
# print("Element 1: " + liste[0])

# limit = input("identifiant :").split("-")
# print(limit)
# note = [
#     8, 15, 17,
#     16, 8, 14.5,
#     19, 12, 10
# ]
# print(note)
# shuffle(note)
# print(note)
# resultat = statistics.mean(note)
# print(resultat)

# Boucles
# emails = [
#     "Ashuka@gmail.com",
#     "dior@gmail.com",
#     "Leodubois.@gmail,com"
# ]
# for email in emails:
#     print("Envoye a : ", email)

limite = 100000
while True:
    salaire = input("Veuillez entrer votre salaire : ")
    salaire = int(salaire) 
    if salaire < limite:
        print(f"Votre salaire doit etre superieur a {limite}.")
    else:
        print("Salaire valide !!")
        break