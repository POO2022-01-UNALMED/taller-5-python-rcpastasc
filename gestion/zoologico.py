class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getNombre(self):
        return self._nombre

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getUbicacion(self):
        return self._ubicacion

    def getZona(self):
        return self._zonas

    def cantidadTotalAnimales(self):
        tot = 0
        for i in self._zonas:
            tot = tot + i.cantidadAnimales()
        return tot