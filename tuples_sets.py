#tuplas: uma lista imutável:

# tupla = (valor1, valor2, ..., valorn)
# não muda após criar

# tupla = "valor", - válido
# tupla = ("valor",) - válido
# tupla = ("valor") - inválido, python acha que é uma função

# tuplas: parênteses ()
# listas: colchetes []
# dicionários: chaves {}

# tuplas possuem dois métodos: count(algo) e index(algo) -> retorna quantas vezes algo ocorre na tupla e o índice de algo
# os demais métodos podem ser os de listas

# motivos de usar tuplas:

# mais eficientes que listas
# para dados que não devem mudar
# alguns métodos retornam tuplas, como dict.items() -> (chave, valor)
# uma tupla pode ser chave de um dicionário

### 

# sets (conjuntos): conjunto de dados únicos, imutáveis e não-ordenados

# set = {1,2,3,4} -> declaração de um conjunto
# geralmente, o tipo de dados é o mesmo para os valores de um conjunto

# conjuntos são desordenados pois seus itens não são indexados

# set.add(valor) -> adiciona ao conjunto
# set.remove(valor) -> remove valor
# set.discard(valor) -> tenta remover, mas se não existir, não levanta um erro, diferente do remove

# operadores entre dois conjuntos

set1 = {1,2,3}
set2 = {3,4,5,6}
# intersecção: retorna um conjunto com elementos em comum
print((set1 & set2)) # {3}
# diferença: retorna um conjunto com elementos que tenham no conjunto da esquerda, mas não da direita
print((set1 - set2)) # {1,2}
# união: união dos conjuntos
print((set1 | set2)) # {1, 2, 3, 4, 5, 6} (retira elementos repetidos)

# set1.union(set2)
# set1.difference(set2)
# set1.intersection(set3)
# mesmo resultado que o código acima

# quando usar:
# quando se quer verificar se algo existe em uma coleção (só aceita um valor)
# removem duplicatas