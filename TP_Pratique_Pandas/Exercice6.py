from Imports import *

df["dep"] = df["INSEE commune"].str.slice(0, 2)
df_city["dep"] = df_city["CODGEO"].str.slice(0, 2)

# 1. Repartir de df_wide = df.copy()
df_wide = df.copy()

# 2. Reconstruire le DataFrame, au format long, des données d’émissions par secteur en
# gardant comme niveau d’analyse la commune puis faire la somme par département et secteur
df_long = df_wide.groupby(["INSEE commune", "dep"]).sum().reset_index()

id_vars = ["INSEE commune", "dep"]
df_long = df_long.melt(id_vars=id_vars,
                       value_vars='CO2 biomasse hors-total',
                       var_name='secteur',
                       value_name='emissions')

df_sum = df_long.groupby(["INSEE commune", "dep"]).sum().reset_index()


somme_par_dep = df_sum.groupby('dep')["emissions"].sum()
somme_par_secteur = df_sum.groupby('INSEE commune')["emissions"].sum()

# 3. Passer au format wide pour avoir une ligne par secteur et une colonne par
# département
df_wide = df_sum.pivot(index="INSEE commune", columns="dep", values="emissions")

# 4. Calculer, pour chaque secteur, la place du département dans la hiérarchie des
# émissions nationales
emissions_nat = df_sum.groupby("dep")["emissions"].sum()
rang_emissions = emissions_nat.sort_values(ascending=False)


# 5. A partir de là, en déduire le rang médian de chaque département dans la hiérarchie
# des émissions et regarder les 10 plus mauvais élèves, selon ce critère.
median_per_dep = df_sum.groupby('dep')['emissions'].median()

mauvais_eleves_10 = median_per_dep.nsmallest(10)


