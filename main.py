import pickle

from pessoa import *
from pokemon import *
from escolherInicial import escolherPokemonInicial


def SalvarJogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print("Erro ao salvor o jogo")
        print(error)

def CarregarJogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("---------------------------------------")
            print("Load feito com sucesso!")
            print('---------------------------------------')
            return player
    except Exception as error:
        print("\nSave não encontrado\n")

   
if __name__ == "__main__":
    print("-------------------------------------")
    print("BEM VINDO AO POKEMON RPG DE TERMINAL!")
    print("-------------------------------------")

    player = CarregarJogo()

    if not player:
        nome = input("Qual é o seu nome: ")
        player=Player(nome)
        print("\nOlá {}, este é um mundo habitado por pokemons, a partir de agora sua missão é se tornar um mestre dos pokemons!".format(player))
        print("\nCapture o máximo de pokemons que conseguir e lute com seus inimigos\n")
        player.mostrarDinheiro()

        if player.pokemons:
            print("\n\nJá vi que você tem alguns pokemons")
            player.mostrarPokemons()
        else:
            print("\n\nVocê não tem nenhum pokemon, portando precisa escolher um.\n")
            escolherPokemonInicial(player)

        print("\nPronto, agora que você já possui um pokemon, enfrente seu arqui-rival desde o jardim da infância Gary\n")
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)
        SalvarJogo(player)

    while True: 
        print("--" * 10)
        print("O que deseja fazer mestre {}?".format(player))
        print("1 - Explorar pelo mundo a fora")
        print("2 - Lutar com um inimigo")
        print("3 - Mostrar Pokeagenda")
        print("4 - Mostrar quantidade de dinheiro")
        print("0 - Sair do jogo")
        escolha = input("Sua escolha: ")

        if escolha == '0':
            print("Fechando o jogo")
            break
        elif escolha == '1':
            player.explorar()
            SalvarJogo(player)
        elif escolha == '2':
             player.batalhar(Inimigo())
             SalvarJogo(player)
        elif escolha == '3':
            player.mostrarPokemons()
        elif escolha == '4':
            player.mostrarDinheiro()           

