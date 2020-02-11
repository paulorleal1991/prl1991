#embaralhar umw lista gerando um sequencia nova
from random import shuffle
print('')
print('')
print('_' *40)
a1 = str(input('Aluno 1:'))
a2 = str(input('Aluno 2:'))
a3 = str(input('Aluno 3:'))
a4 = str(input('Aluno 4:'))
lista = [a1, a2, a3, a4]
shuffle(lista)
g= str('******A Sequencia escolhida é*******')
print ('{:^40}'.format(g))
print(lista)
print('_' *40)
