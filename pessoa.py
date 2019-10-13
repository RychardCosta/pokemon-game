import random

from pokemon import *

NOME = ['Davi', 'Miguel','Artur', 'Enzo', 'Guilherme', 'Lucas', 'Nicos', 'Lourezo',
    'Daniel', 'Vitor', 'Fábio', 'José', 'Pedro',    "João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego",
    "Patrícia", "Marcelo", "Gustavo", "Gerônimo", "Gary"
    ]

POKEMONS = [
PokemonFogo('charmander'), 
PokemonFogo('Flarion'),
PokemonFogo('Charmilion'),
PokemonEletrico('Pikachu'),
PokemonEletrico('Raichu'),
PokemonAgua('Squirtle'),
PokemonAgua('Margicapo')]


class Pessoa: 
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else: 
            self.nome  = random.choice(NOME)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrarPokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} não tem nenhum pokemon!".format(self))

      

    def escolherPokemon(self):
        if self.pokemons:
            pokemonEscolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemonEscolhido))
            return pokemonEscolhido

        else:
            print("ERRO: O jogador {} não possui nenhum pokemon para ser escolhido".format(self))


    def mostrarDinheiro(self):
        print("Você possui $ {} em sua conta".format(self.dinheiro))
    
    def ganharDinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Você ganhou $ {}".format(quantidade))
        self.mostrarDinheiro()
    
    def perderDinheiro(self, quantidade):
        self.dinheiro -= quantidade
        print("Você perdeu $ {}".format(quantidade))
        self.mostrarDinheiro()
    
    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))
        
        pessoa.mostrarPokemons()
        pokemonInimigo  = pessoa.escolherPokemon()

        pokemon = self.escolherPokemon()

        if pokemon and pokemonInimigo:
            while True:
                vitoria = pokemon.atacar(pokemonInimigo)
                if vitoria:
                    print("{} ganhou a batalha!".format(self))
                    self.ganharDinheiro(pokemonInimigo.level * 100)
                    break
                vitoriaInimiga = pokemonInimigo.atacar(pokemon)
                if vitoriaInimiga:
                    print("{} ganhou a batalha".format(pessoa))
                    self.perderDinheiro(pokemonInimigo.level * 100)
                    break
                
                if pokemon.vida <= 0:
                    print("{} perder a batalha".format(self))
                elif pokemonInimigo.vida <=0:
                    print("{} perder a batalha".format(pessoa))
        else:
            print("Essa batalha não pode ocorrer")


class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("\n{} capturou {}".format(self, pokemon))

    def escolherPokemon(self):
        self.mostrarPokemons()
        if self.pokemons:
            while True:
                try:
                    escolha = input("Escolha o seu Pokemon: ")
                    pokemonEscolhido = self.pokemons[int(escolha)]
                    print("{} eu escolho você!!".format(pokemonEscolhido))
                    return pokemonEscolhido
                except:
                    print("Escolha invalída!")
        else: 
            print("ERRO: O jogador {} não possui nenhum pokemon para ser escolhido".format(self))

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print("Um pokemon selvagem apareceu: {}".format(pokemon))
            escolha = input("Deseja capturar o pokemon? (s/n)")

            if escolha == 's' or escolha == 'S' or escolha == 'Sim' or escolha == 'sim':
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print("{} fugiu, que pena!!".format(pokemon))
            else: 
                print("Ok, boa viagem")
                        
        else: 
            print("Essa exploração não deu em nada")



class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemonsAlatorios = []
            for i in range(random.randint(1, 6)):
                pokemonsAlatorios.append(random.choice(POKEMONS))
    
            super().__init__(nome=nome, pokemons=pokemonsAlatorios)
        else: 
            super().__init__(nome=nome, pokemons=pokemons)


