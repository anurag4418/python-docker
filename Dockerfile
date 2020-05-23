FROM ubuntu:16.04
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    python3.4 \
    python3-pip    
RUN python3 -m pip install --upgrade pip
RUN pip install mysql-connector-python
COPY . /opt/app
CMD [python insert-scripy.py]
