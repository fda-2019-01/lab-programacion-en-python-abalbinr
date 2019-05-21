##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
datos = open('data.csv', 'r').readlines()
datos = [fila[:-1].split("\t") for fila in datos]

agrupamiento = [i.split(":") for fila in datos for i in fila[4].split(",")]

letras = sorted(set([lista[0] for lista in agrupamiento]))

dicc = {letra : [] for letra in letras}

for lista in agrupamiento:
    dicc[lista[0]] +=  [int(lista[1])]

for letra in letras:
    print ("{},{},{}".format(letra,min(dicc[letra]),max(dicc[letra])))


    

        