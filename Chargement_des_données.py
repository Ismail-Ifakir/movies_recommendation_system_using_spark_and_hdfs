from pyspark.sql import SparkSession

# Créer une session Spark
spark = SparkSession.builder.appName("MovieRecommendation").getOrCreate()

# Remplacez "path_to_data" par le chemin réel vers vos données dans HDFS
path_to_data = "hdfs://userr/maria_de/ifakir/"

# Charger les données en DataFrame
ratings = spark.read.csv(path_to_data + "ratings.csv", header=True, inferSchema=True)
movies = spark.read.csv(path_to_data + "movies.csv", header=True, inferSchema=True)
