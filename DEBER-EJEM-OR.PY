#Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos 
# obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga 
# una calificación mayor que 90 en cualquiera de los exámenes es aceptado; 
# en caso contrario es rechazado.

class Tarea ():
    def __init__(self):
        pass
    
    def cond_or(self):
     c1= int(input("Esciba la nota de su primer examen: "))
     c2= int(input("Esciba la nota de su segundo examen: "))
     if c1 >= 90 or c2 >= 90:
      print("Felicidades usted ha sido  aceptado!")
    
     else: print("Lo sentimos usted ha sido rechazado")