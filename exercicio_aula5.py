'''
Exercicio: Faça um programa que leia a quantidade de pessoas que 
serao convidadas para uma festa

Apos isso o programa ira perguntar o nome de todas as pessoas e colocar numa
lista de convidados

Apos isso ira imprimir todos os nomes da lista

'''

quantidade_pessoas = input("Digite a quantidade de convidados: ")

i = 0
nomes = []

while i < int(quantidade_pessoas):
  nome = input('Digite o nome do convidado:')
  nomes.append(nome)
  i += 1

for nome in nomes:
  print(nome)