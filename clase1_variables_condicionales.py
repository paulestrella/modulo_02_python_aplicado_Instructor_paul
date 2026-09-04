# Variables y tipos de datos


# String (texto)
nombre = "Natasha"

# int
edad = 30

#float
altura = 1.63

# Bool
es_estudiante = True


print(nombre)
print(edad)
print(altura)
print(es_estudiante)

print(type(nombre), type(edad), type(altura), type(es_estudiante))



# entrada y salida de datos

nombre = input("Como te llamas? ")
edad = int(input("Cuantos años tienes? "))

print(f"Hola, {nombre}. el año que viene vas a tener {edad + 1} años.")

"""
pidanle a su compañero su temperatura corporal en grados Celsius.
convertir a numero y mostrara cuantos grados Fahrenheit equivale.
la formula: 'fahrenheit = celsius * 9/5 + 32'
"""

#Condicionales
temperatura_corporal = 19.5

if temperatura_corporal >= 32:
    print("temperatura alta")
elif temperatura_corporal >= 20:
    print("temparatura neutral")
else:
    print("temperatura fria")


# Ejercicio integrador de conceptos

edades = [55, 27, 28, 17, 30]

for edad in edades:
    if edad >=55:
        print(f"{edad} años: persona adulta")
    elif edad >=30:
        print(f"{edad} años: persona promedio")
    else:
        print(f"{edad} años: persona joven") 

        