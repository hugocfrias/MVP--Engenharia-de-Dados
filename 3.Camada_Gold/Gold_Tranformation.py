from pyspark import pipelines as dp
from pyspark.sql.functions import col, count, count_if, avg, when
from utilities import utils

@dp.table(
    name="mvp.gold.Gold_Tranformation"
)
def Gold_Tranformation():
    return (
        spark.read.table("mvp.silver.silver_tranformation")
        .groupBy(col("Country"))
        .agg(
            count("*").alias("rows_per_group"),
            count_if(col("Age") >= 40).alias("over40_count"),

            # ✅ Média de felicidade apenas para pessoas acima dos 40 anos
            avg(when(col("Age") >= 40, col("Happiness_Score"))).alias("avg_happiness_over40"),

            # ✅Média de felicidade para todos
            avg(col("Happiness_Score")).alias("avg_happiness_all"),

            # ✅ Média de horas de sono apenas para pessoas acima dos 40 anos
            avg(when(col("Age") >= 40, col("Sleep_Hours"))).alias("avg_sleep_over40"),

            # ✅ Média de horas de sono para todos
            avg(col("Sleep_Hours")).alias("avg_sleep_all")
        )
    )
