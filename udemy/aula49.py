numero_str = input('Vou dobrar o número que digitar: ')

try:
    print(f'STR: {numero_str}')
    numero_float = float(numero_str)
    print(f'FLOAT: {numero_float}')
    print(f'O dobro desse número é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
