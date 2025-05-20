# list comprehension: um jeito de criar uma nova lista a partir de uma existente, podendo, para cada item, aplicar uma condição:

# de forma geral: [<o que você quer> <para cada elemento da lista> <aplica uma condição se possível>]

lista = [1,2,3]
# seria o mesmo que dizer: para cada número dentro de 'lista', me retorne o dobro. A condição é opcional.
lista2 = [num * 2 for num in lista]
print(lista2)
# seria o mesmo que dizer: para cada número dentro de 'lista', me retorne o quadrado. A condição é opcional.
lista2 = [num * num for num in lista]
print(lista2)

# números pares de 0 a 10:
pares = [num for num in range(11) if num % 2 == 0]
# retornar par ou ímpar dependendo do número:
resultados = ['Par' if num % 2 == 0 else 'Ímpar' for num in range(11)]

# na parte do 'que se quer', pode ser uma expressão if/else completa
# depois, vai se analisar o que quer, para cada número da lista.
# O resultado, vai ser uma nova lista.
print(resultados)

# para recuperar o dobro dos valores utilizando um laço for normal:

dobros = []
for num in lista:
    dobros.append(num * 2)

# como seria em list comprehension:

dobros = [num * 2 for num in lista]

print(dobros)

nomes = ["João", "Martins", "Víctor", "Alves"]
palavras = [nome for nome in nomes if "j" in nome.lower()]
print(palavras)

# em resumo: list comprehension -> especifica uma ação a ser feita em cada item de uma lista existente e ao final, retorna uma
# nova lista com os resultados de cada operação