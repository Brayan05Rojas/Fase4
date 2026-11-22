
from clientes import Cliente
from servicios import Servicio
from excepciones import (
    ErrorReserva,
    ReservaInvalida,
    ServicioNoDisponible
)


class Reserva:
    """
    Gestiona las reservas realizadas por los clientes
    de la empresa Software FJ.
    """

    def __init__(self, identificador, cliente, servicio, duracion):

        if not identificador:
            raise ReservaInvalida(
                "El identificador de la reserva es obligatorio."
            )

        if not isinstance(cliente, Cliente):
            raise ReservaInvalida(
                "Debe proporcionar un cliente válido."
            )

        if not isinstance(servicio, Servicio):
            raise ReservaInvalida(
                "Debe proporcionar un servicio válido."
            )

        servicio.validar_parametros(duracion)

        self.__identificador = identificador
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = servicio.calcular_costo(duracion)

    @property
    def identificador(self):
        return self.__identificador

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self):
        """
        Confirma una reserva que se encuentra pendiente.
        """
        if self.__estado != "Pendiente":
            raise ReservaInvalida(
                "Solamente se pueden confirmar reservas pendientes."
            )

        self.__estado = "Confirmada"
        return "La reserva ha sido confirmada correctamente."

    def cancelar(self):
        """
        Cancela una reserva pendiente o confirmada.
        """
        if self.__estado == "Cancelada":
            raise ReservaInvalida(
                "La reserva ya se encuentra cancelada."
            )

        self.__estado = "Cancelada"
        return "La reserva ha sido cancelada correctamente."

    def procesar(self):
        """
        Procesa la reserva y controla los posibles errores.
        """
        try:
            if self.__estado != "Pendiente":
                raise ReservaInvalida(
                    "La reserva no está disponible para procesarse."
                )

            self.__costo = self.__servicio.calcular_costo(
                self.__duracion
            )

            self.confirmar()

        except ReservaInvalida:
            raise

        except Exception as error:
            raise ErrorReserva(
                "No fue posible procesar la reserva."
            ) from error

        else:
            return "Reserva procesada correctamente."

        finally:
            print(
                f"Finalizó el intento de procesamiento "
                f"de la reserva {self.__identificador}."
            )

    def obtener_informacion(self):
        """
        Muestra la información completa de la reserva.
        """
        return (
            f"Reserva: {self.identificador}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion} horas\n"
            f"Costo: ${self.costo:,.2f}\n"
            f"Estado: {self.estado}"
        )
