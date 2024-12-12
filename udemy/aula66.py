def borda(s1):
    tam = len(s1)

    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

borda('CALCULADORA')

while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ') 
    operador = input('Digite o operador [+][-][*][/]: ')
    resultado = 0

    try:
        n1 = float(num1)
        n2 = float(num2)
    except:
        print('Você não digitou um valor válido')
        continue
    
    
    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    
    if operador == '+':
        resultado = n1 + n2
    elif operador == '-':
        resultado = n1 - n2
    elif operador == '*':
        resultado = n1 * n2
    elif operador == '/':
        resultado = n1 / n2
    print(resultado)
    
    sair = input('Quer sair? Se sim, digite S: ')
    if sair.capitalize() == 'S':
        print('Você saiu')
        break

    