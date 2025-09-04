"""
Operaciones CRUD para Hotel
===========================

Este módulo contiene todas las operaciones de base de datos
para las entidades Habitacion y Reserva.
"""

from sqlalchemy.orm import Session
from entities.Habitacion import Habitacion, HabitacionCreate, HabitacionUpdate
from entities.Reserva import Reserva, ReservaCreate, ReservaUpdate

class Hotel:
    """Clase para operaciones CRUD de Habitaciones y Reservas"""

    # ------------------- Habitaciones -------------------
    @staticmethod
    def crear_habitacion(session: Session, habitacion_data: HabitacionCreate) -> Habitacion:
        """Crea una nueva habitación"""
        habitacion = Habitacion(**habitacion_data.dict())
        session.add(habitacion)
        session.commit()
        session.refresh(habitacion)
        return habitacion

    @staticmethod
    def obtener_habitacion(session: Session, habitacion_id: int) -> Habitacion | None:
        """Obtiene una habitación por ID"""
        return session.query(Habitacion).filter(Habitacion.id == habitacion_id).first()

    @staticmethod
    def actualizar_habitacion(session: Session, habitacion_id: int, habitacion_data: HabitacionUpdate) -> Habitacion | None:
        """Actualiza una habitación existente"""
        habitacion = Hotel.obtener_habitacion(session, habitacion_id)
        if not habitacion:
            return None
        for field, value in habitacion_data.dict(exclude_unset=True).items():
            setattr(habitacion, field, value)
        session.commit()
        session.refresh(habitacion)
        return habitacion

    @staticmethod
    def eliminar_habitacion(session: Session, habitacion_id: int) -> bool:
        """Elimina una habitación"""
        habitacion = Hotel.obtener_habitacion(session, habitacion_id)
        if not habitacion:
            return False
        session.delete(habitacion)
        session.commit()
        return True

    # ------------------- Reservas -------------------
    @staticmethod
    def crear_reserva(session: Session, reserva_data: ReservaCreate) -> Reserva:
        """Crea una nueva reserva"""
        reserva = Reserva(**reserva_data.dict())
        session.add(reserva)
        session.commit()
        session.refresh(reserva)
        return reserva

    @staticmethod
    def obtener_reserva(session: Session, reserva_id: int) -> Reserva | None:
        """Obtiene una reserva por ID"""
        return session.query(Reserva).filter(Reserva.id == reserva_id).first()

    @staticmethod
    def actualizar_reserva(session: Session, reserva_id: int, reserva_data: ReservaUpdate) -> Reserva | None:
        """Actualiza una reserva existente"""
        reserva = Hotel.obtener_reserva(session, reserva_id)
        if not reserva:
            return None
        for field, value in reserva_data.dict(exclude_unset=True).items():
            setattr(reserva, field, value)
        session.commit()
        session.refresh(reserva)
        return reserva

    @staticmethod
    def eliminar_reserva(session: Session, reserva_id: int) -> bool:
        """Elimina una reserva"""
        reserva = Hotel.obtener_reserva(session, reserva_id)
        if not reserva:
            return False
        session.delete(reserva)
        session.commit()
        return True
