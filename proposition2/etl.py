from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, when, to_date, split, trim, explode, from_json
from pyspark.sql.types import LongType, FloatType, IntegerType, BooleanType, DateType, ArrayType, StringType




spark = SparkSession.builder \
    .appName("airbnb ETL") \
    .config("spark.jars", "./lib/postgresql-42.7.3.jar") \
    .getOrCreate()



df = spark.read.option("header", True) \
    .option("multiline", True) \
    .option("quote", '"') \
    .option("escape", '"') \
    .option("mode", "PERMISSIVE") \
    .option("inferSchema", True) \
    .csv("./data/listings.csv")

colonnes = [
    "neighbourhood_cleansed","host_picture_url" ,"host_verifications","host_is_superhost", "host_since", "host_response_time", "host_response_rate",
    "calculated_host_listings_count", "property_type", "room_type", "accommodates",
    "bedrooms", "beds", "minimum_nights",
    "maximum_nights", "has_availability", "availability_30", "availability_60", "availability_90", "availability_365",
    "number_of_reviews", "reviews_per_month", "first_review", "last_review", "review_scores_rating",
    "review_scores_accuracy", "review_scores_cleanliness", "review_scores_checkin",
    "review_scores_communication", "review_scores_location", "review_scores_value",
    "amenities", "price"
]

df_filtered = df.select(*colonnes)

amenities_schema = ArrayType(StringType())


def safe_cast(df, column_name, to_type):
    if to_type == FloatType():

        return when(col(column_name).cast(to_type).isNotNull(), 
                   col(column_name).cast(to_type)).otherwise(0)
    elif to_type == DateType():
        return col(column_name).cast(to_type)
    else:
        return col(column_name).cast(to_type)
    

df_filtered = df_filtered \
    .withColumn("host_response_rate",
    regexp_replace(col("host_response_rate"), "%", "").cast(FloatType())
) \
    .withColumn("calculated_host_listings_count", col("calculated_host_listings_count").cast(IntegerType())) \
    .withColumn("accommodates", col("accommodates").cast(IntegerType())) \
    .withColumn("bedrooms", col("bedrooms").cast(IntegerType())) \
    .withColumn("beds", col("beds").cast(IntegerType())) \
    .withColumn("minimum_nights", col("minimum_nights").cast(IntegerType())) \
    .withColumn("maximum_nights", col("maximum_nights").cast(IntegerType())) \
    .withColumn("availability_30", col("availability_30").cast(IntegerType())) \
    .withColumn("availability_60", col("availability_60").cast(IntegerType())) \
    .withColumn("availability_90", col("availability_90").cast(IntegerType())) \
    .withColumn("availability_365", col("availability_365").cast(IntegerType())) \
    .withColumn("number_of_reviews", col("number_of_reviews").cast(IntegerType())) \
    .withColumn("reviews_per_month", col("reviews_per_month").cast(FloatType())) \
    .withColumn("review_scores_rating", col("review_scores_rating").cast(FloatType())) \
    .withColumn("review_scores_accuracy", col("review_scores_accuracy").cast(FloatType())) \
    .withColumn("review_scores_cleanliness", col("review_scores_cleanliness").cast(FloatType())) \
    .withColumn("review_scores_checkin", col("review_scores_checkin").cast(FloatType())) \
    .withColumn("review_scores_communication", col("review_scores_communication").cast(FloatType())) \
    .withColumn("review_scores_location", col("review_scores_location").cast(FloatType())) \
    .withColumn("review_scores_value", col("review_scores_value").cast(FloatType())) \
    .withColumn("has_availability", when(col("has_availability") == "t", True).when(col("has_availability") == "f", False).otherwise(False)) \
    .withColumn("host_is_superhost", when(col("host_is_superhost") == "t", True).when(col("host_is_superhost") == "f", False).otherwise(False)) \
    .withColumn("host_verifications",when(col("host_verifications").contains("phone"), True).otherwise(False)
)\
    .withColumn(
    "host_picture_url",
    when(
        col("host_picture_url").isNotNull() & (col("host_picture_url") != ""), True
    ).otherwise(False)
).withColumnRenamed("host_picture_url", "host_has_profile")\
    .withColumn("host_since_tmp", 
                when(to_date(col("host_since"), "MM/dd/yyyy").isNotNull(), 
                     to_date(col("host_since"), "MM/dd/yyyy"))
                .when(to_date(col("host_since"), "yyyy-MM-dd").isNotNull(),
                     to_date(col("host_since"), "yyyy-MM-dd"))
                .otherwise(None)) \
    .drop("host_since").withColumnRenamed("host_since_tmp", "host_since") \
    .withColumn("first_review_tmp", 
                when(to_date(col("first_review"), "MM/dd/yyyy").isNotNull(), 
                     to_date(col("first_review"), "MM/dd/yyyy"))
                .when(to_date(col("first_review"), "yyyy-MM-dd").isNotNull(),
                     to_date(col("first_review"), "yyyy-MM-dd"))
                .otherwise(None)) \
    .drop("first_review").withColumnRenamed("first_review_tmp", "first_review") \
    .withColumn("last_review_tmp", 
                when(to_date(col("last_review"), "MM/dd/yyyy").isNotNull(), 
                     to_date(col("last_review"), "MM/dd/yyyy"))
                .when(to_date(col("last_review"), "yyyy-MM-dd").isNotNull(),
                     to_date(col("last_review"), "yyyy-MM-dd"))
                .otherwise(None)) \
    .drop("last_review").withColumnRenamed("last_review_tmp", "last_review")\
    .withColumn(
    "price",
    regexp_replace("price", "[$,]", "").cast("double")
)\
    .withColumn(
    "amenities",
    from_json(col("amenities"), amenities_schema)
)



amenities_df = df_filtered.select(explode("amenities").alias("amenity")) \
    .withColumn("amenity", trim(col("amenity"))) \
    .filter(col("amenity") != "") \
    .dropna() \
    .distinct()


df_filtered.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/airbnb_db") \
    .option("dbtable", "listings") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .option("driver", "org.postgresql.Driver") \
    .mode("append") \
    .save()
    



amenities_df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/airbnb_db") \
    .option("dbtable", "amenities") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .option("driver", "org.postgresql.Driver") \
    .mode("append") \
    .save()


print("Importation finie")

