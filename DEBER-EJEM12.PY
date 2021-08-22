#Determinar si un número entero proporcionado por el usuario es primo. Un número
# primo es un entero que no tiene más divisores que él mismo y la unidad. 
# Elaborar Pseudocódigo:


class tarea:
    def __init__(self):
        pass
    def numeroprimo(self):
        divisor, num, res= 0,0,0
        primo = True
        divisor = 2
        num = int(input("Digite un numero:"))
        while divisor < num:
            res = num/2
            if res<0:
                divisor = divisor+1
                print("f")
            if primo == True:
                print("El numero :{} no es primo".format(num))
        else: 
            print("El numero:",num,"no es primo:")
                
                   
tarea = tarea()
tarea.numeroprimo()   