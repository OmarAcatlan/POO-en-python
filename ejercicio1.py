#crea un programa que solicite datos de un estudiante
class Estudiante:
    def __init__(self, nombre, edad, grado, matricula, carrera, promedio):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.matricula = matricula
        self.carrera = carrera
        self.promedio = promedio
    
    def estudiar(self):
        print('Estas inscrito!...')

    @classmethod
    def agregar_estudiante(cls):
        print("Ingresa los datos:\n") 
        nombre = input("Nombre \n")
        edad   = input("edad \n")
        grado  = input("grado \n")
        matricula = input("matricula \n")
        carrera   = input("carrera \n")
        promedio  = input("promedio \n")
        return  cls(nombre, edad, grado, matricula, carrera, promedio)

    def imprimir_estudiante(self):
        return f"""DATOS DEL ESTUDIANTE:\n\n 
                    Nombre: {self.nombre}\n 
                    Edad: {self.edad}\n 
                    Grado: {self.grado}\n 
                    Matricula: {self.matricula}\n 
                    Carrera: {self.carrera}\n 
                    Promedio: {self.promedio}\n"""

    
#Creamos un estudiante, usando el constructor
estudiante1 = Estudiante('Juan Jimenez',
                         18,'5to semestre',
                         421043394, 'Derecho',
                         8.5)

print(estudiante1.imprimir_estudiante())

estudiante2 = Estudiante.agregar_estudiante()
print(estudiante2.imprimir_estudiante())


while True:
    print('deseas inscribirte para este semestre, escribe SI o No')
    inscrito = input()
    if(inscrito.lower() == 'si'):
        estudiante2.estudiar()
        break
    elif(inscrito.lower() == 'no'):
        print('no te has inscrito para este semestere')
        break