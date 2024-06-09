#caso1
import pandas as pd

df_airbnb = pd.read_csv("./data/airbnb.csv")

print(df_airbnb.head())

print(df_airbnb.dtypes)



tipo_propiedad = "Entire home/apt"
barrio = "Santa Maria Maior"
puntuacion_minima = 4.5
capacidad_minima = 2
precio_maximo = 70

alojamientos_filtrados = df_airbnb[
    (df_airbnb['room_type'] == tipo_propiedad) &
    (df_airbnb['neighborhood'] == barrio) &
    (df_airbnb['overall_satisfaction'] >= puntuacion_minima) &
    (df_airbnb['accommodates'] >= capacidad_minima) &
    (df_airbnb['price'] <= precio_maximo)
]

print(alojamientos_filtrados)

precio_medio_por_barrio = df_airbnb.groupby('neighborhood')['price'].mean().reset_index()

print(precio_medio_por_barrio)


#caso2
df_roberto_clara = df_airbnb[(df_airbnb['host_id'] == 97503) | (df_airbnb['host_id'] == 90387)]


df_roberto_clara.to_excel("roberto.xls", index=False)


print(df_roberto_clara)

#caso 3
df_diana = df_airbnb[df_airbnb['price'] <= 50]

df_diana_shared = df_diana[df_diana['room_type'] == 'Shared room']


df_diana_sorted = df_diana.sort_values(by=['price', 'overall_satisfaction'], ascending=[True, False])


df_diana_top_10 = df_diana_sorted.head(10)


print(df_diana_top_10)

