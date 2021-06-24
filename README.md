# Calculatesum
Calculer la somme entre deux nombres 
On s'aventure dans un genre d'exercice qui paraît simple, car il n'y a finalement qu'une seule ligne de code, mais pour que notre programme fonctionne dans tous les cas il fallait faire un peu attention.

J'imagine que beaucoup d'entre vous on tout simplement fait le code suivant :

    def somme(a, b):
        return sum(range(a, b + 1))
     
    print(somme(2, 6))

Le problème avec ce code est qu'il ne fonctionne que si l'on donnait les nombres dans l'ordre.
Si on utilise la fonction en donnant le nombre le plus grand en premier, la fonction nous retournerait 0 car la fonction range retourne une liste vide si le premier nombre est plus grand que le second :

    def somme(a, b):
        return sum(range(a, b + 1))
     
    print(somme(6, 2))
    0

Afin de s'assurer que la fonction range prenne bien les nombres a et b dans le bon ordre, nous utilisons les fonctions min et max, qui permettent de récupérer le nombre le plus petit et le nombre le plus grand entre plusieurs nombres.

    range(min(a, b), max(a, b))

Il ne fallait pas oublier également d'ajouter 1 au deuxième nombre car la fonction range est exclusive et nous voulons également additionner le deuxième nombre passé à la fonction 'somme' :

    range(min(a, b), max(a, b) + 1)

La fonction range nous retourne donc une liste qui contient tous les nombres de 2 à 6, il ne nous reste donc plus qu'à les additionner avec la fonction sum :

    sum(range(min(a, b), max(a, b)+1))
