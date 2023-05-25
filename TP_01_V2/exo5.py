# E. Exercice 5 : Comparaison expérimentale des méthodes de tri
# 1. Écrire une fonction copie (t) qui renvoie un nouveau tableau contenant dans le même
# ordre les mêmes valeurs que le tableau t ; vérifier qu'une modification de la copie n'altère
# pas le tableau original.
import random
import time
import subprocess
import gnuplotpy
from Exo4 import tri_insertion, tri_extraction, tri_a_bulles

def copie(t):
    copie_t = []

    for element in t:
        copie_t.append(element)

    copie_t.append("New element")

    if "New element" in t:
        print("altération du tableau original")
    else:
        print("pas d'altération du tableau original")

    return copie_t

# 2. Proposer une fonction inverse (t) qui fournit un nouveau tableau contenant les mêmes
# valeurs que le tableau t mais dans l'ordre inverse.
def inverse(t):
    inverse_t = []

    for i in range(len(t) -1, -1, -1):
        inverse_t.append(t[i])

    return inverse_t

# 3. Implémenter des fonctions pour produire des tableaux :
# Une fonction tableau_premiers_entiers (n) qui produit un tableau contenant
# dans l'ordre tous les entiers de 1 à n
def tableau_premiers_entiers(n):
    tableau = []
    for x in range(1, n+1):
        tableau.append(x)
    return tableau

# Une fonction tableau_premiers_entiers_melanges (n) qui propose ces
# mêmes entiers mélangés aléaoirement
def tableau_premiers_entiers_melanges(n):
    tableau = list(range(1, n+1))
    random.shuffle(tableau)
    return tableau

# Une fonction tableau_premiers_entiers_inverses (n) qui propose ces
# mêmes entiers du plus grand au plus petit.
def tableau_premiers_entiers_inverses(n):
    tableau = []
    for x in range(n, 0, -1):
        tableau.append(x)
    return tableau

# 4. Proposer une procédure ligne_dans_fichier (f,n,t) dont le rôle est d'écrire dans le
# fichier f la valeur (numérique) de n, une tabulation, la valeur (numérique) de t et enfin un
# passage à la ligne.
def ligne_dans_ficher(f, n, t):
    with open(f, 'a') as fichier:
        fichier.write(str(n) + "\t"+ str(t) + '\n')

# print(ligne_dans_ficher("test.txt", n=50, t=45.5))

# 5. Écrire une fonction temps_tri_bulles (t) qui fait une copie du tableau t et renvoie le
# temps nécessaire au tri à bulles pour classer cette copie.

def temps_tri_bulles(t):
    copie_t = t.copy()

    debut = time.time()
    tri_a_bulles(copie_t)
    fin = time.time()

    temps_execution = fin - debut
    return temps_execution

'''
t = [7, 8, 2, 5, 10]
temps = temps_tri_bulles(t)
print("Temps de tri à bulles :", temps, "secondes")
'''

# 6. Coder la procédure stats_melange (nmin,nmax,pas,fois) qui pour chaque taille de
# tableau comprise entre nmin et nmax en avançant de pas en pas produit fois tableaux
# mélangés aléatoirement et écrit dans un fichier le temps moyen nécessaire au tri à bulles
# pour classer ces tableaux.

def stats_melange(nmin, nmax, pas, fois, fichier):
    with open(fichier, 'w') as f:
        f.write("Temps nécéssaire")

        for n in range(nmin, nmax+1, pas):
            temps_total = 0.0

            for _ in range(fois):
                t = tableau_premiers_entiers_melanges(n)

                temps = temps_tri_bulles(t)
                temps_total += temps

            temps_moyen = temps_total / fois

            texte = str(n) + "\t" + str(temps_moyen) + "\n"
            f.write(texte)
'''
nmin = 300
nmax = 2500
pas = 100
fois = 15
fichier = "resultats_tri_bulles.txt"

stats_melange(nmin, nmax, pas, fois, fichier)
'''
# 7. Même question avec la fonction stats_ordonne (nmin,nmax,pas,fois) pour des
# tableaux déjà ordonnés.

def stats_ordonne(nmin, nmax, pas, fois, fichier):
    with open(fichier, 'w') as f:
        f.write("Temps nécéssaire")

        for n in range(nmin, nmax+1, pas):
            temps_total = 0.0

            for _ in range(fois):
                t = tableau_premiers_entiers(n)

                temps= temps_tri_bulles(t)
                temps_total += temps

            temps_moyen = temps_total / fois

            texte = str(n) + "\t" + str(temps_moyen) + "\n"
            f.write(texte)
'''
nmin = 300
nmax = 2500
pas = 100
fois = 10
fichier = "resultats_stats_ordonnés.txt"

stats_ordonne(nmin, nmax, pas, fois, fichier)
'''
# 8. Même question avec la fonction stats_inverse (nmin,nmax,pas,fois) pour des
# tableaux déjà ordonnés mais en ordre inverse.
def stats_inverse(nmin, nmax, pas, fois, fichier):
    with open(fichier, 'w') as f:
        f.write("Temps nécéssaire")

        for n in range(nmin, nmax+1, pas):
            temps_total = 0.0

            for _ in range(fois):
                t = tableau_premiers_entiers_inverses(n)

                temps= temps_tri_bulles(t)
                temps_total += temps

            temps_moyen = temps_total / fois

            texte = str(n) + "\t" + str(temps_moyen) + "\n"
            f.write(texte)
'''
nmin = 300
nmax = 2500
pas = 100
fois = 10
fichier = "resultats_stats_inverses.txt"
stats_inverse(nmin, nmax, pas, fois, fichier)
'''

# 9. Produire à l'aide de votre code des fichiers de statistiques pour des tailles de tableau variant
# de 100 en 100, entre 100 et 1000, avec 5 répétitions pour chaque taille de tableau. Visualiser
# ces données avec gnuplot et comparer l'évolution du temps nécessaire au tri bulles selon le
# type de tableaux et selon leurs tailles.
nmin= 100
nmax= 1000
pas = 100
fois = 5

for n in range(nmin, nmax + 1, pas):
    fichier = "stats_{}.txt".format(n)
    stats_melange(n, n, 1, fois, fichier)


# stats_ordonne(nmin, nmax, pas, fois, fichier)
# stats_inverse(nmin, nmax, pas, fois, fichier)
liste_fichiers = []
for n in range(nmin, nmax + 1, pas):
    liste_fichiers.append("stats_{}.txt".format(n))

script_gnuplot = "set title 'Temps d'execution tri à bulles'\n" \
                 "set xlabel 'Taille'\n" \
                 "set ylabel 'Temps'\n"

for i, fichier in enumerate(liste_fichiers):
    script_gnuplot += f"plot '{fichier}' using 1:2 with lines title 'Courbe {i+1}'\n"
with open("plot_script.gp", "w") as fichier_script:
    fichier_script.write(script_gnuplot)
'''
chemin = r"C:\chemin\vers\gnuplot\bin\gnuplot"
subprocess.call([chemin, script_gnuplot])
'''

# 10. Généraliser votre code pour pouvoir également comparer les méthodes de tri entre elles : tri
# à bulles, tri insertion, tri extraction et tri rapide.
def tri_rapide(t):
    if len(t) <= 1:
        return arrow
    pivot = t[0]
    elements_inf = [x for x in t[1:] if x <= pivot]
    element_sup = [x for x in t[1:] if x > pivot]
    return tri_rapide(elements_inf) + [pivot] + tri_rapide(element_sup)


def choix_de_tri(t, choix):
    # 1 - tri à bulles
    if choix_de_tri == 1:
        tri_a_bulles(t)
    # 2 - tri a extraction
    elif choix_de_tri == 2:
        tri_extraction(t)
    # 3 - tri à insertion
    elif choix_de_tri == 3:
        tri_insertion(t)
    # 4 - tri rapide
    elif choix_de_tri == 4:
        tri_rapide(t)
    else:
        print("Mauvais choix")

t = random.sample(range(1, 100), 10)
choix_tri = input("Choisissez la méthode: ")
tableau_trié = choix_de_tri(t, choix_tri)
print("tableau trié: ", tableau_trié)

# 11. Tester des modifications des méthodes de tri, calculer les écarts-types des temps de calcul
# sur les tableaux mélangés, explorer les possibilités de gnuplot, expliquer théoriquement les
# courbes obtenues


