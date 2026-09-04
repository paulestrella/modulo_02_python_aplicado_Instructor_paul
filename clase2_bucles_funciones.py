# Bucle for
edades = [24, 31, 19, 45, 27]

suma = 0
for edad in edades:
    suma += edad

print("suma total:", suma)
print("Promedio:", suma / len(edades))


"""
ejercicio

con la misma lista que utilizamos "edades" contar cuantas edades son mayores o iguales a 30, utilizar el bucle "for" y una variable contadora.
variable contadora: es una variable que empieza en 0 y le suma 1 cada vez que se cumple la condicion. ejemplo: contador += 1

pista: necesitar combinar lo que vimos ahora con el bucle for con lo que ustedes aprendiendo en la clase pasada "condicionales"

"""

edades = [24, 31, 19, 45, 27]

contador = 0
for edad in edades:
    if edad >= 30:
        contador += 1

print("Cantidad de personas de 30 años o mas:", contador)


#Bucle While
contador = 1
while contador <= 5:
    print("vuelta - numero", contador)
    contador += 1



"""
ejercicio - while:

utilicen "while", hagan una cuenta regresiva desde 5 hasta 1 y al final impriman "Iniciamos"

"""

numero = 5
while numero >= 1:
    print(numero)
    numero -= 1

print("Iniciamos")

#Funciones
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

resultado = calcular_imc(150, 1.85)
print(f"IMC:{round(resultado, 2)}")


"""
escribir una funcion le llamaran "clasificar_imc(imc) que reciba un IMC y devuelva un texto: "bajo de peso" si es menor a 18.5. "peso normal" si esta entre 18.5 y 25
"sobrepeso" si esta entre 25 y 30, "obesidad" si es de 30 o mas. despues, llamar el "Resultado" de la funcion anterior.
"""

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo de peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

print(clasificar_imc(resultado))