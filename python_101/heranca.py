# herança: uma classe herda atributos e funcionalidade de outra

class Feline:
    
    def __init__(self, name):
        self.name = name
    
    def purr(self):
        print(f"{self.name} purrs")
    
class Lion(Feline): # -> sintaxe para dizer que a classe 'Lion' herda de 'Feline'

    def roar(self):
        print(f"{self.name} says ROAR")

lion = Lion("Murder Mittens")
lion.roar()
lion.purr()

# super() -> método usado para chamar o construtor da classe base, na classe filha.

class Feline:
    
    def __init__(self, name):
        self.name = name
    
    def purr(self):
        print(f"{self.name} purrs")
    
class Lion(Feline): # -> sintaxe para dizer que a classe 'Lion' herda de 'Feline'

    def __init__(self, name):
        super().__init__(name)
        self.mane = True

    def roar(self):
        print(f"{self.name} says ROAR")

# mesmo que Lion herde de Feline, muito provavelmente sua inicialização é diferente.
# quando se define seu próprio __init__, chamando o super().__init__(name), é o mesmo que chamar o init de Feline
# mas Lion pode ter atributos extras definidos no seu próprio __init__
# self.mane é exclusivo de Lion