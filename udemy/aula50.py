"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if --> ruim
     <--- Contagem de complexidade --> ruim (muitos blocos dentro de outros blocos, assim como o if, que vai afastando cada vez mais o código)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 90 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade do carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('Multado em radar 1')