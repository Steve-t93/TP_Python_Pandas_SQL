import random
import time
import pandas as pd

# Exercice 2 : tableaux de nombres
# 1 Définir en Python un tableau d'entiers


# a)  Écrire (et valider sur le tableau déjà défini) les fonctions qui :

tableau = []
for _ in range(10):
    aléatoires = random.randint(0,50)
    tableau.append(aléatoires) # Définition d'un tableau d'entiers aléatoires

print(tableau)

# 1. moyenne
somme = sum(tableau)
moyenne = somme / len(tableau)
print("moyenne: ", moyenne)

# 2. nombre d'occurences
élément = random.choice(tableau)
print(tableau.count(élément))
print(élément)


# 3. Combien d'éléments supérieurs ou égaux à 0
print(tableau)

sup_10 = 0
for x in tableau:
    if x >= 10:
        sup_10 += 1
print("nombre de nombre supérieurs à 10: ", sup_10)

# 4. Rechercher la valeur maximale du tableau

print(tableau)

maximum = tableau[0]
for x in tableau:
    if x >= maximum:
        maximum = x
print("la valeur maximale de la liste est: ", maximum)

# 5. tester si un élément est présent ou non
print(tableau)

élément = random.choice([x for x in range(0,50)])

if élément in tableau:
    print(True)
else:
    print(False)

# b) Ecrire les fonctions qui, pour une taille donnée n:

# 1.
def fournir_tableau(n, plage):
    tableau = []
    for _ in range(n): # Fournir un tableau de n entiers aléatoires
        tableau.append(random.randint(0,plage))
    return tableau

# 2.
tableau = fournir_tableau(15, 200) # Construit le tableau des n premiers entiers mélangés aléatoirement
# print(tableau)

def moyenne(tableau):
    somme = sum(tableau)
    moyenne = somme / len(tableau)
    return moyenne
def occurrence(élément, tableau):
    occurence = tableau.count(élément)
    return occurence

# 1. Sur des grands tableaux, mesurer le temps nécessaire à chacune des fonctions calculant la
# moyenne et recherchant un élément.
debut = time.perf_counter()

test = fournir_tableau(10000,10000000)
moyenne_test = moyenne(test)
test_d_occurence = occurrence(1500, test)

fin = time.perf_counter()
durée = fin - debut

print("le temps nécéssaire est de: ", durée, "secondes.")




