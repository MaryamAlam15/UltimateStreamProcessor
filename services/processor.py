import logging
import re

from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_list, lit, udf, col
from pyspark.sql.types import StringType

from config.mongo_config import MongoConfig
from models.tweet import Tweet
from services.worldo_meters_scraper import WorldoMetersScrapper


def getSparkSessionInstance(sparkConf):
    return SparkSession \
        .builder \
        .master('local[2]') \
        .config(conf=sparkConf) \
        .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1') \
        .getOrCreate()


class Processor:

    def process(self, data):
        data.foreachRDD(self.process_rdd)

    def process_rdd(self, time, rdd):
        try:
            # Get the singleton instance of SparkSession
            spark = getSparkSessionInstance(rdd.context.getConf())

            # read tweet.
            tweets_dataframe = self.get_tweet_df(spark, rdd, time)

            # get total corona cases via scrapping.
            coronavirus_latest_cases = self.fetch_corona_cases()

            # merge the data.
            processed_data = self.clean_and_merge_data(tweets_dataframe, coronavirus_latest_cases)

            # write to mongo DB.
            self.write_data_to_mongo(processed_data)

        except Exception as e:
            logging.exception(e)

    ####################### helper method #####################################

    def clean_tweet(self, value):
        # eliminate '#', 'RT:' or any url.
        regex_to_clean = r'(#|RT:|(http|https):+[^\s]+[\w])'
        cleaned_value = re.sub(regex_to_clean, '', value).strip()
        return cleaned_value

    def write_data_to_mongo(self, df):
        """
        writes the final data into mongo db.
        """
        config = MongoConfig()

        df.write.format(config.WRITE_FORMAT) \
            .options(**config.DATABASE_OPTIONS) \
            .mode(config.MODE_TO_WRITE) \
            .save()

    def get_tweet_df(self, spark, rdd, time):
        """
        Convert RDD[String] to RDD[Row] to DataFrame
        """
        row_rdd = rdd.map(lambda tweet: Tweet(tweet_value=tweet, time_stamp=time))
        return spark.createDataFrame(row_rdd)

    def fetch_corona_cases(self):
        """
        calls the Scrapper service to fetch the total corona cases.
        """
        return WorldoMetersScrapper().scrap_latest_cases()

    def clean_and_merge_data(self, tweets_dataframe, coronavirus_latest_cases):
        """
        cleans tweets, merge the DF with corona total cases, and
        finally group-up the data.
        """

        # UDF to cleanup the tweet text.
        clean_tweet_udf = udf(self.clean_tweet, StringType())
        tweets_dataframe = tweets_dataframe.withColumn('cleaned_tweet', clean_tweet_udf(col('tweet_text')))

        merged_df = tweets_dataframe.withColumn('total_case_count', lit(coronavirus_latest_cases))

        return merged_df \
            .select('*') \
            .groupBy('time_stamp', 'total_case_count') \
            .agg(collect_list('cleaned_tweet').alias('content'))
