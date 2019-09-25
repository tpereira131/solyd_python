'''
Faca um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela esta apta a ser do exercito
Para entrar no exercito é preciso ter mais de 18 anos,
pesar mais ou igual a 60
e medir mais ou igual 1,70 metros

'''

idade = input('digite sua idade: ')
peso = input('digite seu peso: ')
altura = input('digite sua altura: ')

if (int(idade) > 18) and (int(peso) >= 60) and (float(altura) >= 1.70):
    print('voce esta apto')
else:
    print('voce nao esta apto')
