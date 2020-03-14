import pandas as pd
class PD:
    df = pd.read_excel("data.xlsx",sheet_name="init").iloc[0,0]
    shop = pd.read_excel("data.xlsx",sheet_name="init").iloc[1,0]
    print(shop)