##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
datos = open('data.csv', 'r').readlines()
datos = [fila[:-1].split("\t") for fila in datos]

registrosMeses = [fila[2].split("-")[1] for fila in datos]

meses = sorted(set(registrosMeses))

for mes in meses:
    print ("{},{}".format(mes,registrosMeses.count(mes)))
    