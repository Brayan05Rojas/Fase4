
import logging

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipos, AsesoriaEspecializada
from reservas import Reserva


# =====================================================
# CONFIGURACIÓN DEL REGISTRO DE EVENTOS Y ERRORES
# =====================================================

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger("SoftwareFJ")


def registrar_evento(mensaje):
    logger.info(mensaje)


def registrar_error(mensaje):
    logger.error(mensaje)


def registrar_advertencia(mensaje):
    logger.warning(mensaje)


# =====================================================
# LISTAS PRINCIPALES DEL SISTEMA
# =====================================================

clientes = []
servicios = []
reservas = []


# =====================================================
# FUNCIONES DE GESTIÓN DE CLIENTES
# =====================================================

def registrar_cliente(identificador, nombre, correo, telefono):
    try:
        cliente = Cliente(identificador, nombre, correo, telefono)
        clientes.append(cliente)

        registrar_evento(
            f"Cliente registrado: {cliente.nombre}"
        )

        print("Cliente registrado correctamente.")
        print(cliente.obtener_informacion())

        return cliente

    except Exception as error:
        registrar_error(f"Error al registrar cliente: {error}")
        print(f"No fue posible registrar el cliente: {error}")
        return None


# =====================================================
# FUNCIONES DE GESTIÓN DE SERVICIOS
# =====================================================

def registrar_servicio(servicio):
    try:
        servicios.append(servicio)

        registrar_evento(
            f"Servicio registrado: {servicio.nombre}"
        )

        print("Servicio registrado correctamente.")
        print(servicio.obtener_informacion())

        return servicio

    except Exception as error:
        registrar_error(f"Error al registrar servicio: {error}")
        print(f"No fue posible registrar el servicio: {error}")
        return None


# =====================================================
# FUNCIONES DE GESTIÓN DE RESERVAS
# =====================================================

def crear_reserva(identificador, cliente, servicio, duracion):
    try:
        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            duracion
        )

        reservas.append(reserva)

        registrar_evento(
            f"Reserva creada: {reserva.identificador}"
        )

        print("Reserva creada correctamente.")
        print(reserva.obtener_informacion())

        return reserva

    except Exception as error:
        registrar_error(f"Error al crear reserva: {error}")
        print(f"No fue posible crear la reserva: {error}")
        return None


# =====================================================
# EJECUCIÓN DE PRUEBAS DEL SISTEMA
# =====================================================

def ejecutar_sistema():

    print("\n==========================================")
    print(" SISTEMA INTEGRAL DE GESTIÓN SOFTWARE FJ")
    print("==========================================\n")

    registrar_evento("Sistema Software FJ iniciado.")

    # OPERACIÓN 1: Registro de un cliente válido
    print("\n--- OPERACIÓN 1: CLIENTE VÁLIDO ---")
    cliente1 = registrar_cliente(
        "C001",
        "Carlos Pérez",
        "carlos@gmail.com",
        "3001234567"
    )

    # OPERACIÓN 2: Registro de un cliente con correo inválido
    print("\n--- OPERACIÓN 2: CLIENTE INVÁLIDO ---")
    registrar_cliente(
        "C002",
        "Laura Gómez",
        "correo_incorrecto",
        "3101234567"
    )

    # OPERACIÓN 3: Registro de una reserva de sala
    print("\n--- OPERACIÓN 3: SERVICIO DE SALA ---")
    sala = registrar_servicio(
        ReservaSala("S001", "Sala de reuniones", 50000)
    )

    # OPERACIÓN 4: Intento de crear un servicio con precio inválido
    print("\n--- OPERACIÓN 4: SERVICIO INVÁLIDO ---")
    try:
        registrar_servicio(
            ReservaSala("S002", "Sala inválida", -10000)
        )
    except Exception as error:
        registrar_error(f"Error al crear servicio: {error}")
        print(f"Servicio rechazado: {error}")

    # OPERACIÓN 5: Registro de alquiler de equipos
    print("\n--- OPERACIÓN 5: ALQUILER DE EQUIPOS ---")
    equipos = registrar_servicio(
        AlquilerEquipos("S003", "Alquiler de computadores", 30000)
    )

    # OPERACIÓN 6: Registro de asesoría especializada
    print("\n--- OPERACIÓN 6: ASESORÍA ESPECIALIZADA ---")
    asesoria = registrar_servicio(
        AsesoriaEspecializada("S004", "Asesoría informática", 70000)
    )

    # OPERACIÓN 7: Creación de una reserva válida
    print("\n--- OPERACIÓN 7: RESERVA VÁLIDA ---")
    reserva1 = None

    if cliente1 and sala:
        reserva1 = crear_reserva(
            "R001",
            cliente1,
            sala,
            2
        )

    # OPERACIÓN 8: Intento de reserva con duración inválida
    print("\n--- OPERACIÓN 8: RESERVA INVÁLIDA ---")

    if cliente1 and equipos:
        crear_reserva(
            "R002",
            cliente1,
            equipos,
            -3
        )

    # OPERACIÓN 9: Procesamiento de una reserva
    print("\n--- OPERACIÓN 9: PROCESAMIENTO ---")

    if reserva1:
        try:
            resultado = reserva1.procesar()
            print(resultado)
            registrar_evento("Reserva R001 procesada correctamente.")

        except Exception as error:
            registrar_error(f"Error al procesar reserva: {error}")
            print(f"Error durante el procesamiento: {error}")

    # OPERACIÓN 10: Cancelación y nuevo intento de procesamiento
    print("\n--- OPERACIÓN 10: CANCELACIÓN Y CONTROL DE ERROR ---")

    if reserva1:
        try:
            print(reserva1.cancelar())
            registrar_evento("Reserva R001 cancelada.")

            reserva1.procesar()

        except Exception as error:
            registrar_advertencia(
                f"Intento de procesar una reserva cancelada: {error}"
            )
            print(f"Operación controlada: {error}")

    # RESUMEN FINAL
    print("\n==========================================")
    print(" RESUMEN DEL SISTEMA")
    print("==========================================")

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas registradas: {len(reservas)}")

    registrar_evento("Ejecución del sistema finalizada.")

    print("\nEl sistema terminó su ejecución.")
    print("Los eventos y errores se guardaron en logs.txt.")


# =====================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# =====================================================

if __name__ == "__main__":
    ejecutar_sistema()
