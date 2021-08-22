class Sintaxis:
    frase= "Hola mi nombre es Ronny"
    def __init__(self,dato="Hola mi nombre es Ronny"):
          self.frase=dato
    def uso_de_variables(self):
        edad, __peso= 27, 50.3
        nombres= "Kerly Palacios"
        Sexo= "Masculino"
        civil= True
        Estudiante=()
        Estudiante= ("rcaicedov3", 246,"rommel2511@gmail.com", True)
        materias = ["algoritmo y logica de programacion", "java"]
        materias[1]= "Python"
        materias.append("Calculo")
        Maestro={}
        Maestro= {"nombre": "Kerly", "edad": "27"}
        Maestro["edad"]= 30
        Maestro["profesion"]= "docente"
        print(nombres,nombres[0],nombres[0:3],nombres[-1])
        print(Estudiante,Estudiante[0],Estudiante[0:2],Estudiante[-1])
        print(materias,materias[2:],materias[:1],materias[::],materias[-2:])
        
        
    
        
        
ejerc1 = Sintaxis()
ejerc1.uso_de_variables()
