class Dog:
    species = "Canine" # atributo de classe -> cada instância vai ter acesso
    num_dogs = 0
    def __init__(self, name, breed):
        self.tricks = []
        self.name = name
        self.breed = breed
        # diferente de java ou c#, os atributos da classe ficam dentro de __init__, e não definidos na classe em si
        Dog.num_dogs += 1 # serve como atributo estático

    def bark(self):
        print(f"{self.name} says WOOF")

    def add_trick(self, trick):
        self.tricks.append(trick)

    @classmethod
    def create_anon(cls):
        return cls("Unknown")


meg = Dog("meg", "french bulldog")
print(meg.breed)
print(meg.name)
meg.add_trick("sit")
meg.add_trick("bark")
print(meg.tricks)
meg.bark()
print(meg.species)
print(Dog.species) # atributo de classe também é visto pela classe em si
Dog.species = "C. LUPUS" # python permite alterar
print(Dog.species)
# isinstance(meg, Dog) -> indica se algo é instância de uma classe

# é possível também ter métodos de instância e métodos de classe
# instância = os métodos são restritos às instâncias criadas
# classe = os métodos são restritos à classe em si, de forma geral

# exemplo de método de instância

# def bark(self):
#     print(f"{self.name} says WOOF") -> recebe o self como parâmetro
# se o método for chamado através de uma instância, ele deve ter o self como parâmetro, mesmo que ele não o utilize

# atributos de classe: atributos compartilhados por todos os objetos da classe
# métodos de classe: métodos da classe em si:

# @classmethod -> decorator pra identificar o método da classe
# def create_anon(cls): -> passa por parâmetro a classe em si
#     return cls("Unknown") -> quando se chama dessa forma, é o mesmo que chamar Dog() para criar uma instância