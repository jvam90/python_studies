# Módulo: um arquivo que contém código python que pode ser compartilhado entre diferentes projetos

# 1 - built-in: os que vêm com python (random)
# 2 - custom: customizados, que o programador pode criar
# 3 - 3rd party: de terceiros: algo que você pode baixar e usar em um projeto

# basicamente a sintaxe é: import <módulo>
# import random
# import calendar
# print(calendar.isleap(2012))

# outra forma: import random as <algo>: cria um alias
import random as rand
print(rand.random())

# se quiser algo específico: FROM <modulo> IMPORT <algo>

# pip: instalador de pacotes python
# python3 -m pip install <pacote> ou pip install <pacote>
from art import *
print(art("woman"))

from translate import Translator
translator = Translator(to_lang="zh")
translator = translator.translate("João Víctor")
print(translator)