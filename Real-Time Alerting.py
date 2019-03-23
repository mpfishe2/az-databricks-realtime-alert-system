# Databricks notebook source
# Event Hub Namespace Name
NAMESPACE_NAME = ""
# Key Value for the RootManageSharedAccessKey or the key at the namespace level you created and chose to use for this 
KEY_VALUE = ""

# The connection string to your Event Hubs Namespace
connectionString = "Endpoint=sb://{0}.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey={1};EntityPath=ingestion".format(NAMESPACE_NAME, KEY_VALUE)

# Event Hubs Connection Configuration
ehConf = {
  'eventhubs.connectionString' : connectionString
}

productsSoldStream = spark \
  .readStream \
  .format("eventhubs") \
  .options(**ehConf) \
  .load()

# COMMAND ----------

# When data is streamed into the Event Hub and Spark reads it, the message body will be stored as binary data
# We need to cast the binary data as a string to get the contents of the message
GetMessageData = productsSoldStream.select(productsSoldStream.body.cast("string").alias("body"))

# Here we import some necessary libraries
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Here we establish our schema for the incoming JSON messages
schema = StructType([
  StructField("storeId", IntegerType(), True),
  StructField('productid', IntegerType(), True),
  StructField("timestamp", TimestampType(), True),
  StructField("name", StringType(), True),
  StructField("category", StringType(), True),
  StructField("price", DecimalType(18,8), True),
  StructField("quantity", IntegerType(), True)
])

# From the string representation of the message contents we extract the JSON structure using the schema defined above and the from_json() function
FilterForCoughSyrupTransactions = GetMessageData.select(from_json("body", schema=schema).alias("body")) \
                                                .where("body.productid == 14") \
                                                .where("body.quantity > 10")

# COMMAND ----------

# The connection string to your Event Hubs Namespace
connectionStringAlerting = "Endpoint=sb://{0}.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey={1};EntityPath=alerting".format(NAMESPACE_NAME, KEY_VALUE)

# Event Hubs Connection Configuration
ehConfAlerting = {
  'eventhubs.connectionString' : connectionStringAlerting
}


FilterForCoughSyrupTransactions.select(FilterForCoughSyrupTransactions.body.cast("string")).writeStream \ # Cast the filtered transactions to strings
                  .format("eventhubs") \ # write to event hubs as the sink
                  .options(**ehConfAlerting) \ # configuration for the 'alerting' Event Hub
                  .option("checkpointLocation", "/streamingDataDemos/demo/checkpoints") \ # Location for the checkpoints
                  .start()
