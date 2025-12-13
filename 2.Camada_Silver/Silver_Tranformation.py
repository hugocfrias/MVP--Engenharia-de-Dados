from pyspark import pipelines as dp
from pyspark.sql.functions import col

# Alteração do nome das colunas para o padrão do Databricks. 
# Remoção da coluna Mental Health Condition, conforme a etapa de 'Exploration_Data' (595 eventos nulos)

@dp.table(
    name="mvp.silver.Silver_Tranformation"
)
def Silver_Tranformation():
    return (
        spark.read.table("mvp.bronze.mental_health_lifestyle_dataset")
        .select(
            col("Country").alias("Country"),
            col("Age").alias("Age"),
            col("Gender").alias("Gender"),
            col("Exercise Level").alias("Exercise_Level"),
            col("Diet Type").alias("Diet_Type"),
            col("Sleep Hours").alias("Sleep_Hours"),
            #col("Mental Health Condition").alias("Mental_Health_Condition"), 
            col("Work Hours per Week").alias("Work_Hours_per_Week"),
            col("Screen Time per Day (Hours)").alias("Screen_Time_per_Day_Hours"),
            col("Social Interaction Score").alias("Social_Interaction_Score"),
            col("Happiness Score").alias("Happiness_Score"),
            col("Stress Level").alias("Stress_Level")
        )
    )