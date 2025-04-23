# # dicionários são bons para guardar dados em pares chave x valor
# # listas são boas para dados "ordenados"

# # em um dicionário, você procura algo pela chave, que vai retornar o valor correspondente.

# # sintaxe: algo = {} ou algo = dict() -> função devolve um dicionário
# # algo = list() -> devolve uma lista

# algo = {}
# algo = {"nome": "João", "idade": 34} # semelhante a JSON

# # valores podem ser qualquer coisa
# # chaves podem ser de tipos imutáveis, como números ou strings (mais comum)

# # internamente, as chaves vão passar por um processo de hashing, e nem todo tipo de dados pode sofrer hashing
# # mais comum: criar como JSON: algo = {"nome": "João", "idade": 34}

# # print(algo)
# # print(algo["idade"]) # pega pela chave 'idade'
# # print(algo["nome"]) # pega pela chave 'nome'
# algo2 = {3: 3}

# # se eu tivesse algo como: teste = {True: 'true', 45: '45'}, eu poderia acessar por teste[True] ou teste[45]
# # ele não trataria como índices de lista, pois acessa por chaves que foram criadas pelo usuário.

# # para mudar algo ou para adicionar algo:

# algo2[3] = "3"
# algo2[4] = "4"
# # algo2.clear() # limpa tudo
# algo2.pop(3) # remove pela chave, ao invés do índice, como em listas
# algo2.popitem() # remove o último item adicionado (retorna uma tupla: (chave, valor))
# del algo2[chave] -> remove pela chave fornecida




## importante: em um dicionário, deve existir apenas chaves únicas.
## dicionários são mutáveis: pode mudar o conteúdo, mas o container (referência de memória) permanece o mesmo

# # para verificar se uma chave existe num dicionário:

teste = {"chave1": 1, "chave2": 2}
#print("chave3" in teste) # verifica se existe no dicionário a chave
#print(teste.get("chave1")) # tenta pegar o valor pela chave, se não existir, retorna None

# como iterar sobre dicionários

# teste.keys() => retorna array com as chaves
# teste.values() => retorna array com os valores
# teste.items() => retorna tupla chave x valor

# for item in teste.keys():
#     print(item, type(item))

#teste.update(dict) => vai adicionar um dicionário a outro existente, semelhante ao extend de listas (não cria um novo)
# novoDict = {**dict1, **dict2} => semelhante ao desconstruct de javascript: é o mesmo que dizer que: novoDict vai ser um novo
# dicionário com todo o conteúdo (chaves e valores) de dict1 e dict2
# dict = d1 | d2 => união de dicionários