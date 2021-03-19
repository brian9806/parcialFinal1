texto = """Hola, mundo. Esto es una cadena, se supone que debe tener varias palabras pues 
vamos a realizar un conteo de frecuencia de las mismas usando el lenguaje de programación Python. 
Ya no sé qué escribir pero sigo escribiendo para que poco a poco la cadena sea más larga y el 
ejercicio de programación sea demostrable. Creo que con todo esto que he escrito es suficiente"""


quitar = ",;:.\n!\"'"
for letra in quitar:
    texto = texto.replace(letra,
                          "")  
texto = texto.lower()

palabras = texto.split(" ")

diccionario = {}
for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1

for palabra in diccionario:
    frecuencia = diccionario[palabra]
    print(f"'{palabra}'-> se repite : {frecuencia}")