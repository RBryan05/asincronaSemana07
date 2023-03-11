# Variables a utilizar.
print("     ")
print('\033[1m' + "A continuación, se desarrollará la actividad asincrona de la semana 07." + '\033[0m')

# Variables para operador aritmetico entero (int)
multi1 = 4
multi2 = 8
multi3 = 5
variableDivi1 = 243
variableDivi2 = 3
# Variables para operador aritmetico flotante (float)
expo1 = 5
expo2 = 3
modu1 = 53
modu2 = 9
# Variables para operador aritmetico complejo (complex)
comp1 = 51j
comp2 = 28j
comp3 = 15j
comp4 = 7j
# Variables para operador aritmetico carácter (string)
fruta1 = "banana"
fruta2 = "mora"
fruta3 = "mango"
fruta4 = "pera"
#Variables para tipos de datos booleanos (bool)
nombre1 = "Jonathan Humberto Alas Landaverde."
nombre2 = "Karla Patricia Miranda Orellana."
nombre3 = "Jeremy Odir Fuentes Soriano."
nombre4 = "Bryan Alexis Rauda Gómez."

print ("     ")
#Se hará una multiplicación con tres variables distintas
print ("Multiplicación de 3 variables.")
print("Se hará la multiplicación de las siguientes cantidades:", multi1, ",", multi2, "y", multi3)
respuesta1 = multi1 * multi2 * multi3
#Se imprime el resultado
print ("El resultado de la multiplicación de: ", multi1, "*", multi2, "*", multi3, " es igual a: ", respuesta1)
#La multiplicación se finalizó con exito
print ("     ")

#Se hará una división de dos variables
print ("División entera con 2 variables distintas.")
print ('Las variables a dividir serán:',variableDivi1, 'y', variableDivi2)
#Se procederá a hacer la división entre las dos variables
División1 = variableDivi1 / variableDivi2
print ("El resultado de la división de las dos variables es de: ", División1)
#La división se finalizó con exito

#Se hará una suma de la multiplicación y la división ya hechas
print ("     ")
print ("Suma de las variables de los resultados de la multiplicación y la división.")
#Se procederá a poner los datos a sumar y a hacer la suma de la multiplicación y la división
resultado1 = respuesta1 + División1
#Se establecieron los datos a sumar
print ("Las variables a sumar son: ", respuesta1, "y", División1)
#Se estableció la suma
print ("El resultado de la suma de los resultados es de: ", resultado1)
#La suma se finalizó con exito

print("    ")
#Se realizara un exponencia con datos Flotantes (float)
print("Exponenciación de un numero elevado a otro.")
numFloat = expo1 ** expo2
print(f"El resultado de {expo1} elevado al {expo2} es: {numFloat}")
print("Modulo de la divicion de dos numeros")
numFloat1 = modu1 % modu2
print(f"El resultado del modulo al divir {modu1} entre {modu2} es: {numFloat1}")
print("    ")

#Resta del exponente con el modulo
print("Se realizara una resta del resultado del expoenente y del modulo.")
restaFloat = numFloat - numFloat1
print(f"El resultado de restar {numFloat} - {numFloat1} es: {restaFloat}")
print("    ")

#Realizar la división entre el resultado de la resta y el resultado de la suma 
print("Se hara una división entre el resultado de la suma y el resultado de la resta.")
divRes = resultado1 / restaFloat
print(f"El resultado de divir {resultado1} entre {restaFloat} es: {divRes}")

#Se hará la definición de 4 números complejos.
print("    ")
print("Los 4 números complejos definidos son:")
print("El primer número compejo definido es: ", complex(comp1))
print("El segundo número compejo definido es: ", complex(comp2))
print("El tercer número compejo definido es: ", complex(comp3))
print("El cuarto número compejo definido es: ", complex(comp4))
#La definición de 4 números complejos se realizó con exito.
print("    ")

#Se hará la definición de las variables string
print("Se hizo la seleción de 4 frutas diferentes.")
print("La primera fruta solicitada es: ", fruta1)
print("La segunda fruta solicitada es: ", fruta2)
print("La tercera fruta solicitada es: ", fruta3)
print("La cuarta fruta solicitada es: ", fruta4)
#La definición de las variables se realizó con exito
print("    ")

# Tipos de datos booleanos (bool)

#Definición de variable que permita capturar desde teclado.
print("    ")
fruta = input('\033[1m' + "Digitar un nombre de una fruta. Frutas definidas: banana, mora, mango y pera  (se recomienda escribir todas las letras en minusculas): " + '\033[0m')

#Estructura de control if.
if fruta == fruta1:
    print("La fruta:", fruta1, "pertenece a nuestro compañero", nombre1)

if fruta == fruta2:
    print("La fruta:", fruta2, "pertenece a nuestra compañera", nombre2)

if fruta == fruta3:
    print("La fruta:", fruta3, "pertenece a nuestro compañero", nombre3)

if fruta == fruta4:
    print("La fruta:", fruta4, "pertenece a nuestro compañero", nombre4)
print("    ")

#Mensaje final.
print("La ejecución del programa ha terminado.")