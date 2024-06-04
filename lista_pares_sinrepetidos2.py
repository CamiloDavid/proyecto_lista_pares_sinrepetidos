
# averigua las posiciones contando desde cero, si el dato a buscar no se encuentra devuelve None
def averiguar_posicion(lista, num):
    # print(f'La longitud de la lista es: {len(lista)}')
    pos = None
    for i in range(len(lista)):
        if lista[i] == num:
            pos = i
            break
    return pos

def respuesta_ingresar_datos():
    resp = None
    while True:
        resp = input('Deseas ingresar más números (si/no): ')
        resp = resp.lower()
        if resp == 'si' or resp == 'no':
            break
        else:
            print('Ingresaste una respuesta incorrecta, vuelve a responder')
    return resp

def mostrar_lista(lista):
    if len(lista) > 0:
        for elemento in lista:
            print(elemento , end =' ')
    else:
        print(f'Lista vacía: {lista}')


pares = []  # creo una lista vacía
while True:
    num = int(input('Ingresa un número: '))
    if num % 2 == 0:
        # print(f'{num} es par')
        if averiguar_posicion(pares, num) == None:
            # print(f'{num} aún no está en la lista')
            pares.append(num)
            # print(f'Lista hasta el momento:\n{pares}')
        else:
            print(f'{num} ya estaba en la lista de pares, termina ingreso de números')
            break
    # else:
        # print(f'{num} no es par, no se llena en la lista')
        
    if respuesta_ingresar_datos() == 'no':
        break
    else:
        continue

print('\nLista de Pares Sin Repetidos: '.center(50,'-'))
mostrar_lista(pares)




# Pruebas de las funciones

# primera función aveiguar posición de un elemento en una lista
# lista = [10,7,8,7,5,4,10,2,0,8]
# num = 10
# lista = []

# print(f'La posición del {num} es: {averiguar_posicion(lista, num)}')

# segunda función respuesta_ingresar_datos
# print(f'La respuesta fue: {respuesta_ingresar_datos()}')

# tercera función mostrar_lista
# lista = []
# mostrar_lista(lista)
# pares = [10,7,8,7,5,4,10,2,0,8]


