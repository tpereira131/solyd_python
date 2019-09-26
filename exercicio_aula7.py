'''

EXERCICIO: Escreva uma funcao que recebe um objeto de coleção
e retorna o valor do maior numero dentro dessa colecao
faça outra função que retorna o menor numero dessa coleção
'''

lista = []

def retorna_maior(lista):
  maior = max(lista)
  return print(maior)

def retorna_menor(lista):
  menor = min(lista)
  return print(menor)


retorna_maior([2,5,10,15,3,4])
retorna_menor([2,5,10,15,3,4])