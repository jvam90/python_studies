# # # sintaxe: lista = [valor1, valor2, ..., valorN]
# # #ex: listaStr = ['str1', 'str2', 'str3']

# # high_scores = [10, 9, 8, 7]
# # total = 0
# # for score in high_scores:
# #     total += score

# # avg = total / len(high_scores)

# # # print(f"Average score: {avg}")

# # # gera uma lista a partir de algum iterável
# # test = list(range(10))
# # print(test)

# # # para acessar: lista[índice]

# # print(test[0])
# # print(test[1])

# test = list(range(10))

# for index, num in enumerate(test):
#     print(index, num)

# # enumerate retorna um enumerável a partir de um objeto iterável

# # atualizar algum elemento da lista:

# # lista[indice] = valor -> atribuição normal

# # assim como strings, se acessarmos o indíce -1, vai retornar o último elemento:

# # list = [0,1,2]
# # list[-1] == 2
# # list[-2] == 1

list = [1,2,3,4,5]
# # append adiciona ao final da lista
# list.append(6)
# list.append(7)
# # extend vai adicionar ao final da lista, um outro objeto iterável, no caso, uma lista
# # semelhante ao AddRange do c#
# list.extend([8,9])
# print(list)

# insert vai inserir em um índice: onde o elemento desejado vai ser inserido. 
list.insert(0, -1)
# o python vai mover os elementos para a direita ou para esquerda dependendo do índice
list.insert(0, -2)
# se o índice for maior que o tamanho da lista, python vai inserir no final
list.insert(10, -2)
print(list)