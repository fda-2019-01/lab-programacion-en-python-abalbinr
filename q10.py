##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
datos = open('data.csv', 'r').readlines()
datos = [fila[:-1].split("\t") for fila in datos]

columna5 = [fila[4].replace(":",",").split(",") for fila in datos]

agrupamiento = []
for fila in columna5:
    for i in range(1,len(fila)+1):
        if (i%2 != 0):
            agrupamiento += [fila[i-1]]

valoresUnicos = sorted(set(agrupamiento))

for valor in valoresUnicos:
    print ("{},{}".format(valor,agrupamiento.count(valor)))
            
