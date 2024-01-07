import os
import random
import shutil


students_list = [
    "Paul",
    "Ashuka",
    "Louis",
    "Edouard",
    "Laurent"
]

""" file = open("fichiers/meals.txt", "r+")
repas = file.readlines()
meal_choice = random.choice(repas)
print(f"Je vous propose {meal_choice} comme repas. Enjoy your meal !!")
file.close() """

source = "students.txt"
destination = "fichiers"

shutil.copy(source, destination)
os.remove(source)