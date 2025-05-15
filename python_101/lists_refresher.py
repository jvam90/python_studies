# listas

lista = []  # definida pelos colchetes
lista = [1,2,3] # pode ter valores
lista = list() # pode ser construída
print(type(lista)) # <class 'list'>

# tuplas

tupla = () # definida por parênteses
tupla = (1,2,3) # pode ter valores
tupla = tuple() # pode ser construída
print(type(tupla)) # <class 'tuple'>

# a principal diferença de listas e tuplas é que listas são mutáveis, e tuplas não.

# conjuntos

conjunto = {} # definida por chaves
conjunto = {1,2,3} # pode ter valores
conjunto = set() # pode ser construída
print(type(conjunto)) # <class 'set'>

# conjuntos não podem possuir elementos repetidos
# listas e tuplas mantêm a ordem de elementos inseridos
# conjuntos não

# os elementos de listas e tuplas podem ser acessados por índices
# print({1,2,3}[2]) o mesmo não vale para conjuntos, uma vez que eles não guardam a ordem dos elementos inseridos

# lista.append() -> insere no final da lista
# lista.remove() -> remove o elemento desejado
# conunto.add() -> insere um elemento (não se preocupa com ordem) e se tentar inserir repetidos, eles são ignorados

# conjuntos podem fazer operações de união, interseção e diferença:

c1 = {1,2,3}
c2 = {1,2}

c3 = c1.difference(c2) # o que tem no primeiro e não no segundo
print(c3) # {3}
c3 = c1.union(c2) # o que tem no primeiro e no segundo
print(c3) # {1,2,3}
c3 = c1.intersection(c2) # o que tem em ambos
print(c3) # {1,2}

# lembrando que a ordem importa: por exemplo: c1.intersection(c2) pode ser diferente de c2.intersection(c1)
