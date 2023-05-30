# Exercice 4 : Algorithmes avancés sur les tableaux
import random


# 1. Sur les tableaux quelconques
# 1. Implémenter une fonction index_minimum(t,d,f) qui renvoie le numéro de la case
# contenant la plus petite valeur du tableau t entre les cases d et f.
def index_minimum(t,d,f):
    index_min = d

    for i in range(d+1, f+1):
        if t[i] < t[index_min]:
            index_min = i

    return index_min

# 2. Programmer un tri à bulles.
def tri_a_bulles(t):
    n = len(t)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
    return t
'''
t = [random.randint(0,15) for x in range(15)]
indice_min = index_minimum(t, 3, 5)
tri_a_bulles(t)
print("Tableau trié: ", t)
print(100*("-"))
'''
# 2. Sur les tableaux déjà triés

t2 = [random.randint(0,20) for x in range(20)]

# 1. Implémenter une fonction de recherche d'un élément utilisant une boucle tant que et
# tirant parti du fait que les éléments sont ordonnés.
def recherche_element(element, t):
    gauche = 0
    droite = len(t) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2
        valeur_milieu = t[milieu]

        if element == valeur_milieu:
            return milieu
        elif element < valeur_milieu:
            droite = milieu - 1
        else:
            gauche = milieu + 1
    return -1
'''
element = 10
indice = recherche_element(element, t2)
if indice != -1:
    print(f"indice = {indice}")
else:
    print("pas dans le tableau")
print(50*("-"))
'''

# 2. Écrire une fonction de recherche dichotomique.
def recherche_dichotomique(t, element):
    debut = 0
    fin = len(t) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2

        if t[milieu] == element:
            return milieu
        elif t[milieu] < element:
            debut = milieu + 1
        else:
            fin = milieu - 1

    return -1


# 3. Proposer une procédure insertion(e,t,n) qui ajoute un élément e à sa place dans un
# tableau t de taille n.
def insertion(e, t, n):
    i = n - 1

    while i >= 0 and t[i] > e:
        t[i + 1] = t[i]
        i -= 1

        t[i + 1] = e
    return t
'''
t = [1,3,5,8,11,14]
n = 6
e = 6
print("Insertion faite: ", t)
'''

# 3. Autres méthodes de tri
# 1. tri_extraction utilisant index_minimum(t,d,f) : on récupère le minimum du tableau
# et on le place dans la première case, on récupère le minimum du tableau privé de la
# première case et on le place dans la deuxième, etc.
def tri_extraction(t):
    n = len(t)

    for i in range(n):
        indice_min = index_minimum(t, i, n - 1)
        t[i], t[indice_min] = t[indice_min], t[i]
    return t

# 2. tri_insertion utilisant insertion(e,t,n) : prendre le i ème élément et le mettre à sa
# place dans les i-1 premières cases déjà triées.
def tri_insertion(t):
    n = len(t)

    for i in range(1, n):
        element_courant = t[i]
        insertion(element_courant, t, i)

    return t