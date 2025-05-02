# OOP - abordagem de programação onde as coisas são estruturadas como classes
# essas coisas podem ter valores e comportamentos (propriedades e métodos)

# por exemplo: um jogo de xadrez:

# tabuleiro
# peça
# jogador
# outroJogador
# partida

# são possíveis modelagens

# classe: contém dados e funcionalidade.  Funciona como um molde para gerar nossos objetos. Ela descreve o que eles têm e o que
# podem fazer

# instâncias: objetos feitos a partir das classes

# por exemplo: classe: peça / instância: peão, rei, rainha, torre, etc.

# sintaxe de classe:

# class Test: -> nome da classe
#     def __init__(self, param1): -> método construtor -> automaticamente chamado quando se instancia um novo objeto
#         self.param1 = param1 -> self: se refere a instância criada atualmente.

# basicamente, ao instanciar, python passa por baixo dos panos a referência do objeto recêm criado. 'self' sempre deve
# ser o primeiro parâmetro

# e para instanciar:

# test = Test("param1")
# test.param1 == "param1"