import time

from blackjack.model import Blackjack


class BlackjackConsole:

    def __init__(self):
        self.blackjack: Blackjack = Blackjack()
        self.opciones ={"1": self.iniciar_nuevo_juego, "0": self.salir}

    @staticmethod
    def mostrar_menu():
        titulo = "BLACK JACK"
        print(f"\n{titulo:-^30}")
        print("1. Iniciar un nuevo juego")
        print("0. salir")
        print(f"{"_":_^30}")

    def ejecutar_app(self):
        print("\nBIENVENID@ A UN NUEVO JUEGO DE BLACKJACK")
        self.registrar_usuario()
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")


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
        self.mostrar_mano(self.blackjack.cupier.mano, self.blackjack.jugador.mano)

        if not self.blackjack.jugador.mano.es_blackjack():
            self.hacer_jugada_del_jugador()
        else:
            self.finalizar_juego()

    def hacer_jugada_del_jugador(self):
        while not self.blackjack.jugador.mano.calcular_valor() > 21:
            respuesta = input("¿Deseas otra carta? (s/n): ")
            if respuesta == "s":
                self.blackjack.repartir_carta_a_jugador()
                self.mostrar_mano(self.blackjack.cupier.mano, self.blackjack.jugador.mano)
            elif respuesta == "n":
                break

        if self.blackjack.jugador.mano.calcular_valor() > 21:
            self.finalizar_juego()
        else:
            self.hacer_jugada_de_la_casa()

    def hacer_jugada_de_la_casa(self):
        print("\nAHORA ES EL TURNO DE LA CASA\n")
        self.blackjack.destapar_mano_de_la_casa()
        self.mostrar_mano(self.blackjack.cupier.mano, self.blackjack.jugador.mano)

        time.sleep(3)

        while self.blackjack.casa_puede_pedir():
            print("\nLA CASA PIDE OTRA CARTA\n")
            time.sleep(1)
            self.blackjack.repartir_carta_a_la_casa()
            self.mostrar_mano(self.blackjack.cupier.mano, self.blackjack.jugador.mano)
            time.sleep(2)

    def finalizar_juego(self):
        print(f"\n{'RESULTADOS':_^30}\n")
        nombre_jugador = self.blackjack.jugador.nombre
        if self.blackjack.jugador_gano():
            if self.blackjack.jugador.mano.es_blackjack():
                print(f"¡¡¡BLACKJACK!!!\n¡FELICITACIONES {nombre_jugador}! HAS GANADO EL JUEGO\n")
            else:
                print(f"¡FELICITACIONES {nombre_jugador}! HAS GANADO EL JUEGO\n")
        elif self.blackjack.casas_gano():
            print(f"¡LO SENTIMOS {nombre_jugador}! LA CASA GANA\n")
        elif self.blackjack.hay_empate():
            print(f"¡HAY UN EMPATE!\n")

            self.blackjack.finalizar_juego()
            print(f"AHORA TIENES {self.blackjack.jugador.fichas} FICHAS\n")

        self.blackjack.finalizar_juego()
        print(f"AHORA TIENES {self.blackjack.jugador.fichas} FICHAS\n")

    @staticmethod
    def mostrar_mano(mano_casa, mano_jugador):
        print(f"\n{'MANO DE LA CASA':<15}\n{str(mano_casa):<15}")
        print(f"{'VALOR: ' + str(mano_casa.calcular_valor()):<15}\n")
        print(f"\n{'TU MANO':<15}\n{str(mano_jugador):<15}")
        print(f"{'VALOR: ' + str(mano_jugador.calcular_valor()):<15}\n")


    @staticmethod
    def salir():
        print("¡GRACIAS POR JUGAR BLACKJACK!")
        exit()
