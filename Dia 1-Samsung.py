
def convertir_base_7_a_19(numero_base_7):
    # Convertir el número de base 7 a decimal
    decimal = int(str(numero_base_7), 7)

    # Convertir el decimal a base 19
    resultado_base_19 = ""
    while decimal > 0:
        residuo = decimal % 19
        if residuo > 9:
            # Convertir dígitos mayores a 9 a letras
            letra = chr(ord('A') + residuo - 10)
            resultado_base_19 = letra + resultado_base_19
        else:
            resultado_base_19 = str(residuo) + resultado_base_19
        decimal //= 19

    return resultado_base_19

# Función para cambiar números por letras en el rango 10-19
def cambiar_numeros_por_letras(numero):
    if 10 <= numero <= 19:
        return chr(ord('A') + numero - 10)
    else:
        return str(numero)

# Bucle principal
while True:
    numero_base_7 = input("Ingrese un número en base 7 (o 'salir' para terminar): ")

    if numero_base_7.lower() == 'salir':
        break

    try:
        resultado_base_19 = convertir_base_7_a_19(numero_base_7)
        resultado_con_letras = ''.join([cambiar_numeros_por_letras(int(digito)) for digito in resultado_base_19])
        print(f"El número {numero_base_7} en base 19 es: {resultado_con_letras}")
    except ValueError:
        print("Error: Ingrese un número válido en base 7.")
