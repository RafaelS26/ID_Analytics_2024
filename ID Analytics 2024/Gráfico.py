import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('digital_id_final.csv')

ranking =df.groupby('country')['digital_id_usage_pct'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
ranking.plot(kind='bar',color='royalblue')

plt.title('Top 10 paises - Adoção de Indentidade Digital', fontsize=15)
plt.xlabel('Paises', fontsize=12)
plt.ylabel('Porcentagem de Uso (%)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y',linestyle='--',alpha=0.7)

plt.tight_layout()
plt.show()