from services.pipeline import Pipeline


class UltimateStreamProcessor:

    @staticmethod
    def process():
        pipeline = Pipeline()
        pipeline.start()


if __name__ == "__main__":
    UltimateStreamProcessor.process()
