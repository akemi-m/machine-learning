O projeto tem como objetivo aplicar **árvores de decisão** para **classificar clientes** em faixas de **pontuação de crédito**. A base contém informações bancárias e dados relacionados ao histórico financeiro, permitindo treinar e avaliar um **modelo de classificação** que auxilie na **análise de risco**.

Para o desenvolvimento, foram utilizadas bibliotecas do ecossistema Python, como **pandas** e **numpy** para manipulação e análise de dados, **matplotlib** para visualizações, e **scikit-learn** para construção, treinamento e avaliação do modelo de aprendizado de máquina.

## Exploração dos Dados

Análise inicial do conjunto de dados - com explicação sobre a natureza dos dados -, incluindo visualizações e estatísticas descritivas.

Nesta etapa foi realizada uma **análise inicial** do conjunto de dados para compreender sua **estrutura** e as **características das variáveis** disponíveis.

### Descrição e estatísticas descritivas das colunas

A base contém as seguintes 28 colunas:

- `ID`: Representa uma identificação única de um registro. Esta coluna é estatisticamente irrelevante, considerando que uma vez que nenhum registro se repete.
- `Customer_ID`: Representa uma identificação única de uma pessoa. Esta coluna é estatisticamente irrelevante, considerando que uma vez que nenhum registro se repete.
- `Month`: Representa o mês do ano. Os valores dessa coluna estão bem distribuidos, com todos os meses representando 12,5% da base.
- `Name`: Representa o nome de uma pessoa. Esta coluna é estatisticamente irrelevante, considerando que uma vez que nenhum registro se repete.
- `Age`: Representa a idade da pessoa. Os valores dessa coluna estão bem distribuidos, sendo a porcentagem maior da base apenas de 3%.
- `SSN`: Representa o número de seguridade social de uma pessoa. Esta coluna é estatisticamente irrelevante, considerando que uma vez que nenhum registro se repete.
- `Occupation`: Representa a ocupação da pessoa. Os valores dessa coluna estão bem distribuidos, com todos as ocupações representando 6,6% da base.
- `Annual_Income`: Representa a renda anual da pessoa. Os valores dessa coluna estão bem distribuidos, com todos os valores representando 0,016% da base.
- `Monthly_Inhand_Salary`: Representa o salário base mensal de uma pessoa. Os valores dessa coluna estão bem distribuidos, com todos os valores representando 0,018% da base.
- `Num_Bank_Accounts`: Representa o número de contas bancárias que a pessoa possui. Os valores dessa coluna estão bem distribuidos, a maior representatividade sendo 13%.
- `Num_Credit_Card`: Representa o número de outros cartões de crédito que a pessoa possui. Os valores dessa coluna estão bem distribuidos, a maior representatividade sendo 18%.
- `Interest_Rate`: Representa a taxa de juros do cartão de crédito. Os valores dessa coluna estão bem distribuidos, com todos os valores representando 5% da base.
- `Num_of_Loan`: Representa o número de empréstimos feitos no banco. Os valores dessa coluna estão bem distribuidos, a maior representatividade sendo 15%.
- `Type_of_Loan`: Representa os tipos de empréstimos feitos por uma pessoa. Os valores dessa coluna estão bem distribuidos, com todos os valores representando 1,44% da base.
- `Delay_from_due_date`: Representa a média de dias de atraso em relação à data de pagamento. Os valores dessa coluna estão bem distribuidos, com todos os valores representando 3,6% da base.
- `Num_of_Delayed_Payment`: Representa a média de pagamentos atrasados por uma pessoa. Os valores dessa coluna estão bem distribuidos, a maior representatividade sendo 8,6%.
- `Changed_Credit_Limit`: Representa a porcentagem de alteração no limite do cartão de crédito. No momento, esta coluna é estatisticamente irrelevante, considerando que uma vez que nenhum registro se repete. Porém, com feature engineering poderiamos extrair informações interessantes para o modelo.
- `Num_Credit_Inquiries`: Representa o número de consultas de cartão de crédito. Os valores dessa coluna estão bem distribuidos, a maior representatividade sendo 11,5%.
- `Credit_Mix`: Representa a classificação da composição de créditos. Os valores dessa coluna estão bem distribuidos, a maior representatividade sendo 36,5%.
- `Outstanding_Debt`: Representa a dívida pendente a ser paga (em USD). No momento, esta coluna é estatisticamente irrelevante, considerando que uma vez que nenhum registro se repete. Porém, com feature engineering poderiamos extrair informações interessantes para o modelo.
- `Credit_Utilization_Ratio`: Representa a taxa de utilização do cartão de crédito. No momento, esta coluna é estatisticamente irrelevante, considerando que uma vez que nenhum registro se repete. Porém, com feature engineering poderiamos extrair informações interessantes para o modelo.
- `Credit_History_Age`: Representa o tempo de histórico de crédito da pessoa. No momento, esta coluna é estatisticamente irrelevante, considerando que a coluna tem informações má construídas. Porém, com feature engineering poderiamos extrair informações interessantes para o modelo.
- `Payment_of_Min_Amount`: Representa se a pessoa pagou apenas o valor mínimo. Os valores dessa coluna estão bem distribuidos, a maior representatividade sendo 52,3%.
- `Total_EMI_per_month`: Representa os pagamentos mensais de EMI (em USD). No momento, esta coluna é estatisticamente irrelevante, considerando que uma vez que nenhum registro se repete. Porém, com feature engineering poderiamos extrair informações interessantes para o modelo.
- `Amount_invested_monthly`: Representa o valor investido mensalmente pelo cliente (em USD). No momento, esta coluna é estatisticamente irrelevante, considerando que uma vez que nenhum registro se repete. Porém, com feature engineering poderiamos extrair informações interessantes para o modelo.
- `Payment_Behaviour`: Representa o comportamento de pagamento do cliente (em USD). Os valores dessa coluna estão bem distribuidos, a maior representatividade sendo 25,5%.
- `Monthly_Balance`: Representa o saldo mensal do cliente (em USD). No momento, esta coluna é estatisticamente irrelevante, considerando que uma vez que nenhum registro se repete. Porém, com feature engineering poderiamos extrair informações interessantes para o modelo.
- `Credit_Score`: Representa a faixa da pontuação de crédito (Poor, Standard, Good). Os valores dessa coluna estão bem distribuidos, a maior representatividade sendo 53,2%.

### Tipagem das colunas

O dataset é composto por apenas três tipos de dados, `Object`, `Float64` e `Int64`:

- **Object(20):** `ID`, `Customer_ID`, `Month`, `Name`, `Age`, `SSN`, `Occupation`, `Annual_Income`, `Num_of_Loan`, `Type_of_Loan`, `Num_of_Delayed_Payment`, `Changed_Credit_Limit`, `Outstanding_Debt`, `Credit_History_Age`, `Payment_of_Min_Amount`, `Amount_invested_monthly`, `Monthly_Balance`, `Payment_Behaviour`, `Credit_Score`, `Credit_Mix`.
- **Float64(4):** `Monthly_Inhand_Salary`, `Num_Credit_Inquiries`, `Credit_Utilization_Ratio`, `Total_EMI_per_month`.
- **Int64(4):** `Num_Bank_Accounts`, `Num_Credit_Card`, `Interest_Rate`, `Delay_from_due_date`.

### Variável Alvo

O modelo tem como **variável alvo (target)** a coluna **`Credit_Score`**, que representa a **classificação de crédito** dos clientes.

A distribuição de classificação dessa variável é a seguinte:

- Standard: 53174 (53,2%)
- Poor: 28998 (29%)
- Good: 17828 (17,8%)

### Amostra dos Dados

A seguir, um exemplo com 3 linhas de um total de 100.000 registros:

=== "data sample (3/100.000)"

    ```python exec="1"
    --8<-- "./docs/arvore-decisao/dataset.py"
    ```

### Visualizações

## Pré-processamento

Nesta etapa foi realizada a **limpeza dos dados** e o **tratamento de valores ausentes**, além da **alteração de tipagem das colunas** para adequação ao modelo. Esse processo é essencial para garantir consistência e qualidade antes do treinamento da árvore de decisão.

### Alteração de Tipagem dos Dados

Como destacado anteriormente, grande parte das colunas do dataset estavam no formato `object`.  
O primeiro passo foi padronizar essas tipagens, ajustando-as para `float64`, `int64` e `category`, de acordo com a natureza de cada variável.

As 20 colunas originalmente do tipo `object` foram tratadas em dois grupos:

- **Apenas alteração de tipo**: `ID`, `Customer_ID`, `Month`, `Name`, `SSN`, `Occupation`, `Type_of_Loan`, `Payment_Behaviour`, `Payment_of_Min_Amount` e `Credit_Score`.
  Essas variáveis puderam ser convertidas diretamente utilizando a função `astype()` do Pandas.

- **Necessidade de alterações antes da conversão**: `Age`, `Annual_Income`, `Num_of_Loan`, `Outstanding_Debt`, `Amount_invested_monthly`, `Monthly_Balance`, `Num_of_Delayed_Payment`, `Changed_Credit_Limit`, `Credit_Mix` e `Credit_History_Age`.
  Muitas dessas colunas apresentavam valores com o caractere `'_'`, impossibilitando a conversão imediata. Nesses casos, o caractere foi substituído por nulos lógicos e, em seguida, a tipagem correta foi aplicada.

### Colunas Retiradas do Modelo

Algumas variáveis foram consideradas irrelevantes para a análise de risco e, portanto, removidas do modelo:

- `ID`, `Customer_ID`, `Month`, `Name`, `SSN`, `Type_of_Loan` e `Credit_History_Age`.

Com isso, restaram **21 colunas** efetivamente utilizadas no processo de modelagem.

- **Float64(9):** `Monthly_Inhand_Salary`, `Num_Credit_Inquiries`, `Credit_Utilization_Ratio`, `Total_EMI_per_month`, `Annual_Income`, `Changed_Credit_Limit`, `Outstanding_Debt`, `Amount_invested_monthly`, `Monthly_Balance`.
- **Int64(7):** `Num_Bank_Accounts`, `Num_Credit_Card`, `Interest_Rate`, `Delay_from_due_date`, `Age`, `Num_of_Loan`, `Num_of_Delayed_Payment`.
- **Category(5):** `Credit_Score`, `Occupation`, `Credit_Mix`, `Payment_of_Min_Amount`, `Payment_Behaviour`.

### Linhas Retiradas do Modelo

Remoção das linhas nulas.

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
