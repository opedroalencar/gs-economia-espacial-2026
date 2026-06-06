FIAP - Faculdade de Informática e Administração Paulista
<p align="center">
<a href="https://www.fiap.com.br/">
<img src="../../assets/logo-fiap.png"
     alt="FIAP - Faculdade de Informática e Administração Paulista"
     width="50%">
</a>
</p>
<br>

# EcoSpace Habitat
## Grupo: EcoSpace Solutions

## 🧑‍🎓 Integrantes:
* rm573473 - João Pedro Ferreira Alencar
* rm573512 - alisson vinicius de Souza rabelo texeira
* rm570050 - Lucas Michels Kuntz

## 👩‍🏫 Professores:
### Tutor(a)
* Sabrina

## 📜 Descrição
O **EcoSpace Habitat** é uma Prova de Conceito (POC) desenvolvida para responder ao desafio da Global Solution 2026.1 sobre Economia Espacial. A solução consiste em um **Sistema Inteligente de Monitoramento e Predição Climática para Cultivos em Ambientes Extremos**, projetado para estufas de alta tecnologia em regiões remotas da Terra.

O projeto integra três pilares fundamentais do aprendizado:
1. **Hardware & IoT (ESP32):** Simulação no Wokwi utilizando um microcontrolador ESP32 conectado a um sensor DHT22 para capturar leituras de temperatura e umidade em tempo real dentro do habitat espacial.
2. **Análise de Dados (Python & Pandas):** Um script em Python recebe e estrutura os logs brutos gerados pelo sensor em um arquivo CSV, organizando-os em tabelas limpas (DataFrames) prontas para auditoria.
3. **Machine Learning & Visualização (Matplotlib & Scikit-Learn):** A ferramenta gera gráficos visuais de linha mostrando o histórico climático e aplica um algoritmo de **Regressão Linear** para calcular a tendência de aquecimento ou resfriamento do ambiente. Em vez de emitir alertas tardios, o sistema prevê se a temperatura cruzará a linha de perigo nas próximas horas, permitindo ações preventivas de automação para salvar o cultivo.

## 🔗 Link da Simulação (Wokwi)
* https://wokwi.com/projects/466088547314584577

## 📁 Estrutura de pastas
* **data/**: Armazena o banco de dados histórico em formato CSV (`dados\_estufa.csv`).
* **docs/**: Contém a documentação do projeto, relatórios em PDF e os gráficos gerados (`grafico\_previsao.png`).
* **src/**: Contém os códigos-fonte do projeto, incluindo o script de geração de dados, o script de análise preditiva em Python e o código em C++ rodado no ESP32.
