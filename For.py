class For:
    def __init__(self,limit=0):
        self.n=limit
    
    def uso_del_For(self):
        nombre= "Victor"
        datos= ["Victor",46,True]
        numeros= (3,2,7,8,4.7)
        maestro= {"nombre":"Victor", "edad": 45, "facu": "faci"}
        notas= [(20,30),(30,40,60), (60,40)]
        Alumnos= [{"nombre": "Ronny", "final":80},{"nombre": "Juan","final":50},{"nombre":"Sergio","final":97}]
        
        for i in range(1,5):
            print("i={}".format(i))
        for i in range(9,3,-2):
            print("i={}".format(i))
bucle= For()
bucle.uso_del_For()

      
    
