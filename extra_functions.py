# *args: significa que a função que aceita um número N de argumentos:
# os argumentos são agrupados em uma tupla e podem ser usados como tal
def teste(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)

teste(1,2) # 3
teste(1,2,3) # 6

#lembrando que argumentos obrigatórios devem ir antes dos opcionais

# def teste(param1, param2, *args)

# **kwargs: similar ao *args mas os argumentos devem ser passados como chave e valor e retorna em tuplas de chave e valor

def print_ages(**kwargs):
    for k,v in kwargs.items():
        print(k, v)

print_ages(nome="João",idade=34) # na função é recebido um dicionário

# quando definir funções, a ordem dos parâmetros importa:
# (parâmetros, *args, default, **kwargs)

# unpacking: uma função definida com *args, espera uma tupla, mas ao ser chamada, não espera uma lista:

#def teste(*args)
#teste([1,2,3,4]) -> vai ocasionar um erro, pois espera que seja passado cada valor individual
# para fazer o unpack: teste(*array) -> seria o mesmo que passar: teste(1,2,3,4), só que passa diretamente a lista
# e o python se encarrega de 'desconstruir'