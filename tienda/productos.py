class Prod():
    def __init__(self, producto, precio):
        self.__producto = producto
        self.__precio = precio

    def __str__(self):
        return f'Producto: {self.__producto}, Precio: {self.__precio}'

prod1=Prod('Monitor HP 24"', 500)
prod2=Prod('Teclado Redragon K551', 200)
prod3=Prod('Disco SSD Gigabyte 480Gb', 400)