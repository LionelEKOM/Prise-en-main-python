while True:
    try:
        prixHT = int(input("Entrez votre prix HT : "))
        prixHT += prixHT * 2
        print(prixHT)
        break
    except ValueError:
        print(f"Attention vous devew entrer un nombre !!")
    finally:
        print(f"Fin du programme !!")

# Pour personnaliser une Exception 
        # raise Exception("Exception personnalisee")
        # except FileNotFoundError//Le fichier n'existe pas 