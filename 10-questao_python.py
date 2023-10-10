10- 

import random

def consultar_previsao_tempo(cidade):
    
    clima = random.choice(['Ensolarado', 'Nublado', 'Chuvoso', 'Neve'])
    temperatura = random.uniform(-10, 40)  
    umidade = random.randint(0, 100)  
    pressao = random.uniform(900, 1100)  
    vento = random.uniform(0, 20)  

    print(f'Previsão do tempo para {cidade}:')
    print(f'Clima: {clima}')
    print(f'Temperatura: {temperatura:.2f}°C')
    print(f'Umidade: {umidade}%')
    print(f'Pressão: {pressao:.2f} hPa')
    print(f'Velocidade do Vento: {vento:.2f} m/s')

if __name__ == '__main__':
    cidade = input('Indique o nome da localidade para verificar a previsão meteorológica: ')
    consultar_previsao_tempo(cidade)