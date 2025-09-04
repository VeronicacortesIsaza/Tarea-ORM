from crud.Hotel import Hotel
from database.database import get_session_context
from entities.Habitacion import Habitacion
from entities.Reserva import Reserva, ReservaCreate

hotel = Hotel()
def menu():
    while True:
        print("\n===== SISTEMA DE RESERVAS DE HOTEL =====")
        print("1. Reservar habitación")
        print("2. Cancelar reserva")
        print("3. Mostrar reservas")
        print("4. Salir")
        
        while True:
            opcion = input("Elige una opción (1-4): ")
            if opcion.isdigit() and 1 <= int(opcion) <= 4:
                opcion = int(opcion)
                break
            print("Opción inválida. Intente de nuevo.")

        if opcion == 1:
            print("\n==========")
            print("Reservar habitación")
            cliente = input("Nombre del cliente: ")
            documento = input("Documento del cliente: ")
            while True:
                noches = input("Número de noches: ")
                if noches.isdigit() and int(noches) > 0:
                    noches = int(noches)
                    break
                print("Opción inválida. Intente de nuevo.")

            print("Tipos de habitación:")
            print("1. Estándar ($200000/noche)")
            print("2. Suite ($300000/noche)")
            print("3. Premium ($450000/noche)")
            while True:
               tipo = input("Seleccione tipo: ")
               if tipo.isdigit() and 1 <= int(tipo) <= 3:
                   tipo = int(tipo)
                   break
               print("Opción inválida. Intente de nuevo.")

            if tipo == 1:
                tipo = "Estándar"
            elif tipo == 2:
                tipo = "Suite"
            elif tipo == 3:
                tipo = "Premium"
            else:
                print("Tipo inválido.")
                continue

            with get_session_context() as session:
                habitacion = session.query(Habitacion).filter_by(tipo=tipo, disponible=True).first()

                if habitacion:
                    reserva_data = ReservaCreate(
                        cliente=cliente,
                        documento=documento,
                        noches=noches,
                        habitacion_id=habitacion.id
                    )
                    reserva = hotel.crear_reserva(session, reserva_data)
                    print("Reserva realizada con éxito:", reserva)
                else:
                    print("No hay habitaciones disponibles de ese tipo.")

        elif opcion == 2:
            documento = input("Ingrese el documento del cliente para cancelar la reserva: ")
            with get_session_context() as session:
                hotel = Hotel()
                reserva = session.query(Reserva).filter_by(documento=documento).first()
                if reserva and hotel.eliminar_reserva(session, reserva.id):
                    print("Reserva cancelada correctamente.")
                else:
                    print("No se encontró una reserva con ese documento.")

        elif opcion == 3:
            with get_session_context() as session:
                reservas = session.query(Reserva).all()
                if not reservas:
                    print("No hay reservas activas.")
                else:
                    for r in reservas:
                        print(r)

        elif opcion == 4:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
