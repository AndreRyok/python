brinquedos = input('Insira os brinquedos:')

if brinquedos:
    brinOrg = sorted(brinquedos)
    print(brinOrg)
else:
    print('Vazio!')