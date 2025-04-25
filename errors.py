# alguns tipos de erros comuns:

# SyntaxError (algo inválido sintaticamente)
# IndexError (índice inexistente em uma lista)
# ValueError (quando algo aceita um parâmetro, mas seu valor é incompatível: int("teste"): o parâmetro é válido, mas seu valor não)
# NameError (variável não declarada, por exemplo)
# TypeError (quando se tenta fazer uma operação entre dois ou mais tipos de dados incompatíveis: int + string, por exemplo)
# KeyError (quando a chave em um dicionário é inexistente)

# para lançar uma exceção:

# raise <erro>

# raise TypeError -> seria o mesmo que um throw new exception()
# também posso mandar com uma mensagem: raise TypeError("Invalid Type!")

# try-except

# try:
#     # código que pode levantar uma exceção
# except:
#     # código que vai ser executado se houver exceção (catch)

# pode tratar vários erros com excepts separados ou por uma tupla:
try: 
    num = int(input("Digite um número: "))
except ValueError:
    print("Apenas números!")
except EOFError:
    print("Digita!")
except(TypeError, IndexError): # -> se cair ou em typeerror ou em indexerror, vai ter o mesmo tratamento
    print("Outro erro")

# por padrão, é melhor ser específico com relação aos erros

# LBYL: look before you leap: se testa explicitamente por pré-condições antes de fazer chamadas, ou pulos (leaping)
year = input()
if year.isnumeric(): # verifica antes pra depois fazer o pulo
    year = int(year) # <- pulo ou leaping
else:
    year = 2025

# EAFP: easier to ask for forgiveness than permission: assume que vai dar certo, se não, levanta errotry: 
try:
    num = int(input("Digite um número: "))
except ValueError:
    print("Apenas números!")