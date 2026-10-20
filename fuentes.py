import csv
import json

class FuenteDatos:
    """Clase base abstracta para la lectura de datos."""
    def cargar(self, ruta):
        # Lanza un error si alguien intenta usar la clase base directamente
        raise NotImplementedError("Este método debe ser implementado por las clases hijas")

class FuenteCSV(FuenteDatos):
    """Implementación para cargar datos desde un archivo CSV."""
    def cargar(self, ruta):
        datos = []
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append(fila)
        return datos

class FuenteJSON(FuenteDatos):
    """Implementación para cargar datos desde un archivo JSON."""
    def cargar(self, ruta):
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            # json.load lee el archivo y lo convierte automáticamente en una lista de diccionarios
            datos = json.load(archivo)
        return datos