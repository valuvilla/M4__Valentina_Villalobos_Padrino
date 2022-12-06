import pandas as pd  # Importa pandas y usa un alias para poder utilizar sus recursos

# Cargar como dataframe de pandas el csv imdb_titulos.csv y mostrar sus 5 primeros registros
titulos_peliculas = pd.read_csv('imdb_titulos.csv')
print(titulos_peliculas.head()) #head() devuelve los 5 primeros registros del dataframe

# Cargar como dataframe de pandas el csv imdb_elenco.csv y mostrar sus 5 primeros registros
elenco = pd.read_csv('imdb_elenco.csv')
print(elenco.head()) #head() devuelve los 5 primeros registros del dataframe por defecto pero es modificable mediante el parámetro "n"

#Mostrar el número de registros del dataframe de titulos
print("Mostrar el número de registros del dataframe de titulos: ", "\n", len(titulos_peliculas)) #len() devuelve el número de registros del dataframe.


#Mostrar el número de registros del dataframe de elenco
print("Mostrar el número de registros del dataframe de elenco: ", "\n", len(elenco)) #len() devuelve el número de registros del dataframe.


#Mostrar las 5 peliculas más antiguas del listado de titulos
print("Mostrar las 5 peliculas más antiguas del listado de titulos", "\n")
print(titulos_peliculas.sort_values(by='year').head()) #sort_values() ordena los registros del dataframe por el valor de la columna indicada en el parámetro "by"

#Mostrar las peliculas que en el titulo tienen la palabra "Dracula". También mostrar el número total de peliculas que coincidan con este requisito
print("Mostrar las peliculas que en el titulo tienen la palabra Dracula")
print(titulos_peliculas[titulos_peliculas['title'].str.contains('Dracula')])  #str.contains() devuelve la subcadena indicada en el parámetro
print("Número de peliculas que coincidan con este requisito: ",len(titulos_peliculas[titulos_peliculas['title'].str.contains('Dracula')]), "\n")

#Mostrar los 10 titulos más comunes (que más se repiten)
print("Mostrar los 10 titulos más comunes")
print(titulos_peliculas['title'].value_counts().head(10)) #value_counts() devuelve un dataframe con los valores de la columna indicada en el parámetro y la cantidad de veces que se repite cada uno


#Mostrar cual fue la primer pelicula hecha titulada "Romeo and Juliet"
print("Mostrar cual fue la primer pelicula hecha titulada 'Romeo and Juliet'")
print(titulos_peliculas[titulos_peliculas['title'] == 'Romeo and Juliet'].sort_values(by='year').head(1)) #sort_values() ordena los registros del dataframe por el valor de la columna indicada en el parámetro "by"

#Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
print("Listar todas las peliculas que contengan la palabra 'Exorcist' ordenadas de la más vieja a la más reciente","\n",titulos_peliculas[titulos_peliculas['title'].str.contains('Exorcist')].sort_values(by='year')) #sort_values() ordena los registros del dataframe por el valor de la columna indicada en el parámetro "by"


#Mostrar cuantas peliculas fueron hechas en el año 1950
print("Mostrar cuantas peliculas fueron hechas en el año 1950: ",len(titulos_peliculas[titulos_peliculas['year'] == 1950]),"\n") #len() devuelve el número de registros del dataframe.

#Mostrar cuantas peliculas fueron hechas de 1950 a 1959
print("Mostrar cuantas peliculas fueron hechas de 1950 a 1959: ",len(titulos_peliculas[(titulos_peliculas['year'] >= 1950) & (titulos_peliculas['year'] <= 1959)]),"\n") #len() devuelve el número de registros del dataframe.

#Mostrar todos los roles o papeles que hubo en la pelicula "The Godfather". También mostrar el número total de coincidencias
print("Mostrar todos los roles o papeles que hubo en la pelicula 'The Godfather'","\n",elenco[elenco['title'] == 'The Godfather'], "\n") #mediante el uso d corchetes se puede filtrar el dataframe por una condición
print("Número de coincidencias: ",len(elenco[elenco['title'] == 'The Godfather']), "\n") #len() devuelve el número de registros del dataframe.

#Mostrar el elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958
print("Mostrar el elenco completo ordenado por la clasificacion 'n' de la pelicula 'Dracula' de 1958","\n",elenco[(elenco['title'] == 'Dracula') & (elenco['year'] == 1958)].sort_values(by='year'), "\n") #sort_values() ordena los registros del dataframe por el valor de la columna indicada en el parámetro "by". Mediante el uso de & restrigimos los años

#Mostrar cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas
print("Mostrar cuantos papeles de 'Bruce Wayne' han sido hechos en la historia de las peliculas: ",len(elenco[elenco['character'] == 'Bruce Wayne']), "\n") #len() devuelve el número de registros del dataframe.

#Mostrar cuantos papeles ha hecho "Robert De Niro" en su carrera
print("Mostrar cuantos papeles ha hecho 'Robert De Niro' en su carrera: ",len(elenco[elenco['name'] == 'Robert De Niro']), "\n") #len() devuelve el número de registros del dataframe.

#Listado de papeles como protagonista (n=1) que tuvo el actor "Charlton Heston" en la década de los 60's, ordenado por año de forma descendente
print("Listado de papeles como protagonista (n=1) que tuvo el actor 'Charlton Heston' en la década de los 60's, ordenado por año de forma descendente","\n",elenco[(elenco['name'] == 'Charlton Heston') & (elenco['n'] == 1) & (elenco['year'] >= 1960) & (elenco['year'] <= 1969)].sort_values(by='year', ascending=False), "\n") #sort_values() ordena los registros del dataframe por el valor de la columna indicada en el parámetro "by". Con asceding=False se ordena de forma descendente

#Mostrar cuantos papeles para actores hubo en la década de los 50's
print("Mostrar cuantos papeles para actores hubo en la década de los 50's: ",len(elenco[(elenco['type'] == 'actor') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)]), "\n") #len() devuelve el número de registros del dataframe, mediante el uso de & restrigimos los años, al especificar el tipo de actor, elimiamos cualquier entrada de una actriz

#Mostrar cuantos papeles para actrices hubo en la década de los 50's
print("Mostrar cuantos papeles para actrices hubo en la década de los 50's: ",len(elenco[(elenco['type'] == 'actress') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)]), "\n") #Con el mismo procedimiento que el anterior, pero especificando el tipo de actriz





