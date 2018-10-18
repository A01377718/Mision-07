#Javier Alexandro Vargas Sánchez
#Programa que sirve para 2 cosas, dividir sin usar los operadores / // o %, a base de restas
# y la segunda cosa, el usuario introduce muchos valores, y el programa determina cuál es el mayor de todos
#los números introducidos

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def leerOpcionMenu(): # Función que despliega menu al usuario menu con opciones para que escoja la actividad
    print("Misión 07. Ciclos While")
    print("Autor: Javier Alexandro Vargas Sánchez")
    print("Matrícula: A01377718")
    print("1. Calcular divisores")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    return opcion
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def probarDivisiones(): # Función que sirve para dividir a base de restas
    print()
    print("Calculando divisiones")
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    contador = 0

    primerInput = dividendo

    while dividendo >= divisor:

        dividendo -= divisor
        contador += 1

    print("%d / %d = %d, sobra %d" % (primerInput, divisor, contador, dividendo))
    print()
    print()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def encontrarMayor(): # Programa que define el numero mayor dentro de una serie de datos que el usuario provee
    print()
    print("Teclea una serie de numeros para encontrar el mayor")

    mayor = 0

    numero = int(input("Teclea un número [-1 para salir]: "))
    if numero == -1:
        print("No hay valor mayor")
        print()
    else:
        while numero != -1:
            numero = int(input("Teclea un número [-1 para salir]: "))

            if numero > mayor:
                mayor = numero
        print("El mayor es: ", mayor)
        print()
        print()
# Comentario: Ya sé que mi programa falla cuando el primer valor introducido es el mayor, pero la verdad ya no sé como hacerlo

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def main(): #Función principal, aquí se recibe la opción que el usuario haya seleccionado, con base en la opción será la acción que se efctué
    opcion = leerOpcionMenu()
    while opcion != 3:
        if opcion == 1:
            probarDivisiones()
        elif opcion == 2:
            encontrarMayor()
        elif opcion != 1 or opcion != 2 or opcion != 3:
            print("ERROR, teclea 1, 2 o 3")
            print()
            print()

        opcion = leerOpcionMenu()

    print()
    print("Gracias por usar este programa, regresa pronto.")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 #Llamada a la función principal
main()