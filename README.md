FIAP - Faculdade de Informática e Administração Paulista
<p align="center">
<a href="https://www.fiap.com.br/">
<img src="../../assets/logo-fiap.png"
     alt="FIAP - Faculdade de Informática e Administração Paulista"
     width="50%">
</a>
</p>
<br>

# EcoSpace Habitat - Controle Preditivo de Inércia Térmica para Biosferas Fechadas
## Grupo: EcoSpace Solutions

## 🧑‍🎓 Integrantes (1TIAO):
* [cite_start]João Pedro Ferreira Alencar - RM573473 [cite: 3, 5]
* [cite_start]Alisson Vinicius de Souza Rabelo Teixeira - RM573512 [cite: 6]
* [cite_start]Lucas Michels Kuntz - RM570050 [cite: 6]

### 👩‍🏫 Tutor(a)
* Sabrina

## 📜 Descrição Técnica e Fundamentação Científica
Diferente de sistemas meteorológicos abertos, que se configuram como sistemas dinâmicos caóticos de alta complexidade e imprevisibilidade inerente, o microclima de uma estufa ou biosfera artificial fechada em ambientes extremos opera sob condições de contorno rigidamente controladas. [cite_start]O **EcoSpace Habitat** é uma Prova de Conceito (POC) que rejeita abordagens puramente reativas (como sistemas baseados em termostatos simples) e introduz o conceito de **Controle Preditivo Baseado em Modelo (MPC)** para a manutenção biológica e eficiência energética do ecossistema[cite: 11, 12].

O cerne do projeto reside na análise da **inércia térmica** do ambiente isolado. Quando ocorre uma falha em sistemas críticos de suporte à vida ou uma variação abrupta na radiação externa, a temperatura interna não decai instantaneamente, mas segue uma taxa de transferência de calor em regime transitório. Em curtos intervalos temporais, esse comportamento pode ser aproximado por uma função linear de decaimento ou ganho térmico.

A solução integra três camadas fundamentais:
1. [cite_start]**Instrumentação e Coleta de Dados (IoT):** Um microcontrolador ESP32 realiza a leitura contínua das variáveis termodinâmicas do ambiente (temperatura e umidade relativa) por meio de um transdutor DHT22 emulado via Wokwi[cite: 15, 103].
2. [cite_start]**Estruturação de Séries Temporais (Python & Pandas):** O fluxo de logs brutos é serializado e processado em DataFrames através da biblioteca Pandas, garantindo o tratamento, consistência matemática e eliminação de ruídos de leitura do sensor[cite: 16].
3. [cite_start]**Análise Preditiva e Ajuste de Curva (Machine Learning & Matplotlib):** Utilizando a biblioteca Scikit-Learn, aplicamos um algoritmo de **Regressão Linear** para modelar o coeficiente angular da variação térmica recente[cite: 17]. [cite_start]Ao calcular a inclinação da reta em tempo real, o algoritmo projeta a tendência termodinâmica para uma janela de curto horizonte (próximas 4 horas)[cite: 18]. 

Se a projeção estatística indicar que o sistema cruzará os limites críticos de estresse biológico do cultivo, um gatilho preventivo é acionado *antes* que a temperatura atinja o ponto de degradação. [cite_start]Isso compensa o tempo de resposta físico (atraso de transporte calórico) dos atuadores térmicos e otimiza o consumo energético do habitat[cite: 12].

## 🔗 Link da Simulação (Wokwi)
* [cite_start]https://wokwi.com/projects/466088547314584577 [cite: 103]

## 🔗 Link do Repositório GitHub
* [cite_start]https://github.com/opedroalencar/gs-economia-espacial-2026 [cite: 105]

## 📁 Estrutura de pastas
* [cite_start]**data/**: Armazena o banco de dados histórico em formato CSV (`dados_estufa.csv`)[cite: 16].
* **docs/**: Contém a documentação do projeto, relatórios em PDF e os gráficos de projeção gerados (`grafico_previsao.png`).
* [cite_start]**src/**: Contém os códigos-fonte da solução, incluindo o script de geração de dados artificiais, o script de análise preditiva em Python e o firmware em C++ compilado para o microcontrolador[cite: 20, 44].
