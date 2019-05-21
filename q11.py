##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
datos = open('data.csv', 'r').readlines()
datos = [fila[:-1].split("\t") for fila in datos]

for fila in datos:
    print("{},{},{}".format( fila[0] , len(fila[3].split(",")) , len(fila[4].split(",")) ))