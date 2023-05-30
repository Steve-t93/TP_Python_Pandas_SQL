# Exercice 4 : Algorithmes avancés sur les tableaux
import random
import unittest


# 1. Sur les tableaux quelconques
# 1. Implémenter une fonction index_minimum(t,d,f) qui renvoie le numéro de la case
# contenant la plus petite valeur du tableau t entre les cases d et f.
def index_minimum(t, d, f):
    index_min = d

    for i in range(d+1, f+1):
        if t[i] < t[index_min]:
            index_min = i

    return index_min

# 2. Programmer un tri à bulles.
def tri_a_bulles(t):
    n = len(t)

    for i in range(n):
        for j in range(0, n-i-1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]

    return t
# 2. Sur les tableaux déjà triés

t2 = [random.randint(0, 20) for x in range(20)]

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

class TestExo4(unittest.TestCase):
    def test_index_minimum(self):
        resultat = index_minimum([2, 6, 5, 4, 9, 1, 8, 15, 4], 3, 7)
        self.assertEqual(resultat, 5)


    def test_tri_a_bulles(self):
        resultat = tri_a_bulles([5, 3, 9, 1])
        self.assertEqual(resultat, [1, 3, 5, 9])

    def test_recherche_element(self):
        resultat = recherche_element(3, [2, 3, 5, 9, 11, 6, 4])
        self.assertEqual(resultat, 1)

    def test_recherche_dichotomique(self):
        resultat = recherche_dichotomique([2, 3, 5, 9, 11, 6, 4], 9)
        self.assertEqual(resultat, 3)

    def test_insertion(self):
        resultat = insertion(8, [2, 3, 5, 9, 11, 6, 4], 4)
        self.assertEqual(resultat, [2, 3, 5, 8, 9, 6, 4])

    def test_tri_extraction(self):
        resultat = tri_extraction([2, 3, 5, 9, 11, 6, 4])
        self.assertEqual(resultat, [2, 3, 4, 5, 6, 9, 11])

    def test_tri_insertion(self):
        resultat = tri_insertion([15, 3, 5, 9, 11, 6, 4])
        self.assertEqual(resultat, [3, 4, 5, 6, 9, 11, 15])


if __name__ == '__main__':
    unittest.main()