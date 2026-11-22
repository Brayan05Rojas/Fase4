
from abc import abstractmethod
from entidades import Entidad


class Servicio(Entidad):
    """
    Clase abstracta que representa los servicios
    ofrecidos por la empresa Software FJ.
    """

    def __init__(self, identificador, nombre, precio_base):
        super().__init__(identificador, nombre)

        if not isinstance(precio_base, (int, float)) or isinstance(precio_base, bool):
            raise ValueError("El precio debe ser un valor numérico.")

        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero.")

        self._precio_base = float(precio_base)

    @property
    def precio_base(self):
        return self._precio_base

    def obtener_informacion(self):
        return self.describir_servicio()

    def describir_servicio(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Código: {self.identificador} | "
            f"Precio base: ${self.precio_base:,.2f}"
        )

    def calcular_total(self, duracion, impuesto=0, descuento=0):
        """
        Calcula el costo aplicando impuestos y descuentos porcentuales.
        """
        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool):
            raise ValueError("El impuesto debe ser numérico.")

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool):
            raise ValueError("El descuento debe ser numérico.")

        if impuesto < 0:
            raise ValueError("El impuesto no puede ser negativo.")

        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        subtotal = self.precio_base * duracion
        valor_impuesto = subtotal * (impuesto / 100)
        valor_descuento = subtotal * (descuento / 100)

        return subtotal + valor_impuesto - valor_descuento

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass


# =====================================================
# SERVICIO 1: RESERVA DE SALAS
# =====================================================

class ReservaSala(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        return self.calcular_total(duracion, impuesto, descuento)

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise ValueError("La duración debe ser numérica.")

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

    def describir_servicio(self):
        return (
            f"Reserva de salas: {self.nombre} | "
            f"Tarifa por hora: ${self.precio_base:,.2f}"
        )


# =====================================================
# SERVICIO 2: ALQUILER DE EQUIPOS
# =====================================================

class AlquilerEquipos(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        return self.calcular_total(duracion, impuesto, descuento)

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise ValueError("La duración del alquiler debe ser numérica.")

        if duracion <= 0:
            raise ValueError("El tiempo de alquiler debe ser mayor que cero.")

    def describir_servicio(self):
        return (
            f"Alquiler de equipos: {self.nombre} | "
            f"Tarifa por hora: ${self.precio_base:,.2f}"
        )


# =====================================================
# SERVICIO 3: ASESORÍA ESPECIALIZADA
# =====================================================

class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        return self.calcular_total(duracion, impuesto, descuento)

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise ValueError("La duración de la asesoría debe ser numérica.")

        if duracion <= 0:
            raise ValueError("La duración de la asesoría debe ser mayor que cero.")

    def describir_servicio(self):
        return (
            f"Asesoría especializada: {self.nombre} | "
            f"Tarifa por hora: ${self.precio_base:,.2f}"
        )

