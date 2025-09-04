"""
Inicialización de la base de datos
=================================

Este script crea todas las tablas necesarias y precarga
habitaciones estándar, suite y premium.
"""

from database.database import create_tables, get_session_context
from entities.Habitacion import Habitacion

def precargar_habitaciones():
    """Precarga habitaciones si la tabla está vacía"""
    with get_session_context() as session:
        if not session.query(Habitacion).first():
            # Estándar (101–199)
            for i in range(101, 200):
                session.add(Habitacion(numero=i, tipo="Estándar", precio=200000))
            # Suite (201–299)
            for i in range(201, 300):
                session.add(Habitacion(numero=i, tipo="Suite", precio=300000))
            # Premium (301–399)
            for i in range(301, 400):
                session.add(Habitacion(numero=i, tipo="Premium", precio=450000))
            
            session.commit()
            print("✅ Habitaciones precargadas")

if __name__ == "__main__":
    print("Creando tablas...")
    create_tables()
    print("✅ Tablas creadas correctamente")

    print("Precargando habitaciones...")
    precargar_habitaciones()
