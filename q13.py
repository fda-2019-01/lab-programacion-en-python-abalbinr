##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
datos = open('data.csv', 'r').readlines()
datos = [fila[:-1].split("\t") for fila in datos]

for fila in datos:
    lista = fila[4].replace(":",",").split(",")
    lista = [int(lista[i-1]) for i in range(1,len(lista)+1) if(i%2 == 0)]
    print("{},{}".format(fila[0],sum(lista)))
        
            