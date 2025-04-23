list = [1,2,3,4]

# slices: similar ao de strings: list[começo:fim:step]
# vai incluir o início, e vai até o fim, mas não o inclui

# test = list[0:2] # [1,2]
# test = list[0:1] # [1]
# test = list[0:19] # se o final for maior que o tamanho da lista, retorna ela inteira
# test = list[:] # [1,2,3,4]

#list.pop() # remove o último por padrão, mas pode passar o índice. O default é -1. Se a lista for vazia ou o índice > len, dá erro
#list.remove(1) # remove a primeira ocorrência do elemento passado por parâmetro. Se a lista for vazia ou o índice > len, dá erro
#list.clear() # limpa a lista inteira
del list[3] # expressão que vai remover de um índice específico. não é exatamente uma função, mas uma declaração.
print(list)