O projeto tem como objetivo aplicar **árvores de decisão** para **classificar clientes** em faixas de **pontuação de crédito**. A base contém informações bancárias e dados relacionados ao histórico financeiro, permitindo treinar e avaliar um **modelo de classificação** que auxilie na **análise de risco**.

Para o desenvolvimento, foram utilizadas bibliotecas do ecossistema Python, como **pandas** e **numpy** para manipulação e análise de dados, **matplotlib** para visualizações, e **scikit-learn** para construção, treinamento e avaliação do modelo de aprendizado de máquina.

## Exploração dos Dados

Análise inicial do conjunto de dados - com explicação sobre a natureza dos dados -, incluindo visualizações e estatísticas descritivas.

Nesta etapa foi realizada uma **análise inicial** do conjunto de dados para compreender sua **estrutura** e as **características das variáveis** disponíveis.

### Estrutura do Conjunto de Dados

O dataset é composto por **28 colunas**, com diferentes tipos de dados:

- **Object(20):** `ID`, `Customer_ID`, `Month`, `Name`, `Age`, `SSN`, `Occupation`, `Annual_Income`, `Num_of_Loan`, `Type_of_Loan`, `Num_of_Delayed_Payment`, `Changed_Credit_Limit`, `Outstanding_Debt`, `Credit_History_Age`, `Payment_of_Min_Amount`, `Amount_invested_monthly`, `Monthly_Balance`, `Payment_Behaviour`, `Credit_Score`, `Credit_Mix`.
- **Float64(4):** `Monthly_Inhand_Salary`, `Num_Credit_Inquiries`, `Credit_Utilization_Ratio`, `Total_EMI_per_month`.
- **Int64(4):** `Num_Bank_Accounts`, `Num_Credit_Card`, `Interest_Rate`, `Delay_from_due_date`.

### Variável Alvo

O modelo tem como **variável alvo (target)** a coluna **`Credit_Score`**, que representa a **classificação de crédito** dos clientes.

Essa variável é categórica, indicando a faixa de risco associada a cada cliente, e será utilizada para treinar e avaliar o desempenho das **árvores de decisão**.

### Amostra dos Dados

A seguir, um exemplo com 3 linhas de um total de 100.000 registros:

=== "data sample (3/100.000)"

    ```python exec="1"
    --8<-- "./docs/arvore-decisao/dataset.py"
    ```

### Estatísticas Descritivas

A tabela abaixo resume as **estatísticas descritivas** calculadas para as variáveis numéricas do dataset:

=== "summary statistics"

    ```python exec="1"
    --8<-- "./docs/arvore-decisao/describe.py"
    ```

Essas medidas incluem **contagem de valores (count)**, **média (mean)**, **desvio padrão (std)**, **mínimo (min)**, **percentis (25%, 50%, 75%)** e **máximo (max)**.  
É importante destacar que algumas colunas aparecem como `object` no dataset, o que impede que sejam incluídas nessa análise estatística automaticamente.

### Visualizações

## Pré-processamento

Limpeza dos dados, tratamento de valores ausentes e normalização.

### Alteração de tipagem dos dados

Considerando a quantidade de colunas de tipo Object mencionadas anteriormente, traz a importância de fazer a mudança de tipagem adequada para cada coluna.

A primeiro momento, foquei em definir os tipos da colunas como string, float64 e int64.

Deixando um pouco de lado o tipo `category`, já que a maioria das colunas, tirando `Credit_Score`, eram necessárias efetuar limpeza antes de serem feitas a mudança de tipagem, que será feita nos próximos passos.

Assim, nesse momento, agrupei as 20 colunas alteradas em duas situações diferentes:

- Apenas alteração de tipo: `ID`, `Customer_ID`, `Month`, `Name`, `SSN`, `Occupation`, `Type_of_Loan`, `Payment_Behaviour`, `Payment_of_Min_Amount` e `Credit_Score` funcionaram apenas utilizando a função de troca de tipo do Pandas;
- Remoção de sujeira para depois converter para o tipo adequado: `Age`, `Annual_Income`, `Num_of_Loan`, `Outstanding_Debt`, `Amount_invested_monthly`, `Monthly_Balance`, `Num_of_Delayed_Payment`, `Changed_Credit_Limit`, `Credit_Mix` e `Credit_History_Age` havia bastante linhas com o caractere '\_', prejudicando a conversão de tipagem. Assim, foi feita uma substituição desses caracteres para nulos lógicos e depois efetuar a tipagem correta.

Por fim, a tipagem das 28 colunas ficou assim:

- **String(11):** `ID`, `Customer_ID`, `Month`, `Name`, `SSN`, `Occupation`, `Type_of_Loan`, `Credit_Mix`, `Credit_History_Age`, `Payment_of_Min_Amount`, `Payment_Behaviour`.
- **Float64(9):** `Monthly_Inhand_Salary`, `Num_Credit_Inquiries`, `Credit_Utilization_Ratio`, `Total_EMI_per_month`, `Annual_Income`, `Changed_Credit_Limit`, `Outstanding_Debt`, `Amount_invested_monthly`, `Monthly_Balance`.
- **Int64(7):** `Num_Bank_Accounts`, `Num_Credit_Card`, `Interest_Rate`, `Delay_from_due_date`, `Age`, `Num_of_Loan`, `Num_of_Delayed_Payment`.
- **Category(1):** `Credit_Score `.

### Colunas retiradas do modelo

As colunas `ID`, `Customer_ID`, `Month`, `Name`, `SSN` e `Type_of_Loan` foram retiradas do modelo, já que não são informações relevantes.
Totalizando 22 colunas para utilizar no modelo.

### Limpeza e mudança de tipagem de colunas categóricas

Sobre as colunas que são categóricas e foram colocadas temporariamente como string, `Occupation`, `Credit_Mix`, `Payment_of_Min_Amount` e `Payment_Behaviour`, elas serão limpas e feitas a alteração de tipo.

Por fim, a tipagem das 22 colunas ficou assim:

- **String(1):** `Credit_History_Age`.
- **Float64(9):** `Monthly_Inhand_Salary`, `Num_Credit_Inquiries`, `Credit_Utilization_Ratio`, `Total_EMI_per_month`, `Annual_Income`, `Changed_Credit_Limit`, `Outstanding_Debt`, `Amount_invested_monthly`, `Monthly_Balance`.
- **Int64(7):** `Num_Bank_Accounts`, `Num_Credit_Card`, `Interest_Rate`, `Delay_from_due_date`, `Age`, `Num_of_Loan`, `Num_of_Delayed_Payment`.
- **Category(5):** `Credit_Score `, `Occupation`, `Credit_Mix`, `Payment_of_Min_Amount`, `Payment_Behaviour`.

### Engenharia de dados com `Credit_History_Age`

//

```python exec="on" html="1"
--8<-- "./docs/arvore-decisao/decision-tree.py"
```

## Divisão dos Dados

Separação do conjunto de dados em treino e teste.

## Treinamento do Modelo

Implementação do modelo Decision Tree.

## Avaliação do Modelo

Avaliação do desempenho do modelo utilizando métricas apropriadas.

## Relatório Final

Documentação do processo, resultados obtidos e possíveis melhorias.
