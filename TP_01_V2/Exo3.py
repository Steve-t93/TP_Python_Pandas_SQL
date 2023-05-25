# C. Exercice 3 : tableaux d'enregistrements, les étudiants
import pandas as pd

Bernard = {
    "Français": 14.5,
    "Maths": 9.0,
    "Anglais": 12.0,
    "Histoire": 17.5,
    "Svt": 11.5
}

Camille = {
    "Français": 17.5,
    "Maths": 13.5,
    "Anglais": 15.0,
    "Histoire": 12.5,
    "Svt": 10.0
}

Samir = {
    "Français": 13.0,
    "Maths": 16.0,
    "Anglais": 8.5,
    "Histoire": 14.0,
    "Svt": 11.0
}

Eleonore = {
    "Français": 11.0,
    "Maths": 12.5,
    "Anglais": 7.5,
    "Histoire": 13.5,
    "Svt": 18.0
}
# 1. Créer une promotion comme un tableau d'étudiants,
promotion = pd.DataFrame([Bernard, Camille, Samir, Eleonore], index=["Bernard","Camille","Samir","Eleonore"])
print(sum(promotion.loc["Bernard"].values) / len(promotion.loc["Bernard"].values))

# 2. Implémenter la fonction moyenne d'un étudiant dédiée cette représentation
def moyenne_etudiant(nom):
    moyenne = sum(promotion.loc[nom].values) / len(promotion.loc[nom].values)
    return (f"la moyenne de {nom} est de: {moyenne}/20")

print(promotion["Français"].values)

# 3. Pour chaque discipline, la fonction moyenne de la promotion
def moyenne_promotion(matière):
    moyenne = sum(promotion[matière].values / len(promotion[matière].values))
    return (f"la moyenne de la promotion en {matière} est de: {moyenne}/20")

mean_bernard= moyenne_etudiant("Bernard")
print(mean_bernard)

mean_français = moyenne_promotion("Français")
print(mean_français)

print(100*"-")

# 4. La fonction qui trouve l'étudiant ayant eu la note moyenne maximale, etc.
def moyennes_df(promotion):
    liste_moyennes = []
    etudiants = list(promotion.index)
    for nom in etudiants:
        liste_moyennes.append(sum(promotion.loc[nom].values) / len(promotion.loc[nom].values))
    df = pd.DataFrame(liste_moyennes, index=etudiants, columns=["Moyenne"])
    meilleur_etudiant = None
    meilleur_moyenne = 0.0
    for etudiant in list(df.index):
        if df.loc[etudiant].values > meilleur_moyenne:
            meilleur_moyenne = df.loc[etudiant].values
            meilleur_etudiant = etudiant
    return (f"le ou la meilleur(e) étudiant(e) est {meilleur_etudiant}")


meilleur = moyennes_df(promotion)
print(meilleur)

print(100*"-")

# 5. Généraliser à un type d'étudiant qui possède un nombre quelconque de notes.
# La fonction moyennedf est généralisé de manière à obtenir le meilleur étudiant possédant un nombre quelconque de notes.




