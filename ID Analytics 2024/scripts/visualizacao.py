import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Caminho dos dados gerados no passo anterior
caminho_dados = 'data/tabela_uso.csv'
pasta_viz = 'visualizacoes'

# Criar pasta de visualizações se não existir
if not os.path.exists(pasta_viz):
    os.makedirs(pasta_viz)

if os.path.exists(caminho_dados):
    df = pd.read_csv(caminho_dados)
    
    # Configurar o estilo visual
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(3, 2, figsize=(16, 18))
    fig.suptitle('Análise Exploratória: Identidade Digital Global', fontsize=20)

    # 1. Gráfico de Barras (Média de Uso por Nível de Adoção)
    sns.barplot(x='nivel_adocao', y='digital_id_usage_pct', data=df, ax=axes[0, 0], palette='viridis')
    axes[0, 0].set_title('Uso Médio por Nível de Adoção')

    # 2. Histograma (Distribuição da Porcentagem de Uso) -> [REQUISITO]
    sns.histplot(df['digital_id_usage_pct'], bins=15, kde=True, ax=axes[0, 1], color='skyblue')
    axes[0, 1].set_title('Distribuição Global da Adoção (%)')

    # 3. Boxplot (Para identificar Outliers) -> [REQUISITO]
    sns.boxplot(y=df['digital_id_usage_pct'], ax=axes[1, 0], color='lightgreen')
    axes[1, 0].set_title('Análise de Outliers (Pontos Fora da Curva)')

    # 4. Gráfico de Dispersão (Uso Atual vs Gap Digital) -> [REQUISITO]
    sns.scatterplot(x='digital_id_usage_pct', y='gap_digital', hue='nivel_adocao', data=df, ax=axes[1, 1])
    axes[1, 1].set_title('Dispersão: Uso Atual vs Gap para 100%')

    # 5. Gráfico de Pizza ou Contagem (Proporção de Países por Nível) -> [REQUISITO]
    counts = df['nivel_adocao'].value_counts()
    axes[2, 0].pie(counts, labels=counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    axes[2, 0].set_title('Proporção Global de Níveis de Adoção')

    # Remover o último gráfico vazio
    fig.delaxes(axes[2, 1])

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    # Salvar a imagem final
    plt.savefig(f'{pasta_viz}/analise_exploratoria_final.png')
    print(f"✅ SUCESSO! O gráfico com as 5 análises foi salvo na pasta '{pasta_viz}'.")
    plt.show()
else:
    print("❌ Erro: Tabela de uso não encontrada na pasta 'data'.")