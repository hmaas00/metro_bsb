import csv
import random
from datetime import datetime, timedelta

def generate_dummy_data(filename, num_records=1500):
    estacoes_metro_df = [
        {"nome": "Central", "lat": -15.7925, "lon": -47.8828},
        {"nome": "Galeria", "lat": -15.7981, "lon": -47.8856},
        {"nome": "102 Sul", "lat": -15.8044, "lon": -47.8903},
        {"nome": "106 Sul", "lat": -15.8164, "lon": -47.8997},
        {"nome": "108 Sul", "lat": -15.8228, "lon": -47.9042},
        {"nome": "110 Sul", "lat": -15.8286, "lon": -47.9089},
        {"nome": "112 Sul", "lat": -15.8347, "lon": -47.9133},
        {"nome": "114 Sul", "lat": -15.8406, "lon": -47.9181},
        {"nome": "Terminal Asa Sul", "lat": -15.8483, "lon": -47.9239},
        {"nome": "Shopping", "lat": -15.8336, "lon": -47.9422},
        {"nome": "Feira", "lat": -15.8319, "lon": -47.9547},
        {"nome": "Guará", "lat": -15.8258, "lon": -47.9708},
        {"nome": "Arniqueiras", "lat": -15.8378, "lon": -48.0169},
        {"nome": "Águas Claras", "lat": -15.8406, "lon": -48.0264},
        {"nome": "Concessionárias", "lat": -15.8361, "lon": -48.0381},
        {"nome": "Estrada Parque", "lat": -15.8333, "lon": -48.0494},
        {"nome": "Praça do Relógio", "lat": -15.8319, "lon": -48.0569},
        {"nome": "Centro Metropolitano", "lat": -15.8344, "lon": -48.0772},
        {"nome": "Ceilândia Sul", "lat": -15.8378, "lon": -48.0933},
        {"nome": "Guariroba", "lat": -15.8306, "lon": -48.1022},
        {"nome": "Ceilândia Centro", "lat": -15.8236, "lon": -48.1128},
        {"nome": "Ceilândia Norte", "lat": -15.8142, "lon": -48.1189},
        {"nome": "Terminal Ceilândia", "lat": -15.8078, "lon": -48.1258},
        {"nome": "Taguatinga Sul", "lat": -15.8569, "lon": -48.0336},
        {"nome": "Furnas", "lat": -15.8672, "lon": -48.0469},
        {"nome": "Samambaia Sul", "lat": -15.8753, "lon": -48.0817},
        {"nome": "Terminal Samambaia", "lat": -15.8744, "lon": -48.0964}
    ]

    headers = [
        'timestamp',
        'estacao',
        'geolocalizacao',
        'equipamento_id',
        'tipo_equipamento',
        'vibracao',
        'impacto',
        'temperatura',
        'velocidade_corrente',
        'abertura_porta',
        'posicao',
        'torque',
        'desalinhamento',
        'contagem_pessoas',
        'travamento',
        'posicao_suspeita'
    ]

    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        start_time = datetime.now() - timedelta(days=5)

        for i in range(num_records):
            timestamp = (start_time + timedelta(minutes=5*i)).strftime('%Y-%m-%d %H:%M:%S')

            estacao_escolhida = random.choice(estacoes_metro_df)
            estacao_nome = estacao_escolhida['nome']
            geolocalizacao = f"{estacao_escolhida['lat']},{estacao_escolhida['lon']}"

            tipo = random.choice(['Elevador', 'Escada_Rolante'])
            equipamento_id = f"{tipo}_{random.randint(1, 4)}"

            # 5% de chance de ser uma anomalia (possível vandalismo)
            is_vandalism = random.random() < 0.05

            if is_vandalism:
                vibracao = round(random.uniform(5.0, 15.0), 2) # mm/s
                impacto = random.choice(['Forte', 'Extremo'])
                temperatura = round(random.uniform(35.0, 50.0), 1) # °C
                velocidade_corrente = round(random.uniform(0.0, 3.0), 2) # m/s (anômala)
                abertura_porta = 'Forçada' if tipo == 'Elevador' else 'N/A'
                posicao = random.choice(['Entre andares', 'Bloqueada']) if tipo == 'Elevador' else 'N/A'
                torque = round(random.uniform(80.0, 150.0), 2) # Nm
                desalinhamento = random.choice(['Severo', 'Crítico'])
                contagem_pessoas = random.randint(8, 25) # Possível aglomeração/pulo
                travamento = 'Sim'
                posicao_suspeita = 'Sim'
            else:
                vibracao = round(random.uniform(0.1, 2.5), 2)
                impacto = 'Nenhum' if random.random() < 0.9 else 'Leve'
                temperatura = round(random.uniform(20.0, 30.0), 1)
                velocidade_corrente = round(random.uniform(0.9, 1.1), 2) if tipo == 'Escada_Rolante' else round(random.uniform(1.0, 2.5), 2)
                abertura_porta = random.choice(['Aberta', 'Fechada']) if tipo == 'Elevador' else 'N/A'
                posicao = f"Andar {random.randint(1, 10)}" if tipo == 'Elevador' else 'Em movimento'
                torque = round(random.uniform(20.0, 50.0), 2)
                desalinhamento = 'Nenhum'
                contagem_pessoas = random.randint(0, 8)
                travamento = 'Não'
                posicao_suspeita = 'Não'

            writer.writerow([
                timestamp,
                estacao_nome,
                geolocalizacao,
                equipamento_id,
                tipo,
                vibracao,
                impacto,
                temperatura,
                velocidade_corrente,
                abertura_porta,
                posicao,
                torque,
                desalinhamento,
                contagem_pessoas,
                travamento,
                posicao_suspeita
            ])

if __name__ == '__main__':
    generate_dummy_data('dados_sensores_anomalias.csv')
    print("Arquivo CSV gerado com sucesso!")
