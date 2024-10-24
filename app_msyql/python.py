import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_json('Copia de covid19.json')
print(df.info())
print(df)

ord_muerte = df.sort_values('fecha_muerte')
print(ord_muerte)
df_ordenado = df.sort_values('fecha_diagnostico')
df_group_fecha = df_ordenado.groupby(['fecha_diagnostico']).count()['id_de_caso']

print(df_group_fecha.to_string())
df_group_fecha.plot(title='Contagios por fecha', xlabel='Fecha', ylabel='Contagios')
plt.show()

