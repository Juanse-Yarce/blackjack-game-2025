from blackjack.model import Blackjack


class BlackjackConsole:

    def __init__(self):
        self.blackjack: Blackjack = Blackjack()
        self.opciones ={"1": self.iniciar_nuevo_juego, "0": self.salir}

    @staticmethod
    def mostrar_menu(self):
        titulo = "BLACK JACK"
        print(f"\n{titulo:-^30}")
        print("1. Iniciar un nuevo juego")
        print("0. salir")
        print(f"{"_":_^30}")

    def ejecutar_app(self):
        print("\nBIENVENIDO A UN NUEVO JUEGO")
        self.registrar_usuario()
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opcion: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opcion valida")


    def registrar_usuario(self):
        nombre: str = input("Ingrese su nombre: ")
        self.blackjack.registrar_jugador(nombre)

    def recobir_apuesta_jugador(self) -> int:
        while True:
            apuesta = input("¿Cuantas fichas deseas apostar?")
            if apuesta.isdigit():
                apuesta = int(apuesta)
                if self.blackjack.jugador.tiene_fichas(apuesta):
                    return apuesta
                else:
                    print("No tienes suficientes fichas")
            else:
                print("Por favor ingresa el valor numerico")

    def iniciar_nuevo_juego(self):
        if self.blackjack.jugador.fichas == 0:
            print("Paila mi papa ya no hay con que apostar")
            return

        apuesta: int = self.recobir_apuesta_jugador()
        self.blackjack.iniciar_juego(apuesta)
        self.mostrar_manos(self.blackjack.cupier.mano, self.blackjack.jugador.mano)

    def mostrar_mano(self, mano_casa, mano_jugador):
        print(f"{"MANO DE LA CASA":<15}\n{str(mano_casa):<15}")
        print(f"{"VALOR: " + str(mano_casa.calcular_valor()):<15}\n")
        print(f"{"TU MANO: ":<15}\n{str(mano_jugador):<15}")
        print(f"{"VALOR: " + str(mano_jugador.calcular_valor()):<15}\n")

    def salir(self):
        pass
