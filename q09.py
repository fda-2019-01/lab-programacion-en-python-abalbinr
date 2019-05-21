##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas y sin repetir letra) 
## de la primera  columna que aparecen asociadas a dicho valor de la 
## segunda columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'B', 'D', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
datos = open('data.csv', 'r').readlines()
datos = [fila[:-1].split("\t") for fila in datos]

valores = sorted(set([fila[1] for fila in datos]))

agrupamiento = [sorted(set([fila[0] for fila in datos if (valor == fila[1])])) for valor in valores]

for indice in range(len(valores)):
    tupla = (valores[indice] , agrupamiento[indice])
    print (tupla)
