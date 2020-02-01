'___Curso_de_Python___'
'___Aluno_Paulo_R_Leal___'
'___Exercicio_008____'
print('')
print('_' *40)
print('Conversor de Medidas')
m = float(input('Digite o Valor em Metros \n'))
dm = m * 10
cm = m * 100
mm = m * 1000
print('')
print('#' *40)
print('{} Metros Equivale a:\n{:.0f} Centimetros ou {:.0f} milímetros'.format(m,cm,mm))
print('#' *40)
dam = m / 10
hm = m / 100
km = m / 1000
print('')
print('_' *40)
print('Tabela de Medidas referente ao Valor')
print('_' *40)
print('')
print('-----------------------------------------')
print('|Medididas Equivalente    | Valor')
print('|Kilometros               |{:.2f}'.format(km))
print('|Hectômetros              |{:.2f}'.format(hm))
print('|Decâmetros               |{:.2f}'.format(dam))
print('|Metros                   |{:.2f}'.format(m))
print('|Decímetros               |{:.2f}'.format(dm))
print('|Centímetros              |{:.2f}'.format(cm))
print('|Milímetros               |{:.2f}'.format(mm))
print('-----------------------------------------')
print('')
print('-' *35)
print('Paulo Roberto Leal 2020 01 31')
print('paulorleal011291@hotmail.com')
print('-' *35)

