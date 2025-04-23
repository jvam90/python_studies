def is_even(number):
    return number % 2 == 0

def slugify(string):
    return string.lower().strip().replace(' ', '-')

def count_vowels(string):
    string = string.lower()
    count = 0
    for vowel in string:
        if vowel in ['aeiou']:
            count += 1
    return count

#parâmetro padrão (default): se na chamada não for dado, ele assume o valor 10
def intensity(intens = 10):
    print("HA" * intens)

#se uma função tiver parâmetros padrão, eles devem vir após os obrigatórios. por exemplo:
#def func(p1,p2, p3=1, p4=2)
#pois ao chamar, só precisa dos dois primeiros, e os demais são opcionais.
#é possível também usar argumentos nomeados:

#def func(param1, param2, param3)
#func(param1 = 10, param2 = 20, param3 = 30)
#func(param2 = 10, param3 = 20, param1 = 10) -> como estão nomeados explicitamente, a ordem não importa
intensity(5)
