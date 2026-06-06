FIAP - Faculdade de Informática e Administração Paulista
<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="assets/logo-fiap.png" alt="FIAP Logo" width="50%">
  </a>
</p>
<br>

# EcoSpace Habitat - Controle Preditivo de Inércia Térmica para Biosferas Fechadas

## 🧑‍🎓 Integrantes (1TIAO):
* João Pedro Ferreira Alencar - RM573473
* Alisson Vinicius de Souza Rabelo Teixeira - RM573512
* Lucas Michels Kuntz - RM570050

## 👩‍🏫 **Tutora:**
*  Sabrina

---

## 📜 Descrição Técnica e Fundamentação Científica

O **EcoSpace Habitat** é um Mínimo Produto Viável (MVP) desenvolvido como Prova de Conceito (POC) para demonstrar a transição do controle climático reativo para o controle preditivo em ambientes fechados e isolados. 

Diferente de sistemas meteorológicos abertos — que se configuram como sistemas dinâmicos caóticos e de alta imprevisibilidade —, o microclima de uma biosfera artificial ou estufa opera sob **condições de contorno delimitadas**. Contudo, diante de falhas técnicas ou oscilações de carga térmica externa, o ambiente enfrenta o desafio do **regime transitório de transferência de calor**. A temperatura interna não varia instantaneamente; sua dinâmica responde à **inércia térmica** e à **capacidade calorífica** do sistema.

Sistemas de automação comuns (como termostatos liga-desliga) atuam tardiamente, respondendo apenas *após* a violação dos limites seguros de tolerância biológica. Este projeto propõe a aplicação do princípio de **Controle Preditivo Baseado em Modelo (MPC)** de curto horizonte para antecipar essas variações e permitir ações preventivas.

### 🛠️ Arquitetura da Solução
1. **Camada de Instrumentação (IoT):** Coleta contínua de temperatura e umidade utilizando um microcontrolador ESP32 e um transdutor DHT22 emulado via plataforma Wokwi.
2. **Camada de Tratamento de Dados:** Estruturação, limpeza e gerenciamento de séries temporais em arquivos de log (`dados_estufa.csv`) utilizando a biblioteca Pandas em Python.
3. **Camada de Inteligência Preditiva (Machine Learning):** Implementação de um algoritmo de **Regressão Linear** via Scikit-Learn. O modelo analisa o comportamento térmico recente para calcular a taxa de variação (coeficiente angular da reta) e projetar a tendência do microclima para uma janela futura de até 4 horas.

---

## ⚠️ Limitações Físicas do Modelo

Como toda Prova de Conceito inicial, o modelo adotado possui restrições físicas importantes que delimitam seu escopo de aplicação:
* **Aproximação Linear de Curto Prazo:** Processos reais de troca térmica e resfriamento são tipicamente não lineares (governados por leis como a Lei do Resfriamento de Newton). A escolha da Regressão Linear neste MVP é matematicamente válida **estritamente para horizontes temporais curtos**, onde o comportamento da curva de transição pode ser aproximado por uma reta sem perda crítica de acurácia.
* **Premissa de Isolação Estática:** O algoritmo assume que as propriedades de isolamento térmico do ambiente permanecem constantes durante a janela de previsão. Interferências externas abruptas e imediatas (como uma ruptura estrutural) invalidam a capacidade preditiva do modelo estatístico atual.

---

## 🔗 Links do Projeto

* **Simulador do Hardware (Wokwi):** [https://wokwi.com/projects/466088547314584577]
* **Repositório Principal (GitHub):** [https://github.com/opedroalencar/gs-economia-espacial-2026]

---

## 📁 Estrutura de Pastas do Repositório

* **`data/`**: Contém a série temporal histórica estruturada em formato tabular (`dados_estufa.csv`).
* **`docs/`**: Documentação complementar do projeto, relatórios em formato PDF e o gráfico de controle gerado (`grafico_previsao.png`).
* **`src/`**: Códigos-fonte do ecossistema:
  * Script Python de análise preditiva e machine learning.
  * Firmware em C++ desenvolvido para o microcontrolador ESP32.
