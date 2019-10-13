import random


class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100) 
  
        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return "{} (level {})".format(self.nome, self.level)

    def atacar(self, pokemon):
        ataqueEfetivo = int((pokemon.ataque - random.random() * 1.3))
        pokemon.vida -= ataqueEfetivo
        print("{} perdeu {} pontos de vida".format(pokemon, ataqueEfetivo))

        if ataqueEfetivo < 3:
            print("Esse ataque foi muito fraco!")
        elif ataqueEfetivo == 3:
            print("Esse foi um bom ataque!")
        elif ataqueEfetivo <=5: 
            print("Esse ataque foi muito forte!")
        elif ataqueEfetivo == 6:
            print("Esse foi um MEGA ATAQUE!")

        if pokemon.vida <= 0:
            print('{} foi derrotado'.format(pokemon))
            return True
        else:
            return False 


class PokemonEletrico(Pokemon):
    tipo = "eletrico" 

    def atacar(self, pokemon):    
        print("{} lançou um raio do trovão em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "fogo" 

    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo na cabeça de {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = "agua" 

    def atacar(self, pokemon):
        print("{} lançou um jato d'água em {}".format(self, pokemon))
        return super().atacar(pokemon)
