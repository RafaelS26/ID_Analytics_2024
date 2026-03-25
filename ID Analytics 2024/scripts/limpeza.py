import pandas as pd
import os

# Caminho do arquivo que você acabou de colocar na pasta
arquivo_origem = 'data/digital_id_final.csv'

if os.path.exists(arquivo_origem):
    # Lendo o arquivo
    df = pd.read_csv(arquivo_origem)
    
    # --- REQUISITO: CRIAR 2 COLUNAS NOVAS ---
    # 1. Nível de Adoção
    df['nivel_adocao'] = df['digital_id_usage_pct'].apply(
        lambda x: 'Líder' if x > 70 else ('Em Expansão' if x > 40 else 'Início')
    )
    # 2. Gap Digital (O que falta para 100%)
    df['gap_digital'] = 100 - df['digital_id_usage_pct']
    
    # --- REQUISITO: SEPARAR EM 3 TABELAS (Normalização) ---
    # Tabela 1: Países e Regiões
    paises = df[['country_code', 'country', 'region', 'income_group']].drop_duplicates()
    paises.to_csv('data/tabela_paises.csv', index=False)
    
    # Tabela 2: Métricas de Uso
    uso = df[['country_code', 'year', 'digital_id_usage_pct', 'nivel_adocao', 'gap_digital']]
    uso.to_csv('data/tabela_uso.csv', index=False)
    
    # Tabela 3: Descrições
    descricoes = df[['indicator_description', 'source_database']].drop_duplicates()
    descricoes.to_csv('data/tabela_descricoes.csv', index=False)

    print("✅ SUCESSO! As 3 tabelas e as 2 colunas novas foram criadas na pasta 'data'.")
else:
    print("❌ Erro: Arquivo não encontrado. Verifique o nome do arquivo na pasta data.")