#Se importa las librerias de mysql para realizar la conexión a la base de datps local y de pandas para todo el analisis de los datos 
import mysql.connector
import pandas as pd

#Se crea la conexión a la base de datos
conn = mysql.connector.connect(
    user = 'root', 
    database = 'sector_minero_energetico_2', 
    password='', 
    host="localhost"
)
#Realiza una consulta en la base de datos
query = "SELECT * FROM eficiencia_energetica"

#Se lee el archivo 
df = pd.read_sql_query(query, conn)
#Se cierra para evitar conflictos
conn.close()
#Se imprime el dataframe
print(df)
#Esta línea de código, exporta la consulta que se tiene en el query
"""df.to_csv('archivo.csv', index=False)"""
