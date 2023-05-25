from Imports import *
import timeit

df["dep"] = df["INSEE commune"].str.slice(0, 2)
df_city["dep"] = df_city["CODGEO"].str.slice(0, 2)

# 1. Repartir de df et créer une copie df_copy = df.copy() et df_copy2 = df.copy() afin de
# ne pas écraser le DataFrame df
df_copy = df.copy()
df_copy2 = df.copy()

# 2. Utiliser la variable dep comme indice pour df_copy et retirer tout index pour df_copy2
df_copy = df_copy.set_index('dep')
df_copy2 = df_copy2.reset_index(drop=True)

# 3. Importer le module timeit et comparer le temps d’exécution de la somme par secteur,
# pour chaque département, des émissions de CO2
def somme_emission_secteur(df):
    somme = list(round((df.groupby(['dep', 'INSEE commune'])["CO2 biomasse hors-total"].sum()), 2))
    somme_str = list(map(str, somme))
    return somme_str

debut = timeit.default_timer()
somme_emission_secteur(df_copy)
fin = timeit.default_timer()

temps_execution = fin - debut
print("temps_execution : ", round(temps_execution, 2) , "secondes")

