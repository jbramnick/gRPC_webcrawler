FROM debian:10

RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN apt-get install -y curl vim

RUN python3 -m pip install grpcio validators click protobuf

RUN mkdir /app

COPY crawl /app

COPY crawler_pb2_grpc.py /app

COPY crawler_pb2.py /app