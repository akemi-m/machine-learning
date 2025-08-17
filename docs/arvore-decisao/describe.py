import pandas as pd

df = pd.read_csv('./docs/arvore-decisao/credit_score_classification.csv')

from tabulate import tabulate
print(tabulate(df.describe(), headers="keys", tablefmt="github"))
