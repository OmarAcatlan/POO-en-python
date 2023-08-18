#ejemplo de una clase 'Celular'

class Celular():
    marca = "Samsung"
    modelo = "S23"
    camara = "48Mp"

celular1 = Celular
celular2 = Celular

print(celular1.camara, celular2.modelo, celular2.marca)

#propiedades o atributos de una clase
#se crean cuando se instancia un objeto de una clase
# self se auto referencia
#metodos self es importante para referenciar el metodo al objeto de la clase a la que se referencia
class Cualquier_celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Camara: {self.camara} Px"
    
    def llamada(self):
        print(f'Estas en una llamada con un: {self.modelo}')

    def fin_llamada(self):
        print(f'Fin de la llamada de tu: {self.modelo}')

celular3 = Cualquier_celular("Apple","Ifon 14", "32")
print(celular3)

celular3.llamada()
celular3.fin_llamada()
