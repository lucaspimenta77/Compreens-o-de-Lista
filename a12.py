sublistas = [[1, 2, 10], [4, 11, 6], [43, 8, 22]]


lista_concatenada = [elemento for sublista in sublistas for elemento in sublista]

print(lista_concatenada)
