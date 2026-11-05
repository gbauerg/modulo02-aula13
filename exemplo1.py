import pandas as pd
from datetime import datetime
import polars as pl

ENDEREÇO_DADOS = "./../Base de Dados/"
#tempo pandas = 24.949447
#tempo polars = 07.225629'
try:
    inicio = datetime.now()
    #df_janeiro = pd.read_csv(ENDEREÇO_DADOS + "202601_NovoBolsaFamilia.csv", sep =";", encoding='iso-8859-1')

    #Polars
    df_janeiro = pl.read_csv(ENDEREÇO_DADOS + "202601_NovoBolsaFamilia.csv", separator =";", encoding='iso-8859-1')
    
    print(df_janeiro.head())
    print(df_janeiro.columns)

    fim = datetime.now()
    print(f"Tempo Total {fim - inicio}")

except Exception as e:
    print(f"Erro ao obter Dados: {e}")