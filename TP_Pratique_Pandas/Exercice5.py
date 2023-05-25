from Imports import *

df["dep"] = df["INSEE commune"].str.slice(0, 2)
df_city["dep"] = df_city["CODGEO"].str.slice(0, 2)

# 1. Créer une copie des données de l’ADEME en faisant df_wide = df.copy()
df_wide = df.copy()

# 2. Restructurer les données au format long pour avoir des données d’émissions par
# secteur en gardant comme niveau d’analyse la commune (attention aux autres variables identifiantes).
id_vars = ['dep']

df_wide = pd.melt(df_wide[["dep", 'CO2 biomasse hors-total']],
                  id_vars=id_vars, var_name="variable", value_name='valeur')

# 3. Faire la somme par secteur et représenter graphiquement
somme_par_secteur = df_wide.groupby('dep')['valeur'].sum()

plt.figure(figsize=(10,6))
somme_par_secteur.plot(kind="bar")
plt.xlabel('departement')
plt.ylabel("Emissions")
plt.title("Emissions de CO2 par departement")
# plt.show()

# 4. Garder, pour chaque département, le secteur le plus polluant
indices_max = df_wide.groupby("dep")["valeur"].idxmax()
df_wide_max = df_wide.loc[indices_max]