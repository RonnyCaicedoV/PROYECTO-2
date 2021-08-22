class Sintaxis:
    frase= "Hola mi nombre es Ronny"
    def __init__(self,dato="Hola mi nombre es Ronny"):
          self.frase=dato
    def uso_de_variables(self):
        edad, __peso= 21, 50.3
        nombres= "Ronny Caicedo"
        Sexo= "Masculino"
        civil= True
        print("Civil es ={} y su tipo de dato es:{}".format(civil,type(civil)))
ejerc1 = Sintaxis()
ejerc1.uso_de_variables()
print(ejerc1.frase)