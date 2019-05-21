##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
datos = open('data.csv', 'r').readlines()
datos = [fila[:-1].split("\t") for fila in datos]

letras = sorted(set([fila[0] for fila in datos]))

agrupamiento = [[fila[1] for fila in datos if (fila[0] == letra)] for letra in letras]

for indice in range(len(letras)):
    print ("{},{},{}".format(letras[indice],max(agrupamiento[indice]),min(agrupamiento[indice])))
        
            
