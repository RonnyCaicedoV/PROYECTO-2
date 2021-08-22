#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. 
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por 
# las tres ventas que realiza en el mes y el total que recibirá en el mes tomando
# en cuenta su sueldo base y sus comisiones.

class ejem2:
    def __init__(self):
        pass
    
    def totalrecibir(self):
        SalarioBasico= int(input("Ingrese su salario basico: "))
        Valor1= int(input("Ingrese primer valor: "))
        Valor2= int(input("Ingrese segundo valor: "))
        Valor3= int(input("Ingrese tercer valor: "))
        Totaldevalores= Valor1+Valor2+Valor3
        Comision= Totaldevalores*0.10
        Totalarecibir=SalarioBasico+Comision
        print("El total de sus valores es de: {} Su comision es de: {} Su Salario Basico incluida las comisiones es de: {}".format(Totaldevalores,Comision,Totalarecibir))
        
ej2= ejem2()
ej2.totalrecibir()
        