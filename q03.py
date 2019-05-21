##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
datos = open('data.csv', 'r').readlines()
datos = [fila[:-1].split("\t") for fila in datos]

letras = sorted(set([fila[0] for fila in datos]))

dicc = { letra : 0 for letra in letras}

for fila in datos:
    dicc[fila[0]] += int(fila[1])

for letra in letras:
    print ("{},{}".format(letra,dicc[letra]))


