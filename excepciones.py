
# =====================================================
# EXCEPCIONES PERSONALIZADAS - SOFTWARE FJ
# =====================================================


class ErrorSistema(Exception):
    """
    Excepción general para los errores del sistema.
    """
    pass


class ErrorCliente(ErrorSistema):
    """
    Se utiliza cuando ocurre un problema con un cliente.
    """
    pass


class ErrorServicio(ErrorSistema):
    """
    Se utiliza cuando ocurre un problema con un servicio.
    """
    pass


class ErrorReserva(ErrorSistema):
    """
    Se utiliza cuando ocurre un problema con una reserva.
    """
    pass


class ServicioNoDisponible(ErrorServicio):
    """
    Se genera cuando se intenta utilizar un servicio
    que no se encuentra disponible.
    """
    pass


class ReservaInvalida(ErrorReserva):
    """
    Se genera cuando una reserva no cumple
    las condiciones necesarias.
    """
    pass


class ClienteNoEncontrado(ErrorCliente):
    """
    Se genera cuando no existe el cliente solicitado.
    """
    pass
