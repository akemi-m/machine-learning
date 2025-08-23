import matplotlib.pyplot as plt
import pandas as pd

from io import StringIO
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

plt.figure(figsize=(12, 10))

df = pd.read_csv('./docs/arvore-decisao/credit_score_classification.csv')

label_encoder = LabelEncoder()

# Carregar o conjunto de dados

# todas as colunas menos o target
x = df.drop("Credit_Score", axis=1)

# aplicar label encoder nas categóricas
x['Occupation'] = label_encoder.fit_transform(x['Occupation'])
x['Credit_Mix'] = label_encoder.fit_transform(x['Credit_Mix'])
x['Payment_of_Min_Amount'] = label_encoder.fit_transform(x['Payment_of_Min_Amount'])
x['Payment_Behaviour'] = label_encoder.fit_transform(x['Payment_Behaviour'])

# apenas a target
y = df["Credit_Score"]
y['Credit_Score'] = label_encoder.fit_transform(y['Credit_Score'])

# Dividir os dados em conjuntos de treinamento e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo de árvore de decisão
classifier = tree.DecisionTreeClassifier()
classifier.fit(x_train, y_train)

# Avaliar o modelo
accuracy = classifier.score(x_test, y_test)
print(f"Accuracy: {accuracy:.2f}")
tree.plot_tree(classifier)

# Para imprimir na página HTML
buffer = StringIO()
plt.savefig(buffer, format="svg")
print(buffer.getvalue())