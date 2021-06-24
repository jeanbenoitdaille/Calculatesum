from datetime import datetime
     
age = 25
mois_de_naissance = 10
     
annee_actuelle = datetime.today().year
mois_actuel = datetime.today().month
     
resultat = annee_actuelle - age - (1 if mois_de_naissance > mois_actuel else 0)
print(resultat)