from Imports import *
from Exercice2 import code_communs

# 1. Fixer comme indice la variable de code commune dans les deux bases. Regarder le
# changement que cela induit sur le display du DataFrame
df_code_communs = df[df["INSEE commune"].isin(code_communs)]
df_city_code_communs = df_city[df_city["CODGEO"].isin(code_communs)]

# 2. Les deux premiers chiffres des codes communes sont le numéro de département.
# Créer une variable de département dep dans df et dans df_city
df["dep"] = df["INSEE commune"].str.slice(0, 2)
df_city["dep"] = df_city["CODGEO"].str.slice(0, 2)

# 3. Calculer les émissions totales par secteur pour chaque département. Mettre en log
# ces résultats dans un objet df_log. Garder 5 départements et produire un barplot
emissions_par_secteur = df.groupby('INSEE commune')['CO2 biomasse hors-total'].sum()

secteur_5_barplot = emissions_par_secteur[0:5]

plt.bar(secteur_5_barplot.index, secteur_5_barplot.values)
plt.xlabel('secteur')
plt.ylabel('Somme')
plt.title("somme des émissions par secteur")
# plt.show()

# 4. Repartir de df. Calculer les émissions totales par département et sortir la liste des 10
# principaux émetteurs de CO2 et des 5 départements les moins émetteurs. Sans faire
# de merge, regarder les caractéristiques de ces départements (population et niveau de vie)
emissions_par_dep = df.groupby('dep')['CO2 biomasse hors-total'].sum()


principaux_emetteurs = sorted(range(len(emissions_par_dep)), key=lambda i: emissions_par_dep[i], reverse=True)[:10]
moins_emetteurs = sorted(range(len(emissions_par_dep)), key=lambda i: emissions_par_dep[i])[:5]

df_principaux_emetteurs = df[df['dep'].isin(principaux_emetteurs)]
df_moins_emetteurs = df[df['dep'].isin(moins_emetteurs)]


