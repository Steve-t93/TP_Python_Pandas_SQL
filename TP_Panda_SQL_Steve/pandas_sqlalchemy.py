import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root@localhost/fromagerie")

sql_select_Query = "select * from dataw_fro where points > 100"

df = pandas.read_sql(sql_select_Query, engine)

#Configuration du plot
df.plot(kind="bar", x="villecli", y="Nbcolis")

#Exécution et visualisation du plot
plt.show()