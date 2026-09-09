# src/dominio/empleado.py

class Departamento:
    """Clase que representa a un departamento"""

    def __init__(self, nombre:str):
        self.nombre = nombre

    def mostrardatos(self) -> str:
        return f"Departamento: {self.nombre}"