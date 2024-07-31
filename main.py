import json
from fuzzywuzzy import fuzz

# Subir los datos desde el archivo Json
with open('conocimiento.json', 'r') as file:
    data = json.load(file)

# Convertir el input del usuario en una lista, tomando cada elemento en base a las comas
def inputUsuario(input_genres):
    return [genre.strip().lower() for genre in input_genres.split(',')]

# Obtener lista de géneros disponibles y el nombre de los juegos
def getGeneros(data):
    genres = set()
    for game in data['target']:
        for genre in game['genre'].values():
            genres.add(genre.lower())
    return genres

# Filtrar juegos basados en los géneros especificados y calcular probabilidad usando FuzzyWuzzy
def recomendaciones(data, input_genres):
    genres = inputUsuario(input_genres)
    availableGenres = getGeneros(data)
    recommendations = [] # Lista de recomendaciones
    similitudMinima = 0.6  # Se requiere un mínimo de 60% de probabilidad para que permita pasar el dato

    for game in data['target']:
        gameName = game['name']
        gameGenres = [v.lower() for v in game['genre'].values()]
        similitudMaxima = 0

        for genre in genres:
            for gameGenre in gameGenres:
                similarity = fuzz.ratio(genre, gameGenre) / 100
                if similarity > similitudMaxima: # Si fuzzywuzzy calcula una probabilidad mayor a 100%, hace default a 100%
                    similitudMaxima = similarity

        # Añadir solo si la similitud es mayor al porcentaje mínimo
        if similitudMaxima >= similitudMinima:
            recommendations.append((gameName, similitudMaxima))
    
    # Ordenar recomendaciones por similitud (de mayor a menor)
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

# Obtener input del usuario
generosUsuario = input("Ingresa los géneros que te interesan (separados por comas): ")

# Obtener recomendaciones
recommended = recomendaciones(data, generosUsuario)

# Imprimir resultados
if recommended:
    print("Juegos recomendados:")
    for game, similarity in recommended[:15]:  # Limitar a los 15 primeros resultados
        message = f"{game}"
        print(message)
else:
    print("No se encontraron juegos con esas características")
