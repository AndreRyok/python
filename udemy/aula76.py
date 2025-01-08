import os

palavra = "bosta"
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas UMA letra!')
        continue

    if len(letra_digitada) < 1:
        print('Digite pelo menos uma letra!')

    if letra_digitada in palavra:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print(f'A palavra era "{palavra}"')
        print(f'Tentativas: {numero_tentativas}')
        break