# MVP- Engenharia-de-Dados 📊

<span style="color:red">Nome: Hugo Coelho de Frias</span>

Matrícula: 4052025000248

Linkedin: https://www.linkedin.com/in/hugo-frias-7059b622/

E-mail: hugofrias2@hotmail.com

___________

**🎯 1. Objetivo**

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

___________

**🔢 2. Coleta**

O dataset analisado foi escoliho na coleção da plataforma Kaggle:

Dataset: https://www.kaggle.com/datasets/atharvasoundankar/mental-health-and-lifestyle-habits-2019-2024

Trata-se de um de um dataset (tabela única) que possui 3000 instâncias, de maneira balanceada em relação aos seus atributos categóricos (Países, Gêneros, Tipo de Dieta etc). No total, possui 12 atributos.

Os dados foram armazenados em um Volume do Databricks:

<img width="1162" height="423" alt="image" src="https://github.com/user-attachments/assets/037e5b4b-5ab7-408c-b116-dd3d19680c55" />

___________

**❄ 3. Modelagem**

Como citado no item anterior de coleta de dados, o dataset 'Mental Health and Lifestyle Habits Dataset (2019-2024)' ***é uma tabela única na qual não se torna necessária a construção de esquemas mais refinados, como Esquema Estrela ou Snowflake***.

O Catálogo dos dados foi realizado dentro da própria tabela importada (camada bronze do Databricks):

<img width="1143" height="490" alt="image" src="https://github.com/user-attachments/assets/a70432cf-3e12-446f-9848-b61608ce702c" />


-  **Linhagem de Dados:**
    - Origem: Plataforma Kaggle
    - Dataset: [Mental_Health_Lifestyle](https://www.kaggle.com/datasets/atharvasoundankar/mental-health-and-lifestyle-habits-2019-2024)
    -  Trata-se de um de um dataset (tabela única) que possui 3000 instâncias, de maneira balanceada em relação aos seus atributos categóricos (Países, Gêneros, Tipo de Dieta etc). No           total,    possui 12 atributos.
   

**🔼 4. Carga**

Toda a etapa de ETL (Extração, Transformação e Carga) foi realizada ***com a utilização da funcionalidade nativa do Databricks para contrução de Pipelines***.

<img width="915" height="229" alt="image" src="https://github.com/user-attachments/assets/d16fb229-9ca7-4163-a350-9329de671223" />


Todo conceito de contrução foi baseado na metolologia **'Medallion Architecture'**:

<img width="662" height="318" alt="image" src="https://github.com/user-attachments/assets/224409a1-0b4a-4fc2-ae58-59cf5945ad5a" />
<br>

Fonte: https://www.databricks.com/glossary/medallion-architecture

Arquitetura no Databricks:

<img width="449" height="352" alt="image" src="https://github.com/user-attachments/assets/56502d4e-b22d-4266-ac94-e02780dba95f" />

Criação dos esquemas no Databricks:
<br>

<img width="576" height="325" alt="image" src="https://github.com/user-attachments/assets/e6664da5-cd95-47d3-a69b-b4796307aa64" />
<br>

Acessar Arquivo SQL: https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/Catalog%20Creation.sql

<br>

>🥉Camada Bronze:

Ingestão dos ***Dados Raw*** utilizando a funcionalidade nativa do Databricks para o início do Pipeline:

<img width="550" height="185" alt="image" src="https://github.com/user-attachments/assets/45882e48-833a-4cc8-b92c-819759628f15" />

<img width="585" height="147" alt="image" src="https://github.com/user-attachments/assets/0fb63e41-d90b-4b49-9c36-852be9e70366" />

Segue no link abaixo a documentação (.pdf) do processo da camada bronze:

https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/1.Camada_Bronze/Camada_Bronze_Processo.pdf

<br>

>🥈Camada Silver:

A limpeza consiste na verificação da consistência das informações, correção de possíveis erros de preenchimento ou eliminação de valores desconhecidos, redundantes ou não pertencentes ao domínio.

Foi criado um notebook com uma análise primária para a detecção de possíveis comportamentos que fossem prejudiciais às análises finais.

Acessar Link: https://hugocfrias.github.io/MVP--Engenharia-de-Dados/2.Camada_Silver/Exploration_Data.html

Foi identificada a necessidade de remoção do atributo **'Mental Health Condition'**. Analisando o dataset original, foram encontrados 595 linhas nulas (status de 'None'). Por ser tratar de um estado de desordem mental (Mental Health Condition), tive a dúvida se realmente são informações faltantes ou simplesmente instâncias nas quais o respondente não possuía algum tipo de desordem mental. Persistente essa indefinição, optei pela remoção do atributo.

**Pipeline (Camada Silver)**
<img width="1320" height="435" alt="image" src="https://github.com/user-attachments/assets/321624c6-8b82-4efa-89b5-4201be147a02" />

Como o Pipeline foi contruído utilizando a opção nativa do Databricks, os códigos são gerados no formado (.py). **Dessa forma, NÃO é possível o export do código com os outputs.**

Código (.py): https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/2.Camada_Silver/Silver_Tranformation.py

Eviência Output: https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/2.Camada_Silver/Output_Camada_Silver.pdf

<br>

>🥇Camada Gold:

Esta etapa contém dados trabalhados e agregados que repondem as principais perguntas levantadas no início do projeto.

**Pipeline (Camada Gold)**
<img width="1321" height="436" alt="image" src="https://github.com/user-attachments/assets/82b9f37a-b332-48b4-a4bd-68911a3efbd2" />

Como o Pipeline foi contruído utilizando a opção nativa do Databricks, os códigos são gerados no formado (.py). **Dessa forma, NÃO é possível o export do código com os outputs.**

***IMPORTANTE: DESCREVER O OBJETIVO DE CADA CÓDIGO!!!!!!!!!!!!!!***

Código (.py): https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/3.Camada_Gold/Gold_Tranformation.py

Código (.py): https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/3.Camada_Gold/Gold_Tranformation_2.py

Eviência Output: https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/3.Camada_Gold/Output_Camada_Gold.pdf

**Análises e Solução do Problema**

***EXPLICAR A ETAPA***

Acessar Link: https://hugocfrias.github.io/MVP--Engenharia-de-Dados/3.Camada_Gold/Data_Analisys.html
___________

**📈 5. Dashboards Databricks**

Utilizado a funcionalidade nativa da ferramenta, podemos ver em Dashboards análises graficas dos dados:
<br>

<img width="1228" height="564" alt="image" src="https://github.com/user-attachments/assets/d9cbb8fb-bc90-4f1f-ba20-57b24c0c9c91" /><br>



**Análise 1:** Os diferentes níveis de stress (Stress_Level) têm média de idade similares<br>
**Análise 2:** O atributo de horas dormidas (Sleep_Hours) tem uma distrubuição normal<br>
**Análise 3:** A mediana dos das idades (Age) são bem próximas quando analisado o atributo do tipo de dieta (Diet_Type)<br>
**Análise 4:** Os diferentes tipos de gênero (Gender) têm média de horas semanais trabalhadas (Work_Hours_per_Week) similares<br>
**Análise 5:** Os dados do dataset são balanceados. Nesse caso, podemos chegar a conclusões mais precisas.


___________

**🔄 6. Criação de Jobs Databricks**

Utilizado a funcionalidade nativa da ferramenta, foi criado um **Job** com o objetivo de agendar e orquestrar tarefas:<br>

>Criação do Job:<br>

<img width="1323" height="352" alt="image" src="https://github.com/user-attachments/assets/0fe6c9df-7683-4a9e-859c-53983febab60" /><br>

>Visualização Gráfica do Job:<br>

<img width="1146" height="454" alt="image" src="https://github.com/user-attachments/assets/4332550a-4edf-4eb4-9cd8-f09db453c5bf" /><br>

Pode-se verificar que a a seguinte sequência de execução:<br>

**1.** Execução do Notebook de exploração de dados da Camada Silver (Data_Exploration)<br>
**2.** Execução do Pipeline (Restante da Camada Silver e inícioda Camada Gold)<br>
**3.** Execução do Notebook Análise de Dados da Camada Gold (Data_Analisys)<br>

>Execução do Job:<br>

<img width="1103" height="399" alt="image" src="https://github.com/user-attachments/assets/11469ed4-f737-4ec6-9c13-1f77ebc2a711" />


___________

**📖 7. Respostas das Perguntas Iniciais**



