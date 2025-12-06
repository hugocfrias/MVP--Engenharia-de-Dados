from pyspark import pipelines as dp
from pyspark.sql.functions import col

# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.

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
            col("Work Hours per Week").alias("Work_Hours_per_Week"),
            col("Screen Time per Day (Hours)").alias("Screen_Time_per_Day_Hours"),
            col("Social Interaction Score").alias("Social_Interaction_Score"),
            col("Happiness Score").alias("Happiness_Score"),
            col("Stress Level").alias("Stress_Level")
        )
    )