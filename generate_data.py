import csv
import random
from datetime import datetime, timedelta

def generate_dummy_data(filename, num_records=1500):
    headers = [
        'timestamp',
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
