"# Sistema-experto-juegos" 
Sistema de Recomendación de Juegos
Este script de Python recomienda juegos basados en los géneros que el usuario ingresa. Utiliza un archivo JSON que contiene una lista de juegos y sus géneros para generar recomendaciones ajustadas a las preferencias del usuario. La similitud entre los géneros del usuario y los géneros de los juegos se calcula utilizando la librería FuzzyWuzzy.

Funcionalidades
Carga de Datos: Lee los datos de un archivo JSON llamado conocimiento.json, que debe contener una lista de juegos con sus géneros.
Entrada del Usuario: Permite al usuario ingresar una lista de géneros separados por comas.
Filtrado y Recomendaciones: Calcula la similitud entre los géneros ingresados por el usuario y los géneros de los juegos utilizando FuzzyWuzzy. Solo se consideran juegos con una similitud mínima del 60%.
Resultado: Muestra los 15 juegos más recomendados en base a la similitud calculada.

Este proyecto logra decidir sobre varias opciones en base a las características de las mismas, el mayor problema al que me enfrente es que es demasiado libre con lo que acepta el sistema como válido

Video explicativo: https://youtu.be/KAtu2hz9hf4