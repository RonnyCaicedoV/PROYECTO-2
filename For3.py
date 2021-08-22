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
        
        long= len(nombre)
        for posi in range(long):
            print(nombre[posi],end= " ")
            
        for pos,elemen in enumerate(datos):
            print(pos," ",elemen)
        
        for n in numeros:
            print(n)
            
bucle1= For()
bucle1.uso_del_For()

