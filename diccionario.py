"""
    crear el siguiente diccionario
    person = {"name":"Alice", "age": 25}

    teniendo en cuenta el anterior diccionario:
    * Preguntar al usuario si:
        * Desea realizar la impresión de todo el diccionario o de alguna de sus keys
        * Si desea consultar alguna de sus keys, validar que la key que proporciona exista
        * Realizar la impresión según lo seleccionado

    Si ingreso tal key, mostrar su correspondiente valor
    sino mostrar las keys y values de todo el diccionario

"""
# def respuesta_todo_diccionario():
#     resp = None
#     while True:
#         resp = input('Deseas realizar impresion de todo el dicionario (si/no): ')
#         resp = resp.lower()
#         if resp == 'si' or resp == 'no':
#             break
#         else:
#             print('Ingresaste una respuesta incorrecta, vuelve a responder')
#     return resp

# def respuesta_key():
#     resp = None
#     while True:
#         resp = input('Deseas realizar impresion de una key del diccionario (si/no): ')
#         resp = resp.lower()
#         if resp == 'si' or resp == 'no':
#             break
#         else:
#             print('Ingresaste una respuesta incorrecta, vuelve a responder')
#     return resp

# función que busca si una key está o no en un diccionario, si está retorna true sino false

def buscar_key(diccionario, key):
    for termino in diccionario:
        if termino == key:
            return True
            break
    else:
        return False

def imprimir_diccionario(diccionario):
    for key, value in diccionario.items():
        print(key, value)


def imprimir_key():
    key = input('Cual es la llave que deseas consultar en el diccionario ?: ')
    if buscar_key(person, key):
        # si retorna true, si esta en el diccionaario
        # accedo a la key-value del diccionario, y la imprimo
        value = person[key]
        print(f'key= {key} : value= {value}')
    else:
        print(f'La llave que ingresaste: {key} no coincide con ninguna llave del diccionario')


person = {"name":"Alice", 
            "age": 25}


while True:

    print('\n----------- M E N U  D I C C I O N A R I O ------------')
    print('1. Imprimir todo el diccionario ')
    print('2. Imprimir la llave indicada, con su respectivo valor')
    print('3. Salir del menú')
    print('-------------------------------------------------------')

    opc = int(input('\nIngresa una opción: '))

    if opc == 1:
        print('----- Diccionario person -----')
        imprimir_diccionario(person)
        continue
    elif opc == 2:
        imprimir_key()
        continue
    elif opc == 3:
        print('Fue un gusto atenderte, adiooos =)')
        break
    else:
        print('Ingresaste una opción incorrecta')


# Prueba de las funciones

# función 1 buscar si una key está o no en un diccionario

# resp = buscar_key(person,'lastname')
# print(f'lastname está en el diccionario ?: {resp}')

# función 2 imprimir el diccionario, key-value por key-value
# imprimir_diccionario(person)

# función 3 imprimir_key
# imprimir_key()