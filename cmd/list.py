etudiants = {
    "Onana Lionel":{
        "note" : 15.5,
        "mention" : "Bien"
    },
    "Bessala Emgbang" :{
        "note" : 09.5,
        "mention" : "Mediocre !!"
    },
    "Nyom Guimbous" : {
        "note" : 18.5,
        "mention" : "Tres Bien"
    }
}

for identifiant, infos in etudiants.items():
    notes = infos["note"]
    mention = infos["mention"]
    print(f"L'etudiant {identifiant} a eu {notes}/20 avec la mention {mention}")