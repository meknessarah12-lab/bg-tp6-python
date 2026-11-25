

# ( JSON : slide 33)
import json

# (slide 24 variables, slide 26 listes, slide 28 tuples)

students = [
    (1000, "JOHN", "DOE", 14, 5),
    (2000, "BOB", "CARLTON", 7, 1),
    (3000, "RAYANE", "SMITH", 13, 3),
]

# Constante en majuscules  (slide 24)
SEUIL_ADMISSION = 10.0



# (slide 40 fonctions avec retour, slide 41 typage des paramètres/retour)
def B(note: float) -> bool:
    # Opérateur relationnel >= (slide 34) 
    return note >= SEUIL_ADMISSION



# (slide 41 typage, slide 32 liste de dictionnaires, slide 33 JSON)
def A(students: list) -> list:
    resultats = []  # liste vide (slide 26)
    # Boucle for sur la liste (slide 38) ; décomposition d'un tuple (slide 28)
    for mat, nom, prenom, note, absences in students:
        # Condition if/else (slide 35) 
        if B(float(note)):
            statut = "ADMIS"
        else:
            statut = "AJOURNE"
        # Dictionnaire {clé: valeur} (slide 31) ajouté à la liste avec append (slide 27)
        resultats.append({"mat": mat, "result": statut})
    
    return resultats



# (slide 40 fonctions sans retour)
def C():
    # Boucle for sur les tuples (slide 38)
    for mat, nom, prenom, note, absences in students:
        # Appel de B (slide 40) + condition (slide 35)
        if B(float(note)):
            print(f"{mat}: ADMIS")      # f-string (slide 55)
        else:
            print(f"{mat}: AJOURNE")


# Point d'entrée du programme (slide 55)
if __name__ == "__main__":
    print(A(students))         # affiche le résultat JSON de A
    C()
