#for in cadena- in(tupla)

frase = input("Ingrese frase:")
for indice in range(len(frase)):
    print(indice,'=',frase[indice])


for car in frase:
    if car in ("a","b","c","d","e","A","B","C","D","E"):
        continue
    else:
     cvoc=cvoc+1
print('cantidad vocales:{}'.format(cvoc))
