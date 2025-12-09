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
            count_if(col("Age") >= 40).alias("adults_count"),

            # ✅ Média de felicidade apenas para adultos
            avg(when(col("Age") >= 40, col("Happiness_Score"))).alias("avg_happiness_adults"),

            # ✅ Média de felicidade para todos
            avg(col("Happiness_Score")).alias("avg_happiness_all"),

            # ✅ Média de horas de sono apenas para adultos
            avg(when(col("Age") >= 40, col("Sleep_Hours"))).alias("avg_sleep_adults"),

            # ✅ Média de horas de sono para todos
            avg(col("Sleep_Hours")).alias("avg_sleep_all")
        )
    )
