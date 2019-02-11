# Importar paquetes necesarios: pandas y folium
# Es necesario instalar el paquete folium desde Anaconda Navigator añadiendo el canal 'conda-forge'
# También se puede hacer desde el Anaconda Prompt con el comando: 'conda install -c conda-forge folium'
import

# Debeis descargaros un fichero csv con un conjunto de ocurrencias de una especie
# desde la pagina del GBIF (es necesario registrarse): https://www.gbif.org y leerla en un DataFrame
# de pandas. El fichero descargado es zip, así que hay que
# descomprimirlo para obtener el csv
# ########################################################
# Funcion: read_csv (pandas)
# Parametros: sep, [index_col], [parse_dates]
# Tutorial: http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#getting-data-in-out
# Referencia: http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# ########################################################
specie =

# Debeis crear un mapa para la visualizacion de la especie.
# Es necesario ajustar las coordenadas (norte-este) y el zoom del mapa a la localizacion de la especie
# ########################################################
# Funcion: Map (folium)
# Parametros: location, [zoom_start], [tiles]
# Tutorial: http://python-visualization.github.io/folium/quickstart.html#Getting-Started
# Referencia: http://python-visualization.github.io/folium/modules.html#folium.folium.Map
# ########################################################
specie_map =

# Iteramos por las ocurrencias y las añadimos al conjunto de puntos
for label, ocurrence in specie.iterrows():
    # Obtenemos la latitud y la longitud
    longitude =
    latitude =

    # Comprobamos que existen coordenadas
    if ():
        # Creamos el marcador
        # ########################################################
        # Funcion: Marker (folium)
        # Parametros: location, [popup]
        # Tutorial: http://python-visualization.github.io/folium/quickstart.html#Markers
        # Referencia: http://python-visualization.github.io/folium/modules.html#folium.map.Marker
        # ########################################################
        marker =
        # Lo insertamos en el mapa
        marker.add_to(specie_map)

# Se guarda el mapa como una pagina web
specie_map.save('mapa.html')
