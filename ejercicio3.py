#Función  con retorno de valores

def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)
listanotas = [2, 4, 6, 8, 10, 12, 14, 16, 20]
prom = promedio(listanotas)
print("Promedio: {} = {}".format(listanotas, prom))
