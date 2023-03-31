"""
    CONSTANTE = "Variáveis que não vão mudar
    
    Colocar muitas condições no mesmo if é ruim
"""

velocidade = 64
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

carro_ultrapassou_velocidade_radar = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_passou_radar_1 and carro_ultrapassou_velocidade_radar

if carro_passou_radar_1:
    print('Carro está no radar')

if carro_multado:
    print('Carro multado por velocidade alta')
else:
    print('Carro não foi multado')