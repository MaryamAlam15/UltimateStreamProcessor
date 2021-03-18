FROM python:3.8-buster

RUN apt-get update

# Installing JDK 8
RUN apt update && apt-get install -y openjdk-11-jdk-headless

# deleting folder if already exist.
RUN rm -f ultimate_streaming

# create new folder and make it working dir.
RUN mkdir /ultimate_streaming
RUN cd /ultimate_streaming
WORKDIR .

# copy all content of the repo on docker.
COPY . .

# install requirements.
RUN pip3 install -r requirememts.txt

# set environment variables.
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV SPARK_HOME=/usr/local/lib/python3.8/site-packages/pyspark
ENV PYTHONPATH=${SPARK_HOME}/python
ENV PYTHONPATH=${PYTHONPATH}:${PYTHONPATH}/lib/py4j-0.10.9-src.zip

# copy jar files which are missing in default pyspark package.
COPY jars/* ${SPARK_HOME}/jars/

# run command.
CMD ["python3", "ultimate_stream_processor.py"]