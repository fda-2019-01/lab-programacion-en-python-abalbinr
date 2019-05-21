##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
datos = open('data.csv', 'r').readlines()
datos = [fila[:-1].split("\t") for fila in datos]

registros = [fila[0] for fila in datos]

letras = sorted(set(registros))

for letra in letras:
    print ("{},{}".format(letra, registros.count(letra)))
    
