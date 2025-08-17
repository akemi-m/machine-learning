# import matplotlib.pyplot as plt
# import pandas as pd

# from io import StringIO

# plt.figure(figsize=(5, 4))

# # 'Good', 'Poor', 'Standard'
# # Credit_Score

# df = pd.read_csv('./docs/arvore-decisao/credit_score_classification.csv')
# good = df[df['Credit_Score'] == 'Good']
# standard = df[df['Credit_Score'] == 'Standard']
# poor = df[df['Credit_Score'] == 'Poor']
# plt.plot(
#     normais['Periodo'], normais['Valor'], 'ob',
#     fraudes['Periodo'], fraudes['Valor'], 'or',
# )

# # Para imprimir na página HTML
# buffer = StringIO()
# plt.savefig(buffer, format="svg", transparent=True)
# print(buffer.getvalue())