O projeto tem como objetivo aplicar **árvores de decisão** para **classificar clientes** em faixas de **pontuação de crédito**. A base contém informações bancárias e dados relacionados ao histórico financeiro, permitindo treinar e avaliar um **modelo de classificação** que auxilie na **análise de risco**.

Para o desenvolvimento, foram utilizadas bibliotecas do ecossistema Python, como **pandas** e **numpy** para manipulação e análise de dados, **matplotlib** para visualizações, e **scikit-learn** para construção, treinamento e avaliação do modelo de aprendizado de máquina.

## Exploração dos Dados

Análise inicial do conjunto de dados - com explicação sobre a natureza dos dados -, incluindo visualizações e estatísticas descritivas.

Nesta etapa foi realizada uma **análise inicial** do conjunto de dados para compreender sua **estrutura** e as **características das variáveis** disponíveis.

### Estrutura do Conjunto de Dados

O dataset é composto por **28 colunas**, com diferentes tipos de dados:

- **Object:** `ID`, `Customer_ID`, `Month`, `Name`, `Age`, `SSN`, `Occupation`, `Annual_Income`, `Num_of_Loan`, `Type_of_Loan`, `Num_of_Delayed_Payment`, `Changed_Credit_Limit`, `Outstanding_Debt`, `Credit_History_Age`, `Payment_of_Min_Amount`, `Amount_invested_monthly`, `Monthly_Balance`, `Credit_Score`.
- **Float64:** `Monthly_Inhand_Salary`, `Num_Credit_Inquiries`, `Credit_Utilization_Ratio`, `Total_EMI_per_month`.
- **Int64:** `Num_Bank_Accounts`, `Num_Credit_Card`, `Interest_Rate`, `Delay_from_due_date`.
- **Category:** `Payment_Behaviour`.

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
