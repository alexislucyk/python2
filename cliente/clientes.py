class Clientes():
    def __init__(self, nombre, apellido, dni):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni

    def comprar(self, producto, cant, precio):
        self.__producto=producto
        self.__cant=cant
        self.__precio=precio


