# MVP- Engenharia-de-Dados 📊

Nome: Hugo Coelho de Frias

Matrícula: 4052025000248

Linkedin: https://www.linkedin.com/in/hugo-frias-7059b622/

E-mail: hugofrias2@hotmail.com

**1. Objetivo**

O Conjunto de Dados de 'Mental Health and Lifestyle Habits Dataset (2019-2024)' é uma coleção abrangente de dados que visa compreender como diversos fatores de estilo de vida afetam o bem-estar mental. Esta base de dados captura aspectos como rotinas de exercícios, hábitos alimentares, padrões de sono, níveis de estresse e interações sociais, além de informações demográficas. A partir do conjunto de dados, se deseja responder as seguintes perguntas:

1. Podemos classificar os 'níveis de stress e bem-estar' de acordo a faixa etária?

2. Podemos identificar diferenças relevantes em atributos considerando determinada faixa etária?

3. Quais países têm maior nível médio de estresse?

4. Quais países têm maior felicidade média?

5. Há países onde as pessoas dormem mais?

6. O tempo de tela varia muito entre países?

7. Há algum padrão facilmente de ser identificado apenas com uma análise gráfica?

8. Podemos identificar 'níveis de stress e bem-estar' de acordo com hábitos do cotidiano?

9. Podemos segregar os diferentes níveis de stress e bem-estar de acordo com as aferições de horas de sono, horas de trabalho e horas em telas diários, por exemplo?

**2. Coleta**

O dataset analisado foi escoliho na coleção da plataforma Kaggle:

Dataset: [Mental_Health_Lifestyle](https://www.kaggle.com/datasets/atharvasoundankar/mental-health-and-lifestyle-habits-2019-2024)

Trata-se de um de um dataset (tabela única) que possui 3000 instâncias, de maneira balanceada em relação aos seus atributos categóricos (Países, Gêneros, Tipo de Dieta etc). No total, possui 12 atributos.

Os dados foram armazenados em um Volume do Databrticks:

<img width="1162" height="423" alt="image" src="https://github.com/user-attachments/assets/037e5b4b-5ab7-408c-b116-dd3d19680c55" />


**3. Modelagem**

Como citado no item anterior de coleta de dados, o dataset 'Mental Health and Lifestyle Habits Dataset (2019-2024)' é uma tabela única na qual não se torna necessária a contrução de esquemas mais refinados, como Esquema Estrela ou Snowflake.

O Catálogo dos dados foi realizado dentro da tabela (camada bronze do Databricks):

<img width="1143" height="490" alt="image" src="https://github.com/user-attachments/assets/a70432cf-3e12-446f-9848-b61608ce702c" />


___________

-  **Linhagem de Dados:**
    - Origem: Plataforma Kaggle
    - Dataset: [Mental_Health_Lifestyle](https://www.kaggle.com/datasets/atharvasoundankar/mental-health-and-lifestyle-habits-2019-2024)
    -  Trata-se de um de um dataset (tabela única) que possui 3000 instâncias, de maneira balanceada em relação aos seus atributos categóricos (Países, Gêneros, Tipo de Dieta etc). No           total,    possui 12 atributos.
   

**4. Carga**

Toda a etapa de ETL (Extração, Transformação e Carga) foi realizada com a utilização da funcionalidade nativa do Databricks para contrução de Pipelines.

<img width="915" height="229" alt="image" src="https://github.com/user-attachments/assets/d16fb229-9ca7-4163-a350-9329de671223" />

___________

Todo conceito de contrução foi baseado na metolologia **'Medallion Architecture'**:

<img width="662" height="318" alt="image" src="https://github.com/user-attachments/assets/224409a1-0b4a-4fc2-ae58-59cf5945ad5a" />

Fonte: https://www.databricks.com/glossary/medallion-architecture

Arquitetura no Databricks:

<img width="449" height="352" alt="image" src="https://github.com/user-attachments/assets/56502d4e-b22d-4266-ac94-e02780dba95f" />

Criação dos esquemas no Databricks:

<img width="576" height="325" alt="image" src="https://github.com/user-attachments/assets/e6664da5-cd95-47d3-a69b-b4796307aa64" />

Acessar Arquivo SQL: https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/Catalog%20Creation.sql

___________
>🥉Camada Bronze:

Ingestão dos "Dados Raw" utilizando a funcionalidade nativa do Databricks para o início do Pipeline:

<img width="550" height="185" alt="image" src="https://github.com/user-attachments/assets/45882e48-833a-4cc8-b92c-819759628f15" />

<img width="585" height="147" alt="image" src="https://github.com/user-attachments/assets/0fb63e41-d90b-4b49-9c36-852be9e70366" />

Acessar Link: https://hugocfrias.github.io/MVP--Engenharia-de-Dados/1.Camada_Bronze/Exploration_Data.html

___________
>🥈Camada Silver:

Após a análise dos dados importados pela camada bronze, foi realizada uma análise do dataset. Dessa forma, foi identificada a necessidade de remoção do atributo ''

A limpeza consiste na verificação da consistência das informações, correção de possíveis erros de preenchimento ou eliminação de valores desconhecidos, redundantes ou não pertencentes ao domínio.

Acessar Link: https://hugocfrias.github.io/MVP--Engenharia-de-Dados/2.Camada_Silver/Exploration_Data.html

No dataframe 'df', podemos ver abaixo que há 595 instâncias com valores nulos no atributo 'Mental Health Condition'. Analisando o dataset original, as 595 linhas nulas estão com o status de 'NaN'. Por ser tratar de um estado de desordem mental (Mental Health Condition), tive a dúvida se realmente são informações faltantes ou simplesmente instâncias nas quais o respondente não possuía algum tipo de desordem mental.

<img width="1320" height="435" alt="image" src="https://github.com/user-attachments/assets/321624c6-8b82-4efa-89b5-4201be147a02" />

Código: https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/2.Camada_Silver/Silver_Tranformation.py

___________
>🥇Camada Gold:

<img width="1321" height="436" alt="image" src="https://github.com/user-attachments/assets/82b9f37a-b332-48b4-a4bd-68911a3efbd2" />



https://hugocfrias.github.io/MVP--Engenharia-de-Dados/1.Camada_Bronze/Exploration_Data.html


