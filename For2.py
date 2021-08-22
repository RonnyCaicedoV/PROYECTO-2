class For:
    def __init__(self,limit=8):
        self.n=limit
    
    def uso_del_For(self):
        nombre= "Victor"
        datos= ["Victor",46,True]
        numeros= (3,2,7,8,4.7)
        maestro= {"nombre":"Victor", "edad": 45, "facu": "faci"}
        notas= [(20,30),(30,40,60), (60,40)]
        Alumnos= [{"nombre": "Ronny", "final":80},{"nombre": "Juan","final":50},{"nombre":"Sergio","final":97}]
        
        for i in range(4,self.n,4):
            print("i={}".format(i),end=" ")
            
bucle1= For()
bucle1.uso_del_For()

bucle2= For(10)
bucle2.uso_del_For()