class Cargo:
    Secuencia=0
    def __init__(self,des="Sin Cargo"):
        Cargo.Secuencia=Cargo.Secuencia+1
        self.codigo=Cargo.Secuencia
        self.descripcion=des
        
cargo1= Cargo("Profesor")
print("Cargo1", cargo1.Secuencia)
print(cargo1.codigo,cargo1.descripcion)

cargo2= Cargo("Decano")
print("Cargo2", cargo2.Secuencia)
print(cargo2.codigo,cargo2.descripcion)

cargo3= Cargo("Seguridad")
print("Cargo3", Cargo.Secuencia)
print(cargo3.codigo,cargo3.descripcion)