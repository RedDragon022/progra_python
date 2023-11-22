
def convertir_base_13_a_5(numero_base_13):
    # Convertir el número de base 13 a decimal
    decimal = int(str(numero_base_13), 13)

    # Convertir el decimal a base 5
    resultado_base_5 = ""
    while decimal > 0:
        residuo = decimal % 5
        if residuo > 4:
            # Convertir dígitos mayores a 4 a letras
            letra = chr(ord('A') + residuo - 5)
            resultado_base_5 = letra + resultado_base_5
        else:
            resultado_base_5 = str(residuo) + resultado_base_5
        decimal //= 5

    return resultado_base_5

# Función para cambiar números por letras en el rango 10-19
def cambiar_numeros_por_letras(numero):
    if 10 <= numero <= 19:
        return chr(ord('A') + numero - 10)
    else:
        return str(numero)

# Bucle principal
while True:
    numero_base_13 = input("Ingrese un número en base 13 (o 'salir' para terminar): ")

    if numero_base_13.lower() == 'salir':
        break

    try:
        resultado_base_5 = convertir_base_13_a_5(numero_base_13)
        resultado_con_letras = ''.join([cambiar_numeros_por_letras(int(digito)) for digito in resultado_base_5])
        print(f"El número {numero_base_13} en base 5 es: {resultado_con_letras}")
    except ValueError:
        print("Error: Ingrese un número válido en base 13.")

