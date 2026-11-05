# Alonso Lopez Garcia NC = 0087 | Fecha 05/11/2026
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 6 listas de redes sociales con 4 elementos por lista 
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# Creamos una lista de listas 
lista_redes_sociales = [fb, twt, ig, wsp, tel, lkn]
# print(lista_redes_sociales)
# Utilizar pandas para organizar la tabla (dataframe o marco de datos)
# A cada columna le ponemos su nombre 
df_redes_sociales = pd.DataFrame(lista_redes_sociales, columns=["Nombre", "Cantidad", "Es_FB", "Año"])
print(df_redes_sociales)
# Creamos el archivo CSV y lo guardamos en CSV }
# df_redes_sociales.to_csv("redessociales.csv", index=False)
# Crear grafica de lineas
# Donde x es Nombre en el eje horizontal 
# Donde y es Cantidad en el eje vertical 
plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Gráfica Redes Sociales NC 0087")
plt.xlabel("Nombres de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Creamos una grafica de puntos
plt.scatter(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Gráfica de puntos Redes Sociales NC 0087")
plt.xlabel("Nombres de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Creamos grafica de barras 
plt.bar(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
# Etiquetas y titulo 
plt.title("Gráfica de barras Redes Sociales NC 0087")
plt.xlabel("Nombres de las redes")
plt.ylabel("Cantidad de usuarios")
# Mostrar la gráfica 
plt.show()
# Ordenar la grafica de barras de manera descendente
# De la mas grande a la mas pequeña 
df_rs_ordenar = df_redes_sociales.sort_values("Cantidad", ascending = False)
plt.bar(df_rs_ordenar["Nombre"], df_rs_ordenar["Cantidad"])
plt.title("Gráfica de barras descendente Redes Sociales NC 0087")
plt.xlabel("Nombres de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Darle color a la grafica
plt.bar(df_rs_ordenar["Nombre"], df_rs_ordenar["Cantidad"],
        color = ["b", "g", "c", "m", "y", "r"])
plt.title("Gráfica de barras descendente con color Redes Sociales NC 0087")
plt.xlabel("Nombres de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
print(" ")
# Grafica pastel pie
# plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],
        labels=df_redes_sociales["Nombre"])
plt.title("Gráfica Pastel Redes Sociales NC 0087")
plt.show()


print("Alonso Lopez Garcia NC = 0087 | Fecha 05/11/2026")