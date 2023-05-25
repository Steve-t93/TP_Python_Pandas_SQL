import pandas
import matplotlib.pyplot as plt

from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root@localhost/fromagerie")
# Charger la requête : select * from dataw_fro where qte > 5 and timbrecli >0
sql_select_Query = "SELECT * FROM dataw_fro WHERE qte > 5 AND timbrecli > 0"

df = pandas.read_sql(sql_select_Query, engine)

df_columns = list(df.columns)
print(f"df possède {df.shape[0]} lignes et {df.shape[1]} colonnes.")
print(50*("-"))

# Faire des regroupements du DF

# par code postal + code client + date commande
# j'en fais un nouveau dataFrame appelé df_2
df_2 = df[["cpcli", "codcli", "datcde"]]

# Donner la moyenne des prix des conditionnementt
moyenne_prix_cond = df['prixcond'].mean()
print(f"la moyenne des prix des conditionnements est {round(moyenne_prix_cond, 2)}.")
print(50*("-"))

# Donner la somme des qté
somme_qté = df['qte'].sum()
print(f"la somme des quantités est de {somme_qté} unités.")

# Puis faire une stat sur les Objets
objet = df[["codobj","libobj", "Tailleobj", "puobj", "Poidsobj"]]

pourcentage = ((objet["libobj"].value_counts()) / (objet["libobj"].value_counts().sum())) * 100

for index, value in pourcentage.items():
    print(f"Objet: {index}, représente {round(value,1)} %")

print(50*("-"))

