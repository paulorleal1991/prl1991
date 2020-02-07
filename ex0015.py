'___Curso_Python___'
'___Aluno_Paulo_R_Leal___'
'___Exercicio_015___'
print('Exercicio 015 Aluguel de Carro')
diaria = int(60)
km = float(0.15)
usod = float(input('Quantos dias de uso?:\n'))
usok = float(input('Quantos Kilometros rodados?:\n'))
dv = (diaria * usod) + (km * usok)
print('')
print('#' *40)
print('Total a Pagar é de R${:.2f}'.format(dv))
print('#' *40)
print('')
print('OBS: Tabela vigente : Diaria R$60,00 e R$0,15 por km percorido')
print('Diraria somaram {:.2f} e adicional por km percorido {:.2f}.'.format(usod*diaria, usok*km))
