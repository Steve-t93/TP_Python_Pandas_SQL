# Exercice 1 : Les basiques de Python 3
import random
import turtle

# 1. Affichages
# Tester l'instruction d'affichage print de Python:
print(12) # afficher un nombre
print("Bonjour") # afficher une chaîne de caractères

prenom = "Steve"
#print(prenom) # afficher une variable

texte = "Bonjour, je m'appelle Steve. \n J'aime le sport, particulièrement la boxe"
# print(texte)
# Pour passer à la ligne, on peut utiliser "\n"
# Pour ne pas passer à la ligne, on utilise l'argument "end" dans la fonction print()

# 2. Boucles
# 1. Écrire une boucle while qui compte jusqu'à 100. Idem avec une boucle for.
x = 0
while x != 100: # Boucle while qui compte jusqu'a 100
    x +=1
    print(x)

for x in range(0,101): # Boucle for
    print(x)

# 2. À l'aide de boucles imbriquées, dessiner des figures géométriques : triangles et carrés, creux ou non.
# Idem à l'aide de procédures et de leurs paramètres.
def carre_plein(taille):
    for x in range(taille):
        for y in range(taille):
            print("*", end="")
        print("")
taille = 4
print(carre_plein(taille))

def triangle_plein(taille):
    for x in range(taille + 1):
        for y in range(x):
            print("x", end="")
        print("")

taille = 10
print(triangle_plein(taille))

# 3. Listes

l1 = [] # Créer une liste vide
l2 = ["bleu", "rouge", "noir", "blanc", "vert", "orange"] # liste contenant des éléments

print("longueur de la liste l1:", len(l1))
print("longueur de la liste l2:", len(l2))

l2[3] = "or" # remplacer une des valeurs
print(l2)

l2.remove(l2[4]) # enlever une case
print(l2)

l2.append("rose") # ajouter une nouvelle valeur
print(l2)

# Différentes syntaxes pour afficher les éléments d'une liste

for x in l2:
    print(x)

for x in range(len(l2)):
    print(l2[x])

for x, y in enumerate(l2):
    print(x,y)

# 4. Aléatoire en Python
random1 = random.randint(1, 50)
print(random1)
# random.randint choisit un nombre aléatoire dans une fourchette que nous définissons

random2 = random.randrange(15)
print(random2) # Génère un nombre entier aléatoire

random3 = random.choice("Bonjour")
print(random3) # Choisit un élément parmi une chaîne de caractère

liste = [1,2,3,4,5,6]
random.shuffle(liste)
print(liste) # random.shuffle permet de changer aléatoirement l'ordre des éléments d'une liste
