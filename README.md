# 🛡 Autonomous AI SOC Cloud Lab

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


Plataforma de simulação de um Security Operations Center (SOC) com engine de risco baseada em IA, desenvolvida em Python e Streamlit.

O projeto simula eventos de segurança, calcula score de risco contextual, classifica níveis de ameaça e exibe tendências históricas em tempo real — funcionando como um mini-SIEM educacional.

## 🎯 Objetivo do Projeto

Demonstrar a aplicação de Inteligência Artificial e modelagem de risco em um ambiente simulado de Security Operations Center (SOC), com foco em:

- Automação de análise de eventos
- Cálculo contextual de risco
- Classificação automática de ameaças
- Visualização estratégica de métricas
  
---

## 🚀 Funcionalidades

- 🔥 Simulação de eventos de segurança
- 🧠 Engine de cálculo de risco contextual
- 🎯 Classificação automática de ameaças (LOW / MEDIUM / HIGH / CRITICAL)
- 📊 Visualização de tendência de risco ao longo do tempo
- 📈 Métricas do SOC (Total de eventos e risco médio)
- 🔄 Modo automático (simulação em tempo real)
- 🧹 Reset do ambiente

---

## 🏗 Arquitetura do Sistema

Fluxo de funcionamento:

Gerador de Evento → Engine de Risco → Classificação → Dashboard → Histórico

O cálculo de risco considera:

- Severidade do evento
- Tipo de ameaça (CVE, phishing, brute force, malware)
- Peso contextual aplicado por tipo de ataque

---

## 🛠 Stack Tecnológica

- Python 3.12
- Streamlit
- Pandas
- Docker (opcional para deploy)

---

## ▶ Como Executar Localmente

1️⃣ Criar ambiente virtual:

```bash

```
python -m venv venv
```
2️⃣ Ativar ambiente:

Windows:

venv\Scripts\Activate

3️⃣ Instalar dependências:

pip install -r requirements.txt

4️⃣ Executar aplicação:

streamlit run app/app.py

Abrir no navegador:

http://localhost:8501
🧪 Casos de Uso

Portfólio para Segurança da Informação

Demonstração de lógica de cálculo de risco

Simulação de fluxo de SOC

Laboratório educacional de cibersegurança

Base para construção de SIEM customizado

🔮 Próximas Evoluções

Integração com API de Threat Intelligence

Persistência em banco de dados (PostgreSQL)

Autenticação de usuários

Multi-tenant

Deploy em nuvem (AWS / Render / Azure)




## 👩‍💻 Sobre a Autora

**Paula Sabino**  
Security Engineering | AI aplicada à Cibersegurança  

🔗 GitHub: https://github.com/Paula-Tech007  
🔗 LinkedIn: https://www.linkedin.com/in/paula-sabino-49830573/


Projeto desenvolvido como parte de um portfólio técnico focado em:

Inteligência Artificial aplicada à Segurança

Engenharia de Segurança

Blue Team / SOC

Análise de risco automatizada
