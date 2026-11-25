

# json ( slide 33 )
import json

# un dictionnaire {"nom", "solde"} (slide 31),
#  C est une liste de dictionnaires (slide 32)
C = [
    {"nom": "compte1", "solde": 3000.0},
    {"nom": "compte2", "solde": 500.0},
    {"nom": "compte3", "solde": 1000.0},
]


# deposer  (slide 40 fonction avec paramètres + retour, slide 41 typage)
def deposer(c: dict, somme: float) -> dict:
    # condition if (slide 35) + opérateur relationnel (slide 34)
    if somme <= 0:
        return {"erreur": "montant invalide"}
    # c est un dict mutable : passage par référence (slide 40)
    c["solde"] += somme   # opérateur += (slide 34)
    # Retour d'un objet JSON (dictionnaire, slide 33)
    return {"compte": c["nom"], "solde": c["solde"]}



def retirer(c: dict, somme: float) -> dict:
    # Condition avec opérateur logique "or" (slide 34) 
    if somme <= 0 or somme > c["solde"]:
        return {"erreur": "montant invalide ou solde insuffisant"}
    c["solde"] -= somme   # opérateur -= (slide 34)
    return {"compte": c["nom"], "solde": c["solde"]}



def afficher(c: list) -> dict:
    # List compréhension (slide 39) + fonction intégrée sum
    total = sum([compte["solde"] for compte in c])
    return {"total": total}



def filtre1000(c: list) -> list:
    # List compréhension avec condition (slide 39) ; opérateur >= (slide 34)
    return [{"compte": x["nom"], "solde": x["solde"]} for x in c if x["solde"] >= 1000]



def trier_par_solde(c: list) -> list:
    # sorted + fonction anonyme lambda comme clé (slide 42) ; reverse=True = décroissant
    triee = sorted(c, key=lambda x: x["solde"], reverse=True)
    return [{"compte": x["nom"], "solde": x["solde"]} for x in triee]  # slide 39


# Point d'entrée du programme (slide 55)
if __name__ == "__main__":
    print(deposer(C[0], 500))        
    print(retirer(C[1], 200))        
    print(retirer(C[1], 99999))      
    print(afficher(C))               
    print(filtre1000(C))
    print(json.dumps(trier_par_solde(C)))  # encodage JSON (slide 33)
