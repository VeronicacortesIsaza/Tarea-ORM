from entities.Habitacion import Habitacion

class HabitacionPremium(Habitacion):
    def beneficios_exclusivos(self) -> list[str]:
        return ["Jacuzzi privado", "Minibar incluido", "Vista panorámica"]
