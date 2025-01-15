import os

print('Selecione uma opção')

resposta = input('[i]nserir    [a]pagar    [l]istar: ')

lista = ''

if resposta == 'i':
    os.system('cls')
    lista = input('Valor: ')
    lista = list(lista)


