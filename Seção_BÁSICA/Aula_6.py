# Limpeza de Codigo

# num = 12   - Variavel
# NUM = 12   - Constante('NÃO MUDA)

# Exercicio

velocidade = 61
posicao_carro = 100 

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

 # INICIO Calculo da posição do radar para multar (BOOL)
calc_Pass_antes_radar = posicao_carro >= LOCAL_1 - RADAR_RANGE
calc_pass_depois_radar = posicao_carro <= LOCAL_1 - RADAR_RANGE
 # FiM calculo da posiçao do radar para multar


vel_carro_passou_radar = velocidade > RADAR_1   # Denomina se a velocidade do carro é maior que o radar

carro_passou_radar = calc_Pass_antes_radar and calc_pass_depois_radar   # Denomina se o carro foi detectado 

carro_multado_radar = carro_passou_radar and vel_carro_passou_radar     # Decisão final se o carro deve ser multado



if vel_carro_passou_radar : 
    print('Passou da velocidade =', True)

if carro_passou_radar :
    print('Carro Passou = ', True)

if carro_multado_radar :
    print('Mutado = ', True )

else : print('Mutado = ', False)


