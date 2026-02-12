import pandas as pd
df = pd.read_csv('digital_id_usage_cleaned.csv')

# Limpar os noms das colunas
df.columns = df.columns.str.strip()

# tratar os Dados de texto
df['country'] = df['country'].str.strip()
df['region'] = df['region'].str.strip()

# Coração da limpeza valores null
'digital_id_usage_pct'
df_limpo = df.dropna(subset=['digital_id_usage_pct'])
df_limpo.to_csv('digital_id_final.csv',index=False)

print("Faxina Concluida! O novo Arquivo 'digital_id_final.csv' foi criado.")

print("total de Linhas ANTES:", len(df))
print("total de linhas DEPOIS:", len(df_limpo))

print("Linhas duplicadas indificadores:",df_limpo.duplicated().sum())
# remover as Linhas duplicadas indificadores: 6
df_limpo = df_limpo.drop_duplicates()

print("Novo Total de linhas (sem duplicados):", len(df_limpo))