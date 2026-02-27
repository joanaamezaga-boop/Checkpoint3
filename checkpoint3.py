# Ejercicio 1
# Create a string, number, list, and boolean, each stored in their own variable.
string = "Soy un texto"
numero = 634
lista = ["azul", "rojo", "verde", "blanco"]
booleano = True


# Ejercicio 2
# Use an index to grab the first 3 letters in your string, store that in a variable. 
tres_primeras_letras = string[0:3]
print (tres_primeras_letras)


# Ejercicio 3
# Use an index to grab the first element from your list.
primer_elemento = lista[0]
print (primer_elemento)


# Ejercicio 4
# Create a new number variable that adds 10 to your original number.
numero_mas_diez = numero + 10
print (numero_mas_diez)


# Ejercicio 5
# Use an index to get the last element in your list.
print (lista[-1])


# Ejercicio 6
# Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
lista_names = names.split(",")
print (lista_names)


# Ejercicio 7
"""
Get the first word from your string using indexes. 
Use the upper function to transform the letters into uppercase. 
Create a new string that takes the uppercase word and the rest of the original string.
"""
primera_palabra = string.rstrip ("un texto")
primera_palabra = primera_palabra.upper()
print (primera_palabra)
resto_string = string.lstrip ("Soy")
nueva_string = primera_palabra + resto_string
print (nueva_string)


# Ejercicio 8
# Use string interpolation to print out a sentence that contains your number variable.
interpolacion = f"Este piso cuesta {numero} euros al mes"
print (interpolacion)


# Ejercicio 9
# Print “hello world”
print("hello world")


# Ejercicio 10
"""
Además necesito que me crees una cadena que contenga la palabra "Hola". 
Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. 
Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".
"""
nueva_cadena = "Cuando la vio le dijo hola"
nueva_cadena = nueva_cadena.replace("hola","adiós")
print (nueva_cadena)