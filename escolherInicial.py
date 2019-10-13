from pokemon import *
from pessoa import *

class escolherPokemonInicial:
    def __init__(self, player):

        self.player = player
        
        print("Olá {}, você pode escolher agora o pokemon que irá lhe acompanhar nessa jornada!".format(self.player))

        pikachu = PokemonEletrico("Pikachu", level=1)
        charmander = PokemonFogo("Charmander", level=1)
        squirtle = PokemonAgua("Squirtle", level=1)

        print("Você possui 3 escolhas: ")
        print("1 -", pikachu)
        print('2 -', charmander)
        print('3 -', squirtle)

        while True:
            escolha = input("Escolha o seu Pokemon: ")
            if escolha == '1' or escolha == 'pikachu' or escolha == "Pikachu":
                self.player.capturar(pikachu)
                break
            elif escolha == '2' or escolha == 'charmander' or escolha == "Charmander":
                self.player.capturar(charmander)
                break
            elif escolha == '3' or escolha == 'squirtle' or escolha == "Squirtle":
                self.player.capturar(squirtle)
                break
            else: 
                print("Escolha invalída!")
