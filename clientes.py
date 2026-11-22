
from entidades import Entidad


class Cliente(Entidad):
    """
    Representa un cliente registrado en Software FJ.
    Hereda los atributos y métodos de Entidad.
    """

    def __init__(self, identificador, nombre, correo, telefono):

        super().__init__(identificador, nombre)

        if not correo or "@" not in correo or "." not in correo:
            raise ValueError("El correo electrónico no es válido.")

        if not telefono or not telefono.isdigit():
            raise ValueError("El teléfono debe contener solamente números.")

        if len(telefono) < 7 or len(telefono) > 15:
            raise ValueError("La longitud del teléfono no es válida.")

        self.__correo = correo.strip().lower()
        self.__telefono = telefono

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def obtener_informacion(self):
        """
        Devuelve la información general del cliente.
        """
        return (
            f"ID: {self.identificador} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )

    def actualizar_telefono(self, nuevo_telefono):
        """
        Permite actualizar el teléfono después de validarlo.
        """
        if not nuevo_telefono or not nuevo_telefono.isdigit():
            raise ValueError("El nuevo teléfono no es válido.")

        if len(nuevo_telefono) < 7 or len(nuevo_telefono) > 15:
            raise ValueError("La longitud del teléfono no es válida.")

        self.__telefono = nuevo_telefono
