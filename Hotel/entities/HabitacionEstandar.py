from entities.Habitacion import Habitacion

class HabitacionEstandar(Habitacion):
    def tiene_tv_cable(self) -> bool:
        return True
