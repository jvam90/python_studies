#global: a variável é vista em qualquer lugar do programa.
#local: quando a variável é declarada dentro de uma função
#variáveis dentro de um laço não ficam restritas a ele: código fora do loop pode acessá-las. O mesmo vale para uma condicional.
#O mesmo vale para a declaração do laço: for x in range(10): mesmo ao final, podemos acessar x
#enclosing: se uma função declara uma variável, ela é vista também em funções internas à mais externa
#built-in: são coisas próprias do python: podemos acessá-las em qualquer lugar

#do mais restrito para o mais acessível (escopo): local -> enclosing -> global -> built-in 
#a precedência é da esquerda pra direita

#é possível declarar algo localmente e dizer que ele é global:

# def func():
#   global x = 10
#   
#fora de func, é possível acessar x