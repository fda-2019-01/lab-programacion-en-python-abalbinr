##
## Imprima la suma de la segunda columna.
##
datos = open('data.csv', 'r').readlines()
datos = [fila[:-1].split("\t") for fila in datos]
    
contador = 0
for fila in datos:
    contador += int(fila[1])
    
print(contador)