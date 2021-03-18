FROM python:3.8-buster

RUN apt-get update
# Installing JDK 8
RUN apt update && apt-get install -y openjdk-11-jdk-headless

RUN rm -f ultimate_streaming

RUN mkdir /ultimate_streaming
WORKDIR ultimate_streaming

COPY . .

RUN pip3 install -r requirememts.txt

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV SPARK_HOME=/usr/local/lib/python3.8/site-packages/pyspark
ENV PYTHONPATH=${SPARK_HOME}/python
ENV PYTHONPATH=${PYTHONPATH}:${PYTHONPATH}/lib/py4j-0.10.9-src.zip

COPY jars/* ${SPARK_HOME}/jars/

CMD ["python3", "ultimate_stream_processing.py"]