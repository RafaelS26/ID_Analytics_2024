import pandas as pd
from openpyxl.worksheet.print_settings import PRINT_AREA_RE

df = pd.read_csv('digital_id_final.csv')

ranking = df.groupby('country')['digital_id_usage_pct'].mean().round(2).reset_index()

ranking = ranking.sort_values(by='digital_id_usage_pct', ascending=False)

print("\n" + "="*40)
print("   TOP 10 - ADOÇÃO DE INDENTIDADE DIGITAL")
print("="*40)

print(ranking.head(10).to_string(index=False))
print("="*40)
