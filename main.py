class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = self._obter_ataque()
        print(f"O {self.tipo} atacou usando {ataque}")

    def _obter_ataque(self):
        if self.tipo == 'mago':
            return 'magia'
        elif self.tipo == 'guerreiro':
            return 'espada'
        elif self.tipo == 'monge':
            return 'artes marciais'
        elif self.tipo == 'ninja':
            return 'shuriken'
        else:
            return 'ataque indefinido'


#Exemplo:
heroi_mago = Heroi(nome='Gandalf', idade=55000, tipo='mago')
heroi_mago.atacar()

heroi_guerreiro = Heroi(nome='Aragorn', idade=87, tipo='guerreiro')
heroi_guerreiro.atacar()

heroi_ninja = Heroi(nome='Gabimaru', idade=16, tipo='ninja')
heroi_ninja.atacar()

heroi_monge = Heroi(nome='Zenyatta', idade=20, tipo='monge')
heroi_monge.atacar()
