"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')
try:
    numInt = int(num)
    if (numInt % 2) == 0:
        print('Esse número é par')
    else:
        print('Esse número é ímpar')
except:
    print('Isso não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex (Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23)
"""

hora = input('Que horas são agora? ')
try:
    hInt = int(hora)
    if (hInt >= 0) and (hInt <= 11):
        print('Bom dia!')
    elif (hInt >= 12) and (hInt <= 17):
        print('Boa tarde!')
    elif (hInt >= 18) and (hInt <= 23):
        print('Boa noite')
    else:
        print('Você não digitou um horário válido')
except:
    print('Você não digitou um horário válido')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""
nome = input('Digite seu primeiro nome: ')
if len(nome) <= 4:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')