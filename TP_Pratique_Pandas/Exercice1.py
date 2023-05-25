from Imports import *

# A. Exercice 1: Afficher des données

# 1. Utiliser les méthodes adéquates pour les 10 premières valeurs, les 15 dernières et un
# échantillon aléatoire de 10 valeurs

premieres_10 = df.head(10)
dernieres_15 = df.tail(15)
aléatoire_10 = df.sample(10)

print(premieres_10)
print(50*("-"))
print(dernieres_15)
print(50*("-"))
print(aléatoire_10)
print(50*("-"))

# 2. Tirer 5 pourcent de l’échantillon sans remise
sample_size = int(0.05 * len(df))
sample = df.sample(n=sample_size)
print(sample)
print(50*("-"))

# 3. Ne conserver que les 10 premières lignes et tirer aléatoirement dans celles-ci pour
# obtenir un DataFrame de 100 données.
sample2 = premieres_10.sample(n=100, replace=True)
print(sample2)
print(100*("-"))

# 4. Faire 100 tirages à partir des 6 premières lignes avec une probabilité de 1/2 pour la
# première observation et une probabilité uniforme pour les autres
df_head = df.head(6)
proba = [0.5] + [0.5 / (len(df_head)-1)] * (len(df_head)-1)
sample3 = df_head.sample(n=100, replace=True, weights=proba)
print(sample3)

# 5. Faire la même chose sur df_city
premieres_10_city = df_city.head(10)
dernieres_15_city = df_city.tail(15)
aléatoire_10_city = df_city.sample(10)

sample_size = int(0.05 * len(df_city))
sample = df_city.sample(n=sample_size)

sample2 = premieres_10_city.sample(n=100, replace=True)

df_city_head = df_city.head(6)
proba = [0.5] + [0.5 / (len(df_city_head)-1)] * (len(df_city_head)-1)
sample3 = df_city_head.sample(n=100, replace=True, weights=proba)