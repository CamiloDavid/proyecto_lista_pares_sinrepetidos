lista_numeros = [2,2,4,6,6,8,8]
# lista_sin_repe = []
lista_canti_repes = []

# while True:
#     num = int(input('Ingresa un numero: '))
#     if num % 2 == 0:
#         lista_numeros.append(num)

#     respuesta = input('Deseas ingresar otro número ? : ')

#     if respuesta.lower() == 'no':
#         break
#     else:
#         continue

# print(f'Lista completa de pares repetidos: \n{lista_numeros}')

# # recorro la lista de todos los pares
# for num in lista_numeros:
#     if len(lista_sin_repe) == 0:
#         lista_sin_repe.append(num)
#     else:
#         if not num in lista_sin_repe:
#             lista_sin_repe.append(num)
#         else:
#             print(f'{num} ya estaba en la lista')

# print(f'Lista de pares sin repetidos: \n{lista_sin_repe}')



# recorro la lista de todos los pares
for num in lista_numeros:
    if len(lista_canti_repes) == 0:
        valor = num
        cont = 0
        for i in lista_numeros:
            if valor == i:
                cont+=1
        lista_canti_repes.append(cont)
    else:
        

print(f'Lista con la cantidad de repeticiones:\n{lista_canti_repes}')


