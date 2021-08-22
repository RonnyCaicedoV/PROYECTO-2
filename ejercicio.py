x=int(input("Ingresa un numero entero: "))
if x < 1:
      x = 0
      print('Negativo cambiado a uno')
elif x == 1:
      print('Uno')
elif x == 2:
      print("Dos")
else:
      print("Ninguna opcion")

print("ok") if type(x) == int else print("-")

     
