# Automação de Relatório Mensal de Vendas com Python

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

Projeto real de automação que elimina trabalho manual repetitivo — exatamente o tipo de solução que eu já entreguei em produção no Itaú e na DASA.

## Objetivo do projeto
Ler um CSV bruto de vendas, tratar os dados, calcular KPIs automaticamente e gerar um relatório Excel formatado com duas abas (dados completos + resumo executivo) em menos de 5 segundos.

## Funcionalidades
- Leitura automática de CSV brasileiro (separador `;` e vírgula como decimal)
- Tratamento de datas e cálculo de valor total
- Cálculo automático de:
  - Total vendido no mês
  - Ticket médio
  - Melhor vendedor
- Geração de arquivo Excel com duas abas (Dados Completos + Resumo executivo)
- 100% automatizado — pode ser agendado com Windows Task Scheduler ou Airflow

## Tecnologias utilizadas
- Python 3
- Pandas
- openpyxl (para Excel)

## Como executar
```bash
# 1. Clone o repositório
git clone https://github.com/santiago0070/automacao-relatorio-mensal.git
cd automacao-relatorio-mensal

# 2. Instale as dependências
pip install pandas openpyxl

# 3. Execute
python automacao_relatorio.py
