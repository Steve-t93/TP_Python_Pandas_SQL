import mysql.connector
from mysql.connector import Error

import matplotlib.pyplot as plt
import pandas as pd

database = 'fromagerie'

table = 'dataw_fro'

try:
    connection = mysql.connector.connect(host='localhost',
                                         database=database,
                                         user='root',
                                         password='', connection_timeout=180)

    if connection.is_connected():

        sql_select_Query = "select * from dataw_fro"

        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        df = pd.DataFrame(records)
        print(df.head(30))

except Error as e:
    print("Error while connecting to Mysql", e)
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")