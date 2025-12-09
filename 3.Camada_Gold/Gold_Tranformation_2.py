from pyspark import pipelines as dp
from pyspark.sql.functions import col, count, avg, when, lit
from utilities import utils

@dp.table(
    name="mvp.gold.Gold_Tranformation_2"
)
def Gold_Tranformation_2():

    # Carrega a tabela Silver
    df = spark.read.table("mvp.silver.silver_tranformation")

    # ✅ Criar coluna de faixa etária
    df = df.withColumn(
        "age_group",
        when(col("Age") < 25, "18–24")
        .when(col("Age") < 35, "25–34")
        .when(col("Age") < 45, "35–44")
        .when(col("Age") < 60, "45–59")
        .otherwise("60+")
    )

    # ✅ Lista fixa de faixas etárias
    age_groups = spark.createDataFrame(
        [("18–24",), ("25–34",), ("35–44",), ("45–59",), ("60+",)],
        ["age_group"]
    )

    # ✅ Lista fixa de níveis de estresse
    stress_levels = spark.createDataFrame(
        [("Low",), ("Moderate",), ("High",)],
        ["Stress_Level"]
    )

    # ✅ Todas as combinações possíveis
    full_grid = stress_levels.crossJoin(age_groups)

    # ✅ Agregação real dos dados
    agg_df = (
        df.groupBy("Stress_Level", "age_group")
          .agg(
              count("*").alias("total_people"),
              # avg("Sleep_Hours").alias("avg_sleep"),
              # avg("Work_Hours_per_Week").alias("avg_work_hours")
          )
    )

    # ✅ LEFT JOIN para garantir que todos os grupos apareçam
    result = (
        full_grid
        .join(agg_df, ["Stress_Level", "age_group"], "left")
        .fillna(0, subset=["total_people"])
    )

    return result
