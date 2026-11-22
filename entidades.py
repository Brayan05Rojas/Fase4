
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    dentro del sistema de gestión Software FJ.
    """

    def __init__(self, identificador, nombre):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self._identificador = identificador
        self._nombre = nombre.strip()

    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def obtener_informacion(self):
        """
        Método abstracto que deben implementar
        las clases que hereden de Entidad.
        """
        pass
