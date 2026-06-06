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
* João Pedro Ferreira Alencar - RM573473
* Alisson Vinicius de Souza Rabelo Teixeira - RM573512
* Lucas Michels Kuntz - RM570050

## 👩‍🏫 Professores:
### Tutor(a)
* Sabrina

### Coordenador(a)
* Nome do Coordenador

## 📜 Descrição Técnica e Fundamentação Científica
Diferente de sistemas meteorológicos abertos, que se configuram como sistemas dinâmicos caóticos de alta complexidade e imprevisibilidade inerente, o microclima de uma estufa ou biosfera artificial fechada em ambientes extremos opera sob condições de contorno rigidamente controladas. O **EcoSpace Habitat** é uma Prova de Conceito (POC) que rejeita abordagens puramente reativas (como sistemas baseados em termostatos simples) e introduz o conceito de **Controle Preditivo Baseado em Modelo (MPC)** para a manutenção biológica e eficiência energética do ecossistema.

O cerne do projeto reside na análise da **inércia térmica** do ambiente isolado. Quando ocorre uma falha em sistemas críticos de suporte à vida ou uma variação abrupta na radiação externa, a temperatura interna não decai instantaneamente, mas segue uma taxa de transferência de calor em regime transitório. Em curtos intervalos temporais, esse comportamento pode ser aproximado por uma função linear de decaimento ou ganho térmico.

A solução integra três camadas fundamentais:
1. **Instrumentação e Coleta de Dados (IoT):** Um microcontrolador ESP32 realiza a leitura contínua das variáveis termodinâmicas do ambiente (temperatura e umidade relativa) por meio de um transdutor DHT22 emulado via Wokwi.
2. **Estruturação de Séries Temporais (Python & Pandas):** O fluxo de logs brutos é serializado e processado em DataFrames através da biblioteca Pandas, garantindo o tratamento, consistência matemática e eliminação de ruídos de leitura do sensor.
3. **Análise Preditiva e Ajuste de Curva (Machine Learning & Matplotlib):** Utilizando a biblioteca Scikit-Learn, aplicamos um algoritmo de **Regressão Linear** para modelar o coeficiente angular da variação térmica recente. Ao calcular a inclinação da reta em tempo real, o algoritmo projeta a tendência termodinâmica para uma janela de curto horizonte (próximas 4 horas).

Se a projeção estatística indicar que o sistema cruzará os limites críticos de estresse biológico do cultivo, um gatilho preventivo é acionado antes que a temperatura atinja o ponto de degradação. Isso compensa o tempo de resposta físico (atraso de transporte calórico) dos atuadores térmicos e otimiza o consumo energético do habitat.

## 🔗 Link da Simulação (Wokwi)
* https://wokwi.com/projects/466088547314584577

## 🔗 Link do Repositório GitHub
* https://github.com/opedroalencar/gs-economia-espacial-2026

## 📁 Estrutura de pastas
* **data/**: Armazena o banco de dados histórico em formato CSV (`dados_estufa.csv`).
* **docs/**: Contém a documentação do projeto, relatórios em PDF e os gráficos de projeção gerados (`grafico_previsao.png`).
* **src/**: Contém os códigos-fonte da solução, incluindo o script de geração de dados artificiais, o script de análise preditiva em Python e o firmware em C++ compilado para o microcontrolador.
