import pandas as pd # Importamos pandas

# Cargar como dataframe de pandas el csv imdb_titulos.csv y mostrar sus 5 primeros registros
titulos_peliculas = pd.read_csv('imdb_titulos.csv')
print(titulos_peliculas.head())

# Cargar como dataframe de pandas el csv imdb_elenco.csv y mostrar sus 5 primeros registros
elenco = pd.read_csv('imdb_elenco.csv')
print(elenco.head())

#Mostrar el número de registros del dataframe de titulos
print("Mostrar el número de registros del dataframe de titulos: " ,len(titulos_peliculas), "\n") #len() devuelve el número de registros del dataframe.


#Mostrar el número de registros del dataframe de elenco
print("Mostrar el número de registros del dataframe de elenco: ",len(elenco), "\n") #shape[0] devuelve el número de filas del dataframe



#Mostrar las 5 peliculas más antiguas del listado de titulos
print("Mostrar las 5 peliculas más antiguas del listado de titulos", "\n",titulos_peliculas.sort_values(by='year').head(), "\n") #sort_values() ordena los registros del dataframe por el valor de la columna indicada en el parámetro "by"

#Mostrar las peliculas que en el titulo tienen la palabra "Dracula". También mostrar el número total de peliculas que coincidan con este requisito
print("Mostrar las peliculas que en el titulo tienen la palabra Dracula","\n",titulos_peliculas[titulos_peliculas['title'].str.contains('Dracula')],"\n")  #str.contains() devuelve la subcadena indicada en el parámetro
print("Número de peliculas que coincidan con este requisito: ",len(titulos_peliculas[titulos_peliculas['title'].str.contains('Dracula')]), "\n")

#Mostrar los 10 titulos más comunes (que más se repiten)
print("Mostrar los 10 titulos más comunes", "\n", titulos_peliculas['title'].value_counts().head(10), "\n") #value_counts() devuelve un dataframe con los valores de la columna indicada en el parámetro y la cantidad de veces que se repite cada uno


#Mostrar cual fue la primer pelicula hecha titulada "Romeo and Juliet"
print("Mostrar cual fue la primer pelicula hecha titulada 'Romeo and Juliet'","\n",titulos_peliculas[titulos_peliculas['title'] == 'Romeo and Juliet'].sort_values(by='year').head(1),"\n")

#Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
print("Listar todas las peliculas que contengan la palabra 'Exorcist' ordenadas de la más vieja a la más reciente","\n",titulos_peliculas[titulos_peliculas['title'].str.contains('Exorcist')].sort_values(by='year'))


#Mostrar cuantas peliculas fueron hechas en el año 1950
print("Mostrar cuantas peliculas fueron hechas en el año 1950: ",len(titulos_peliculas[titulos_peliculas['year'] == 1950]),"\n") #len() devuelve el número de registros del dataframe.

#Mostrar cuantas peliculas fueron hechas de 1950 a 1959
print("Mostrar cuantas peliculas fueron hechas de 1950 a 1959: ",len(titulos_peliculas[(titulos_peliculas['year'] >= 1950) & (titulos_peliculas['year'] <= 1959)]),"\n") #len() devuelve el número de registros del dataframe.

#Mostrar todos los roles o papeles que hubo en la pelicula "The Godfather". También mostrar el número total de coincidencias
print("Mostrar todos los roles o papeles que hubo en la pelicula 'The Godfather'","\n",elenco[elenco['title'] == 'The Godfather'], "\n")
print("Número de coincidencias: ",len(elenco[elenco['title'] == 'The Godfather']), "\n")

#Mostrar el elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958
print("Mostrar el elenco completo ordenado por la clasificacion 'n' de la pelicula 'Dracula' de 1958","\n",elenco[(elenco['title'] == 'Dracula') & (elenco['year'] == 1958)].sort_values(by='n'), "\n")

#Mostrar cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas
print("Mostrar cuantos papeles de 'Bruce Wayne' han sido hechos en la historia de las peliculas: ",len(elenco[elenco['character'] == 'Bruce Wayne']), "\n")

#Mostrar cuantos papeles ha hecho "Robert De Niro" en su carrera
print("Mostrar cuantos papeles ha hecho 'Robert De Niro' en su carrera: ",len(elenco[elenco['name'] == 'Robert De Niro']), "\n")

#Listado de papeles como protagonista (n=1) que tuvo el actor "Charlton Heston" en la década de los 60's, ordenado por año de forma descendente
print("Listado de papeles como protagonista (n=1) que tuvo el actor 'Charlton Heston' en la década de los 60's, ordenado por año de forma descendente","\n",elenco[(elenco['name'] == 'Charlton Heston') & (elenco['n'] == 1) & (elenco['year'] >= 1960) & (elenco['year'] <= 1969)].sort_values(by='year', ascending=False), "\n")

#Mostrar cuantos papeles para actores hubo en la década de los 50's
print("Mostrar cuantos papeles para actores hubo en la década de los 50's: ",len(elenco[(elenco['type'] == 'actor') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)]), "\n")

#Mostrar cuantos papeles para actrices hubo en la década de los 50's
print("Mostrar cuantos papeles para actrices hubo en la década de los 50's: ",len(elenco[(elenco['type'] == 'actress') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)]), "\n")





