import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurando o gerador de números aleatórios
np.random.seed(42)

# Criando um intervalo de tempo de 24 horas (uma leitura a cada 15 minutos = 96 leituras)
inicio = datetime.now() - timedelta(days=1)
timestamps = [inicio + timedelta(minutes=15 * i) for i in range(96)]

# Simulando dados: Temperatura começando em 20°C e subindo gradativamente até 26°C
# Adicionamos um pequeno ruído aleatório para simular um sensor real
temperaturas = [20.0 + (0.06 * i) + np.random.uniform(-0.5, 0.5) for i in range(96)]

# Simulando dados: Umidade começando em 60% e caindo conforme esquenta
umidades = [60.0 - (0.15 * i) + np.random.uniform(-1.0, 1.0) for i in range(96)]

# Criando o dicionário de dados
dados = {
    'timestamp': [t.strftime('%Y-%m-%d %H:%M:%S') for t in timestamps],
    'temperatura': np.round(temperaturas, 2),
    'umidade': np.round(umidades, 2)
}

# Transformando em um DataFrame do Pandas
df = pd.DataFrame(dados)

# Salvando em um arquivo CSV
df.to_csv('dados_estufa.csv', index=False)

print("✅ Arquivo 'dados_estufa.csv' gerado com sucesso na pasta do seu projeto!")
print(df.head())  # Mostra as primeiras 5 linhas para validação
