import os

lista = []

while True:

    print('Escolha uma das opções!')
    resposta = input('[i]nserir     [a]pagar     [l]istar: ')
    
    if resposta not in ('i','a','l'):
        os.system('cls')
        print('Por favor, insira uma resposta válida! Apenas "i", "a" ou "l"')
        continue
    elif resposta == 'i':
        os.system('cls')
        itens = input('Item: ')
        lista.append(itens)
        print('Item inserido com sucesso!')
    elif resposta == 'a':
        try:
            indice_apagar = int(input('Digite o índice do item a ser apagado: '))
            del lista[indice_apagar]
            os.system('cls')
            print('Item apagado com sucesso!')
        except ValueError:
            os.system('cls')
            print('Apenas número inteiro!')
        except IndexError:
            os.system('cls')
            print('Esse índice não existe na lista!')
        continue
    elif resposta == 'l':
        os.system('cls')
        for indice, item in enumerate(lista):
            print(indice, item)
        if not lista:
            print('Lista vazia!')
            continue


