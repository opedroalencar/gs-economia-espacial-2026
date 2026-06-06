import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("--- COMEÇANDO A ANÁLISE PREDITIVA (PANDAS & ML) ---")

# 1. PANDAS: Lendo e organizando os dados do CSV
df = pd.read_csv('dados_estufa.csv')
print("\n✅ Dados carregados com sucesso via Pandas!")
print(f"Total de registros encontrados: {len(df)} linhas.")

# Preparando os dados para a Regressão Linear
# O X será o tempo representado por números ordinais (0, 1, 2... 95)
df['tempo_id'] = np.arange(len(df))

X = df[['tempo_id']]       # Variável de entrada (Tempo)
y = df['temperatura']      # Variável que queremos prever (Temperatura)

# 2. MACHINE LEARNING: Criando e treinando a Regressão Linear
modelo = LinearRegression()
modelo.fit(X, y)

# Prevendo o comportamento para as próximas 4 horas (16 novos pontos no futuro)
futuro_id = np.arange(len(df), len(df) + 16).reshape(-1, 1)
previsoes_futuro = modelo.predict(futuro_id)

print("\n Inteligência Artificial Treinada!")
print(f"Tendência de aumento por período: {modelo.coef_[0]:.4f}°C")
print(f"Previsão de temperatura para as próximas 4 horas: {previsoes_futuro[-1]:.2f}°C")

# 3. MATPLOTLIB: Gerando o gráfico com os dados reais e a linha de previsão da IA
plt.figure(figsize=(10, 5))

# Plota os dados reais coletados pelo sensor
plt.plot(df['tempo_id'], df['temperatura'], label='Temperatura Real (Histórico)', color='cyan', linewidth=2)

# Plota a linha de tendência que a IA calculou se estendendo para o futuro
tempo_total = np.append(df['tempo_id'], futuro_id)
previsao_total = np.append(modelo.predict(X), previsoes_futuro)
plt.plot(tempo_total, previsao_total, label='Projeção da IA (Tendência)', color='red', linestyle='--', linewidth=2)

# Customizando o gráfico para ficar com uma estética limpa/robusta
plt.title('EcoSpace Habitat: Controle Preditivo de Temperatura', fontsize=14, fontweight='bold')
plt.xlabel('Pontos de Medição (Intervalos de 15 min)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Salvando o gráfico automaticamente como imagem para usar no PDF final
plt.savefig('grafico_previsao.png', dpi=300, bbox_inches='tight')
print("\n📊 Gráfico 'grafico_previsao.png' gerado e salvo com sucesso!")

plt.show()
