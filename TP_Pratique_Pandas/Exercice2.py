from Imports import *

# 1. Vérifier les types des variables. S’assurer que les types des variables communes aux
# deux bases sont cohérents. Pour les variables qui ne sont pas en type float alors
# qu’elles devraient l’être, modifier leur type.
df_types = df.dtypes
# Seule INSEE commune et Commune sont de type objet, ce qui est cohérent.
df_city_types = df_city.dtypes

# Toutes les colonnes sont de type objet ici, il va falloir modifier leur type. CODGEO et LIBGEO restent en objet
columns_to_float = df_city.columns[df_city.isna().any()].tolist()
for column in columns_to_float:
    df_city[column] = df_city[column].astype(float)

# 2. Vérifier les dimensions des DataFrames
df_dimensions = df.shape
city_dimensions = df_city.shape

# 3. Vérifier le nombre de valeurs uniques des variables géographiques dans chaque base.
# Les résultats apparaissent-ils cohérents ?
df_unique_counts = df[["INSEE commune", "Commune"]].nunique()
df_city_unique_counts = df_city[["CODGEO","LIBGEO"]].nunique()
#On obtient plus de codes postaux que de noms de communes différents. Cela ne me parait pas cohérent

# 4. Identifier dans df_city les noms de communes qui correspondent à plusieurs codes
# communes et sélectionner leurs codes. En d’autres termes, identifier les CODGEO tels
# qu’il existe des doublons de LIBGEO et les stocker dans un vecteur x
# (conseil: faire attention à l’index de x)
duplicates = df_city["LIBGEO"].duplicated(keep=False)
index_repetitions = df_city["LIBGEO"][duplicates].index

code_communs = []
for x in index_repetitions:
    code_communs.append(df_city["CODGEO"][x])
# code_communs est une liste de 3707 éléments contenant tous les CODGEO associé à des doublons de LIBGEO

# 5. Regarder dans df_city ces observations
df_city_filtre = df_city[df_city["CODGEO"].isin(code_communs)]

# 6. Pour mieux y voir, réordonner la base obtenue par ordre alphabétique
df_city_filtre_trie = df_city_filtre.sort_values('LIBGEO')

# 7. Déterminer la taille moyenne (variable nombre de personnes: NBPERSMENFISC16) et
# quelques statistiques descriptives de ces données. Comparer aux mêmes statistiques
# sur les données où libellés et codes communes coïncident
moyenne_taille = round((df_city["NBPERSMENFISC16"].mean()), 2)
statistiques_descr = df_city["NBPERSMENFISC16"].describe()
moyenne_taille_code_communs = round((df_city_filtre["NBPERSMENFISC16"].mean()), 2)



# 8. Vérifier les grandes villes (plus de 100 000 personnes), la proportion de villes pour
# lesquelles un même nom est associé à différents codes commune.
cities_100k_plus = df_city_filtre[df_city_filtre["NBPERSMENFISC16"] > 100000]
cities_100k_plus_proportions = cities_100k_plus["LIBGEO"].value_counts()
# Parmi les villes de plus de 100 000 personnes, il n'y a que Saint-Denis qui est associé à différents codes communes.

# 9. Vérifier dans df_city les villes dont le libellé est égal à Montreuil. Vérifier également
# celles qui contiennent le terme ‘Saint-Denis’
df_city_montreuil = df_city[df_city["LIBGEO"] == "Montreuil"]
df_city_saint_denis = df_city[df_city["LIBGEO"] == "Saint-Denis"]

