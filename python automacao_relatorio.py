import pandas as pd
from datetime import datetime
import os

vendas_2025 = os.path.join(os.getcwd(), 'dados', 'vendas_2025.csv')
print("=== AUTOMAÇÃO DE RELATÓRIO MENSAL ===\n")

# Leitura correta do seu CSV brasileiro
df = pd.read_csv(vendas_2025, sep=';', encoding='utf-8', decimal=',')

# Conversão das colunas numéricas (a mágica que faltava)
df['Quantidade']     = pd.to_numeric(df['Quantidade'], errors='coerce')
df['Preço Unitário'] = pd.to_numeric(df['Preço Unitário'].astype(str).str.replace('.', '').str.replace(',', '.'), errors='coerce')

# Tratamento da data
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)

# Cálculo do valor total
df['Valor_Total'] = df['Quantidade'] * df['Preço Unitário']

# KPIs
total          = df['Valor_Total'].sum()
ticket_medio   = df['Valor_Total'].mean()
melhor_vendedor = df.groupby('Vendedor')['Valor_Total'].sum().idxmax()

# Relatório no terminal
print("=== RELATÓRIO MENSAL ===")
print(f"Total de vendas:  R$ {total:,.2f}")
print(f"Ticket médio:     R$ {ticket_medio:,.2f}")
print(f"Melhor vendedor:  {melhor_vendedor}\n")

# Gera o Excel lindo
arquivo = f"Relatorio_{datetime.now().strftime('%Y_%m')}.xlsx"
with pd.ExcelWriter(arquivo, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Dados_Completos', index=False)
    pd.DataFrame({
        'Métrica': ['Total Vendido', 'Ticket Médio', 'Melhor Vendedor', 'Gerado em'],
        'Valor': [f"R$ {total:,.2f}", f"R$ {ticket_medio:,.2f}", melhor_vendedor, datetime.now().strftime('%d/%m/%Y %H:%M')]
    }).to_excel(writer, sheet_name='Resumo', index=False)

print(f"RELATÓRIO GERADO COM SUCESSO: {arquivo} 🎉🎉🎉")
print("Abra a pasta e confira o Excel lindo que acabou de nascer!")