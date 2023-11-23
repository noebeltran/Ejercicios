class persona:

    def __init__(self,unNombre):
        self.nombre = unNombre
        self.edad = 0

    def dametunombre(self):
        return self.nombre

    def dametuedad(self):
        return self.edad

    def __str__(self):
        return f"<{self.nombre};{self.edad}>"
    
    def __int__(self):
        return 11

class juguete:
    
    def __init__(self, nombre="luis", edad=22):
        self.estado = list()

    def hablameDeTi(self):
        print(self.estado)


p1 = persona("juan")
print(p1)
print(p1.__int__())
#nombre = p1.dametunombre()
#print(f"hola, {nombre}, veo tu edad de {p1.dametuedad()}")

p2 = persona("luis",40)
print(p2)
#nombre2 = p2.dametunombre()
#print(f"hola, {nombre2}, veo tu edad de {p2.dametuedad()}")

j = juguete("juan",33)
print(juguete)





