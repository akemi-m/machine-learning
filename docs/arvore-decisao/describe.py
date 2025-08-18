import pandas as pd
from tabulate import tabulate

df = pd.read_csv('./docs/arvore-decisao/credit_score_classification.csv')

print(tabulate(df.describe(), headers="keys", tablefmt="github"))
