##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
datos = open('data.csv', 'r').readlines()
datos = [fila[:-1].split("\t") for fila in datos]

letras = sorted(set([letra for fila in datos for letra in fila[3].split(",")]))

dicc = { letra : 0 for letra in letras}

for fila in datos:
    for letra in fila[3].split(","):    
        dicc[letra] += int(fila[1])

for letra in letras:
    print ("{},{}".format(letra,dicc[letra]))


