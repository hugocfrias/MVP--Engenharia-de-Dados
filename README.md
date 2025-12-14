# MVP- Engenharia-de-Dados 📊

Nome: Hugo Coelho de Frias

Matrícula: 4052025000248

Linkedin: https://www.linkedin.com/in/hugo-frias-7059b622/

E-mail: hugofrias2@hotmail.com

---

### <u>**🎯 1. Objetivo**<u>

O Conjunto de Dados de 'Mental Health and Lifestyle Habits Dataset (2019-2024)' é uma coleção abrangente de dados que visa compreender como diversos fatores de estilo de vida afetam o bem-estar mental. Esta base de dados captura aspectos como rotinas de exercícios, hábitos alimentares, padrões de sono, níveis de estresse e interações sociais, além de informações demográficas. A partir do conjunto de dados, se deseja responder as seguintes perguntas:

>1. Podemos classificar os 'níveis de stress e bem-estar' de acordo a faixa etária dos indivíduos?

>2. Existem diferenças relevantes nos atributos considerando determinada faixa etária?

>3. Quais países têm maior índice médio de interação social (Social_Interaction_Score)?

>4. Qual gênero apresenta maior felicidade média?

>5. Há países onde as pessoas dormem mais?

>6. O tempo de tela varia muito entre os diferentes níveis de stress?

>7. Há algum padrão facilmente identificável por meio de análise gráfica?

>8. Existe correlação entre os atributos numéricos do dataset?

>9. É possível segregar níveis de stress e bem-estar com base em horas de sono, horas de trabalho e tempo de tela, por exemplo?

---

### **🔢 2. Coleta**

O dataset analisado foi selecionado a partir da coleção disponível na plataforma Kaggle:

Dataset: https://www.kaggle.com/datasets/atharvasoundankar/mental-health-and-lifestyle-habits-2019-2024

Trata-se de um de um dataset (tabela única) que possui 3000 instâncias, de maneira balanceada em relação aos seus atributos categóricos (Países, Gêneros, Tipo de Dieta etc). No total, possui 12 atributos.

Trata-se de um conjunto de dados composto por uma **única tabela**, contendo aproximadamente 3.000 instâncias. O dataset é balanceado em relação aos seus principais atributos categóricos (como País, Gênero, Tipo de Dieta, entre outros) e possui, ao todo, 12 atributos.

Os dados foram armazenados em um **Volume do Databricks**, permitindo sua ingestão e processamento ao longo das etapas do projeto.

<img width="1162" height="423" alt="image" src="https://github.com/user-attachments/assets/037e5b4b-5ab7-408c-b116-dd3d19680c55" />

---

### **❄ 3. Modelagem**

Como mencionado na etapa de coleta de dados, o dataset “Mental Health and Lifestyle Habits Dataset (2019–2024)” ***consiste em uma única tabela. Por esse motivo, não há necessidade de modelagens mais complexas, como esquemas em Estrela ou Snowflake***.

O catálogo dos dados foi estruturado diretamente sobre a tabela importada, compondo a camada Bronze do Databricks, onde o dataset foi armazenado e disponibilizado para as etapas seguintes de transformação e análise.

<img width="1143" height="490" alt="image" src="https://github.com/user-attachments/assets/a70432cf-3e12-446f-9848-b61608ce702c" />


-  **Linhagem de Dados:**
    - Origem: Plataforma Kaggle
    - Dataset: [Mental_Health_Lifestyle](https://www.kaggle.com/datasets/atharvasoundankar/mental-health-and-lifestyle-habits-2019-2024)
    -  O dataset consiste em uma tabela única com aproximadamente 3.000 instâncias, apresentando distribuição balanceada entre seus principais atributos categóricos (como País, Gênero, Tipo de Dieta, entre outros). No total, o conjunto de dados contém 12 atributos.
   

---

### **🔼 4. Carga**

Toda a etapa de ETL (Extração, Transformação e Carga) ***foi executada utilizando a funcionalidade nativa de Pipelines do Databricks, que permite orquestrar e automatizar o fluxo de dados de forma integrada e escalável.*** <br>

<img width="915" height="229" alt="image" src="https://github.com/user-attachments/assets/d16fb229-9ca7-4163-a350-9329de671223" /> <br>


A construção do pipeline seguiu os princípios da **Medallion Architecture**, metodologia recomendada pelo Databricks para organizar dados em camadas (Bronze, Silver e Gold), garantindo qualidade, rastreabilidade e governança ao longo de todo o processo:/><br>

<img width="662" height="318" alt="image" src="https://github.com/user-attachments/assets/224409a1-0b4a-4fc2-ae58-59cf5945ad5a" />/> <br>


Fonte: https://www.databricks.com/glossary/medallion-architecture

Arquitetura no Databricks:

<img width="449" height="352" alt="image" src="https://github.com/user-attachments/assets/56502d4e-b22d-4266-ac94-e02780dba95f" /><br>

A arquitetura do projeto foi organizada seguindo as boas práticas recomendadas pelo Databricks, contemplando as camadas de ingestão, transformação e disponibilização dos dados.<br>

Criação dos esquemas no Databricks:
<br>

<img width="576" height="325" alt="image" src="https://github.com/user-attachments/assets/e6664da5-cd95-47d3-a69b-b4796307aa64" /><br>

A estruturação dos esquemas foi realizada diretamente no ambiente do Databricks, garantindo organização, governança e separação lógica entre as diferentes camadas do pipeline de dados.<br>

Acessar Arquivo SQL: https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/Catalog%20Creation.sql
<br>

>**🥉Camada Bronze**:

A ingestão dos dados brutos **(Raw Data)** foi realizada utilizando a funcionalidade nativa de Pipelines do Databricks, que permite iniciar o fluxo de processamento de forma automatizada e integrada ao ambiente da plataforma.

<img width="550" height="185" alt="image" src="https://github.com/user-attachments/assets/45882e48-833a-4cc8-b92c-819759628f15" />

<img width="585" height="147" alt="image" src="https://github.com/user-attachments/assets/0fb63e41-d90b-4b49-9c36-852be9e70366" />

Para mais detalhes sobre o processo de ingestão e estruturação da Camada Bronze, consulte a documentação (.pdf) disponível no link abaixo:<br>

https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/1.Camada_Bronze/Camada_Bronze_Processo.pdf

<br>

>**🥈Camada Silver**:

A etapa de limpeza dos dados envolveu a verificação da consistência das informações, a correção de possíveis erros de preenchimento e a eliminação de valores desconhecidos, redundantes ou fora do domínio esperado.

Para apoiar esse processo, foi criado um notebook dedicado à **análise exploratória inicial**, com o objetivo de identificar comportamentos que pudessem comprometer as análises posteriores.

Exploração Inicial dos Dados: https://hugocfrias.github.io/MVP--Engenharia-de-Dados/2.Camada_Silver/Exploration_Data.html

Durante essa análise, identificou-se a necessidade de remover o atributo **“Mental Health Condition”**. No dataset original, foram encontradas **595 linhas com valor nulo (“None”)**. Por se tratar de um atributo relacionado a condições de saúde mental, não foi possível determinar se esses valores representavam dados ausentes ou simplesmente a ausência de qualquer condição relatada pelo respondente. Diante dessa indefinição e para evitar interpretações equivocadas, optou-se pela **remoção completa do atributo**.

**Pipeline – Camada Silver**
<img width="1320" height="435" alt="image" src="https://github.com/user-attachments/assets/321624c6-8b82-4efa-89b5-4201be147a02" />

O pipeline da Camada Silver foi construído utilizando a **funcionalidade nativa de Pipelines do Databricks**, que gera automaticamente os scripts no formato .py. **Por esse motivo, não é possível exportar o código contendo os outputs diretamente pelo ambiente**.

Código (.py): https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/2.Camada_Silver/Silver_Tranformation.py

Evidência dos Outputs: https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/2.Camada_Silver/Output_Camada_Silver.pdf

<br>

>**🥇Camada Gold**:

A Camada Gold reúne os dados refinados e agregados, estruturados especificamente para responder às principais perguntas definidas no início do projeto. É nesta etapa que os insights finais são consolidados e preparados para consumo analítico.

**Pipeline – Camada Gold**
<img width="1321" height="436" alt="image" src="https://github.com/user-attachments/assets/82b9f37a-b332-48b4-a4bd-68911a3efbd2" />

O pipeline foi construído utilizando a **funcionalidade nativa de Pipelines do Databricks**, que gera automaticamente os scripts no formato .py. **Por esse motivo, não é possível exportar o código contendo os outputs diretamente pelo ambiente**.

**Tabelas Criadas na Camada Gold**

**1. Gold Transformation**

A primeira tabela da Camada Gold tem como objetivo **comparar a população total com o grupo de indivíduos acima de 40 anos**. O foco dessa análise é avaliar o impacto da idade em atributos como:

média do score de felicidade (**Happiness_Score**)

média de horas de sono (**Sleep_Hours**)

Código (.py): https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/3.Camada_Gold/Gold_Tranformation.py

**2. Gold Transformation 2**

A segunda tabela tem como objetivo **criar faixas etárias** e realizar a **contagem de indivíduos por nível de stress (Stress_Level)** dentro de cada faixa. Essa estrutura permite identificar padrões de stress ao longo das diferentes idades.

Código (.py): https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/3.Camada_Gold/Gold_Tranformation_2.py

Evidências dos Outputs da Camada Gold:

https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/3.Camada_Gold/Output_Camada_Gold.pdf

**Análises e Solução do Problema**

Para complementar as tabelas da Camada Gold, foi desenvolvido um notebook com uma análise exploratória aprofundada, voltada a responder de forma objetiva as questões levantadas no início do projeto.

Acessar Análise Completa: https://hugocfrias.github.io/MVP--Engenharia-de-Dados/3.Camada_Gold/Data_Analisys.html

---

### **📈 5. Dashboards Databricks**

Utilizando a funcionalidade nativa de **Dashboards do Databricks**, foi possível visualizar diversas **análises gráficas** dos dados, facilitando a interpretação dos padrões e insights identificados ao longo do projeto.
<br>

<img width="1228" height="564" alt="image" src="https://github.com/user-attachments/assets/d9cbb8fb-bc90-4f1f-ba20-57b24c0c9c91" /><br>


**Análise 1:** *Os níveis de stress (Stress_Level) apresentam médias de idade semelhantes.*<br>
**Análise 2:** *O atributo de horas dormidas (Sleep_Hours) segue uma distribuição aproximadamente normal.*<br>
**Análise 3:** *As medianas do atributo idade (Age) são próximas analisando os diferentes tipo de dieta (Diet_Type).*<br>
**Análise 4:** *Os gêneros (Gender) apresentam médias similares de horas semanais trabalhadas (Work_Hours_per_Week).*<br>
**Análise 5:** *O dataset é balanceado, o que favorece conclusões mais robustas.*<br>

---

### **🔄 6. Criação de Jobs Databricks**

Utilizando a funcionalidade nativa da plataforma, foi criado um **Job** com o objetivo de **agendar e orquestrar as tarefas** do pipeline de forma automatizada:<br>

>Criação do Job:
><br>

<img width="1323" height="352" alt="image" src="https://github.com/user-attachments/assets/0fe6c9df-7683-4a9e-859c-53983febab60" /><br>

>Visualização Gráfica do Job:
><br>

<img width="1146" height="454" alt="image" src="https://github.com/user-attachments/assets/4332550a-4edf-4eb4-9cd8-f09db453c5bf" /><br>
<br>

<img width="801" height="268" alt="image" src="https://github.com/user-attachments/assets/5b9c88eb-e30e-459f-be77-081cb0d7b990" /><br>
<br>

A partir da visualização, é possível identificar a seguinte **sequência de execução**:<br>

**1.** Execução do notebook de exploração de dados da **Camada Silver** (Data_Exploration)<br>
**2.** Execução do **Pipeline**, contemplando o restante da Camada Silver e o início da Camada Gold<br>
**3.** Execução do notebook de **Análise de Dados da Camada Gold** (Data_Analisys)<br>
<br>
>Execução do Job:
><br>

<img width="1103" height="399" alt="image" src="https://github.com/user-attachments/assets/11469ed4-f737-4ec6-9c13-1f77ebc2a711" />


---

### **📖 7. Respostas das Perguntas Iniciais**

As respostas para as perguntas levantadas no início do projeto serão respondidas com base nas informações geradas e dispobibilizadas nos item anteriores.<br>

Principais Links: 

https://github.com/hugocfrias/MVP--Engenharia-de-Dados/blob/main/3.Camada_Gold/Output_Camada_Gold.pdf<br>

https://hugocfrias.github.io/MVP--Engenharia-de-Dados/3.Camada_Gold/Data_Analisys.html<br>

<br>


>1. Podemos classificar os níveis de stress e bem-estar de acordo com a faixa etária??

***Resposta:*** *Na tabela da camada Gold (gold_transformation), as médias de Happiness_Score e Sleep_Hours para o grupo acima de 40 anos são muito próximas das médias gerais. Isso indica que, para esses atributos, não há diferenças significativas entre as faixas etárias analisadas.*

<img width="369" height="352" alt="image" src="https://github.com/user-attachments/assets/1f0f9113-f077-4687-be81-0e78d9c058f1" /><br>


>2. Existem diferenças relevantes nos atributos considerando determinada faixa etária?

***Resposta:*** *Na tabela da camada Gold (gold_transformation), as médias de **Happiness_Scor**e e **Sleep_Hours** para o grupo acima de 40 anos são muito próximas das médias gerais. Isso indica que, para esses atributos, não há diferenças significativas entre as faixas etárias analisadas.*


<img width="809" height="188" alt="image" src="https://github.com/user-attachments/assets/3f1bf430-27a0-48aa-ba98-b385a5ddbe8e" /><br>


>3. Quais países têm maior índice médio de interação social (Social_Interaction_Score)?

***Resposta:*** *No notebook 'Data_Analysis', o ranking das médias de Social_Interaction_Score mostra que Canadá e Estados Unidos apresentam os maiores índices médios de interação social.*

<img width="520" height="460" alt="image" src="https://github.com/user-attachments/assets/0e984419-9da6-4628-86a5-5fdff10c1517" /><br>


>4. Qual gênero apresenta maior felicidade média?

***Resposta:*** *No notebook 'Data_Analysis', o ranking das médias de **Social_Interaction_Score** mostra que Canadá e Estados Unidos apresentam os maiores índices médios de interação social.*

<img width="523" height="400" alt="image" src="https://github.com/user-attachments/assets/59d4aeea-c61d-4a7d-a626-32fab68c6676" /><br>


>5. Há países onde as pessoas dormem mais?

***Resposta:*** *O ranking das médias de **Sleep_Hours** indica que Canadá e Japão possuem as maiores médias de horas dormidas. No entanto, as diferenças entre os países são pequenas, não caracterizando variações relevantes.*

<img width="498" height="452" alt="image" src="https://github.com/user-attachments/assets/2a5b7dba-f74f-406c-814b-611496d3cea9" /><br>


>6. O tempo de tela varia muito entre os diferentes níveis de stress?

***Resposta:*** *O ordenamento das médias de **Screen_Time_per_Day_Hours** mostra que não há diferenças expressivas entre os níveis de stress. As médias são próximas, indicando baixa variabilidade.*

<img width="586" height="395" alt="image" src="https://github.com/user-attachments/assets/6ef59d84-2e4b-404c-bd59-d90344028b2c" /><br>


>7. Há algum padrão facilmente identificável por meio de análise gráfica?

***Resposta:*** *As visualizações criadas nos Dashboards do Databricks revelam alguns padrões:*

<img width="1228" height="564" alt="image" src="https://github.com/user-attachments/assets/d9cbb8fb-bc90-4f1f-ba20-57b24c0c9c91" /><br>

*Os níveis de stress (Stress_Level) apresentam médias de idade semelhantes.*<br>
*O atributo de horas dormidas (Sleep_Hours) segue uma distribuição aproximadamente normal.*<br>
*As medianas do atributo idade (Age) são próximas analisando os diferentes tipo de dieta (Diet_Type).*<br>
*Os gêneros (Gender) apresentam médias similares de horas semanais trabalhadas (Work_Hours_per_Week).*<br>
* O dataset é balanceado, o que favorece conclusões mais robustas.*<br>


>8. Existe correlação entre os atributos numéricos do dataset?

***Resposta:*** *O mapa de calor de correlação no notebook 'Data_Analysis' mostra que todas as correlações entre variáveis numéricas são fracas, indicando baixa relação linear entre os atributos.*

<img width="553" height="506" alt="image" src="https://github.com/user-attachments/assets/e0e8d860-4515-420a-b1d3-d3d835d865af" /><br>


>9. É possível segregar níveis de stress e bem-estar com base em horas de sono, horas de trabalho e tempo de tela, por exemplo?

***Resposta:*** *As análises no notebook 'Data_Analysis' mostram que as médias de **Sleep_Hours**, **Work_Hours_per_Week** e **Screen_Time_per_Day_Hours** são muito próximas entre os diferentes níveis de stress. Portanto, esses atributos não apresentam diferenças suficientes para segmentar os níveis de stress e bem‑estar.*

<img width="662" height="476" alt="image" src="https://github.com/user-attachments/assets/b1a0e71a-c1fc-4e8b-acc4-c9f9e334d821" /><br>


---


### **💡 8. Autoavaliação**

>1. Planejamento e Estruturação do Projeto

Acredito que o projeto foi desenvolvido de forma coerente, seguindo as estrutura **Medallion Architecture** (Bronze, Silver e Gold). Essa estrutura permitiu um melhor entendimento de cada fase para melhor clareza metodológica.

Considero que o projeto foi desenvolvido de forma coerente, seguindo a estrutura da  **Medallion Architecture** (Bronze, Silver e Gold). Essa abordagem permitiu compreender claramente cada etapa do processo, garantindo maior organização e clareza metodológica.

**Oportunidade de melhoria:** incluir diagramas customizados adicionais para aprimorar a visualização da arquitetura.

>2. Análise Técnica

O projeto foi construído majoritariamente com os recursos nativos do Databricks, como **Pipelines**, **Jobs**, **Volumes**, **Dashboards** e **notebooks**. As camadas Bronze, Silver e Gold foram implementadas utilizando as ferramentas de construção de ETL disponibilizadas pela plataforma.

**Oportunidade de melhoria:** como o projeto utilizou principalmente funcionalidades nativas, há espaço para aprofundar técnicas mais avançadas com Spark.

>3. Resumo Geral da Autoavaliação

Avalio que o MVP foi desenvolvido com técnicas adequadas e análises exploratórias bem estruturadas. A combinação entre a arquitetura de pipelines do Databricks e o uso de código Python/Spark mostrou-se eficiente para alcançar as conclusões propostas. Como evolução, pretendo aprofundar conhecimentos em integração de dados com outras plataformas em nuvem e explorar abordagens mais avançadas de engenharia de dados.

---
