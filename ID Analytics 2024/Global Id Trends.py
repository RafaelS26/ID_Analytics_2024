import pandas as pd
# Carregar os Dados
df = pd.read_csv('digital_id_usage_cleaned.csv')

# Ver o Básico: o que tem de errado?
print(df.info())
print(df.duplicated().sum())

# Limpeza de "Higiene"
df =df.drop_duplicates() #Remover as copias
df['country'] = df['country'].str.strip()

# Tratando Null (aonde não tem o dado uso)
# Estratégia simples: se não tem a porcentagem a linha não serve para análise de uso
df.to_csv('dados_limpos_v1.csv',index=False)
print("limpeza básica concluida com sucesso!")