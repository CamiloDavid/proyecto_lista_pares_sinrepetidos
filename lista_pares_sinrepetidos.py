lista_numeros = []

while True:
    num = int(input('Ingresa un numero: '))
    if num % 2 == 0:
        if len(lista_numeros) == 0:
            lista_numeros.append(num)
            # print(lista_numeros)
        else:
            valor = num in lista_numeros
            # print(f'{valor}: {num} en lista')
            if not valor:
                lista_numeros.append(num)
                # print(lista_numeros)
            # else:
                # print(f'{num} ya estaba en la lista')
    # else: 
        # print('Numero impar, no se añade a la lista')
    respuesta = input('Deseas ingresar otro número ? : ')

    if respuesta.lower() == 'no':
        break
    else:
        continue

print(f'Lista completa de pares sin repetir: \n{lista_numeros}')