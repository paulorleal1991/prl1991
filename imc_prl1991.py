'IMC'
nome = input('Qual o Seu nome?\n') 
print ('Muito praser '+ nome)
import time
time.sleep(2)
peso = float (input('Qual o seu peso atual?\n'))
altura = float (input('Qual a sua altura?\n'))
print ('Bem '+ nome , 'Seu peso é ' , peso , 'Seu Altura ' , altura )
altimc = altura * 2
imc = peso / altimc
print (imc)
import os
os.system('date')