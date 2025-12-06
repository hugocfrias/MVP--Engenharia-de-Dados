# MVP- Engenharia-de-Dados 📊

Nome: Hugo Coelho de Frias

Matrícula: 4052025000248

Linkedin: https://www.linkedin.com/in/hugo-frias-7059b622/

E-mail: hugofrias2@hotmail.com

**1. Objetivo**

O Conjunto de Dados de 'Mental Health and Lifestyle Habits Dataset (2019-2024)' é uma coleção abrangente de dados que visa compreender como diversos fatores de estilo de vida afetam o bem-estar mental. Esta base de dados captura aspectos como rotinas de exercícios, hábitos alimentares, padrões de sono, níveis de estresse e interações sociais, além de informações demográficas. A partir do conjunto de dados, se deseja responder as seguintes perguntas:

1. Podemos identificar 'níveis de stress e bem-estar' de acordo com hábitos do cotidiano?

2. Podemos classificar os 'níveis de stress e bem-estar' de acordo a faixa etária?

3. Podemos segregar os diferentes níveis de stress e bem-estar de acordo com as aferições de horas de sono, horas de trabalho e horas em telas diários, por exemplo?

4. Há algum padrão facilmente de ser identificado apenas com uma análise gráfica?

**2. Coleta**

O dataset analisado foi escoliho na coleção da plataforma Kaggle:

Dataset: [Mental_Health_Lifestyle](https://www.kaggle.com/datasets/atharvasoundankar/mental-health-and-lifestyle-habits-2019-2024)

Trata-se de um de um dataset (tabela única) que possui 3000 instâncias, de maneira balanceada em relação aos seus atributos categóricos (Países, Gêneros, Tipo de Dieta etc). No total, possui 12 atributos.

Os dados foram armazenados em um Volume do Databrticks:

<img width="1170" height="414" alt="image" src="https://github.com/user-attachments/assets/19b1e15c-e2a3-4bb7-bc13-fce0b2a020ad" />

**3. Modelagem**

Como citado no item anterior de coleta de dados, o dataset 'Mental Health and Lifestyle Habits Dataset (2019-2024)' é uma tabela única na qual não se torna necessária a contrução de esquemas mais refinados, como Esquema Estrela ou Snowflake.

O Catálogo dos dados foi realizada dentro da tabela (camada bronze do Databricks):

<img width="1151" height="503" alt="image" src="https://github.com/user-attachments/assets/69adde68-6f12-4f47-8202-1db275581ae5" />

Foi utilizada a funcionalidade nativa do Databricks para o início do Pipeline. Dessa forma, os dados foram carregados conforme os caminhos abaixo:

<img width="546" height="196" alt="image" src="https://github.com/user-attachments/assets/80c0393e-cb78-41f9-aa29-791e350250d1" />

<img width="604" height="235" alt="image" src="https://github.com/user-attachments/assets/33fb3675-57dd-4116-a6a0-39e96bc0593b" />


**4. Carga**
