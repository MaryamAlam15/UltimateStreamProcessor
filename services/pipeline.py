from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from config.socket_config import SocketConfig
from config.spark_config import SparkConfig
from services.processor import Processor


class Pipeline:

    def __init__(self):
        spark_config = SparkConfig()
        self.sc = SparkContext(appName=spark_config.APP_NAME)
        self.streaming_context = StreamingContext(self.sc, spark_config.TIME_TO_BUFFER)

    def start(self):
        data = self.read_data()

        processor = Processor()
        processor.process(data)

        self.streaming_context.start()
        self.streaming_context.awaitTermination()

    def read_data(self):
        config = SocketConfig()
        return self.streaming_context.socketTextStream(config.HOST, int(config.PORT))
