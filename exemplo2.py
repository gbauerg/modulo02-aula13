import pandas as pd
from datetime import datetime
import polars as pl

ENDERECO_DADOS = "./../Base de Dados/"

try:
    inicio = datetime.now()

    lista_arquivos = ["202601_NovoBolsaFamilia.csv", "202602_NovoBolsaFamilia.csv", "202603_NovoBolsaFamilia.csv", "202604_NovoBolsaFamilia.csv", "202605_NovoBolsaFamilia.csv"]

    df_bolsafamilia = None
    
    for arquivo in lista_arquivos:
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator =";", encoding='iso-8859-1')
        
        if df_bolsafamilia is None:
            df_bolsafamilia = df
        else:
            df_bolsafamilia = pl.concat([df_bolsafamilia, df])

        del df

    print(df_bolsafamilia)

    fim = datetime.now()
    print(f"Tempo Total {fim - inicio}")

except Exception as e:
    print(f"Erro ao obter Dados: {e}")