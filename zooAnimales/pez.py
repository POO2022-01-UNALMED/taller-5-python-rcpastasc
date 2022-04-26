from zooAnimales.animal import Animal

class Pez(Animal):
    
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorescamas, cantidadaletas):
        super().__init__(nombre, edad, habitat, genero)
        self.setColorEscamas(colorescamas)
        self.setCantidadAletas(cantidadaletas)
        Pez._listado.append(self)

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    def movimiento(self):
        return "nadar"

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return  Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado