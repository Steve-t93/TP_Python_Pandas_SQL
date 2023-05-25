import matplotlib.pyplot as plt
import pandas as pd

from Imports import *
from Exercice2 import code_communs

df["dep"] = df["INSEE commune"].str.slice(0, 2)
df_city["dep"] = df_city["CODGEO"].str.slice(0, 2)

# 1. Créer une variable emissions qui correspond aux émissions totales d’une commune
df["emissions"] = df.groupby('Commune')['CO2 biomasse hors-total'].sum()

# 2. Faire une jointure à gauche entre les données d’émissions et les données de cadrage.
# Comparer les émissions moyennes des villes sans match (celles dont des variables
# bien choisies de la table de droite sont NaN) avec celles où on a bien une valeur
# correspondante dans la base Insee
code_non_doublons = []
for code in df["INSEE commune"]:
    code_non_doublons.append(code)
# df_merged = pd.merge(df, df_city, how='left', on='dep')
données_emissions = df[["dep", "emissions"]]

left_join = pd.merge(données_emissions, df_city, how="left", on="dep")

emissions_moyennes_par_commune = left_join.groupby("LIBGEO")["emissions"].mean()

# Faire un inner join puis calculer l’empreinte carbone (l’émission rapportée au nombre
# de ménages fiscaux) dans chaque commune. Sortir un histogramme en niveau puis en
# log et quelques statistiques descriptives sur le sujet.

'''
print(df_city[['NBMENFISC16', 'NBPERSMENFISC16']].head(15))
print(df_city.columns)
print(df.columns)
'''


inner_join = pd.merge(df, df_city, how='inner', on="dep")
# print(inner_join.columns)

#print(df.columns)
nbre_menages_par_commune = inner_join.groupby('Commune')['NBMENFISC16'].sum()
emissions_par_communes = inner_join.groupby('Commune')['CO2 biomasse hors-total'].sum()
empreinte_carbone = emissions_par_communes / nbre_menages_par_commune


empreinte_carbone.hist()
plt.show()

empreinte_carbone.hist(log=True)
plt.show()

# 4. Regarder la corrélation entre les variables de cadrage et l’empreinte carbone.
# Certaines variables semblent-elles pouvoir potentiellement influer sur l’empreinte
# carbone






